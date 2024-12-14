from django.shortcuts import render,HttpResponse,redirect
from rest_framework.renderers import JSONRenderer
from django.views.decorators.csrf import csrf_exempt
import pandas as pd
from .models import *
from .serializers import *
from django.http import JsonResponse
import json
from django.contrib.auth.models import User
from django.db.models import Q
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from datetime import datetime
from django.core.paginator import Paginator

from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from .models import Employee  # Assuming Employee is your model

def login_page(request):
    msg = ''
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        
        # Authenticate the user with phone number and password
        user = authenticate(username=username, password=password)
        
        if user is not None:
            login(request,user)
            # Check if the user is a superuser
            if user.is_superuser:
                return redirect("/admin-dashboard")
            else:
                msg = "You are not authorized to login!"
        else:
            msg = "Invalid Phone or Password!"
    
    return render(request, "login.html", {'msg': msg})


@login_required(login_url="/")
def admin_dashboard(request):
    if not (request.user.is_superuser):
        return HttpResponseForbidden("You don't have permission to access this page.")
    emp=Client.objects.filter(username="").count()
    total_client=len(Client.objects.all())
    client_pending=len(Client.objects.filter(client_status="pending"))
    client_followup=len(Client.objects.filter(client_status="followup"))
    client_cancelled=len(Client.objects.filter(client_status="cnp"))
    client_completed=len(Client.objects.filter(client_status="completed"))
    client_ni=len(Client.objects.filter(client_status="not-interested"))
    client_nii=len(Client.objects.filter(client_status="not-in-industry"))

    employee = Employee.objects.all().order_by('-id')  # Simplified with '-' for reverse order
    data = Client.objects.all().order_by('-id')  # Same simplification
    
    

    paginator = Paginator(data, 100)  # Show 10 posts per page
    page_number = request.GET.get('page')
    page_posts = paginator.get_page(page_number)
    current_page = page_posts.number
    total_pages = paginator.num_pages
    page_range = range(max(current_page - 2, 1), min(current_page + 3, total_pages + 1))
    context={
        'total_client':total_client,
        'emp':emp,
        'client_pending':client_pending,
        'client_followup':client_followup,
        'client_cancelled':client_cancelled,
        'client_completed':client_completed,
        'page_posts':page_posts,
        'page_range':page_range,
        'employee':employee,
        'client_ni':client_ni,
        'client_nii':client_nii
        
    }
    return render(request,'index.html',context)



@login_required(login_url="/")
def admin_telesales_employee(request):
    if not (request.user.is_superuser):
        return HttpResponseForbidden("You don't have permission to access this page.")
    emp=Client.objects.filter(username="").count()
    total_client=len(Client.objects.all())
    client_pending=len(Client.objects.filter(client_status="pending"))
    client_followup=len(Client.objects.filter(client_status="followup"))
    client_cancelled=len(Client.objects.filter(client_status="cnp"))
    client_completed=len(Client.objects.filter(client_status="completed"))
    client_ni=len(Client.objects.filter(client_status="not-interested"))
    client_nii=len(Client.objects.filter(client_status="not-in-industry"))

    data=Employee.objects.filter(category="Telesales").order_by('id').reverse()
    paginator = Paginator(data, 100)  # Show 10 posts per page
    page_number = request.GET.get('page')
    page_posts = paginator.get_page(page_number)
    current_page = page_posts.number
    total_pages = paginator.num_pages
    page_range = range(max(current_page - 2, 1), min(current_page + 3, total_pages + 1))
    context={
        'total_client':total_client,
        'emp':emp,
        'client_pending':client_pending,
        'client_followup':client_followup,
        'client_cancelled':client_cancelled,
        'client_completed':client_completed,
        'page_posts':page_posts,
        'page_range':page_range,
        'url':"home",
        'client_ni':client_ni,
        'client_nii':client_nii
    }
    return render(request,'employee.html',context)




@login_required(login_url="/")
def admin_digital_employee(request):
    if not (request.user.is_superuser):
        return HttpResponseForbidden("You don't have permission to access this page.")
    emp=Client.objects.filter(username="").count()
    total_client=len(Client.objects.all())
    client_pending=len(Client.objects.filter(client_status="pending"))
    client_followup=len(Client.objects.filter(client_status="followup"))
    client_cancelled=len(Client.objects.filter(client_status="cnp"))
    client_completed=len(Client.objects.filter(client_status="completed"))
    client_ni=len(Client.objects.filter(client_status="not-interested"))
    client_nii=len(Client.objects.filter(client_status="not-in-industry"))

    data=Employee.objects.filter(category="Digital Marketing").order_by('id').reverse()
    paginator = Paginator(data, 100)  # Show 10 posts per page
    page_number = request.GET.get('page')
    page_posts = paginator.get_page(page_number)
    current_page = page_posts.number
    total_pages = paginator.num_pages
    page_range = range(max(current_page - 2, 1), min(current_page + 3, total_pages + 1))
    context={
        'total_client':total_client,
        'emp':emp,
        'client_pending':client_pending,
        'client_followup':client_followup,
        'client_cancelled':client_cancelled,
        'client_completed':client_completed,
        'page_posts':page_posts,
        'page_range':page_range,
        'url':"home",
        'client_ni':client_ni,
        'client_nii':client_nii
    }
    return render(request,'digital-employee.html',context)



@login_required(login_url="/")
def admin_add_employee(request):
    if not (request.user.is_superuser):
        return HttpResponseForbidden("You don't have permission to access this page.")
    msg = ""
    uname = User.objects.all()
    emp=Client.objects.filter(username="").count()
    total_client=len(Client.objects.all())
    client_pending=len(Client.objects.filter(client_status="pending"))
    client_followup=len(Client.objects.filter(client_status="followup"))
    client_cancelled=len(Client.objects.filter(client_status="cnp"))
    client_completed=len(Client.objects.filter(client_status="completed"))
    client_ni=len(Client.objects.filter(client_status="not-interested"))
    client_nii=len(Client.objects.filter(client_status="not-in-industry"))
    if request.method == "POST":
        b = Employee()
        b.category=request.POST.get("category")
        b.name=request.POST.get("name")
        b.email=request.POST.get("email")
        b.phone=request.POST.get("phone")
        b.password=request.POST.get('password')
        b.address=request.POST.get("address")
        
        try:
            u = User.objects.get(username=b.phone)
            if u:
                print("user already exist")
        except :
            user = User(username=b.phone, email=b.email, first_name=b.name.split(" ")[0], last_name=" ".join(b.name.split(" ")[1:]))
            user.set_password(b.password)
            user.save()
            b.save()
            msg = "Done"
    
    return render(request, "add-employee.html", 
        {'uname': uname, 
        'msg': msg,
        'total_client':total_client,
        'emp':emp,
        'client_pending':client_pending,
        'client_followup':client_followup,
        'client_cancelled':client_cancelled,
        'client_completed':client_completed,
        'client_ni':client_ni,
        'client_nii':client_nii
        })
 

@login_required(login_url="/")
def admin_update_employee(request,id):
    if not (request.user.is_superuser):
        return HttpResponseForbidden("You don't have permission to access this page.")
    emp=Client.objects.filter(username="").count()
    total_client=len(Client.objects.all())
    client_pending=len(Client.objects.filter(client_status="pending"))
    client_followup=len(Client.objects.filter(client_status="followup"))
    client_cancelled=len(Client.objects.filter(client_status="cnp"))
    client_completed=len(Client.objects.filter(client_status="completed"))
    client_ni=len(Client.objects.filter(client_status="not-interested"))
    client_nii=len(Client.objects.filter(client_status="not-in-industry"))
    msg = ""
    from django.shortcuts import get_object_or_404

    # Fetch the Employee object or raise a 404 error if not found
    data = get_object_or_404(Employee, id=id)

    if request.method == "POST":
        # Update Employee fields with values from the POST request
        data.category = request.POST.get("category")
        data.name = request.POST.get("name")
        data.password = request.POST.get("password")  # This password is plain text; be cautious
        data.email = request.POST.get("email")
        data.address = request.POST.get("address")

        # Fetch the associated User object by the phone field in Employee
        try:
            user = User.objects.get(username=data.phone)
            # Update the password securely
            user.set_password(data.password)
            user.save()
        except User.DoesNotExist:
            return HttpResponse("User does not exist", status=404)

        # Save the updated Employee object
        data.save()

        # Indicate success
        msg = "Done"
        

    return render(request, "update-employee.html", 
        {
        'data':data,
        'msg': msg,
        'total_client':total_client,
        'emp':emp,
        'client_pending':client_pending,
        'client_followup':client_followup,
        'client_cancelled':client_cancelled,
        'client_completed':client_completed,
        'client_ni':client_ni,
        'client_nii':client_nii
        })
 

