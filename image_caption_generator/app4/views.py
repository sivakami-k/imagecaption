from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Login,Parent,Child,Awareness,Review
from django.contrib.auth import authenticate,login,logout
import datetime

# Create your views here.

def login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        try:
            data = Login.objects.get(username=username,password=password)
            if data is not None:
                request.session['id'] = data.id
                if data.type=='Admin':
                    return redirect(adminhome)
                elif data.type=='Parent' and data.Status=='accepted':
                    return redirect(parenthome)
                elif data.type=='Child':
                    return redirect(childhome)
                else:
                    return render(request,'login.html',{'error':'Waiting for admin approval'})

            else:
                return render(request, 'login.html',{'error':'invalid credentials'})
        except Exception as e:
            return render(request, 'login.html',{'error':'invalid credentials'})
    else:
        return render(request,'login.html')
    

def register(request):
    if request.method== 'POST':
        name=request.POST['name']
        email=request.POST['email']
        if Login.objects.filter(username=email):
            return render(request,'signup.html',{'data':'Email already registered'})
        dob=request.POST['dob']
        gender=request.POST['gender']
        country=request.POST['country']
        state=request.POST['state']
        city=request.POST['city']
        pin=request.POST['pin']
        phone=request.POST['phone']
        if Login.objects.filter(phone=phone):
            return render(request,'signup.html',{'data':'Phone number  already registered'})
        password=request.POST['password']
        confirm_password=request.POST['confirm_password']
        if password!=confirm_password:
            return render(request,'signup.html',{'data':'Password not matching'})

        data1=Login.objects.create(username=email,password=password,type="Parent")
        data1.save()
        
        data=Parent.objects.create(login=data1,name=name,
                                    email=email,
                                    dob=dob,
                                    gender=gender,
                                    country=country,
                                    state=state,
                                    city=city,
                                    pin=pin,
                                    phone=phone
                                            )
        data.save()
        return render(request,'login.html')
    else:
        return render(request,'signup.html')

def landing(request):
    return render(request,'landingpage.html')

def logout(request):
    # if 'id' in request.session:
        request.session.flush()
        return redirect(landing)
    # else:
    #     return HttpResponse("logout")

################################################


def adminhome(request):
    return render(request,'admin/adminhome.html')

def manage_user(request):
    data=Parent.objects.all()
    return render(request,'admin/usermanage.html',{'data':data})

def accept(request,id):
    data=Login.objects.get(id=id)
    print(data)
    if request.method=='POST':
        data1=request.POST['status']
        print(data1)
        if data1=='accepted':
            data.Status='accepted'
        elif data1=='rejected':
            data.Status='rejected'
        data.save()
        return redirect(manage_user)


def adminreview(request):
    data=Review.objects.all()
    return render(request,'admin/admin_viewreview.html',{'data':data})

def addinstruction(request):
    if request.method =='POST':
        instructions=request.POST['instructions']
        obj=Awareness.objects.create(instructions=instructions)
        obj.save()
        return redirect(admin_viewawareness)
    else:
        return render(request,'admin/add_awareness.html')
    
def addawareness(request):
    if request.method =='POST':
        videos=request.FILES['videos']
        obj=Awareness.objects.create(awareness_videos=videos)
        obj.save()
        return redirect(admin_viewawareness)
    else:
        return render(request,'admin/add_awareness.html')
    
# def addawareness(request):
#     if request.method =='POST':
#         instructions=request.POST['instructions']
#         awareness_videos=request.FILES['videos']
    
#         obj=Awareness.objects.create(instructions=instructions,awareness_videos=awareness_videos)
#         obj.save()
#         return redirect(admin_viewawareness)

#     else:
#         return render(request,'admin/add_awareness.html')

def admin_viewawareness(request):
    data=Awareness.objects.all()
    return render(request,'admin/admin_viewawareness.html',{'data':data})

def delete_awareness(request,id):
    data=Awareness.objects.get(id=id)
    data.delete()
    return redirect(admin_viewawareness)

    

# def studentreg(request):
#     if request.method=='POST':
#         name=request.POST.get('name')
#         username=request.POST.get('username')
#         if student.objects.filter(username=username):
#             return render(request,'',{'message':'username already exists'})
#         password=request.POST.get('password')
#         data1=login.objects.create(username=username,password=password,usertype="student")
#         data1.save()
#         data =student.objects.create(login_id=data1,name=name)
#         data.save()

