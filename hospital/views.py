from django.shortcuts import render,redirect,reverse
from . import forms,models

from django.http import HttpResponseRedirect





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


# -----------------------------------------------

def patient_signup(request):
    userForm=forms.PatientUserForm()
    patientForm=forms.PatientForm()
    mydict={'userForm':userForm,'patientForm':patientForm}
    
    if request.method=='POST':
        userForm=forms.PatientUserForm(request.POST)
        patientForm=forms.PatientForm(request.POST,request.FILES)
        if userForm.is_valid() and patientForm.is_valid():
            user=userForm.save()
            user.set_password(user.password)
            user.save()
            patient=patientForm.save(commit=False)
            patient.user=user
            patient=patient.save()
          
    
        return HttpResponseRedirect('patientlogin')
    return render(request,'patientsignup.html',context=mydict)

# @login_required(login_url='patientlogin')
# @user_passes_test(is_patient)
# def patient_dashboard(request):
#     patient=models.Patient.objects.get(user_id=request.user.id)
#     doctor=models.Doctor.objects.get(user_id=patient.assignedDoctorId)
#     mydict={
#     'patient':patient,
#     'doctorName':doctor.get_name,
#     'doctorMobile':doctor.mobile,
#     'doctorAddress':doctor.address,
#     'symptoms':patient.symptoms,
#     'doctorDepartment':doctor.department,
#     'admitDate':patient.admitDate,
#     }
#     return render(request,'patient_dashboard.html',context=mydict)

def createaccount(request):
    return render(request,'createaccount.html')
    