@login_required(login_url="/")
def admin_update_employee_status(request,id,ops):
    if not (request.user.is_superuser):
        return HttpResponseForbidden("You don't have permission to access this page.")
    e = Employee.objects.get(id=id)
    e.empstatus=ops
    e.save()
    msg = "Done"
    return redirect('/admin-employee')
 


@login_required(login_url="/")
def admin_client(request,ops):
    if not (request.user.is_superuser):
        return HttpResponseForbidden("You don't have permission to access this page.")
    emp=Client.objects.filter(username="").count()
    total_client=len(Client.objects.all())
    client_pending=len(Client.objects.filter(client_status="pending"))
    client_followup=len(Client.objects.filter(client_status="followup"))
    client_cancelled=len(Client.objects.filter(client_status="cnp"))
    client_completed=len(Client.objects.filter(client_status="completed"))
    client_ni=len(Client.objects.filter(client_status="not-interested"))
    client_nii=len(Client.objects.filter(client_status="not-in-industry"))
    employee=Employee.objects.all()
    if(ops=='all'):
       data=Client.objects.all().order_by('id').reverse()
    elif(ops=='fresh'):
       data=Client.objects.filter(username="").order_by('id').reverse()
    else:
       data=Client.objects.filter(client_status=ops).order_by('id').reverse()

    paginator = Paginator(data, 100)  # Show 10 posts per page
    page_number = request.GET.get('page')
    page_posts = paginator.get_page(page_number)
    current_page = page_posts.number
    total_pages = paginator.num_pages
    page_range = range(max(current_page - 2, 1), min(current_page + 3, total_pages + 1))
    context={
        'total_client':total_client,
        'emp':emp,
        'client_pending':client_pending,
        'client_followup':client_followup,
        'client_cancelled':client_cancelled,
        'client_completed':client_completed,
        'page_posts':page_posts,
        'page_range':page_range,
        'employee':employee,
        'client_ni':client_ni,
        'client_nii':client_nii,
        'ops':ops
    }
    return render(request,'index.html',context)


from django.core.paginator import Paginator
from datetime import datetime
from django.shortcuts import render
from django.http import HttpResponse

@login_required(login_url="/")
def admin_filter(request):
    if not (request.user.is_superuser):
        return HttpResponseForbidden("You don't have permission to access this page.")
    emp = Client.objects.filter(username="").count()
    total_client = Client.objects.count()
    client_pending = Client.objects.filter(client_status="pending").count()
    client_followup = Client.objects.filter(client_status="followup").count()
    client_cancelled = Client.objects.filter(client_status="cnp").count()
    client_completed = Client.objects.filter(client_status="completed").count()
    client_ni = Client.objects.filter(client_status="not-interested").count()
    client_nii = Client.objects.filter(client_status="not-in-industry").count()
    employee = Employee.objects.all()

    data = Client.objects.none()  # Default empty queryset
    ops=''
    td=''
    fd=''
    # Filter by operations and date range if provided
    if request.method == "POST":
        ops = request.POST.get('ops', 'all')
        to_date = request.POST.get('to_date')
        from_date = request.POST.get('from_date')
        td=to_date
        fd=from_date
        print("OPS:", ops)
        print("From Date:", from_date)
        print("To Date:", to_date)

        # Filter based on 'ops'
        if ops == 'all' or ops=='':
            data = Client.objects.all().order_by('-id')
        elif ops == 'fresh':
            data = Client.objects.filter(username="").order_by('-id')
        else:
            data = Client.objects.filter(client_status=ops).order_by('-id')

        # Filter by date range
        if to_date and from_date:
            try:
                # Convert date strings to datetime with full day range
                from_date = datetime.strptime(from_date, '%Y-%m-%d').replace(hour=0, minute=0, second=0)
                to_date = datetime.strptime(to_date, '%Y-%m-%d').replace(hour=23, minute=59, second=59)
                data = data.filter(updated_on__range=[from_date, to_date])
            except ValueError:
                # Handle invalid date format
                return HttpResponse("Invalid date format. Please use YYYY-MM-DD.", status=400)

    # Paginator
    paginator = Paginator(data, 100)  # Show 100 posts per page
    page_number = request.GET.get('page')
    page_posts = paginator.get_page(page_number)
    current_page = page_posts.number
    total_pages = paginator.num_pages
    page_range = range(max(current_page - 2, 1), min(current_page + 3, total_pages + 1))

    context = {
        'total_client': total_client,
        'emp': emp,
        'client_pending': client_pending,
        'client_followup': client_followup,
        'client_cancelled': client_cancelled,
        'client_completed': client_completed,
        'page_posts': page_posts,
        'page_range': page_range,
        'employee': employee,
        'client_ni': client_ni,
        'client_nii': client_nii,
        'ops': ops,
        'fd':fd,
        'td':td
    }
    return render(request, 'index.html', context)



@login_required(login_url="/")
def admin_client_by_type(request,ops):
    if not (request.user.is_superuser):
        return HttpResponseForbidden("You don't have permission to access this page.")
    emp=Client.objects.filter(username="").count()
    total_client=len(Client.objects.all())
    client_pending=len(Client.objects.filter(client_status="pending"))
    client_followup=len(Client.objects.filter(client_status="followup"))
    client_cancelled=len(Client.objects.filter(client_status="cnp"))
    client_completed=len(Client.objects.filter(client_status="completed"))
    client_ni=len(Client.objects.filter(client_status="not-interested"))
    client_nii=len(Client.objects.filter(client_status="not-in-industry"))
    employee=Employee.objects.all()
    if(ops=='all'):
       data=Client.objects.all().order_by('id').reverse()
    else:
       data=Client.objects.filter(clinet_type=ops).order_by('id').reverse()

    paginator = Paginator(data, 100)  # Show 10 posts per page
    page_number = request.GET.get('page')
    page_posts = paginator.get_page(page_number)
    current_page = page_posts.number
    total_pages = paginator.num_pages
    page_range = range(max(current_page - 2, 1), min(current_page + 3, total_pages + 1))
    context={
        'total_client':total_client,
        'emp':emp,
        'client_pending':client_pending,
        'client_followup':client_followup,
        'client_cancelled':client_cancelled,
        'client_completed':client_completed,
        'page_posts':page_posts,
        'page_range':page_range,
        'employee':employee,
        'client_ni':client_ni,
        'client_nii':client_nii
    }
    return render(request,'index.html',context)




@login_required(login_url="/")
def admin_upload_excel(request):
    if not (request.user.is_superuser):
        return HttpResponseForbidden("You don't have permission to access this page.")
    emp = len(Employee.objects.all())
    total_client = len(Client.objects.all())
    emp_pending = len(Client.objects.filter(client_status="pending"))
    client_pending = len(Client.objects.filter(client_status="pending"))
    client_followup = len(Client.objects.filter(client_status="followup"))
    client_cancelled = len(Client.objects.filter(client_status="cnp"))
    client_completed = len(Client.objects.filter(client_status="completed"))
    client_ni=len(Client.objects.filter(client_status="not-interested"))
    client_nii=len(Client.objects.filter(client_status="not-in-industry"))
    employee = Employee.objects.all()
    msg=''
    # Lists to store report data
    duplicate_numbers = []
    invalid_numbers = []

    if request.method == "POST":
        ecode = request.FILES.get('file')
        emply = request.POST.get('emply')
        ctype = request.POST.get('ctype')
        df = pd.read_excel(ecode)

        for index, row in df.iterrows():
            phone = str(row['Phone']).strip()
            phone=phone.replace(".0",'')
            name = row.get('Name', '')
            email = row.get('Email', '')

            # Validate phone number
            if not phone.isdigit() or len(phone) != 10:
                invalid_numbers.append({'row': index + 1, 'phone': phone})
                continue  # Skip this row

            # Check for duplicate phone number
            if Client.objects.filter(client_phone=phone).exists():
                duplicate_numbers.append({'row': index + 1, 'phone': phone})
                continue  # Skip this row

            # Create and save the client (name and email can be blank)
            c = Client(
                client_phone=phone,
                client_name=name,  # Set to None if blank
                client_email=email, # Set to None if blank
                username=emply if emply else None , # Set to None if blank
                clinet_type=ctype , # Set to None if blank
                created_on=datetime.now()  # Set to None if blank
            )
            c.save()
            msg='Done'

        # Redirect after saving, but with the report data in the context
        context = {
            'total_client': total_client,
            'emp': emp,
            'msg': msg,
            'client_pending': client_pending,
            'client_followup': client_followup,
            'client_cancelled': client_cancelled,
            'client_completed': client_completed,
            'employee': employee,
            'duplicate_numbers': duplicate_numbers,
            'invalid_numbers': invalid_numbers,
            'emp_pending':emp_pending,
            'client_ni':client_ni,
            'client_nii':client_nii
        }

        return render(request, 'add-excel.html', context)

    context = {
        'msg': msg,
        'total_client': total_client,
        'emp': emp,
        'client_pending': client_pending,
        'client_followup': client_followup,
        'client_cancelled': client_cancelled,
        'client_completed': client_completed,
        'employee': employee,
        'emp_pending':emp_pending,
        'client_ni':client_ni,
        'client_nii':client_nii
    }

    return render(request, 'add-excel.html', context)