################################################


def parenthome(request):
    return render(request,'parent/parenthome.html')

def viewprofile(request):
    data=request.session['id']
    data1=Login.objects.get(id=data)
    data2=Parent.objects.get(login=data1.id)
    return render(request,'parent/viewprofile.html',{'data':data2})

def editprofile(request,id):
    data=Parent.objects.get(id=id)
    if request.method=='POST':
        data.name=request.POST['name']
        data.email=request.POST['email']
        data.dob=request.POST['dob']
        
        data.country=request.POST['country']
        data.state=request.POST['state']
        data.city=request.POST['city']
        data.pin=request.POST['pin']
        data.phone=request.POST['phone']

        data.save()
        return render(request,'parent/viewprofile.html',{'data':data})
    else:  
        return render(request,'parent/editprofile.html',{'data':data})

def changepw(request):
    data=request.session['id']
    data1=Login.objects.get(id=data)
    if request.method=='POST':
        current_password=request.POST['current_password']
        new_password=request.POST['new_password']
        confirm_password=request.POST['confirm_password']
        if new_password!=confirm_password:
            return render(request,'parent/changepassword.html',{'message':'Password not matching'})
        
        else:
            data1.password=confirm_password
            data1.save()
            return render(request,'parent/changepassword.html',{'message':'Password changed successfully'})
    else:
        return render(request,'parent/changepassword.html')

def vision(request):
    return render(request,'parent/visionverb.html')

def addreview(request):
    data=request.session['id']
    data1=Login.objects.get(id=data)
    data2=Parent.objects.get(login=data1.id)
    if request.method=='post':
        review=request.POST['review']
        date=datetime.datetime.now().date()
        obj=Review.objects.create(login=data1,parent=data2,date=date,review=review)
        obj.save()
        return redirect(parentreview)
    else:
        return render(request,'parent/add_review.html')

def parentreview(request):
    data=request.session['id']
    data1=Login.objects.get(id=data)
    data2=Parent.objects.get(login=data1.id)
    data3=Review.objects.filter(parent=data2.id)
    return render(request,'parent/parent_viewreview.html',{'data':data3})

def parent_viewawareness(request):
    data=Awareness.objects.all()
    return render(request,'parent/parent_viewawareness.html',{'data':data})
    

def addchild(request):
    data=request.session['id']
    data1=Login.objects.get(id=data)
    data2=Parent.objects.get(login=data1.id)
    if request.method== 'POST':
        name=request.POST['name']
        dob=request.POST['dob']
        gender=request.POST['gender']
        disability_type=request.POST['disability_type']
        disability_percentage=request.POST['disability_per']
        username=request.POST['username']
        if Login.objects.filter(username=username):
            return render(request,'parent/add_child.html',{'message':'Username already exists'})
        password=request.POST['password']
        confirm_password=request.POST['confirm_password']
        if password!=confirm_password:
            return render(request,'parent/add_child.html',{'message':'Password not matching'})

        obj=Login.objects.create(username=username,password=password,type="Child",Status="accepted")
        obj.save()
        
        data2=Child.objects.create(login=data1,parent=data2,name=name,
                                    dob=dob,
                                    gender=gender,
                                    disability_type=disability_type,
                                    disability_percentage=disability_percentage,
                                            )
        data2.save()
        return redirect(parenthome)
    else:
        return render(request,'parent/add_child.html')

    

def parent_viewchild(request):
    data=request.session['id']
    data1=Login.objects.get(id=data)
    data2=Parent.objects.get(login=data1.id)
    data3=Child.objects.filter(parent=data2.id)
    return render(request,'parent/parent_viewchild.html',{'data':data3})

def editchild(request,id):
    data=Child.objects.get(id=id)
    if request.method=='POST':
        data.name=request.POST['name']
        data.dob=request.POST['dob']
        data.disability_type=request.POST['disability_type']
        data.disability_percentage=request.POST['disability_per']
        data.save()
        return redirect(parent_viewchild)
    else:
        return render(request,'parent/edit_child.html',{'data':data})

################################################



def childhome(request):
    return render(request,'child/childhome.html')

def vision2(request):
    return render(request,'child/visionverb2.html')