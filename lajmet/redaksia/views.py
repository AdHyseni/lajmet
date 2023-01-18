from django.shortcuts import render, redirect,get_object_or_404
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from .forms import UserRegisterForm,LajmiForm
from django.core.mail import send_mail
from django.core.mail import EmailMultiAlternatives
from django.template.loader import get_template
from flash.models import Lajmi
from django.views.generic import ListView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin


  

class StartingPage(LoginRequiredMixin,ListView):
    login_url = 'login/'
    redirect_field_name = 'redaksia/login/'
    template_name = 'user/index.html'
    model = Lajmi
    context_object_name = 'lajmet'
    ordering = ['-data']

    def get_queryset(self):
        query_set= super().get_queryset()
        data = query_set[:1]
        return data
    

  
########### register here #####################################
def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')
            ######################### mail system ####################################
            htmly = get_template('user/Email.html')
            d = { 'username': username }
            subject, from_email, to = 'welcome', 'your_email@gmail.com', email
            html_content = htmly.render(d)
            msg = EmailMultiAlternatives(subject, html_content, from_email, [to])
            msg.attach_alternative(html_content, "text/html")
            msg.send()
            ##################################################################
            messages.success(request, f'Your account has been created ! You are now able to log in')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'user/register.html', {'form': form, 'title':'register here'})
  
################ login forms###################################################
def Login(request):
    if request.method == 'POST':
  
        # AuthenticationForm_can_also_be_used__
  
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username = username, password = password)
        if user is not None:
            form = login(request, user)
            messages.success(request, f' welcome {username} !!')
            return redirect('index')
        else:
            messages.info(request, f'account done not exit plz sign in')
    form = AuthenticationForm()
    return render(request, 'user/login.html', {'form':form, 'title':'log in'})

@login_required(login_url='/redaksia/login/')
def lajmet_e_mia(request):
    username = None
    if request.user.is_authenticated():
        username = request.user.username
        lajmet = get_object_or_404(Lajmi, autori=username)
    return render(request, 'user/lajmet_e_mia.html',{'lajmet':lajmet})

@login_required(login_url='/redaksia/login/')
def redakto(request):
    if request.method == 'POST':
        form = LajmiForm(request.POST)
        if form.is_valid():
            lajmi = form.save(commit=False)
            lajmi.autori = request.user
            lajmi.save()
    else:
        return render(request, 'user/redakto.html', {'form': LajmiForm()})

@login_required(login_url='/redaksia/login/')
def lajmi(request, id):
    lajmi = get_object_or_404(Lajmi,id=id)
    form = LajmiForm(instance=lajmi)
    return render(request, 'user/lajmi.html', {'lajmi':lajmi,'form':form})
    

def update(request, id):
    lajmi = Lajmi.objects.get(id=id)
    form = LajmiForm(instance=lajmi)
    return redirect(request,'lajmi-redaksia',id=lajmi.id)

def delete(request, id):
    context ={}
    obj = get_object_or_404(Lajmi, id = id)
    if request.method =="POST":
        obj.delete()
        return redirect("redaksia/")
 
    return render(request, "delete_view.html", context)