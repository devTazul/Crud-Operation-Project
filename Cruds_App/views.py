import os

from django.shortcuts import render, redirect
from .models import Profile


# Create your views here.
def HOME(request):
    sch = request.GET.get('search')
    if sch:
        prof = Profile.objects.filter(Name__icontains=sch)
    else:
        prof = Profile.objects.all()
    return render(request, 'home.html', {'prof': prof})


def UPDATE(request, id):
    prof = Profile.objects.get(id=id)
    if request.method == "POST":
        Name = request.POST.get('Name')
        Email = request.POST.get('Email')
        Age = request.POST.get('Age')
        Image = request.FILES.get('Image')
        Address = request.POST.get('Address')
        Phone_Number = request.POST.get('Phn_Num')
        Date_Of_Birth = request.POST.get('Date_Of_Birth')
        Gender = request.POST.get('Gender')
        Religion = request.POST.get('Religion')

        if Image:
            if prof.Image != 'default.png':
                os.remove(prof.Image.path)
            prof.Image = Image
            prof.Name = Name
            prof.Email = Email
            prof.Age = Age
            prof.Address = Address
            prof.Phone_Number = Phone_Number
            prof.Date_Of_Birth = Date_Of_Birth
            prof.Gender = Gender
            prof.Religion = Religion
            prof.save()

        else:
            prof.Name = Name
            prof.Email = Email
            prof.Age = Age
            prof.Address = Address
            prof.Phone_Number = Phone_Number
            prof.Date_Of_Birth = Date_Of_Birth
            prof.Gender = Gender
            prof.Religion = Religion
            prof.save()

    return render(request, 'update.html', {'prof': prof})


def CREATE(request):
    if request.method == "POST":
        Name = request.POST.get('Name')
        Email = request.POST.get('Email')
        Age = request.POST.get('Age')
        Image = request.FILES.get('Image')
        Address = request.POST.get('Address')
        Phone_Number = request.POST.get('Phn_Num')
        Date_Of_Birth = request.POST.get('Date_Of_Birth')
        Gender = request.POST.get('Gender')
        Religion = request.POST.get('Religion')

        if Image:
            prof = Profile(Name=Name, Email=Email, Age=Age, Image=Image, Address=Address, Phone_Number=Phone_Number,
                           Date_Of_Birth=Date_Of_Birth, Gender=Gender, Religion=Religion)
            prof.save()

        else:
            prof = Profile(Name=Name, Email=Email, Age=Age, Address=Address, Phone_Number=Phone_Number,
                           Date_Of_Birth=Date_Of_Birth, Gender=Gender, Religion=Religion)
            prof.save()
    return render(request, 'create.html')


def SEE_PROFILE(request, id):
    prof = Profile.objects.get(id=id)
    return render(request, 'seeProfile.html', locals())


def DELETE(request, id):
    prof = Profile.objects.get(id=id)
    if prof.Image != 'default.png':
        os.remove(prof.Image.path)
    prof.delete()
    return redirect(request,'home')
