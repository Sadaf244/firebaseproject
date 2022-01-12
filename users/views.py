from django.shortcuts import render
import pyrebase
from django.core.files.storage import FileSystemStorage
# Create your views here.
config={
    "apiKey": "AIzaSyC9xEEPSAqirpNED1lKSQCbutfl5I81seA",
    "authDomain": "taskproject-59ac8.firebaseapp.com",
    "projectId": "taskproject-59ac8",
    "storageBucket": "taskproject-59ac8.appspot.com",
    "databaseURL": "https://taskproject-59ac8-default-rtdb.firebaseio.com",
    "messagingSenderId": "1026386388483",
    "appId": "1:1026386388483:web:136632022ac82153f51036",
    "measurementId": "G-R0EG4ZDQYP"
}
firebase=pyrebase.initialize_app(config)
database=firebase.database()
storage=firebase.storage()
auth=firebase.auth()

def signIn(request):
    return render(request,"users/login.html")
def home(request):
    return render(request,"users/home.html")
 
def postsignIn(request):
    email=request.POST.get('email')
    pasw=request.POST.get('pass')
    
    
    try:
        # if there is no error then signin the user with given email and password
        user=auth.sign_in_with_email_and_password(email,pasw)
    except:
        message="Invalid Credentials!!Please ChecK your Data"
        return render(request,"users/login.html",{"message":message})
    session_id=user['idToken']
    request.session['uid']=str(session_id)
    idtoken= request.session['uid']
    a = auth.get_account_info(idtoken)
    a = a['users']
    a = a[0]
    a = a['localId']
    print(a)
    name = database.child('users').child('details').child(a).child('profile').child('username').get().val()
    address = database.child('users').child('details').child(a).child('profile').child('address').get().val()
    dob = database.child('users').child('details').child(a).child('profile').child('dob').get().val()
    img_url = database.child('users').child('details').child(a).child('profile').child('url').get().val()
    context={
        "name":name,
        "address":address,
        "dob":dob,
        "i":img_url
    }
    return render(request,"users/show_user_detail.html",context)
 
def logout(request):
    try:
        del request.session['uid']
    except:
        pass
    return render(request,"users/login.html")
 
def signUp(request):
    return render(request,"users/Registration.html")
 
def postsignUp(request):
    email = request.POST.get('email')
    passs = request.POST.get('pass')
    name = request.POST.get('name')
    try:
        # creating a user with the given email and password
        user=auth.create_user_with_email_and_password(email,passs)
        uid = user['localId']
        print(uid)
    except:
        return render(request, "users/Registration.html",{"message":"Invalid data! Kindly retry"})
        
    data={"name":name,"status":"1","email":email}
    database.child("users").child("details").child(uid).set(data)
    #idtoken = request.session['uid']
    return render(request,"users/login.html")
def reset(request):
    return render(request, "users/reset.html")
 
def postReset(request):
    email = request.POST.get('email')
    try:
        auth.send_password_reset_email(email)
        message  = "A email to reset password is successfully sent"
        return render(request, "users/reset.html", {"msg":message})
    except:
        message  = "Something went wrong, Please check the email you provided is registered or not"
        return render(request, "users/reset.html", {"msg":message})
def profile_create(request):
    return render(request, "users/create_profile.html")
def post_create(request):
    username = request.POST.get('username')
    address = request.POST.get('address')
    dob = request.POST.get('dob')
    url = request.POST.get('url')
    idtoken= request.session['uid']
    a = auth.get_account_info(idtoken)
    a = a['users']
    a = a[0]
    a = a['localId']
    print("info"+str(a))
    
    data = {
        "username":username,
        'address':address,
        "dob":dob,
        'url':url
    }
    print(url)
    # database.child('users').child('a').child('c').child('millis').set(data)
    database.child("users").child("details").child(a).child('profile').set(data)
    name = database.child('users').child('details').child(a).child('profile').child('username').get().val()
    address = database.child('users').child('details').child(a).child('profile').child('address').get().val()
    dob = database.child('users').child('details').child(a).child('profile').child('dob').get().val()
    img_url = database.child('users').child('details').child(a).child('profile').child('url').get().val()
    print(img_url)
    # i = float(time)
    # dat = datetime.datetime.fromtimestamp(i).strftime('%H:%M %d-%m-%Y')
    context={
        "name":name,
        "address":address,
        "dob":dob,
        "i":img_url
    }
    
    return render(request,'users/show_user_detail.html',context)
