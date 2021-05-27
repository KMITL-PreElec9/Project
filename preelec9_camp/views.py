from django.shortcuts import redirect, render
from .models import *
from .forms import *
from django.http import HttpResponse

def index(request):
    completed = False
    try:
        db = Campdata.objects.get(reg_useremail = request.user.email)
        request.session['reg_name'] = db.name
        completed = True
    except:
        completed = False
    try: 
        db2 = Staff_auth.objects.get(email = request.user.email)
        return render(request, 'preelec9_camp/index.html', {'staff': True})
    except:
        return render(request, 'preelec9_camp/index.html', {'completed_reg': completed})

def unregister(request):
    try:
        db = Campdata.objects.get(reg_useremail = request.user.email)
        db.completed = False
        db.reg_useremail = None
        #db.house = None
        db.save()
        del request.session['reg_name']
    except:
        db = False
    return redirect(index)
r'''
def randomHouse(dbobj, data):
    if data.house != None:
        return data.house
    house = "Ares", "Poseidon", "Zues", "Hermes"
    if data.gender == "นาย":
        a = len(dbobj.objects.filter(gender = "นาย", completed = 1))
    else:
        a = len(dbobj.objects.filter(gender = "นางสาว", completed = 1))
    house_id = a % 4
    return house[house_id]
'''
def register(request, page_id=1, message = 0):
    if page_id == 1:
        try:
            del request.session['reg_name']
        except KeyError:
            pass
        try:
            db = Campdata.objects.get(reg_useremail = request.user.email)
            return redirect(index)
        except:
            db = False
        form = register_form1()
        if request.method == 'POST':
            form = register_form1(request.POST)
            if form.is_valid():
                cd = form.cleaned_data
                try:
                    db = Campdata.objects.get(name = cd['name'])
                    if db.reg_useremail:
                        return redirect(register, page_id = 1)
                    db.gender = cd['gender']
                    db.save()
                except:
                    db = False
                request.session['reg_name'] = cd['name']
            return redirect(register, page_id = 2)
        return render(request, 'preelec9_camp/register.html', {'form': form, 'db': db, 'page': page_id})
    elif page_id == 2:
        if request.method == 'POST':
            form = register_form2(request.POST)
            if form.is_valid():
                cd = form.cleaned_data
                db = Campdata.objects.get(name = request.session.get('reg_name'))
                db.nickname = cd['nickname']
                db.birth_date = cd['birth_date']
                db.student_id = cd['student_id']
                db.religion = cd['religion']
                db.save()
            return redirect(register, page_id = 3)
        else:
            try:
                db = Campdata.objects.get(name = request.session.get('reg_name'))
                form = register_form2(
                    initial={
                        'nickname' : db.nickname , 'student_id' : db.student_id,
                        'email' : db.email , 'religion' : db.religion, 'birth_date' : db.birth_date
                    })
            except:
                db = False; form = False           
            return render(request, 'preelec9_camp/register.html', {'form': form,'db': db,'page': page_id})
    elif page_id == 3:
        if request.method == 'POST':
            form = register_form3(request.POST)
            if form.is_valid():
                cd = form.cleaned_data
                db = Campdata.objects.get(name = request.session.get('reg_name'))
                db.address = cd['address']
                db.self_telephone_num = cd['self_telephone_num']
                db.parent_telephone_num = cd['parent_telephone_num']
                db.line_id = cd['line_id']
                db.facebook = cd['facebook']
                db.instagram = cd['instagram']
                db.save()
            return redirect(register, page_id = 4)
        else:
            try:
                db = Campdata.objects.get(name = request.session.get('reg_name'))
                form = register_form3(
                    initial={
                        'address' : db.address , 'self_telephone_num' : db.self_telephone_num,
                        'parent_telephone_num' : db.parent_telephone_num , 
                        'line_id' : db.line_id, 'facebook' : db.facebook, 'instagram': db.instagram
                    })
            except:
                db = False; form = False          
            return render(request, 'preelec9_camp/register.html', {'form': form,'db': db,'page': page_id})
    elif page_id == 4:
            if request.method == 'POST':
                form = register_form4(request.POST)
                if form.is_valid():
                    cd = form.cleaned_data
                    db = Campdata.objects.get(name = request.session.get('reg_name'))
                    db.allergic_foods = cd['allergic_foods']
                    db.allergic_meds = cd['allergic_meds']
                    db.congenital_disease = cd['congenital_disease']
                    db.save()
                return redirect(register, page_id = 5)
            else:
                try:
                    db = Campdata.objects.get(name = request.session.get('reg_name'))
                    form = register_form4(
                        initial={
                            'allergic_foods' : db.allergic_foods , 
                            'allergic_meds' : db.allergic_meds , 
                            'congenital_disease' : db.congenital_disease ,
                        })
                except:
                    db = False; form = False          
                return render(request, 'preelec9_camp/register.html', {'form': form,'db': db,'page': page_id})
    elif page_id == 5:
            if request.method == 'POST':
                form = register_form5(request.POST)
                if form.is_valid():
                    cd = form.cleaned_data
                    db = Campdata.objects.get(name = request.session.get('reg_name'))
                    db.passion = cd['passion']
                    #db.house = randomHouse(Campdata, db)
                    db.save()
                if db.reg_useremail:
                    return redirect(index)
                return redirect(register, page_id = 6)
            else:
                try:
                    db = Campdata.objects.get(name = request.session.get('reg_name'))
                    form = register_form5(
                        initial={
                            'passion' : db.passion , 
                        })
                except:
                    db = False; form = False       
                return render(request, 'preelec9_camp/register.html', {'form': form,'db': db,'page': page_id})
    elif page_id == 6:
        form= ""
        if request.method == 'POST':
            db = Campdata.objects.get(name = request.session.get('reg_name'))
            db.completed = True
            db.reg_useremail = request.user.email
            db.save()
            try:
                del request.session['reg_name']
            except KeyError:
                pass
            return render(request, 'preelec9_camp/register.html', {'form': form,'db': db,'page': page_id, 'success':True})
        else:
            try:
                db = Campdata.objects.get(name = request.session.get('reg_name'))      
            except:
                db = False
            return render(request, 'preelec9_camp/register.html', {'form': form,'db': db,'page': page_id})
    else:
        return redirect(register, page_id = 1)

def viewdata(request):
    try:
        db = Campdata.objects.get(reg_useremail = request.user.email)
        if db.completed ==1:
            return render(request, 'preelec9_camp/viewdata.html',{'db': db})
        else: return redirect(index)
    except:
        return redirect(index)

def viewdata64(request):
    try:  
        db2 = Staff_auth.objects.get(email = request.user.email)
    except:
      return redirect(index)
    if request.GET.get('id')==None:
        db = Campdata.objects.all()
        return render(request,'preelec9_camp/viewdata64.html', {'data': db})
    else:
        value = Campdata.objects.get(id = request.GET["id"])
        return render(request,'preelec9_camp/viewdata64.html', {'value': value})
