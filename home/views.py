from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.shortcuts import render,redirect
from django.contrib.auth import logout,login
from home.models import Addgoal
import requests
# Create your views here.
def index(request):
    if request.user.is_anonymous:
        return redirect("/login")
    url = "https://api.razorpay.com/v1/orders"
    payload={}
    headers = {
    'Authorization': 'Basic cnpwX3Rlc3RfcWJjNnZtNXlOQ0M4SWo6b2k1S1ZtZE5qVkJLRE9YT0hFY3ZtZ1dH'
    }
    response = requests.request("GET", url, headers=headers, data=payload)
    #print(response.text)
    
    response = response.json()
    # print(response)
    cnt = response['count']
    # print(type(cnt))
    goal = response['items'][0]['notes']['goal_name']
    temp=0
    total=0
    for i in range(0,cnt):
        temp = response['items'][i]['amount']/100
        total += temp
    # for key ,value in data.items():
    # print(total)
    context = {
        'rice': total,
        'aim': goal
    }
    return render(request, 'index.html', context)


def loginUser(request):    
    if request.method=="POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            # A backend authenticated the credentials
            login(request,user)
            return redirect("/")
        else :
            # No backend authenticated the credentials
            return render(request, 'login.html')
    return render(request, 'login.html')

def logoutUser(request):
    logout(request)    
    redirect("/login")

def addgoal(request):
    if request.method == "POST":
        gname = request.POST.get('gname')
        desc = request.POST.get('desc')
        addgoal = Addgoal(gname=gname , desc=desc)
        addgoal.save()
    return render(request, 'addgoal.html')
   # return redirect("/addgoal")

def removegoal(request):
    return render(request, 'removegoal.html')
"""


def payment():
    url = "https://api.razorpay.com/v1/orders"
    payload={}
    headers = {
    'Authorization': 'Basic cnpwX3Rlc3RfcWJjNnZtNXlOQ0M4SWo6b2k1S1ZtZE5qVkJLRE9YT0hFY3ZtZ1dH'
    }
    response = requests.request("GET", url, headers=headers, data=payload)
    #print(response.text)
    
    response = response.json()
    # print(response)
    cnt = response['count']
    # print(type(cnt))
    temp=0
    total=0
    for i in range(0,cnt):
        temp = response['items'][i]['amount']
        total += temp
    # for key ,value in data.items():
    print(total)

    
if __name__ == "__main__":
    payment()

"""