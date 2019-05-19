from django.shortcuts import render
from .models import Users
from django.http import HttpResponseRedirect
import django.core.exceptions



from django.shortcuts import redirect


# Create your views here.


def users(request):
    if request.method == 'POST':
        yin = request.POST['usertxt']
        try:
            yan = str(Users.objects.get(user_id=request.POST['usertxt']))
        except yan.ObjectDoesNotExist:
            pass
        if yin == yan:
            member_id = Users.objects.get(user_id=request.POST['usertxt'])
            request.session['firstname'] = member_id.firstname
            print(request.session['firstname'])
            return HttpResponseRedirect('/clock/')
                 
        else:
            return redirect('users')
    else:
        userz = Users.objects.all()
        print(request.method)
        return render(request, "App_users/login.html", {"use": userz})
