from django.http.response import HttpResponse
from django.shortcuts import render, redirect
from mansimehndiratta.models import Contact
from mansimehndiratta.models import Blogs
from datetime import datetime
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from misc_files.generic_function import otp_generate, otp_send
from django.core.files.storage import FileSystemStorage
from mansimehndiratta.forms import *

# Create your views here.
def index(request):
    data={}
    data['blogs']= Blogs.objects.all()
    return render(request, 'index.html', data)


def aboutus(request):
    return render(request, 'about.html')


def contactus(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')
        contact = Contact(name=name, email=email, phone=phone, desc=desc, date=datetime.today())
        contact.save()
        messages.success(request, 'Your message has been received!.')
    return render(request, 'contact.html')


def projects(request):
    return render(request, 'projects.html')


def experiences(request):
    return render(request, 'experiences.html')


def internships(request):
    return render(request, 'internships.html')


def signup(request):
    if request.method == "POST":
        try:
            usernameup= request.POST.get('usernameup')
            emailup = request.POST.get('emailup')
            nameup = request.POST.get('nameup')
            passup1 = request.POST.get('passup1')
            passup2 = request.POST.get('passup2')

            #check for errors
            if passup1 != passup2:
                messages.warning(request,'Passwords do not match')
                return redirect('/')
            if not usernameup.isalnum():
                messages.warning(request, 'Username can only contain a-z,A-Z,0-9')
                return redirect('/')
            if len(passup1) < 8:
                messages.warning(request,'Password is too short')
                return redirect('/')

            #verify
            otp = otp_generate()
            otp_send(otp,emailup)
            request.session['usernameup'] = usernameup
            request.session['nameup']=nameup
            request.session['emailup']=emailup
            request.session['passup1']=passup1
            request.session['otp']=otp
            return redirect('/otp_verification')
            # otp = otp_generate()
            # otp_send(otp,emailup)
            # otp_verification(request,usernameup,emailup,nameup,passup1,passup2,otp)
            # data = {'usernameup':usernameup,'emailup':emailup, 'nameup':nameup, 'passup1':passup1, 'passup2':passup2, 'otp':otp}
            # return redirect('collect')
            # otp = otp_generate()
            # otp_send(otp,emailup)
            # for i in range(3):
            #     otp_received= collect_otp(request)
            #     if otp_received==otp:
            #         email_verification = True
            #         break
            #     else:
            #         messages.warning(request, "OTP Incorrect!, Enter Correct OTP. 2 more chances left")
            # messages.warning(request, "Email Verification failed. Sign Up Again")
            # return redirect('/')
            # #create user
            # if email_verification:
            #     myuser = User.objects.create_user(usernameup, emailup, passup1)
            #     myuser.first_name=nameup
            #     myuser.save()
            #     user = myuser
            #     login(request,user)
            #     messages.success(request,'Account created and logged in successfully!')
            #     return redirect('/')


        except IntegrityError as e:
            messages.warning(request, 'Username already exists! Choose another')
    return redirect('/')


def signin(request):
    if request.method == "POST":
        usernamein = request.POST.get('usernamein')
        passin = request.POST.get('passin')
        user = authenticate(username=usernamein, password=passin)
        if user:
            login(request, user)
            messages.success(request,'Logged In Successfully!')
        else:
            messages.warning(request, 'Invalid Credentials!! Please Try Again')
    return redirect('/')


def signout(request):
    logout(request)
    messages.success(request, 'Logged Out Successfully!')
    return redirect('/')


def otp_verification(request):
    if request.method=="POST":
        try:
            emailup=request.session['emailup']
            usernameup=request.session['usernameup']
            nameup=request.session['nameup']
            passup1=request.session['passup1']
            otp = request.session['otp']
            otp_received= request.POST.get("otp_received")
            print(otp_received)
            print(otp)
            if str(otp_received)!=str(otp):
                messages.warning(request, "OTP Incorrect!,Try again")
                return redirect('/')
                
            else:
                #create user
                myuser = User.objects.create_user(usernameup, emailup, passup1)
                myuser.first_name=nameup
                myuser.save()
                user = myuser
                login(request,user)
                messages.success(request,'Account created and logged in successfully!')
                return redirect('/')
        except IntegrityError as e:
            messages.warning(request, 'Username already exists! Choose another')
            return redirect('/')
    return render(request,"otp.html")


def profile(request,requested_user):
    if request.path == '/profile/'+str(request.user)+'/':
        blogs= Blogs.objects.filter(writer=request.user)
        context ={"blogs": blogs}
        return render(request, 'profile.html',context )
    elif User.objects.filter(username=requested_user):
        blogs= Blogs.objects.filter(writer=requested_user)
        context={'requested_user':requested_user,
                'blogs':blogs                              }
        return render(request,'guest_profile.html',context)
    else:
        return HttpResponse("User doesn't exist!!")
    # return render(request, 'profile.html')


def add_blog(request):
    if request.method=="POST":
        blogtitle= request.POST.get("blogtitle")
        blogcontent=request.POST.get("blogcontent")
        blogwriter= str(request.user)
        readtime= "10 min"
        current_no_of_blogs= len(Blogs.objects.filter(writer=request.user))
        id= str(request.user)+"_"+str(current_no_of_blogs+1)
        # pdf=request.POST.get("contentfile")
        title_image=request.FILES.get("title_image")
        form = BlogsForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('success')
        else:
            form = BlogsForm()
        print("hello", title_image)
        blog= Blogs(id=id,read_time=readtime,writer=blogwriter,content=blogcontent,title=blogtitle, title_image=title_image)
        blog.save()
    return redirect('/profile/'+str(request.user)+'/')


def view_blog(request, blog_id, blog_title):
    blog=Blogs.objects.get(id=blog_id)
    content={'blog':blog}
    return render(request,"blog_page.html",content)



def title_img_view(request):
  
    if request.method == 'POST':
        form = Title_img_uploadForm(request.POST, request.FILES)
  
        if form.is_valid():
            form.save()
            return redirect('success')
    else:
        form = Title_img_uploadForm()
    return render(request, 'blog_page.html', {'form' : form})
  
  
def success(request):
    return HttpResponse('successfully uploaded')








