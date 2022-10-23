from django.shortcuts import render

# Create your views here.
def homepage(request):
	return render(request,'index.html')

def contactuspage(request):
	return render(request,'contactus.html')

def patientclickpage(request):
	return render(request,'patientclick.html')

#for showing signup/login button for doctor(by sumit)
def doctorclick(request):
    # if request.user.is_authenticated:
    #     return HttpResponseRedirect('afterlogin')
    return render(request,'doctorclick.html')

#for showing signup/login button for admin(by sumit)
def adminclick(request):
    # if request.user.is_authenticated:
    #     return HttpResponseRedirect('afterlogin')
    return render(request,'adminclick.html')