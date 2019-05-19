from django.shortcuts import render
from .models  import Clock_in,Clock_out
from App_users.models import Users
# import datetime
from datetime import datetime as tym
from django.http import HttpResponseRedirect
from django.shortcuts import redirect



# Create your views here.
def clock(request):
    if not request.session._session:
           
        return redirect('users')

    else:
        if request.method == 'POST':
            names = request.POST
            
            if names.get('machineon') == 'Machine on':
                uspost = request.POST['useidtxt']
                userin = Users.objects.get(firstname=uspost)                  
                clockobj = Clock_in.objects.create(user_id=userin)
                clockobj.save()
            elif names.get('machineoff') == 'Machine Off':
                tim_id = Clock_in.objects.latest('pk')
                
                
                
                tis = Clock_out.objects.create(time_in_id=tim_id)
                tis.save()
                return redirect('vibrate')
                

           
            # clock_obj2 = Clock_out.objects.all()

            return render(request, 'clocking_system/clock.html',)       
        else:
            return render(request, 'clocking_system/clock.html',)


def logout(request):
    try:
        del request.session['firstname']
        return redirect('users')
    except KeyError :
        pass
    return redirect('users')

