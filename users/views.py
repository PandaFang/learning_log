from django.shortcuts import render

# Create your views here.
from django.contrib.auth import login, logout, authenticate
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm


def logout_view(request):
    logout(request)
    return redirect('/')


def register(request):
    ''' 注册账户 '''
    if request.method != 'POST':
        form = UserCreationForm()
    else:
        form = UserCreationForm(data=request.POST)
        if form.is_valid():
            new_user = form.save()
            authenticated_user = authenticate(username=new_user.username,
                                              password = request.POST['password1'])
            login(request, authenticated_user)
            return redirect('/')

    context = {'form':form}
    return render(request, 'users/register.html', context=context)