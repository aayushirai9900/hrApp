import email
from django.shortcuts import render,redirect
from django.db.models import Q
from . models import User


# Create your views here.

 

def create_profile(request):
    if request.method=="POST":
        user=User()
        user.name=request.POST['name']
        user.email=request.POST['email']
        user.location=request.POST['location']
        user.phone_number=request.POST['phone_number']
        user.skills=request.POST['skills'] 

        #user=User.objects.create_user(username=name, email=email,location=location,phone_number=phone_number,slills=skills)
        user.save();
        print("user created")
        return render(request, "hr_app/show.html")
    else:
        return render(request, "hr_app/create_profile.html")



def display_data(request):
    if request.method=="GET":
        query=request.GET.get('query')
        if query:
            #data=User.objects.filter(location__contains=query)
            multi_data=Q(Q(location__contains=query)|Q(skills__contains=query))
            data=User.objects.filter(multi_data)
            ab={
                "data1": data
              }
            return render(request,"hr_app/display_profile.html", ab)
        else:
            print("no information to show")
            return render(request,"hr_app/display_profile.html",{})


   
    
   


