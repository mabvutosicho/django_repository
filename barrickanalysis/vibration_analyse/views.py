from django.shortcuts import render
from .models import Vibration
from App_users.models import Users
from clocking_system.models import Clock_in,Clock_out
from django.shortcuts import redirect
from random import uniform as un
from bokeh.plotting import figure
from bokeh.io import output_file,show 
import itertools




# Create your views here.


def vibrate(request):
        if request.method == 'POST':
                clock_out = Clock_out.objects.latest('pk')
                clock_in = Clock_in.objects.latest('pk')
                clock_out_i = clock_in.pk
                clock_ind = clock_in.time_in
                clock_hin = clock_ind.minute
                clock_outd = clock_out.time_out
                clock_hout = clock_outd.minute
                dura = clock_hout - clock_hin
                vib = un(0,40)
                sessionname = request.POST['viuse']
                uid = Users.objects.get(firstname=sessionname)
                
                vib = Vibration.objects.create(clock_out_id=clock_out, duration=dura, vibration_Ve=vib, user_id=uid)
                vib.save()

                return redirect('logout')
        else:
                return render(request, 'vibration_analyse/vibrate.html')

def vibrateview(request):
        userz = Users.objects.all()
        durations = Vibration.objects.all()
        clocksin = Clock_in.objects.get(pk=1)
        clocksout = Clock_out.objects.all()
        print(clocksin)
        return render(request, "vibration_analyse/vibrationview.html", {"user": userz, "duration": durations, "timon": clocksin, "timout": clocksout})

def one_user_details(request, **kwargs):
        uso = Users.objects.get(user_id=kwargs['id'])
        vibralevel = Vibration.objects.filter(user_id=uso)
        clocko = Clock_in.objects.filter(user_id=uso)
        #fg = figure(x_axis_label="vibration_velocity",y_axis_label="duration")
        #dir(itertools)
        
        #x = list(vibralevel)
        #y = list(vibralevel)
        #print(x)
        #print(y)
        #for n in vibralevel:
        #        x.append(n)
        #        y.append(n)
        #fg.circle(x,y)
        #output_file('./templates/vibration_analyse/sample.html')
        #show(fg)
        
        return render(request, "vibration_analyse/details.html", {'uza': uso, 'vibs': vibralevel, 'clck': clocko })

def select_details(request):
        usors = Users.objects.all();
        return render(request,'vibration_analyse/detailselect.html',{'usr':usors})
