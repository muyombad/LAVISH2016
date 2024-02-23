from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from addmin.models import *
from django.utils import timezone
from django.contrib.auth.models import User
# Create your views here.

from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm


@login_required
def change_password_emproy(request):
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
                return redirect('user_profile')
            else:
                messages.error(request, 'New passwords do not match.')
                return redirect('user_profile')
        else:
            messages.error(request, 'Current password is incorrect.')

    return render(request, 'user_profile.html')



def home(request):
    use = User.objects.get(pk=1)
    use1 = {'use2':use.username}
    use3 = use1['use2']
    if request.method == 'POST':
        user_name = request.POST.get('user_id')
        user_pass = request.POST.get('user_pass')
        ok = authenticate(username = user_name, password = user_pass)
        if ok is not None:
            if  use3 == user_name:
                messages.error(request, 'Admin please use this page to log in !') 
                return redirect('admin')
             
            login(request, ok)
            return redirect('Dashboard')
        else:
            messages.error(request, 'Incorrect password or office code !')  
            return redirect('home')  
    return render(request, 'home.html')

def log_out(reqeust):
    logout(reqeust)
    return redirect('home')


@login_required(login_url='Dashboard')
def Dashboard(reqeust):
    addm = reqeust.user
    my_mtn = reversed(MTN.objects.all())
    my_airtell = reversed(AIRTELL.objects.all())
    
    return render(reqeust, 'Dashboard.html', {'admin':addm, 'statement':my_mtn, 'statement1':my_airtell})
    

@login_required(login_url='mtn')
def mtn(reqeust):
    addm = reqeust.user
    cash = Had_cash.objects.get(pk=1)
    cash1 = {'cash2':cash.agent}
    chash3 = cash1['cash2']
    mtn_b = MTN.objects.last().Available_Balance
    if reqeust.method == 'POST':
        
        T_type = reqeust.POST.get('transaction-type')
        if T_type == 'credit':
            last = MTN.objects.last()
            last1 = {'last2':last.Available_Balance}
            last3 = last1['last2']
            campany = 'MTM'
            amount = reqeust.POST.get('amount')
            amount1 = int(amount.replace(',',''))
            number = reqeust.POST.get('phone_number')
            name = reqeust.POST.get('Name')
            r_number = reqeust.POST.get('R_number')
            dat = timezone.localtime()
            Availble = int(last3) - int(amount1)
            credit_by = reqeust.user
            debit = '-'
            mtn_save = MTN(Credit=amount1,Debit=debit,Name=name,
                           R_Number=r_number,Phone_N=number,
                           Available_Balance=Availble,Time=dat,Maker=credit_by,campany=campany)
            had = Had_cash.objects.filter(agent = chash3)
            if int(last3) < int(amount1):
                messages.error(reqeust, 'Low Balance You Have ')
                return render(reqeust,'mtn.html', {'last':last3, 'admin':addm, 'mtn_b':mtn_b})
            mtn_save.save()
            had.update(agent = chash3 + amount1)
            return redirect('mtn')
        else:
            last = MTN.objects.last()
            last1 = {'last2':last.Available_Balance}
            last3 = last1['last2']

            campany = 'MTM'
            amount = reqeust.POST.get('amount')
            amount2 = int(amount.replace(',',''))
            number = reqeust.POST.get('phone_number')
            name = reqeust.POST.get('Name')
            r_number = reqeust.POST.get('R_number')
            dat = timezone.localtime()
            Availble = int(last3) + int(amount2)
            credit_by = reqeust.user
            cerdit = '-'
            mtn_save1 = MTN(Credit=cerdit,Debit=amount2,Name=name,
                           R_Number=r_number,Phone_N=number,
                           Available_Balance=Availble,Time=dat,Maker=credit_by,campany=campany)
            
            if chash3 < amount2:
                 
                 messages.error(reqeust, 'Low Balance You Have ')
                 return render(reqeust,'mtn.html', { 'admin':addm, 'mtn_b':mtn_b, 'had':chash3})
            mtn_save1.save()
            had = Had_cash.objects.filter(agent = chash3)
            had.update(agent = chash3 - amount2) 
            return redirect('mtn')

    return render(reqeust, 'mtn.html',{'admin':addm, 'mtn_b':mtn_b})

