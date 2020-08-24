from django.shortcuts import render
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