@login_required(login_url="/")
def admin_add_client(request):
    if not (request.user.is_superuser):
        return HttpResponseForbidden("You don't have permission to access this page.")
    emp = len(Client.objects.filter(username=''))
    total_client = len(Client.objects.all())
    emp_pending = len(Client.objects.filter(client_status="pending"))
    client_pending = len(Client.objects.filter(client_status="pending"))
    client_followup = len(Client.objects.filter(client_status="followup"))
    client_cancelled = len(Client.objects.filter(client_status="cnp"))
    client_completed = len(Client.objects.filter(client_status="completed"))
    client_ni=len(Client.objects.filter(client_status="not-interested"))
    client_nii=len(Client.objects.filter(client_status="not-in-industry"))
    employee = Employee.objects.all()
    msg=""
    msg2=""
    if(request.method=='POST'):
      data=Client()
      data.clinet_type=request.POST.get('clinet_type')
      data.client_name=request.POST.get('client_name')
      data.client_email=request.POST.get('client_email')
      data.client_phone=request.POST.get('client_phone')
      data.client_address=request.POST.get('client_address')
      data.client_status=request.POST.get('client_status')
      data.client_next_followup_date=request.POST.get('client_next_followup_date')
      data.created_on=datetime.now()
      data.updated_on=datetime.now()
      data.allocator=request.user.username
      if(Client.objects.filter(client_phone=request.POST.get('client_phone'))):
          msg2="Done"
      else:
         data.save()
         msg="done"
    context = {
        'msg':msg,
        'total_client': total_client,
        'emp': emp,
        'client_pending': client_pending,
        'client_followup': client_followup,
        'client_cancelled': client_cancelled,
        'client_completed': client_completed,
        'employee': employee,
        'emp_pending':emp_pending,
        'client_ni':client_ni,
        'client_nii':client_nii,
        'msg2':msg2
    }
    return render(request,'add-client.html',context)


@login_required(login_url="/")
def admin_update_client(request,id):
    if not (request.user.is_superuser):
        return HttpResponseForbidden("You don't have permission to access this page.")
    emp = len(Client.objects.filter(username=''))
    total_client = len(Client.objects.all())
    emp_pending = len(Client.objects.filter(client_status="pending"))
    client_pending = len(Client.objects.filter(client_status="pending"))
    client_followup = len(Client.objects.filter(client_status="followup"))
    client_cancelled = len(Client.objects.filter(client_status="cnp"))
    client_completed = len(Client.objects.filter(client_status="completed"))
    client_ni=len(Client.objects.filter(client_status="not-interested"))
    client_nii=len(Client.objects.filter(client_status="not-in-industry"))
    employee = Employee.objects.all()
    msg=""
    data=Client.objects.get(id=id)
    chistory = Client_History.objects.filter(client_phone=data.client_phone)
    if(request.method=='POST'):
      data.clinet_type=request.POST.get('clinet_type')
      data.client_name=request.POST.get('client_name')
      data.client_email=request.POST.get('client_email')
      data.client_address=request.POST.get('client_address')
      data.client_status=request.POST.get('client_status')
      data.client_next_followup_date=request.POST.get('client_next_followup_date')
      data.updated_on=datetime.now()
      data.allocator=request.user.username
      data.save()
      ch=Client_History()
      ch.client_phone=data.client_phone
      ch.client_message=request.POST.get('client_message')
      ch.client_next_followup_date=request.POST.get('client_next_followup_date')
      ch.updated_on=datetime.now()
      ch.save()
      msg="done"
    context = {
        'msg':msg,
        'data':data,
        'total_client': total_client,
        'emp': emp,
        'client_pending': client_pending,
        'client_followup': client_followup,
        'client_cancelled': client_cancelled,
        'client_completed': client_completed,
        'employee': employee,
        'emp_pending':emp_pending,
        'chistory':chistory,
        'client_ni':client_ni,
        'client_nii':client_nii
    }
    return render(request,'update-client.html',context)


@login_required(login_url="/")
def admin_delete_client(request,id,pn):
    if not (request.user.is_superuser):
        return HttpResponseForbidden("You don't have permission to access this page.")
    data=Client.objects.get(id=id)
    data.delete()
    return redirect(f'/admin-client/all/?page=' + str(pn))



def admin_delete_employee(request,id):
    data=Employee.objects.get(id=id)
    user=User.objects.get(username=data.phone)
    user.delete()
    data.delete()
    return redirect("/admin-dashboard")





@login_required(login_url="/")
def admin_exchange_data(request):
    if not (request.user.is_superuser):
        return HttpResponseForbidden("You don't have permission to access this page.")
    emp=Client.objects.filter(username="").count()
    total_client=len(Client.objects.all())
    client_pending=len(Client.objects.filter(client_status="pending"))
    client_followup=len(Client.objects.filter(client_status="followup"))
    client_cancelled=len(Client.objects.filter(client_status="cnp"))
    client_completed=len(Client.objects.filter(client_status="completed"))
    client_ni=len(Client.objects.filter(client_status="not-interested"))
    client_nii=len(Client.objects.filter(client_status="not-in-industry"))
    employee=Employee.objects.all()
    msg = ""
    if request.method == "POST":
        employee1=request.POST.get("employee1")
        employee2=request.POST.get("employee2")
        data1=Client.objects.filter(username=employee1)
        for emp1 in data1:
            emp1.username=employee2
            emp1.allocator=request.user.username
            emp1.save()
        data2=Client.objects.filter(username=employee2)
        for emp2 in data2:
            emp2.username=employee1
            emp2.allocator=request.user.username
            emp2.save()
            msg="Done"
    return render(request, "exchange-client.html", 
        {
        'employee':employee,
        'msg': msg,
        'total_client':total_client,
        'emp':emp,
        'client_pending':client_pending,
        'client_followup':client_followup,
        'client_cancelled':client_cancelled,
        'client_completed':client_completed,
        'client_ni':client_ni,
        'client_nii':client_nii
        })
 



