from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,logout,login
from .models import Doctor,Patient,Appointment
import traceback

# Create your views here.
def About(request):
    return render(request,'about.html')

def Contact(request):
    return render(request,'contact.html')

def Index(request):
    print("Index:",request.user.is_staff )
    if not request.user.is_staff:
        return redirect('login')
    doctor = Doctor.objects.all()
    patient = Patient.objects.all()
    appointment = Appointment.objects.all()
    d,p,a = 0,0,0
    for i in doctor:
        d = d+1
    for j in patient:
        p = p+1
    for k in appointment:
        a = a+1
    d1 = {'d':d,'p':p,'a':a}
    print(d1)
    return render(request,'index.html',d1)

def Login(request):
    error = ""
    if request.method == "POST":
        n = request.POST['aname']
        p = request.POST['apwd']
        user = authenticate(username=n,password=p)
        print(user)
        print(n,' ',p)
        print("Login:",user.is_staff)
        # print(user.is_superuser)
        # print(user.is_authenticated)
        try:
            if user.is_staff:
                login(request,user)
                error = "no"
            else:
                error = "yes"
        except:
            error = "yes"
    print(error)
    d = {'error':error}
    return render(request,'login.html',d)

def Logout(request):
    print("logout:",request.user.is_staff)
    if not request.user.is_staff:
        return redirect('login')
    logout(request)
    return render(request,'login.html')


def View_Doctor(request):
    print("logout:",request.user.is_staff)
    if not request.user.is_staff:
        return redirect('login')
    doc = Doctor.objects.all()
    d = {'doc':doc}
    return render(request,'view_doctor.html',d)


def Add_Doctor(request):
    error = ""
    if not request.user.is_staff:
        return redirect('login')

    if request.method == "POST":
        dn = request.POST['dname']
        dc = request.POST['dcontact']
        ds = request.POST['dspecial']

        try:
            d_entry = Doctor.objects.create(name=dn,mobile=dc,special=ds)
            d_entry.save()
            error = "no"
        except:
            error = "yes"
    print(error)
    d = {'error':error}
    return render(request,'add_doctor.html',d)

def Delete_Doctor(request,pid):
    if not request.user.is_staff:
        return redirect('login')
    doct = Doctor.objects.get(id=pid)
    doct.delete()
    return redirect('view_doctor')

def View_Patient(request):
    print("logout:",request.user.is_staff)
    if not request.user.is_staff:
        return redirect('login')
    pat = Patient.objects.all()
    d = {'pat':pat}
    return render(request,'view_patient.html',d)

def Add_Patient(request):
    error = ""
    if not request.user.is_staff:
        return redirect('login')

    if request.method == "POST":
        pn = request.POST['pname']
        pc = request.POST['mobile']
        pg = request.POST['gender']
        pa = request.POST['address']

        try:
            p_entry = Patient.objects.create(name=pn,gender=pg,mobile=pc,address=pa)
            p_entry.save()
            error = "no"
        except:
            error = "yes"
    print(error)
    d = {'error':error}
    return render(request,'add_patient.html',d)

def Delete_Patient(request,pid):
    if not request.user.is_staff:
        return redirect('login')
    pat = Patient.objects.get(id=pid)
    pat.delete()
    return redirect('view_patient')

def View_Appointment(request):
    print("logout:",request.user.is_staff)
    if not request.user.is_staff:
        return redirect('login')
    appoint = Appointment.objects.all()
    d = {'appoint':appoint}
    return render(request,'view_appointment.html',d)

def Add_Appointment(request):
    error = ""
    if not request.user.is_staff:
        return redirect('login')

    doctor1 = Doctor.objects.all()
    patient1 = Patient.objects.all()
    if request.method == "POST":
        ad = request.POST['doctor']
        ap = request.POST['patient']
        adt = request.POST['date']
        at = request.POST['time']

        doctor = Doctor.objects.filter(name=ad).first()
        patient = Patient.objects.filter(name=ap).first()
        try:
            a_entry = Appointment.objects.create(doctor=doctor,patient=patient,date1=adt,time1=at)
            a_entry.save()
            error = "no"
        except:
            traceback.print_exc()
            error = "yes"
    print(error)
    d = {'error':error,'doctor':doctor1,'patient':patient1}
    return render(request,'add_appointment.html',d)

def Delete_Appointment(request,pid):
    if not request.user.is_staff:
        return redirect('login')
    ap = Appointment.objects.get(id=pid)
    ap.delete()
    return redirect('view_appointment')