from django.shortcuts import render

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
     template_name="polls/forms.html"
     context={"form":form}
     return render(request,template_name,context)