@login_required(login_url="/")
def employee_report_by_status(request,phone,ops):
    if not (request.user.is_superuser):
        return HttpResponseForbidden("You don't have permission to access this page.")
    emp=Client.objects.filter(username="").count()
    available_fresh=len(Client.objects.filter(Q(emp_name__icontains=phone)|Q(username__icontains=phone)))
    total_fresh=len(Client.objects.filter(emp_name=phone))
    total_client=len(Client.objects.filter(emp_name=phone))
    client_pending=len(Client.objects.filter(username=phone,client_status="pending"))
    client_followup=len(Client.objects.filter(username=phone,client_status="followup"))
    client_cancelled=len(Client.objects.filter(username=phone,client_status="cnp"))
    client_completed=len(Client.objects.filter(username=phone,client_status="completed"))
    client_ni=len(Client.objects.filter(username=phone,client_status="not-interested"))
    client_nii=len(Client.objects.filter(username=phone,client_status="not-in-industry"))
    employee=Employee.objects.all()
    empdetails=Employee.objects.get(phone=phone)
    
    cr=0
    try:
       cr = round((client_completed/total_client) * 100, 2)
    except ZeroDivisionError:
        cr = 0  # Handle division by zero if client_completed is 0
    except :
        pass

    if(ops=='all'):
       data=Client.objects.filter(Q(emp_name__icontains=phone)|Q(username__icontains=phone)).order_by('id').reverse()
    elif(ops=='available-fresh'):
       data=Client.objects.filter(emp_name=phone,username="").order_by('id').reverse()
    elif(ops=='total-fresh'):
       data=Client.objects.filter(emp_name=phone).order_by('id').reverse()
    else:
       data=Client.objects.filter(username=phone,client_status=ops).order_by('id').reverse()

    paginator = Paginator(data, 100)  # Show 10 posts per page
    page_number = request.GET.get('page')
    page_posts = paginator.get_page(page_number)
    current_page = page_posts.number
    total_pages = paginator.num_pages
    page_range = range(max(current_page - 2, 1), min(current_page + 3, total_pages + 1))
    context={
        'total_client':total_client,
        'emp':emp,
        'client_pending':client_pending,
        'client_followup':client_followup,
        'client_cancelled':client_cancelled,
        'client_completed':client_completed,
        'page_posts':page_posts,
        'page_range':page_range,
        'employee':employee,
        'ephone':phone,
        'empdetails':empdetails,
        'client_ni':client_ni,
        'client_nii':client_nii,
        'cr':cr,
        'available_fresh':available_fresh,
        'total_fresh':total_fresh,
        'ops':ops
    }
    return render(request,'employee-report.html',context)

@login_required(login_url="/")
def admin_logout(request):
    logout(request)
    return redirect('/')
#API

@csrf_exempt
def app_employee_login(request):
    if request.method=="POST":
        phone=request.POST.get('phone')
        password=request.POST.get('password')
        device_token=request.POST.get('device_token')
        try:
            data=Employee.objects.get(phone=phone,password=password)
            if(data):
                data.device_token=device_token
                dataSerializer=EmployeeSerializer(data,many=False)
                realData={'status':True,'message':"Data found successfully...",'data':[dataSerializer.data]}
                return HttpResponse(json.dumps(realData),content_type="application/json")
               
            else:
                msg={'status':False,'message':"Data not found..."}
                jsonData=JSONRenderer().render(msg)
                return HttpResponse(jsonData,content_type="application/json")

        except:
            msg={'status':False,'message':"Invalid Phone or Password..."}
            jsonData=JSONRenderer().render(msg)
            return HttpResponse(jsonData,content_type="application/json")
        

@csrf_exempt
def app_get_client(request):
    if request.method=="POST":
        username=request.POST.get('username')
        security_key=request.POST.get('security_key')
        if(security_key=="Yjh8-IU8-&*m!@1!&-&*Y-UIY*&"):
            try:
                data=Client.objects.filter(username=username).order_by('id').reverse()
                if(data):
                    dataSerializer=ClientSerializer(data,many=True)
                    realData={'status':True,'message':"Data found successfully...",'data':dataSerializer.data}
                    return HttpResponse(json.dumps(realData),content_type="application/json")
                   
                else:
                    msg={'status':False,'message':"Data not found..."}
                    jsonData=JSONRenderer().render(msg)
                    return HttpResponse(jsonData,content_type="application/json")
    
            except:
                msg={'status':False,'message':"Invalid Phone or Password..."}
                jsonData=JSONRenderer().render(msg)
                return HttpResponse(jsonData,content_type="application/json")
        else:
            msg = {'status': False, 'message': "Invalid security key."}
            return JsonResponse(msg, status=403)

    else:
        return JsonResponse({'status': False, 'message': "Invalid request method."}, status=405)
    


@csrf_exempt
def app_get_client_details(request):
    if request.method == "POST":
        username = request.POST.get('username')
        client_id = request.POST.get('client_id')
        security_key = request.POST.get('security_key')

        if security_key == "Yjh8-IU8-&*m!@1!&-&*Y-UIY*&":
            try:
                # Fetch the client data
                data1 = Client.objects.get(username=username, id=client_id)
                # Fetch the related client history
                data2 = Client_History.objects.filter(client_phone=data1.client_phone)
                
                if data1:
                    dataSerializer1 = ClientSerializer(data1, many=False)
                    dataSerializer2 = Client_HistorySerializer(data2, many=True)
                    
                    realData = {
                        'status': True,
                        'message': "Data found successfully...",
                        'data1': [dataSerializer1.data],
                        'data2': dataSerializer2.data  # Ensure you're serializing `data2.data`
                    }
                    return JsonResponse(realData, safe=False)

            except Client.DoesNotExist:
                msg = {'status': False, 'message': "Client not found."}
                return JsonResponse(msg, status=404)

            except Client_History.DoesNotExist:
                msg = {'status': False, 'message': "Client history not found."}
                return JsonResponse(msg, status=404)

            except Exception as e:
                msg = {'status': False, 'message': "Invalid details.", 'error': str(e)}
                return JsonResponse(msg, status=400)

        else:
            msg = {'status': False, 'message': "Invalid security key."}
            return JsonResponse(msg, status=403)

    else:
        return JsonResponse({'status': False, 'message': "Invalid request method."}, status=405)


@csrf_exempt
def app_update_client(request):
    if request.method == "POST":
        username = request.POST.get('username')
        client_id = request.POST.get('client_id')
        security_key = request.POST.get('security_key')

        if security_key == "Yjh8-IU8-&*m!@1!&-&*Y-UIY*&":
            try:
                # Fetch the client data
                data1 = Client.objects.get(username=username, id=client_id)
                # Fetch the related client history
                
                if data1:
                    data1.clinet_type=request.POST.get('clinet_type')
                    data1.client_name=request.POST.get('client_name')
                    data1.client_email=request.POST.get('client_email')
                    data1.client_address=request.POST.get('client_address')
                    data1.client_status=request.POST.get('client_status')
                    data1.client_next_followup_date=request.POST.get('client_next_followup_date')
                    data1.updated_on=datetime.now()
                    data1.save()
                    ch=Client_History()
                    ch.client_phone=data1.client_phone
                    ch.client_message=request.POST.get('client_message')
                    ch.client_next_followup_date=request.POST.get('client_next_followup_date')
                    ch.updated_on=datetime.now()
                    ch.save()
                    dataSerializer1 = ClientSerializer(data1, many=False)
                    data2 = Client_History.objects.filter(client_phone=data1.client_phone)
                    dataSerializer2 = Client_HistorySerializer(data2, many=True)
                    
                    realData = {
                        'status': True,
                        'message': "Data Updated successfully...",
                        'data1': [dataSerializer1.data],
                        'data2': dataSerializer2.data  # Ensure you're serializing `data2.data`
                    }
                    return JsonResponse(realData, safe=False)

            except Client.DoesNotExist:
                msg = {'status': False, 'message': "Client not found."}
                return JsonResponse(msg, status=404)

            except Client_History.DoesNotExist:
                msg = {'status': False, 'message': "Client history not found."}
                return JsonResponse(msg, status=404)

            except Exception as e:
                msg = {'status': False, 'message': "Invalid details.", 'error': str(e)}
                return JsonResponse(msg, status=400)

        else:
            msg = {'status': False, 'message': "Invalid security key."}
            return JsonResponse(msg, status=403)

    else:
        return JsonResponse({'status': False, 'message': "Invalid request method."}, status=405)




@login_required(login_url="/")
def assign_employees(request):
    if not (request.user.is_superuser):
        return HttpResponseForbidden("You don't have permission to access this page.")
    if request.method == 'POST':
        selected_clients = request.POST.getlist('selected_clients')
        selected_employee = request.POST.get('selected_employee')

        if selected_clients and selected_employee:
            for client_id in selected_clients:
                client = Client.objects.get(id=client_id)
                client.username = selected_employee  # Assign the selected employee to the client
                client.client_status = "pending"  # Assign the selected employee to the client
                client.allocator=request.user.username
                client.save()
            return redirect('/admin-client/all')
        else:
            # Handle error if no employee or clients are selected
            return redirect('/admin-client/all')


