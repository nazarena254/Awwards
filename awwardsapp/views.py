from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.http import HttpRequest,Http404,HttpResponse,HttpResponseRedirect
from .models import Profile, Project, Rate
from .email import send_welcome_email
from .forms import *

# Create your views here.
def signup_view(request):
    if request.method=="POST":
        form=SignUpForm(request.POST)
        if form.is_valid:
            form.save()
            #cleaned_data.get()-Any data user submits thru form will be passed to server as strings
            username=form.cleaned_data.get("username")
            password=form.cleaned_data.get("password1")
            name=form.cleaned_data['username']
            email=form.cleaned_data['email']
            send_welcome_email(name, email)
            user=authenticate(username=username, password=password)
            login(request,user)
            return redirect('welcome')
        else:
            form=SignUpForm()
        return render(request, 'registration/signup', {"form":form})     

def welcome(request):
    users=User.object.exclude(id=request.user.id)
    profiles=Profile.objects.all()
    projects=Project.objects.all()
    project_average=Rate.objects.order_by('-scores').first()
    ratings=Rate.objects.all()

    params={
        'users':users,
        'profiles':profiles,
        'projects':projects,
        'project_average':project_average,
        'ratings':ratings,
    }
    return render(request,'awwards/index.html',params)

@login_required
def upload_project(request):
    if request.method=="POST":
        form=UploadProjectForm(request.POST, request.FILES)
        if form.is_valid():
            project=form.save(commit=False)
            project.user=request.user
            project.save()
            return redirect('welcome')
        else:
            form=UploadProjectForm()
        return render(request, 'awwards/project.html',{"form":form}) 

@login_required
def rate_project(request, project_title):
    project=Project.objects.get(title=project_title) 
    rates=Rate.objects.filter(user=request.user,project=project).first()
    ratings=Rate.objects.order_by('-rated_at')
    rates_status=None
    if rates is None:
        rate_status=False
    else:
        rate_status=True

    if request.method=='POST':
        form=RateForm(request.POST)
        if form.is_valid():
            rate=form.save(commit=False)
            rate.user=request.user
            rate.project=project
            rate.save()
            project_ratings=Rate.objects.filter(project=project)

            design = form.cleaned_data['design']
            usability = form.cleaned_data['usability']
            content = form.cleaned_data['content']
            rate.design = design
            rate.usability = usability
            rate.content = content
            rate.average = (rate.design + rate.usability + rate.content)/3
            rate.save()

            design_ratings = [d.design for d in project_ratings]
            design_average = sum(design_ratings) / len(design_ratings)

            usability_ratings = [us.usability for us in project_ratings]
            usability_average = sum(usability_ratings) / len(usability_ratings)

            content_ratings = [content.content for content in project_ratings]
            content_average = sum(content_ratings) / len(content_ratings)
            score = (design_average + usability_average + content_average) / 3

            rate.design_average = round(design_average, 2)
            rate.usability_average = round(usability_average, 2)
            rate.content_average = round(content_average, 2)
            rate.score = round(score, 2)

            rate.save()
            return HttpResponseRedirect(request.path_info)    
    else:
        form=RateForm()

    params ={
      'project':project,
      'rates_status':rates_status,
      'rating_form':form,
      'ratings':ratings,
     }
    return render(request,'awwards/voteproject.html',params)

@login_required
def search_project(request):
       if 'search_project' in request.GET and request.GET["search_project"]:
         title = request.GET.get("search_project")
         searched_projects = Project.search_project(title)
         message = f"{title}"
         return render(request, 'awwards/search_results.html', {'message':message,'results': searched_projects})
       else:
        message = "You haven't searched for any project"
       return render(request, 'awwards/search_results.html', {'message': message})

def profile(request, username):
   current_user = request.user.profile

   profile=Profile.objects.get(user=current_user.user)
   projects=request.user.project.all()
   if request.method == 'POST':
      user_form = UserUpdateForm(request.POST, instance=request.user)
      profile_form = UserProfileForm(request.POST, request.FILES, instance=request.user.profile)
      if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save(commit=False)
            user.profile=profile
            user.profile = request.user.profile
            user.save()

            prof = profile_form.save(commit=False)
            prof.profile=profile
            prof.profile = request.user.profile
            prof.save() 


            return HttpResponseRedirect(request.path_info)
   else:
      user_form = UserUpdateForm(instance=request.user)
      profile_form = UserProfileForm(instance=request.user.profile)
   params = {
        'user_form': user_form,
        'profile_form': profile_form,
        'projects': projects,

    }
   return render(request, 'awwards/profile.html', params)
def profile(request, username):
   current_user = request.user.profile

   profile=Profile.objects.get(user=current_user.user)
   projects=request.user.project.all()
   if request.method == 'POST':
      user_form = UserUpdateForm(request.POST, instance=request.user)
      profile_form = UserProfileForm(request.POST, request.FILES, instance=request.user.profile)
      if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save(commit=False)
            user.profile=profile
            user.profile = request.user.profile
            user.save()

            prof = profile_form.save(commit=False)
            prof.profile=profile
            prof.profile = request.user.profile
            prof.save() 


            return HttpResponseRedirect(request.path_info)
   else:
      user_form = UserUpdateForm(instance=request.user)
      profile_form = UserProfileForm(instance=request.user.profile)
   params = {
        'user_form': user_form,
        'profile_form': profile_form,
        'projects': projects,

    }
   return render(request, 'awwards/profile.html', params)

def user_profile(request, username):
   current_user = request.user
   user_profile = get_object_or_404(User, username=username)
   if request.user == user_profile:
        return redirect('profile', username=request.user.username)
   
   projects=user_profile.project.all()
   
   params = {
        'projects': projects,
        'user_profile':user_profile,

    }
   return render(request, 'awwards/user_profile.html', params)




