from django.shortcuts import render, redirect
from .forms import *
from django.core.exceptions import ObjectDoesNotExist 
# Create your views here.
def register(request):
    if request.method =='POST':
        form =RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form =RegistrationForm()
    return render(request, 'store/index.html',{'form':form})

def dashboard(request):

    if request.method == 'POST':
        u_form = UpdateRegisterForm(request.POST, instance=request.user)
        p_form = UpdateProfileForm(request.POST,request.FILES,instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            return redirect('dashboard')

    else:
        u_form =  UpdateRegisterForm(instance=request.user)
        p_form = UpdateProfileForm(instance=request.user.profile)

    context = {

        'u_form': u_form,
        'p_form': p_form,
    }

    return render(request, 'userapp/dashboard.html',context)