def assign_type(request):
    data=Client.objects.all()
    for item in data:
        if item.clinet_type=='':
            item.clinet_type="Accountant"
            item.save()
    return redirect("/admin-dashboard")





@login_required(login_url="/")
def admin_search(request):
    if not (request.user.is_superuser):
        return HttpResponseForbidden("You don't have permission to access this page.")
    emp=Client.objects.filter(username="").count()
    total_client=len(Client.objects.all())
    client_pending=len(Client.objects.filter(client_status="pending"))
    client_followup=len(Client.objects.filter(client_status="followup"))
    client_cancelled=len(Client.objects.filter(client_status="cnp"))
    client_completed=len(Client.objects.filter(client_status="completed"))
    client_ni=len(Client.objects.filter(client_status="not-interested"))
    client_nii=len(Client.objects.filter(client_status="not-in-industry"))
    data = Client.objects.all()
    search_query = ''
    
    if request.method == "POST":
        search_query = request.POST.get('name', '')
        request.session['search_query'] = search_query
    elif request.method == "GET":
        search_query = request.GET.get('name', request.session.get('search_query', ''))

    if search_query:
        data = Client.objects.filter(
            Q(client_name__icontains=search_query) |
            Q(client_phone__icontains=search_query) |
            Q(username__icontains=search_query) 
            
        )
    
    employee=Employee.objects.all()
    msg = ""
    paginator = Paginator(data, 100)  # Show 100 posts per page
    page_number = request.GET.get('page')
    page_posts = paginator.get_page(page_number)
    current_page = page_posts.number
    total_pages = paginator.num_pages
    page_range = range(max(current_page - 2, 1), min(current_page + 3, total_pages + 1))
    
    return render(request, "index.html", 
        {
        'employee':employee,
        'msg': msg,
        'total_client':total_client,
        'emp':emp,
        'client_pending':client_pending,
        'client_followup':client_followup,
        'client_cancelled':client_cancelled,
        'client_completed':client_completed,
        'client_ni':client_ni,
        'client_nii':client_nii,
        'page_posts': page_posts,
        'page_range': page_range,
        'search_query': search_query,
        })
 

import csv
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

@login_required(login_url='/')
def admin_download_employee_report(request):
    if not (request.user.is_superuser):
        return HttpResponseForbidden("You don't have permission to access this page.")
    if request.method == "POST":
        employee = request.POST.get('employee')
        categories = request.POST.getlist('category')  # Get selected categories as a list

        # Handle "All" selection to include all categories
        if "all" in categories:
            data = Client.objects.filter(username=employee)
        else:
            data = Client.objects.filter(username=employee, client_status__in=categories)

        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="client.csv"'

        writer = csv.writer(response)
        writer.writerow([
            'Employee Phone', 'Client Type', 'Client Name', 'Client Phone', 'Client Email',
            'Client Address', 'Client Next Followup Date', 'Client Status', 'Created On', 'Updated On'
        ])

        for item in data:
            writer.writerow([
                item.username, item.clinet_type, item.client_name, item.client_phone, item.client_email,
                item.client_address, item.client_next_followup_date, item.client_status, item.created_on, item.updated_on
            ])

        return response

    return HttpResponse("Invalid request method.", status=400)


from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
import csv
from datetime import datetime

@login_required(login_url='/')
def admin_download_data(request):
    if not (request.user.is_superuser):
        return HttpResponseForbidden("You don't have permission to access this page.")
    # Filter by date range if provided
    if request.method == "POST":
        to_date = request.POST.get('to_date')
        from_date = request.POST.get('from_date')
        ops = request.POST.get('ops')
        if(ops):
           if(ops=="fresh"):
              data = Client.objects.filter(username="")
           else:
              data = Client.objects.filter(client_status=ops)
        else:
           data = Client.objects.all()

        # Ensure both to_date and from_date are not empty or None
        # Filter by date range
        if to_date and from_date:
            try:
                # Convert date strings to datetime with full day range
                from_date = datetime.strptime(from_date, '%Y-%m-%d').replace(hour=0, minute=0, second=0)
                to_date = datetime.strptime(to_date, '%Y-%m-%d').replace(hour=23, minute=59, second=59)
                data = data.filter(updated_on__range=[from_date, to_date])
            except ValueError:
                # Handle invalid date format
                return HttpResponse("Invalid date format. Please use YYYY-MM-DD.", status=400)

    # Prepare the CSV response
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="client.csv"'

    writer = csv.writer(response)
    writer.writerow([
        'Employee Phone', 'Client Type', 'Client Name', 'Client Phone', 'Client Email',
        'Client Address', 'Client Next Followup Date', 'Client Status', 
    ])

    for item in data:
        writer.writerow([
            item.username, item.clinet_type, item.client_name, item.client_phone, item.client_email,
            item.client_address, item.client_next_followup_date, item.client_status, 
        ])

    return response




from random import randrange
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.http import HttpResponseForbidden

def employee_login(request):
    username=''
    password=''
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        try:
            user = authenticate(username=username,password=password)
            if user is not None:
                if Employee.objects.filter(phone=username).exists():
                    login(request, user)
                    messages.success(request, "Details Verified! Login successful.")
                    return redirect("/employee-dashboard")
                else:
                    messages.error(request, "Employee not found.")
            else:
                messages.error(request, "Invalid Username and Password.")
        except:
            
            messages.error(request, "Authentication failed. Please try again.")

    return render(request, 'employee/login.html',{'username':username,'password':password})


@login_required(login_url="/employee-login/")
def employee_dashboard(request):
    try:
       emp=Employee.objects.get(phone=request.user.username)
    except:
       return HttpResponseForbidden("You don't have permission to access this page.")
    if not emp:
        return HttpResponseForbidden("You don't have permission to access this page.")
    else:
      total_fresh=len(Client.objects.filter(username="",emp_name=emp.phone))
      total_client=len(Client.objects.filter(username=emp.phone))
      client_pending=len(Client.objects.filter(username=emp.phone,client_status="pending"))
      client_followup=len(Client.objects.filter(username=emp.phone,client_status="followup"))
      client_cancelled=len(Client.objects.filter(username=emp.phone,client_status="cnp"))
      client_completed=len(Client.objects.filter(username=emp.phone,client_status="completed"))
      client_ni=len(Client.objects.filter(username=emp.phone,client_status="not-interested"))
      client_nii=len(Client.objects.filter(username=emp.phone,client_status="not-in-industry"))
      

      data=Client.objects.filter(emp_name=emp.phone).order_by('id').reverse()
      paginator = Paginator(data, 100)  # Show 10 posts per page
      page_number = request.GET.get('page')
      page_posts = paginator.get_page(page_number)
      current_page = page_posts.number
      total_pages = paginator.num_pages
      page_range = range(max(current_page - 2, 1), min(current_page + 3, total_pages + 1))
      context={
        'total_fresh':total_fresh,
        'total_client':total_client,
        'emp':emp,
        'client_pending':client_pending,
        'client_followup':client_followup,
        'client_cancelled':client_cancelled,
        'client_completed':client_completed,
        'page_posts':page_posts,
        'page_range':page_range,
        'client_ni':client_ni,
        'client_nii':client_nii
        
    }
      return render(request,'employee/index.html',context)



