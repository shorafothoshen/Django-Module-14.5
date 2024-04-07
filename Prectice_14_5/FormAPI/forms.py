from django import forms
from django.core import validators

class precticeForm(forms.Form):
    name=forms.CharField(label="Student Name", help_text="Please Inpur your full name...", validators=[validators.MinLengthValidator(7,message="Enter your name at least 7 characters")])
    email=forms.CharField(label="Email Address",widget=forms.EmailInput(attrs={"placeholder":"Type your email.."}),validators=[validators.EmailValidator(message="Please Input Your valid email!!")])
    age=forms.CharField(widget=forms.NumberInput,initial=15)
    birthday=forms.DateField(widget=forms.DateInput(attrs={"type":"date"}))
    GENDERFIELD=[("Male","Male"),("Female","Female"),("Others","Others")]
    Gender=forms.ChoiceField(choices=GENDERFIELD ,widget=forms.RadioSelect)
    YEAR=["2023","2024","2025","2026","2027"]
    start_Date=forms.DateTimeField(widget=forms.SelectDateWidget(years=YEAR),label="Start Date")
    End_Date=forms.DateTimeField(widget=forms.SelectDateWidget(years=YEAR),label="End Date")
    weight=forms.FloatField(required=False, initial="0")
    comment=forms.CharField(widget=forms.Textarea(attrs={"row":2}))
    agree=forms.BooleanField()