@login_required(login_url='airtell')
def airtell(reqeust):
    airtell_b = AIRTELL.objects.last().Available_Balance
    addm = reqeust.user
    cash = Had_cash.objects.get(pk=1)
    cash1 = {'cash2':cash.agent}
    chash3 = cash1['cash2']
    chash4 = int(chash3)
    if reqeust.method == 'POST':
        
        T_type = reqeust.POST.get('transaction-type')
        if T_type == 'credit':
            last = AIRTELL.objects.last()
            last1 = {'last2':last.Available_Balance}
            last3 = last1['last2']
            campany = 'AIRTELL'
            amount = reqeust.POST.get('amount')
            amount1 = int(amount.replace(',',''))
            number = reqeust.POST.get('phone_number')
            name = reqeust.POST.get('Name')
            r_number = reqeust.POST.get('R_number')
            dat = timezone.localtime()
            Availble = int(last3) - int(amount1)
            credit_by = reqeust.user
            debit = '-'
            mtn_save = AIRTELL(Credit=amount1,Debit=debit,Name=name,
                           R_Number=r_number,Phone_N=number,
                           Available_Balance=Availble,Time=dat,Maker=credit_by,campany=campany)
            if int(last3) < int(amount1):
                messages.error(reqeust, 'Low Balance You Have ')
                return render(reqeust,'airtell.html', {'last':last3, 'admin':addm, 'airtell_b':airtell_b})
            mtn_save.save()

            had = Had_cash.objects.filter(agent = chash3)
            had.update(agent = chash3 + amount1)
            
            return redirect('airtell')
        else:
            last = AIRTELL.objects.last()
            last1 = {'last2':last.Available_Balance}
            last3 = last1['last2']

            campany = 'Airtell'
            amount = reqeust.POST.get('amount')
            amount2 = int(amount.replace(',',''))
            number = reqeust.POST.get('phone_number')
            name = reqeust.POST.get('Name')
            r_number = reqeust.POST.get('R_number')
            dat = timezone.localtime()
            Availble = int(last3) + int(amount2)
            credit_by = reqeust.user
            cerdit = '-'
            airtell1 = AIRTELL(Credit=cerdit,Debit=amount2,Name=name,
                           R_Number=r_number,Phone_N=number,
                           Available_Balance=Availble,Time=dat,Maker=credit_by,campany=campany)
            if chash3 < amount2:
                 
                 messages.error(reqeust, 'Low Balance You Have ')
                 return render(reqeust,'airtell.html', {'last':last3, 'admin':addm, 'airtell_b':airtell_b, 'had':chash4})
            airtell1.save()
            had = Had_cash.objects.filter(agent = chash3)
            had.update(agent = chash3 - amount2) 
            return redirect('airtell')
    return render(reqeust, 'airtell.html',{'admin':addm, 'airtell_b':airtell_b})


@login_required(login_url='tatal')
def tatal(reqeust):
    addm = reqeust.user
    last = AIRTELL.objects.last()
    last1 = {'last2':last.Available_Balance}
    last3 = last1['last2']

    last_m = MTN.objects.last()
    last1_m = {'last2':last_m.Available_Balance}
    last3_m = last1_m['last2']
    tatal_on_phone = int(last3) + int(last3_m)

    had_stetionary = Had_cash.objects.last()
    agent = Had_cash.objects.last()
    agent1 = {'agent2':agent.agent}
    agent3 = agent1['agent2']
    tata = int(agent3) + tatal_on_phone
    
    

    return render(reqeust, 'tatal.html', {'admin':addm, 'tatal_agent':tatal_on_phone,
                                           'had_stationary':had_stetionary.stationary,
                                           'had_agent':agent.agent, 'mtn':last_m.Available_Balance,
                                             'airtell':last.Available_Balance, 'tatal':tata} )


@login_required(login_url='stationary')
def stationary(request):
    addm = request.user  
    stationary1 = Had_cash.objects.get(pk=1)
    stationary2 = stationary1.stationary  
    if request.method == 'POST':
         T_type = request.POST.get('transaction-type')
         stationary1 = Had_cash.objects.get(pk=1)
         stationary2 = stationary1.stationary
         amount = request.POST.get('amount')
         amount1 = int(amount.replace(',', ''))
         
         if T_type == 'credit':
            seta = Had_cash.objects.filter(stationary = stationary2)
            seta.update(stationary = stationary2 + amount1)
            
         else:
            seta = Had_cash.objects.filter(stationary = stationary2)
            seta.update(stationary = stationary2 - amount1)

         return redirect('stationary')
            
    return render(request, 'stationary.html', {'admin':addm, 'stationary':stationary2})




@login_required(login_url='user_profile')
def user_profile(reqeust):
    addm = reqeust.user
    
    return render(reqeust, 'user_profile.html', {'admin':addm})  

@login_required(login_url='mtn_statment')
def mtn_statment(reqeust):
    addm = reqeust.user
    my_mtn = reversed(MTN.objects.all())
    nf = AIRTELL.objects.all()
    
    
    
    
    return render(reqeust, 'mtn_statment.html', {'admin':addm, 'statement':my_mtn})



@login_required(login_url='airtell_statment')
def airtell_statment(reqeust):
      my_airtell = reversed(AIRTELL.objects.all()) 
      addm = reqeust.user

      return render(reqeust, 'airtell_statment.html',{'admin':addm, 'statement1':my_airtell})