@login_required(login_url="/employee-login/")
def employee_add_data(request):
    try:
       emp=Employee.objects.get(phone=request.user.username)
    except:
       return HttpResponseForbidden("You don't have permission to access this page.")
    if not emp:
        return HttpResponseForbidden("You don't have permission to access this page.")
    else:
      total_data=len(Client.objects.filter(emp_name=request.user.username))
      total_report=len(Client.objects.filter(emp_name=request.user.username))
      total_fresh=len(Client.objects.filter(username="",emp_name=emp.phone))
      total_client=len(Client.objects.filter(username=emp.phone))
      client_pending=len(Client.objects.filter(username=emp.phone,client_status="pending"))
      client_followup=len(Client.objects.filter(username=emp.phone,client_status="followup"))
      client_cancelled=len(Client.objects.filter(username=emp.phone,client_status="cnp"))
      client_completed=len(Client.objects.filter(username=emp.phone,client_status="completed"))
      client_ni=len(Client.objects.filter(username=emp.phone,client_status="not-interested"))
      client_nii=len(Client.objects.filter(username=emp.phone,client_status="not-in-industry"))
      
      msg=''
      # Lists to store report data
      duplicate_numbers = []
      invalid_numbers = []
  
      if request.method == "POST":
          ecode = request.FILES.get('file')
          ctype = request.POST.get('ctype')
          df = pd.read_excel(ecode)
  
          for index, row in df.iterrows():
              phone = str(row['Phone']).strip()
              phone=phone.replace(".0",'')
              name = row.get('Name', '')
              email = row.get('Email', '')
  
              # Validate phone number
              if not phone.isdigit() or len(phone) != 10:
                  invalid_numbers.append({'row': index + 1, 'phone': phone})
                  continue  # Skip this row
  
              # Check for duplicate phone number
              if Client.objects.filter(client_phone=phone).exists():
                  duplicate_numbers.append({'row': index + 1, 'phone': phone})
                  continue  # Skip this row
  
              # Create and save the client (name and email can be blank)
              c = Client(
                  client_phone=phone,
                  client_name=name,  # Set to None if blank
                  client_email=email, # Set to None if blank
                  emp_name=emp.phone if emp.phone else None , # Set to None if blank
                  clinet_type=ctype , # Set to None if blank
                  created_on=datetime.now(),  # Set to None if blank
                  updated_on=datetime.now()
              )
              c.save()
              msg='Done'
  
          # Redirect after saving, but with the report data in the context
          context = {
              'msg': msg,
              'emp':emp,
              'total_data':total_data,
              'total_report':total_report,
              'duplicate_numbers': duplicate_numbers,
              'invalid_numbers': invalid_numbers,
              'total_fresh':total_fresh,
              'total_client':total_client,
              'client_pending':client_pending,
              'client_followup':client_followup,
              'client_cancelled':client_cancelled,
              'client_completed':client_completed,
              'client_ni':client_ni,
              'client_nii':client_nii
        
          }
  
          return render(request, 'employee/add-excel.html', context)
  
      context = {
              'msg': msg,
              'emp':emp,
              'total_data':total_data,
              'total_report':total_report,
              'duplicate_numbers': duplicate_numbers,
              'invalid_numbers': invalid_numbers,
              'total_fresh':total_fresh,
              'total_client':total_client,
              'client_pending':client_pending,
              'client_followup':client_followup,
              'client_cancelled':client_cancelled,
              'client_completed':client_completed,
              'client_ni':client_ni,
              'client_nii':client_nii
        
          }
      return render(request, 'employee/add-excel.html', context)
  
  
    
@login_required(login_url="/employee-login/")
def employee_update_data(request,id):
    try:
       emp=Employee.objects.get(phone=request.user.username)
    except:
       return HttpResponseForbidden("You don't have permission to access this page.")
    if not emp:
        return HttpResponseForbidden("You don't have permission to access this page.")
    else:
        total_data=len(Client.objects.filter(emp_name=request.user.username))
        total_report=len(Client.objects.filter(emp_name=request.user.username))
        total_fresh=len(Client.objects.filter(username="",emp_name=emp.phone))
        total_client=len(Client.objects.filter(username=emp.phone))
        client_pending=len(Client.objects.filter(username=emp.phone,client_status="pending"))
        client_followup=len(Client.objects.filter(username=emp.phone,client_status="followup"))
        client_cancelled=len(Client.objects.filter(username=emp.phone,client_status="cnp"))
        client_completed=len(Client.objects.filter(username=emp.phone,client_status="completed"))
        client_ni=len(Client.objects.filter(username=emp.phone,client_status="not-interested"))
        client_nii=len(Client.objects.filter(username=emp.phone,client_status="not-in-industry"))
      
        msg=''
        data=Client.objects.get(id=id)
        chistory=Client_History.objects.filter(client_phone=data.client_phone)
        if(request.method=='POST'):
          data.clinet_type=request.POST.get('clinet_type')
          data.client_name=request.POST.get('client_name')
          data.client_email=request.POST.get('client_email')
          data.client_phone=request.POST.get('client_phone')
          data.client_address=request.POST.get('client_address')
          data.client_status=request.POST.get('client_status')
          data.client_next_followup_date=request.POST.get('client_next_followup_date')
          data.created_on=datetime.now()
          data.emp_name=emp.phone
          if(request.POST.get('client_status')):
              data.username=emp.phone
              ch=Client_History()
              ch.client_phone=data.client_phone
              ch.client_message=request.POST.get('client_message')
              ch.client_next_followup_date=request.POST.get('client_next_followup_date')
              ch.updated_on=datetime.now()
              ch.save()
          else:
              data.username=''
        context = {
          'msg': msg,
          'total_data':total_data,  
          'total_report':total_report,
          'data':data,
          'total_fresh':total_fresh,
          'total_client':total_client,
          'emp':emp,
          'client_pending':client_pending,
          'client_followup':client_followup,
          'client_cancelled':client_cancelled,
          'client_completed':client_completed,
          'client_ni':client_ni,
          'client_nii':client_nii,
          'chistory':chistory
        }
        return render(request,'employee/update-client.html',context)


@login_required(login_url="/employee-login/")
def employee_delete_data(request,id,pn):
    data=Client.objects.get(id=id)
    data.delete()
    return redirect(f'/employee-dashboard/?page=' + str(pn))

@login_required(login_url="/employee-login/")
def employee_logout(request):
    logout(request)
    return redirect('/employee-login')


@login_required(login_url="/")
def admin_distribute_data(request):
    employees = Employee.objects.filter(category="Telesales")
    print("Employee: ",employees)
    clients_to_assign = Client.objects.filter(username="",client_status="pending")  # Fetch unassigned clients
    
    for employee in employees:
        # Count the number of clients already assigned to this employee
        assigned_count = Client.objects.filter(username=employee.phone,client_status="pending").count()
        
        # Only assign if the employee has 50 or fewer clients
        if assigned_count < 50:
            # Calculate how many clients this employee can still take
            remaining_capacity = 200 - assigned_count
            
            # Fetch the required number of unassigned clients
            clients_to_assign_batch = clients_to_assign[:remaining_capacity]
            
            # Update clients in bulk
            for client in clients_to_assign_batch:
                client.username = employee.phone
                
            
            # Bulk update in one query
            Client.objects.bulk_update(clients_to_assign_batch, ['username'])
            
            # Remove the assigned clients from the queryset
            clients_to_assign = clients_to_assign.exclude(id__in=[client.id for client in clients_to_assign_batch])

            # Stop if no more clients are available
            if not clients_to_assign.exists():
                break

    return HttpResponse(
        '<p>Data Assigned Successfully... <a href="/admin-dashboard/">Go to the page</a></p>',
        content_type="text/html"
    )



@login_required(login_url="/employee-login/")
def add_image(request):
    try:
        emp = Employee.objects.get(phone=request.user.username)
    except Employee.DoesNotExist:
        return HttpResponseForbidden("You don't have permission to access this page.")
    
    total_data = len(Client.objects.filter(emp_name=request.user.username))
    total_report = len(Client.objects.filter(emp_name=request.user.username))
    
    if request.method == 'POST' and request.FILES:
        images = request.FILES.getlist('image')
        for image_file in images:
            img = Image(image=image_file)
            img.save()
    
    data = Image.objects.all().order_by('id').reverse()
    paginator = Paginator(data, 100)  # Show 100 posts per page
    page_number = request.GET.get('page')
    page_posts = paginator.get_page(page_number)
    current_page = page_posts.number
    total_pages = paginator.num_pages
    page_range = range(max(current_page - 2, 1), min(current_page + 3, total_pages + 1))
    
    context = {
        'page_posts': page_posts,
        'page_range': page_range,
        'emp': emp,
        'total_data': total_data,
        'total_report': total_report
    }
    return render(request, 'employee/image.html', context)


@login_required(login_url="/employee-login/")
def delete_image(request,id):
    try:
        emp = Employee.objects.get(phone=request.user.username)
    except Employee.DoesNotExist:
        return HttpResponseForbidden("You don't have permission to access this page.")
    
    data=Image.objects.get(id=id)
    data.delete()
    return redirect("/add-image/")


