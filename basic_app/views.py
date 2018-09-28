from django.shortcuts import render
from basic_app.forms import UserForm,UserProfileInfoForm,OrderForm
from basic_app.models import UserOrders
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
#for a view to require login

# Create your views here.
def index(request):
    return render(request,'basic_app/index.html')


#decorator to require a user to be logged in in order to logout
@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))


@login_required
def order(request):
    form = OrderForm()
    #ordered = False
    if request.method == "POST":
        form = OrderForm(request.POST)

        if form.is_valid():
            form.save(commit = True)
            return HttpResponseRedirect(reverse('index'))
            #return index(request)
        else:
            print('Form invalid')

    return render(request,'basic_app/order.html',{'form':form})




def register(request):
        registered = False
        if request.method == "POST":
            user_form = UserForm(data=request.POST)
            profile_form = UserProfileInfoForm(data=request.POST)

            if user_form.is_valid() and profile_form.is_valid():
                user=user_form.save()
                #the hasing of the pw
                user.set_password(user.password)
                user.save()

                profile = profile_form.save(commit = False)
                profile.user = user

                if 'profile_pic' in request.FILES:
                    profile.profile_pic = request.FILES['profile_pic']
#the key profile_pic is what we defined in the models
                profile.save()
                registered = True
            else:
                print(user_form.errors,profile_form.errors)
        else:
            user_form = UserForm()
            profile_form = UserProfileInfoForm()

        return render(request,'basic_app/registration.html',
        {'user_form':user_form,
        'profile_form':profile_form,
        'registered':registered})


def user_login(request):

    if request.method == 'POST':

        #grabbing
        #username in green is the same name we gave in the form in login.html
        username = request.POST.get('username')
        password = request.POST.get('password')

#it will automatically authenticate for us
        user = authenticate(username = username, password= password)

        if user:
            if user.is_active:

                #login is imported from django
                login(request,user)
                return HttpResponseRedirect(reverse('index'))

            else:
                return HttpResponse("Account not active")

        else:
            #this printing is in our console / what they tried to login with
            print("someone tried to login and failed")
            print ("Username: {} and password {}".format(username,password))
            return HttpResponse("invalid login details")
    else:
        #if user did not submit anything
        return render(request,'basic_app/login.html',{})
