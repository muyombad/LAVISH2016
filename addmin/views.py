import random
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .Decorator import session_required
from .otp_cod import otp_code_g
from addmin.models import *
from django.conf import settings
from django.core.mail import send_mail
from twilio.rest import Client
from django.utils import timezone



# Create your views here.
# the viw the alow user to chane the password


from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm


@login_required
def change_password(request):
    if request.method == 'POST':
        current_password = request.POST.get('current_password')
        new_password1 = request.POST.get('new_password1')
        new_password2 = request.POST.get('new_password2')

        # Authenticate the user with the current password
        user = authenticate(username=request.user.username, password=current_password)

        if user is not None:
            # Check if the new passwords match
            if new_password1 == new_password2:
                # Update the user's password
                user.set_password(new_password1)
                user.save()

                # Update the session to keep the user logged in
                update_session_auth_hash(request, user)

                messages.success(request, 'Your password was successfully updated!')
                return redirect('user_profile_super')
            else:
                messages.error(request, 'New passwords do not match.')
                return redirect('user_profile_super')
        else:
            messages.error(request, 'Current password is incorrect.')

    return render(request, 'user_profile_super.html')





def admin(request):
    if request.method == 'POST':
        user_name1 = request.POST.get('admin_user_name')
        user_pass = request.POST.get('admin_pass')
        login_admin = authenticate( request, username = user_name1, password = user_pass)
        if login_admin is not None:
            ## get the user id from data bess
            request.session['user_id'] = login_admin.id
            ### sending eimail
            ## get the otp from data bess
            alla = otp_code.objects.get(pk=1)
            dit = {'ts':alla.code_otp}
            don = dit['ts']
            codea = otp_code_g()
            ot = otp_code.objects.filter(code_otp = don)
            ot.update(code_otp = codea )
            ## get the pk from super user
            use = User.objects.get(pk=1)
            use1 = {'use2':use.username}
            use3 = use1['use2']
            
            request.session['user_email'] = login_admin.email
            request.session['user_name'] = login_admin.username
            request.session['user_phone'] = login_admin.last_name

            subject = 'welcome to lavish '
            user_name = request.session.get('user_name')
            phone = request.session.get('user_phone')

            message = f'Hi {user_name}, Your OTP Code Is {codea}.'
            email_from = settings.EMAIL_HOST_USER

            ### send the otp to the mobile
            if use3 == user_name:
                try:
                  # client = Client(settings.TWILIO_ACCOUNT_SID, settings.TWILIO_AUTH_TOKEN)
                  # client.messages.create(
                  # to = phone,
                   #from_ = settings.TWILIO_PHONE_NUMBER,
                  # body = f'Your OTP code is: {codea}')

               ##send an emil
                   user_email = request.session.get('user_email')
               
                   email_to = [user_email, ]
            
                   send_mail( subject, message, email_from, email_to )
                   return redirect( 'otp') 
                except Exception as e:
                    messages.error(request, '[Errno 11001]')
                    return redirect('admin')
            else:
                messages.error(request, 'You Dont Have A Permission To Acsess That Page. Please Use This Page To Login !')
                return redirect('home')    
               
        else:  
           messages.error(request, "Invalid User Name Or Password !") 
           return redirect('admin')
    return render(request, 'admin.html')


@login_required(login_url='admin_home')
def admin_home(request):
    addm = request.user
    state = reversed(Admin_state.objects.all())
    return render(request, 'adminhome.html', {'admin':addm, 'state1':state})

def rest(request):
    return render(request, 'registration/password_reset_form.html')

## funtion for rerequest the otp
def rerequest_otp(request):
            alla = otp_code.objects.get(pk=1)
            dit = {'ts':alla.code_otp}
            don = dit['ts']
            ##get the number from db
           
            ## generet funtion for the code otp
            codea = otp_code_g()
            ot = otp_code.objects.filter(code_otp = don)
            ot.update(code_otp = codea )
            ##ge thye session for the user
            user_name = request.session.get('user_name')
            user_email = request.session.get('user_email')
            phone = request.session.get('user_phone')
            subject = 'welcome to lavish'
            
            message = f'Hi {user_name}, Your OTP Code Is {codea}.'
            email_from = settings.EMAIL_HOST_USER
            
            
            recipient_list = [user_email, ]
            
            try:
                #client = Client(settings.TWILIO_ACCOUNT_SID, settings.TWILIO_AUTH_TOKEN)
                #client.messages.create(
                #to=phone,
                #from_=settings.TWILIO_PHONE_NUMBER,
                #body=f'Your OTP code is: {codea}')
                send_mail( subject, message, email_from, recipient_list )
                messages.success(request, 'New OTP has Been Sent To Your Phone ! ')
                return redirect('otp')
            except Exception as e:
                messages.error(request, '[Erron 10250]')
                return redirect('otp')
           
