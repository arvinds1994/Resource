from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .forms import LoginForm, ResourceForm
from django.contrib.auth import authenticate, login, logout
from .models import Resource
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
# Create your views here.
from django.conf.global_settings import EMAIL_HOST_USER


def home_view(request):
    uname = request.session['uname']
    if uname is not None:
        logout(request)
    return render(request, 'resource/homepage.html')

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                request.session['uname'] = username
                #return profile_view(request)
                return redirect('profile')
            else:
                return render(request, 'resource/login.html', {'form': form, 'msg': "Please Enter correct Id and Password!!!"})
    else:
        form = LoginForm()
        return render(request, 'resource/login.html', {'form': form})

@login_required(login_url="/login")
def profile_view(request):
    uname = request.session['uname'].capitalize()
    return render(request, 'resource/profile.html', {'uname': uname})

@login_required(login_url="/login")
def add_resource(request):
    uname = request.session['uname'].capitalize()
    if request.method == 'POST' :
        form = ResourceForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return redirect('profile')
        else:
            return render(request, 'resource/addresource.html', {'form': form, 'msg': "Enter correct data", 'uname': uname})

    else:
        form = ResourceForm()
        return render(request, 'resource/addresource.html', {'form': form, 'uname': uname})

@login_required(login_url="/login")
def view_resource(request):
    resource_list = Resource.objects.order_by('first_name')

    paginator = Paginator(resource_list,10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    #print(paginator,page_number,page_obj)

    try:
        resource_list = paginator.page(page_number)
    except PageNotAnInteger:
        resource_list = paginator.page(1)
    except EmptyPage:
        resource_list = paginator.page(paginator.num_pages)

    uname = request.session['uname'].capitalize()
    return render(request, 'resource/resourcelist.html',{'res_list': resource_list, 'page_obj': page_obj, 'uname': uname})

@login_required(login_url="/login")
def logout_view(request):
    logout(request)
    #return render(request, 'resource/homepage.html')
    return redirect('/')

@login_required(login_url="/login")
def update_view(request, id):
    resource = Resource.objects.get(employee_id = id)

    if request.method == 'POST':

        resource.employee_id = request.POST['empid']
        resource.first_name = request.POST['fname']
        resource.last_name = request.POST['lname']
        resource.email_id = request.POST['email']
        resource.project_name = request.POST['pname']
        resource.team_name = request.POST['tname']
        resource.assigned_work = request.POST['assignwork']

        resource.save()

        recepient = request.POST['email']
        work = request.POST['assignwork']
        send_mail('New Work Assigned', work, EMAIL_HOST_USER, [recepient], fail_silently= False)
        return redirect('/resourcelist')

    return render(request, 'resource/update.html',{'res': resource})

@login_required(login_url="/login")
def delete_view(request, id):
    resource = Resource.objects.get(employee_id=id)
    resource.delete()
    return redirect('/resourcelist')
