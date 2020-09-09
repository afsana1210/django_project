from django.shortcuts import render,HttpResponse,HttpResponseRedirect
from .models import Signup
from .forms import SignupModelForm
from django.contrib import messages


# Create your views here.
def signup_view(request):
     form=SignupModelForm()
     if request.method=='POST':
       form=SignupModelForm(request.POST)
       if form.is_valid():
        form.save(commit=True)
        context={"message":"User registered successfully"}
        return render(request,"ECP/signin.html",context)
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
        for e in Signup.objects.all():
            if e.email==data and  e.password==data1:
                if e.user=='1':
                    return render(request,"ECP/provider.html")
                else:
                    return render(request,"ECP/consumer.html")
        else:
            messages.error(request, "Invalid Email or Password")
            return render(request,"ECP/signin.html")
    template_name='ECP/signin.html'
    return render(request,template_name)
       