from django.shortcuts import redirect, render
from .models import Profile
from django.contrib.auth.models import User
from django.contrib.auth import login,authenticate,logout
from django.contrib import messages
from .froms import CustomUserCreationForm
# Create your views here.
def loginUser(request):
    page = 'login'
    context = {'page':page}
    if request.user.is_authenticated:
        return redirect('profiles')

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        try:
            user = User.objects.get(username = username)
        except:
            messages.error(request, "Username does not exist")
        user = authenticate(request,username = username,password = password)
        if user is not None:
            login(request,user)
            return redirect('profiles')
        else:
            messages.error(request, "username or password is incorrect")
    return render(request,"users/login_registrer.html")

def logoutUser(request):
    logout(request)
    messages.info(request, "User successfully logged out")
    return redirect('login')

def registerUser(request):
    page = 'register'
    form = CustomUserCreationForm()
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            messages.success(request,"Account was created")
            login(request,user)
            return redirect('profiles')
        else:
            messages.error(request,"An error was occurred during registration")
    context = {'page':page,'form':form}
    return render(request,"users/login_registrer.html",context)

def profiles(request):
    profiles = Profile.objects.all()
    context = {'profiles':profiles}
    return render(request,"users/profiles.html",context)

def userProfile(request,pk):
    user = Profile.objects.get(id=pk)
    topSkills = user.skills_set.exclude(description__exact = "")
    otherSkills = user.skills_set.filter(description = "")
    context = {'profile':user,"topSkills":topSkills,"otherSkills":otherSkills}
    return render(request,"users/user-profile.html",context)