@login_required(login_url="/employee-login/")
def employee_client(request,ops):
    try:
       emp=Employee.objects.get(phone=request.user.username)
    except:
       return HttpResponseForbidden("You don't have permission to access this page.")
    if not emp:
        return HttpResponseForbidden("You don't have permission to access this page.")
    else:
        total_client=len(Client.objects.filter(emp_name=emp.phone,username=emp.phone))
        total_fresh=len(Client.objects.filter(emp_name=emp.phone,username=""))
        client_pending=len(Client.objects.filter(username=emp.phone,client_status="pending"))
        client_followup=len(Client.objects.filter(username=emp.phone,client_status="followup"))
        client_cancelled=len(Client.objects.filter(username=emp.phone,client_status="cnp"))
        client_completed=len(Client.objects.filter(username=emp.phone,client_status="completed"))
        client_ni=len(Client.objects.filter(username=emp.phone,client_status="not-interested"))
        client_nii=len(Client.objects.filter(username=emp.phone,client_status="not-in-industry"))
        employee=Employee.objects.all()
        if(ops=='all'):
           data=Client.objects.filter(emp_name=emp.phone,username=emp.phone).order_by('id').reverse()
        elif(ops=='fresh'):
           data=Client.objects.filter(emp_name=emp.phone,username="").order_by('id').reverse()
        else:
           data=Client.objects.filter(emp_name=emp.phone,client_status=ops).order_by('id').reverse()
    
        paginator = Paginator(data, 100)  # Show 10 posts per page
        page_number = request.GET.get('page')
        page_posts = paginator.get_page(page_number)
        current_page = page_posts.number
        total_pages = paginator.num_pages
        page_range = range(max(current_page - 2, 1), min(current_page + 3, total_pages + 1))
        context={
            'total_client':total_client,
            'emp':emp,
            'client_pending':client_pending,
            'client_followup':client_followup,
            'client_cancelled':client_cancelled,
            'client_completed':client_completed,
            'page_posts':page_posts,
            'page_range':page_range,
            'employee':employee,
            'client_ni':client_ni,
            'client_nii':client_nii,
            'ops':ops,
            'total_fresh':total_fresh
        }
        return render(request,'employee/index.html',context)



@login_required(login_url="/employee-login/")
def employee_search(request):
    try:
        emp = Employee.objects.get(phone=request.user.username)
    except Employee.DoesNotExist:
        return HttpResponseForbidden("You don't have permission to access this page.")
    
    total_client=len(Client.objects.filter(username=emp.phone))
    total_fresh=len(Client.objects.filter(username="",emp_name=emp.phone))
    client_pending=len(Client.objects.filter(username=emp.phone,client_status="pending"))
    client_followup=len(Client.objects.filter(username=emp.phone,client_status="followup"))
    client_cancelled=len(Client.objects.filter(username=emp.phone,client_status="cnp"))
    client_completed=len(Client.objects.filter(username=emp.phone,client_status="completed"))
    client_ni=len(Client.objects.filter(username=emp.phone,client_status="not-interested"))
    client_nii=len(Client.objects.filter(username=emp.phone,client_status="not-in-industry"))
        
    data = Client.objects.filter(Q(username__icontains=emp.phone)|Q(emp_name__icontains=emp.phone))
    search_query = ''
    
    if request.method == "POST":
        search_query = request.POST.get('name', '')
        request.session['search_query'] = search_query
    elif request.method == "GET":
        search_query = request.GET.get('name', request.session.get('search_query', ''))

    if search_query:
        data = Client.objects.filter(
            Q(client_name__icontains=search_query) |
            Q(client_phone__icontains=search_query) |
            Q(username__icontains=search_query) 
            
        )
    
    employee=Employee.objects.all()
    msg = ""
    paginator = Paginator(data, 100)  # Show 100 posts per page
    page_number = request.GET.get('page')
    page_posts = paginator.get_page(page_number)
    current_page = page_posts.number
    total_pages = paginator.num_pages
    page_range = range(max(current_page - 2, 1), min(current_page + 3, total_pages + 1))
    
    return render(request, "employee/index.html", 
        {
        'employee':employee,
        'msg': msg,
        'total_client':total_client,
        'emp':emp,
        'total_fresh':total_fresh,
        'client_pending':client_pending,
        'client_followup':client_followup,
        'client_cancelled':client_cancelled,
        'client_completed':client_completed,
        'client_ni':client_ni,
        'client_nii':client_nii,
        'page_posts': page_posts,
        'page_range': page_range,
        'search_query': search_query,
        })
 

@login_required(login_url="/employee-login/")
def employee_add_single_client(request):
    try:
        emp = Employee.objects.get(phone=request.user.username)
    except Employee.DoesNotExist:
        return HttpResponseForbidden("You don't have permission to access this page.")
    
    total_client=len(Client.objects.filter(username=emp.phone))
    total_fresh=len(Client.objects.filter(username="",emp_name=emp.phone))
    client_pending=len(Client.objects.filter(username=emp.phone,client_status="pending"))
    client_followup=len(Client.objects.filter(username=emp.phone,client_status="followup"))
    client_cancelled=len(Client.objects.filter(username=emp.phone,client_status="cnp"))
    client_completed=len(Client.objects.filter(username=emp.phone,client_status="completed"))
    client_ni=len(Client.objects.filter(username=emp.phone,client_status="not-interested"))
    client_nii=len(Client.objects.filter(username=emp.phone,client_status="not-in-industry"))
        
    msg=""
    msg2=""
    if(request.method=='POST'):
      data=Client()
      data.clinet_type=request.POST.get('clinet_type')
      data.client_name=request.POST.get('client_name')
      data.client_email=request.POST.get('client_email')
      data.client_phone=request.POST.get('client_phone')
      data.client_address=request.POST.get('client_address')
      data.client_status=request.POST.get('client_status')
      data.client_next_followup_date=request.POST.get('client_next_followup_date')
      data.created_on=datetime.now()
      data.updated_on=datetime.now()
      data.emp_name=emp.phone
      if(data.client_status):
          data.username=emp.phone
          ch=Client_History()
          ch.client_phone=data.client_phone
          ch.client_message=request.POST.get('client_message')
          ch.client_next_followup_date=request.POST.get('client_next_followup_date')
          ch.updated_on=datetime.now()
          ch.save()
      else:
          data.username=''
      if(Client.objects.filter(client_phone=request.POST.get('client_phone'))):
          msg2="Done"
      else:
         data.save()
         msg="done"
    context={
        'msg2':msg2,
        'msg': msg,
        'total_client':total_client,
        'emp':emp,
        'total_fresh':total_fresh,
        'client_pending':client_pending,
        'client_followup':client_followup,
        'client_cancelled':client_cancelled,
        'client_completed':client_completed,
        'client_ni':client_ni,
        'client_nii':client_nii,
        }
    return render(request,'employee/add-client.html',context)




#Employee Filter
@login_required(login_url="/")
def admin_employee_filter(request):
    emp = Client.objects.filter(username="").count()
    total_client = Client.objects.count()
    client_pending = Client.objects.filter(client_status="pending").count()
    client_followup = Client.objects.filter(client_status="followup").count()
    client_cancelled = Client.objects.filter(client_status="cnp").count()
    client_completed = Client.objects.filter(client_status="completed").count()
    client_ni = Client.objects.filter(client_status="not-interested").count()
    client_nii = Client.objects.filter(client_status="not-in-industry").count()
    employee = Employee.objects.all()
    username=''
    data = Client.objects.none()  # Default empty queryset
    ops=''
    td=''
    fd=''
    # Filter by operations and date range if provided
    if request.method == "POST":
        ops = request.POST.get('ops', 'all')
        username = request.POST.get('username')
        to_date = request.POST.get('to_date')
        from_date = request.POST.get('from_date')
        td=to_date
        fd=from_date
        print("OPS:", ops)
        print("From Date:", from_date)
        print("To Date:", to_date)
        print("Username:",username)

        # Filter based on 'ops'
        if ops == 'all' or ops=='':
            data = Client.objects.filter(emp_name=username).order_by('-id')
        elif ops == 'fresh':
            data = Client.objects.filter(emp_name=username).order_by('-id')
        else:
            data = Client.objects.filter(client_status=ops,emp_name=username).order_by('-id')

        # Filter by date range
        if to_date and from_date:
            try:
                # Convert date strings to datetime with full day range
                from_date = datetime.strptime(from_date, '%Y-%m-%d').replace(hour=0, minute=0, second=0)
                to_date = datetime.strptime(to_date, '%Y-%m-%d').replace(hour=23, minute=59, second=59)
                data = data.filter(updated_on__range=[from_date, to_date])
            except ValueError:
                # Handle invalid date format
                return HttpResponse("Invalid date format. Please use YYYY-MM-DD.", status=400)

    # Paginator
    paginator = Paginator(data, 100)  # Show 100 posts per page
    page_number = request.GET.get('page')
    page_posts = paginator.get_page(page_number)
    current_page = page_posts.number
    total_pages = paginator.num_pages
    page_range = range(max(current_page - 2, 1), min(current_page + 3, total_pages + 1))

    context = {
        'total_client': total_client,
        'emp': emp,
        'client_pending': client_pending,
        'client_followup': client_followup,
        'client_cancelled': client_cancelled,
        'client_completed': client_completed,
        'page_posts': page_posts,
        'page_range': page_range,
        'employee': employee,
        'client_ni': client_ni,
        'client_nii': client_nii,
        'ops': ops,
        'fd':fd,
        'td':td,
        'ephone':username
    }
    return render(request, 'employee-report.html', context)


