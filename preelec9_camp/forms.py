from django import forms

class register_form1(forms.Form):
    gender_choices = [
        ('นาย', 'นาย'),
        ('นางสาว', 'นางสาว'),
    ]
    gender = forms.ChoiceField(choices=gender_choices)
    name = forms.CharField(label = "ชี่อ-นามสกุล", max_length= 100)

class register_form2(forms.Form):
    religion_choices = [
        ('พุทธ', 'พุทธ'),
        ('คริสต์', 'คริสต์'),
        ('อิสลาม', 'อิสลาม'),
        ('อื่นๆ', 'อื่นๆ'),
    ]
    nickname = forms.CharField(label="ชื่อเล่น", max_length=100)
    student_id = forms.CharField(label="รหัสนักศึกษา", max_length=100)
    email = forms.EmailField(label="อีเมล")
    birth_date = forms.DateField(label="วันเดือนปีเกิด")
    religion = forms.ChoiceField(label = "ศาสนา", choices=religion_choices)

class register_form3(forms.Form):
    address = forms.CharField(widget=forms.Textarea, label = 'ที่อยู่')
    self_telephone_num = forms.CharField(label="เบอร์โทรศัพท์ผู้สมัคร (+66)", max_length=9)
    parent_telephone_num = forms.CharField(label="เบอร์โทรศัพท์ผู้ปกครอง (+66)", max_length=9)
    line_id = forms.CharField(label="ไอดีไลน์", max_length=100)
    facebook = forms.CharField(label="เฟซบุ๊ก", max_length=100)
    instagram = forms.CharField(label="อินสตาแกรม", max_length=100)

class register_form4(forms.Form):
    allergic_meds = forms.CharField(label="ยาที่แพ้", max_length=200)
    allergic_foods = forms.CharField(label="อาหารที่แพ้", max_length=200)
    congenital_disease = forms.CharField(label="โรคประจำตัว", max_length=200)

class register_form5(forms.Form):
    passion = forms.CharField(widget=forms.Textarea, label = 'ความฝัน/เป้าหมายในการเรียน')