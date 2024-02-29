from django.shortcuts import render,redirect
from .forms import CreateUserForm,LoginForm,CreateRecordForm,UpdateRecordForm

from django.contrib.auth.models import auth
from django.contrib.auth import authenticate

from django.contrib.auth.decorators import login_required

from .models import Record
from django.contrib import messages

# Create your views here.

# home page
def home(request):
    return render(request, 'webapp/index.html')


#register a user view
def register(request):

    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)

        if form.is_valid():
            form.save()

            messages.success(request,'Account created successfully!')

            return redirect('my-login')

    context = {'form':form}
    return render(request, 'webapp/register.html', context=context)


# Login a User

def my_login(request):
    form = LoginForm()

    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)

        if form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request,username=username, password=password)

            if user is not None:
                auth.login(request, user)
                return redirect('dashboard')
        

    context = {'form':form}

    return render(request, 'webapp/my-login.html', context=context)



# Dashboard
@login_required(login_url='my-login')
def dashboard(request):

    my_records = Record.objects.all()

    context = {'records': my_records}


    return render(request, 'webapp/dashboard.html', context=context)

# Crearte a record

@login_required(login_url='my-login')
def create_record(request):
    
    form = CreateRecordForm()

    if request.method == 'POST':

        form = CreateRecordForm(request.POST)

        if form.is_valid():

            form.save()

            messages.success(request, 'Your record created successfully!')

            return redirect('dashboard')

    context = {'form': form}

    return render(request, 'webapp/create-record.html', context=context)

# Update record 
@login_required(login_url='my-login')
def update_record(request, pk):

    record = Record.objects.get(id=pk)

    form = UpdateRecordForm(instance=record)

    if request.method == 'POST':

        form = UpdateRecordForm(request.POST, instance=record)

        if form.is_valid():

            form.save()

            messages.success(request, 'Your record updated succesfully!')

            return redirect('dashboard')
    
    context = {'form':form}

    return render(request, 'webapp/update-record.html', context=context)



# Read or view a single record 
@login_required(login_url='my-login')
def view_reord(request, pk):

    all_records = Record.objects.get(id=pk)

    context = {'record':all_records}

    return render(request, 'webapp/view-record.html', context=context)


# Delete a record 
@login_required(login_url='my-login')
def delete_reord(request, pk):
    
    record = Record.objects.get(id=pk)

    record.delete()

    messages.success(request, 'record deleted successfully!')

    return redirect('dashboard')

    

# Logout user

def user_logout(request):
    auth.logout(request)

    messages.success(request, 'Logout success!')

    return redirect('my-login')