@login_required(login_url='/')
def admin_download_employee_data(request):

    # Filter by date range if provided
    if request.method == "POST":
        username = request.POST.get('username')
        from_date = request.POST.get('from_date')
        to_date = request.POST.get('to_date')
        ops = request.POST.get('ops')
        print("Username: ",username)
        if(ops != 'all' and ops !='' ):
           data = Client.objects.filter(username=username,client_status=ops)
        else:
           if(ops=="fresh"):
               data = Client.objects.filter(username="")
           else:
              data = Client.objects.filter(username=username)

        # Ensure both to_date and from_date are not empty or None
        # Filter by date range
        if to_date and from_date:
            try:
                # Convert date strings to datetime with full day range
                from_date = datetime.strptime(from_date, '%Y-%m-%d').replace(hour=0, minute=0, second=0)
                to_date = datetime.strptime(to_date, '%Y-%m-%d').replace(hour=23, minute=59, second=59)
                data = data.filter(updated_on__range=[from_date, to_date])
            except ValueError:
                # Handle invalid date format
                return HttpResponse("Invalid date format. Please use YYYY-MM-DD.", status=400)

    # Prepare the CSV response
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="client.csv"'

    writer = csv.writer(response)
    writer.writerow([
        'Employee Phone', 'Client Type', 'Client Name', 'Client Phone', 'Client Email',
        'Client Address', 'Client Next Followup Date', 'Client Status', 'Created On', 'Updated On'
    ])

    for item in data:
        writer.writerow([
            item.username, item.clinet_type, item.client_name, item.client_phone, item.client_email,
            item.client_address, item.client_next_followup_date, item.client_status, item.created_on, item.updated_on
        ])

    return response




@login_required(login_url="/employee-login/")
def employee_email(request):
    try:
       emp=Employee.objects.get(phone=request.user.username)
    except:
       return HttpResponseForbidden("You don't have permission to access this page.")
    if not emp:
        return HttpResponseForbidden("You don't have permission to access this page.")
    else:
      total_fresh=len(Client.objects.filter(username="",emp_name=emp.phone))
      total_client=len(Client.objects.filter(username=emp.phone))
      client_pending=len(Client.objects.filter(username=emp.phone,client_status="pending"))
      client_followup=len(Client.objects.filter(username=emp.phone,client_status="followup"))
      client_cancelled=len(Client.objects.filter(username=emp.phone,client_status="cnp"))
      client_completed=len(Client.objects.filter(username=emp.phone,client_status="completed"))
      client_ni=len(Client.objects.filter(username=emp.phone,client_status="not-interested"))
      client_nii=len(Client.objects.filter(username=emp.phone,client_status="not-in-industry"))
      

      data=Email_Data.objects.filter(username=emp.phone).order_by('id').reverse()
      paginator = Paginator(data, 100)  # Show 10 posts per page
      page_number = request.GET.get('page')
      page_posts = paginator.get_page(page_number)
      current_page = page_posts.number
      total_pages = paginator.num_pages
      page_range = range(max(current_page - 2, 1), min(current_page + 3, total_pages + 1))
      context={
        'total_fresh':total_fresh,
        'total_client':total_client,
        'emp':emp,
        'client_pending':client_pending,
        'client_followup':client_followup,
        'client_cancelled':client_cancelled,
        'client_completed':client_completed,
        'page_posts':page_posts,
        'page_range':page_range,
        'client_ni':client_ni,
        'client_nii':client_nii
        
    }
      return render(request,'employee/email.html',context)


from email_validator import validate_email, EmailNotValidError

@login_required(login_url="/employee-login/")
def employee_add_email(request):
    try:
        emp = Employee.objects.get(phone=request.user.username)
    except:
        return HttpResponseForbidden("You don't have permission to access this page.")
    
    if not emp:
        return HttpResponseForbidden("You don't have permission to access this page.")
    else:
        total_data = len(Client.objects.filter(emp_name=request.user.username))
        total_report = len(Client.objects.filter(emp_name=request.user.username))
        total_fresh = len(Client.objects.filter(username="", emp_name=emp.phone))
        total_client = len(Client.objects.filter(username=emp.phone))
        client_pending = len(Client.objects.filter(username=emp.phone, client_status="pending"))
        client_followup = len(Client.objects.filter(username=emp.phone, client_status="followup"))
        client_cancelled = len(Client.objects.filter(username=emp.phone, client_status="cnp"))
        client_completed = len(Client.objects.filter(username=emp.phone, client_status="completed"))
        client_ni = len(Client.objects.filter(username=emp.phone, client_status="not-interested"))
        client_nii = len(Client.objects.filter(username=emp.phone, client_status="not-in-industry"))
        
        msg = ''
        duplicate_email = []
        invalid_email = []
  
        if request.method == "POST":
            ecode = request.FILES.get('file')
            df = pd.read_excel(ecode)
  
            for index, row in df.iterrows():
                email = row.get('email', '')
                name = row.get('name', '')
  
                # Validate email
                try:
                    validate_email(email)  # This will raise an error if the email is invalid
                except EmailNotValidError as e:
                    invalid_email.append({'row': index + 1, 'email': email, 'error': str(e)})
                    continue  # Skip invalid emails

                # Check for duplicate email
                if Email_Data.objects.filter(email=email).exists():
                    duplicate_email.append({'row': index + 1, 'email': email})
                    continue  # Skip this row

                # Create and save the client (name and email can be blank)
                c = Email_Data(
                    email=email,
                    name=name,  # Set to None if blank
                    username=emp.phone,  # Set to None if blank
                )
                c.save()
                msg = 'Done'
  
            context = {
                'msg': msg,
                'emp': emp,
                'total_data': total_data,
                'total_report': total_report,
                'duplicate_email': duplicate_email,
                'invalid_email': invalid_email,
                'total_fresh': total_fresh,
                'total_client': total_client,
                'client_pending': client_pending,
                'client_followup': client_followup,
                'client_cancelled': client_cancelled,
                'client_completed': client_completed,
                'client_ni': client_ni,
                'client_nii': client_nii,
            }
  
            return render(request, 'employee/add-email.html', context)
  
        context = {
            'msg': msg,
            'emp': emp,
            'total_data': total_data,
            'total_report': total_report,
            'duplicate_email': duplicate_email,
            'invalid_email': invalid_email,
            'total_fresh': total_fresh,
            'total_client': total_client,
            'client_pending': client_pending,
            'client_followup': client_followup,
            'client_cancelled': client_cancelled,
            'client_completed': client_completed,
            'client_ni': client_ni,
            'client_nii': client_nii,
        }
        return render(request, 'employee/add-email.html', context)


def remove_date(request):
    data=Client.objects.filter(Q(clinet_type__icontains="Telesales")|Q(clinet_type__icontains="Accountant"))
    if(data):
        data.delete()
    return redirect("/admin-dashboard")




@login_required(login_url="/")
def admin_filter_delete(request):
    
    # Filter by operations and date range if provided
    
        to_date = "2024-11-27"
        from_date = "2024-11-27"
        print("From Date:", from_date)
        print("To Date:", to_date)

        # Filter based on 'ops'
        
        data = Client.objects.filter(username="")
        data.delete()
    
        return redirect("/admin-dashboard")
