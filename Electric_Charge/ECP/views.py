from django.shortcuts import render,HttpResponse
from .models import Signup
from .forms import SignupModelForm

# Create your views here.
def signup_view(request):
     form=SignupModelForm()
     if request.method=='POST':
       print('hello')
       form=SignupModelForm(request.POST)
       print(request.POST)
       print("request line",form)

       if form.is_valid():
        print("form.cleaned_data")
        form.save(commit=True)
       else:
        print(form.errors)
     template_name="ECP/forms.html"
     context={"form":form}
     return render(request,template_name,context)

def list_view(request):
    # email=self.cleaned_data.get('email')
    qs=Signup.objects.all()
    print("object_list :",qs)
    template_name='ECP/list.html'
    context={'object_list':qs}
    return render(request,template_name,context)

def signin_view(request):
    if request.method=="POST":
        data=request.POST.get("email_id")
        # data=SignupModelForm(request.POST)
        # print(data)
        qs=Signup.objects.all()
    # context={"object_list":qs}
    # if request.method=='POST':
        for objects in qs:
            email=objects.email
            print("email is :" ,email)
        print("data :",data)
        if email==data:
              print("email :",email) 
              return render(request,"ECP/list.html")
        print("email of signin:",email)
       
    template_name='ECP/signin.html'
    return render(request,template_name)
   
    # context={'user':qs.user,'email':qs.email,'password':qs.password}
    # return render(request,template_name)
   
    
    
    # if qs.user==1 and qs.email==request.POST['email'] and qs.password==request.POST['password']:
    #     return render(request,"ECP/list.html")
    # return render(request,"not right")

def signin_view_work(request):
    if request.method=="POST":
        data=request.POST.get("email_id")
        data1=request.POST.get("password")
        qs=Signup.objects.all()
        for objects in qs:
            email=objects.email
            password=objects.password
            print("email is :" ,email)
            print("password is:",password)
            print("data :",data)
            print("data 1 is :",data1)
            if email==data and password==data1:
              print("email :",email)
              print("password :",password) 
              return render(request,"ECP/list.html")
            # else:
                # return HttpResponse("please check your email and password.you're email and password didn't match ","ECP/signin.html")
        print("email of signin:",email)
        print("password of signin :" , password)
       
    template_name='ECP/signin.html'
    return render(request,template_name)