@session_required(session_key='user_id', redirect_to='admin')
def otp(request):
    if request.method == 'POST':
        user_id = request.session.get('user_id')
        if user_id:
            userid = User.objects.get(id=user_id)
            otp = request.POST.get('otp')
            
            ## get the otp from data bess
            ala = otp_code.objects.get(pk=1)
            dit = {'ts':ala.code_otp}
            don1 = dit['ts']
            
            if int(otp) == don1: 
                login(request, userid) 
                return redirect('admin_home')
            else:
                messages.error(request, 'Incorect OTP!')
                return redirect('otp')
        return redirect('otp')
    return render(request, 'otp.html')


def logout_admin(request):
    logout(request)
    return redirect('admin')

@login_required(login_url='user_profile_super')
def user_profile_super(request):
    addm = request.user
    
    
    return render(request, 'user_profile_super.html', {'admin':addm})



@login_required(login_url='credit_or_debit')
def credit_or_debit(reqeust):
    addm = reqeust.user

    last_mtn = MTN.objects.last()
    last_mat1 = {'mtn':last_mtn.Available_Balance}
    last_mtn2 = last_mat1['mtn']

    last_airtell = AIRTELL.objects.last()
    last_airtell3 = {'airtell':last_airtell.Available_Balance}
    last_airtel2 = last_airtell3['airtell']

    last = Had_cash.objects.last()
    last1 = {'last2':last.agent}
    last3 = last1['last2']       
    
    last_all = int(last_mtn2) + int(last_airtel2) + int(last3)

    if reqeust.method == 'POST':
        
        T_type = reqeust.POST.get('transaction-type')
        T_company = reqeust.POST.get('Company')
        if T_type == 'credit' and T_company == 'mtn':
            last = MTN.objects.last()
            last1 = {'last2':last.Available_Balance}
            last3 = last1['last2']
            campany1 = 'MTM_admin_credit'
            amount = reqeust.POST.get('amount')
            amount1 = int(amount.replace(',',''))
            number = '_ _'
            name = 'Admin'
            r_number = random.randrange(100000, 999999)
            dat = timezone.localtime()
            Availble = int(last3) + int(amount1)
            credit_by = reqeust.user
            debit = '_'
            mtn_save = MTN(Credit=amount1,Debit=debit,Name=name,
                           R_Number=r_number,Phone_N=number,
                           Available_Balance=Availble,Time=dat,Maker=credit_by,campany=campany1)
            mtn_admin = Admin_state(Credit=amount1,Debit=debit,
                                    balance=Availble,Time=dat,campany=campany1)
            mtn_admin.save()
            mtn_save.save()
            return redirect('credit_or_debit')
            
            
        elif T_type == 'debit' and T_company == 'mtn': 
            last_0 = MTN.objects.last()
            last1 = {'last2':last_0.Available_Balance}
            last3 = last1['last2']

            campany = 'MTM_Admin_Debit'
            amount = reqeust.POST.get('amount')
            amount2 = int(amount.replace(',',''))
            number = '_ _'
            name = 'Admin'
            r_number = random.randrange(100000, 999999)
            dat = timezone.localtime()
            Availble = int(last3) - int(amount2)
            credit_by = reqeust.user
            cerdit = '-'
            mtn_save1 = MTN(Credit=cerdit,Debit=amount2,Name=name,
                           R_Number=r_number,Phone_N=number,
                           Available_Balance=Availble,Time=dat,Maker=credit_by,campany=campany)
            if int(last3) < int(amount2):
                messages.error(reqeust, 'Low Balance You Have ')
                return render(reqeust,'credit_or_debit.html', {'last':last3, 'admin':addm, 'airtell' 
                                                   :last_airtell.Available_Balance,
                                                    'mtn':last_mtn.Available_Balance,
                                                       'last_agent':last.agent,
                                                       'last_stationary':last.stationary,
                                                       'last_all':last_all})
            mtn_admin = Admin_state(Credit=cerdit,Debit=amount2,
                                    balance=Availble,Time=dat,campany=campany)
            mtn_admin.save()
            mtn_save1.save()
            return redirect('credit_or_debit')
        elif T_type == 'credit' and T_company == 'airtell':
            last = AIRTELL.objects.last()
            last1 = {'last2':last.Available_Balance}
            last3 = last1['last2']
            campany = 'AIRTELL_Admin_Credit'
            amount = reqeust.POST.get('amount')
            amount1 = int(amount.replace(',',''))
            number = '_ _'
            name = 'Admin'
            r_number = random.randrange(100000, 999999)
            dat = timezone.localtime()
            Availble = int(last3) + int(amount1)
            credit_by = reqeust.user
            debit = '-'
            mtn_save = AIRTELL(Credit=amount1,Debit=debit,Name=name,
                           R_Number=r_number,Phone_N=number,
                           Available_Balance=Availble,Time=dat,Maker=credit_by,campany=campany)
            mtn_admin = Admin_state(Credit=amount1,Debit=debit,
                                    balance=Availble,Time=dat,campany=campany)
            mtn_admin.save()
            mtn_save.save()
            return redirect('credit_or_debit')
        elif T_type == 'debit' and T_company == 'airtell': 
            last_0 = AIRTELL.objects.last()
            last1 = {'last2':last_0.Available_Balance}
            last3 = last1['last2']

            campany = 'Airtell_Admin_Debit'
            amount = reqeust.POST.get('amount')
            amount2 = int(amount.replace(',',''))
            number = '_ _'
            name = 'Admin'
            r_number = random.randrange(100000, 999999) 
            dat = timezone.localtime()
            Availble = int(last3) - int(amount2)
            credit_by = reqeust.user
            cerdit = '-'
            mtn_save1 = AIRTELL(Credit=cerdit,Debit=amount2,Name=name,
                           R_Number=r_number,Phone_N=number,
                           Available_Balance=Availble,Time=dat,Maker=credit_by,campany=campany)
            if int(last3) < int(amount2):
                messages.error(reqeust, 'Low Balance You Have ')
                return render(reqeust,'credit_or_debit.html', {'last':last3, 'admin':addm, 'airtell' 
                                                                  :last_airtell.Available_Balance,
                                                                   'mtn':last_mtn.Available_Balance,
                                                                    'last_agent':last.agent,
                                                                       'last_stationary':last.stationary,
                                                                       'last_all':last_all})
            air_admin = Admin_state(Credit=cerdit,Debit=amount2,
                                    balance=Availble,Time=dat,campany=campany)
            air_admin.save()
            mtn_save1.save()
            return redirect('credit_or_debit')
        elif T_type == 'credit' and T_company == 'had_cash': 
            amount = reqeust.POST.get('amount')
            amount2 = int(amount.replace(',',''))
            debit = '--'
            dat = timezone.localtime()
            Availble = last3 + amount2
            campany1 = "had_cash_credit"
            had = Had_cash.objects.filter(agent = last3)
            had.update(agent = last3 + amount2)
            has_admin = Admin_state(Credit=amount2,Debit=debit,
                                    balance=Availble,Time=dat,campany=campany1)
            has_admin.save()
            
            return redirect('credit_or_debit')
        elif T_type == 'debit' and T_company == 'had_cash': 
            amount = reqeust.POST.get('amount')
            amount2 = int(amount.replace(',',''))
            dat = timezone.localtime()
            Availble = last3 - amount2
            campany1 = "had_cash_debit"
            cerdit = "--"
            had = Had_cash.objects.filter(agent = last3)
            if int(last3) < int(amount2):
                messages.error(reqeust, 'Low Balance You Have ')
                return render(reqeust,'credit_or_debit.html', {'last':last3, 'admin':addm, 'airtell' 
                                                                  :last_airtell.Available_Balance,
                                                                   'mtn':last_mtn.Available_Balance,
                                                                    'last_agent':last.agent,
                                                                       'last_stationary':last.stationary,
                                                                       'last_all':last_all})
            had.update(agent = last3 - amount2)
            had_admin = Admin_state(Credit=cerdit,Debit=amount2,
                                    balance=Availble,Time=dat,campany=campany1)
            had_admin.save()
            
            return redirect('credit_or_debit')
        else:
            messages.error(reqeust, 'select company or T_type ')
            return redirect('credit_or_debit')

    return render(reqeust, 'credit_or_debit.html',{'admin':addm, 'airtell' 
                                                   :last_airtell.Available_Balance,
                                                    'mtn':last_mtn.Available_Balance,
                                                       'last_agent':last.agent,
                                                       'last_stationary':last.stationary,
                                                       'last_all':last_all})
    

