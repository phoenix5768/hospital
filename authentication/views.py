from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from . models import Patient, Doctor
from django.contrib.auth.decorators import login_required

# Create your views here.


def home(request):
    return render(request, "authentication/index.html")

@login_required
def adminpage(request):
    
    patients = Patient.objects.all()
    #patients_list = {'patients': patients}


    doctors = Doctor.objects.all()
    #doctors_list = {'doctors': doctors}

    return render(request, "authentication/adminpage.html", {'patients': patients, 'doctors': doctors})


def showp(request, patient_id):
    patient = Patient.objects.get(id_number = patient_id)
    

    return render(request, "authentication/showp.html", {'patient': patient})

@login_required
def patient(request):
    if request.method == "POST":
        fname = request.POST['fname']
        lname = request.POST['lname']
        mname = request.POST['mname']
        iin = request.POST['iin']
        dob = request.POST['dob']
        blood = request.POST['blood']
        emergency = request.POST['emergency']
        num = request.POST['num']
        email = request.POST['email']
        address = request.POST['address']
        martial = request.POST['martial']


        if Patient.objects.filter(iin_number = iin):
            messages.error(request, "Patient alreaedy exists!")
            return redirect('patient')
        
        if Patient.objects.filter(email = email):
            messages.error(request, "Email already exists!")
            return redirect('patient')
        

        mypatient = Patient.objects.create(fname = fname, lname = lname, mname = mname, iin_number = iin, date_of_birth = dob,
                                            blood_group = blood, emergency_contact_number = emergency, contact_number = num,
                                            email = email, address = address, martial_status = martial)
        
        mypatient.save()

        messages.success(request, "The patient has been successfully registered.")


        return redirect('adminpage')

    return render(request, "authentication/patient.html")


@login_required
def doctor(request):
    if request.method == "POST":
        fname = request.POST['fname']
        lname = request.POST['lname']
        mname = request.POST['mname']
        iin = request.POST['iin']
        dob = request.POST['dob']
        num = request.POST['num']
        department = request.POST['department']
        specialization = request.POST['specialization']
        experience = request.POST['experience']
        category = request.POST['category']
        price = request.POST['price']
        schedule = request.POST['schedule']
        degree = request.POST['degree']
        rating = request.POST['rating']
        address = request.POST['address']


        if Doctor.objects.filter(iin_number = iin):
            messages.error(request, "Doctor alreaedy exists!")
            return redirect('doctor')


        mydoctor = Doctor.objects.create(fname = fname, lname = lname, mname = mname, iin_number = iin, date_of_birth = dob,
                                            contact_number = num, department_id = department, specialization_details_id = specialization,
                                            experience = experience, category = category, price = price, schedule_details = schedule,
                                            education = degree, rating = rating, address = address,)
        
        mydoctor.save()

        messages.success(request, "The doctor has been successfully registered.")


        return redirect('adminpage')



    return render(request, "authentication/doctor.html")


def signin(request):

    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username = username, password = password)

        if user is not None: 
            login(request, user)
            fname = user.first_name
            return render(request, "authentication/adminpage.html", {"fname": fname})
        
        else:
            messages.error(request, "Error")
            return redirect('home')

    return render(request, "authentication/signin.html")

def signout(request):
    logout(request)
    messages.success(request, "Logged out successfully")
    return redirect('home')

