from django.shortcuts import render, HttpResponse, redirect
from django.db import IntegrityError
from datetime import datetime
from home.models import Contact, Food, Shopping, Service, User, UserProfile
from django.contrib import messages
import random
# Create your views here.

def index(request):
    return render(request, 'index.html')
    # return HttpResponse('This is HomePage')

def about(request):
    return render(request, 'about.html')

def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')
        contact = Contact(name=name, email=email, phone=phone, desc=desc, date=datetime.today())
        contact.save()
        messages.success(request, "Your message has been sent!")
    return render(request, 'contact.html')

def food(request):
    return render(request, 'food.html')

def shopping(request):
    return render(request, 'shopping.html')

def services(request):
    return render(request, 'services.html')

def outdoors(request):
    return render(request, 'outdoors.html')

def religious(request):
    return render(request, 'religious.html')

def things(request):
    return render(request, 'things.html')

def season(request):
    return render(request, 'season.html')

def food_output(request):
    if request.method == 'POST':
        area = request.POST.get('area')
        subcategory = request.POST.get('subcategory')
        foods = Food.objects.filter(area__icontains=area, subcategory__icontains=subcategory, rating__gt=3.5)

        global curr_user
        existing_user = UserProfile.objects.filter(user=curr_user)
        areaList = ''

        if curr_user == '':
            return render(request, 'food_output.html', {'foods' : foods})

        if existing_user is not None:
            row = UserProfile.objects.get(user=curr_user)
            List_of_Area = row.areaList.split(',')
            List_of_Area.append(area)
            recom_area_list = List_of_Area
            areaList = ','.join(List_of_Area)
            row.areaList = areaList
            row.save()

        else:
            if curr_user != '':
                new_user = {
                    "user" : curr_user,
                    "areaList" : area
                }
            userprofile = UserProfile(**new_user)
            userprofile.save()

        subcategory_list = ['Restaurant', 'Cafe', 'Ice Cream Parlour', 'Tea and Snacks', 'Bakery']
        recom_subcategory = random.choice(subcategory_list)
        recom_area = random.choice(recom_area_list)
        recom = Food.objects.filter(area__icontains=recom_area, subcategory__icontains=recom_subcategory, rating__gt=3.5).first()

        return render(request, 'food_output.html', {'foods' : foods, 'recom' : recom})
    #return render(request, 'output.html', {'foods' : foods})
    else:
        return render(request, 'food.html')
    
def sign_up(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        try:
            user = User.objects.create(username=username, password=password)
            messages.success(request, '{} Your account has been created and you have been successfully logged In'.format(username))
            # Add any additional logic for newly created users
            global curr_user
            curr_user = username
            rand_area_list = ['Cidco Colony', 'Dwarka Corner', 'Gangapur', 'Nashik Main Road', 'Nashik Road', 'Indira Nagar', 'Partherdi Phata']
            rand_area = random.choice(rand_area_list)
            new_user = UserProfile.objects.create(user=username, areaList=rand_area)
            return redirect('home')

        except IntegrityError:
            # User with this username already exists
            # You can customize the error message or redirect the user to a different page
            # error_message = "Username already exists. Please choose a different username."
            messages.error(request, 'Username already exists. Please choose a different username.')
            # return render(request, 'user.html', {'error_message': error_message})
        
    return render(request, 'sign_up.html')

curr_user = ''

def sign_in(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

    # Check if the user exists in the database
        usernames = User.objects.values_list('username', flat=True)
        passwords = User.objects.values_list('password', flat=True)

        if username in usernames and password in passwords:
            global curr_user
            curr_user = username
            messages.success(request, '{} You have been successfully logged In'.format(username))
            return redirect('home')  # Redirect to the home page after successful login
        else:
            messages.error(request, 'Username does not exists. Please write valid username')
    else:
        return render(request, 'sign_in.html')
    
def logout(request):
    if request.method == 'POST' and 'logout' in request.POST:
        messages.success(request, 'You have been successfully logged Out')
        global curr_user
        curr_user = ''
        return redirect('home')
    
    return render(request, 'logout.html')

def shopping_output(request):
    if request.method == 'POST':
        area = request.POST.get('area')
        subcategory = request.POST.get('subcategory')
        shoppings = Shopping.objects.filter(area__icontains=area, subcategory__icontains=subcategory)

        return render(request, 'shopping_output.html', {'shoppings' : shoppings})
    else:
        return render(request, 'shopping.html')
    
def services_output(request):
    if request.method == 'POST':
        area = request.POST.get('area')
        subcategory = request.POST.get('subcategory')
        services = Service.objects.filter(area__icontains=area, subcategory__icontains=subcategory)

        return render(request, 'services_output.html', {'services' : services})
    else:
        return render(request, 'services.html')