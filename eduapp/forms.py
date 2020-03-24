from django_summernote.widgets import SummernoteWidget, SummernoteInplaceWidget
from django import forms
from .models import *


class RandomForm(forms.Form):
    subject = forms.CharField(widget=forms.TextInput())
    message = forms.CharField(widget=SummernoteWidget())


class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={
        "placeholder": "Enter your username..",
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        "placeholder": "Enter password ....",
        "class": "form-control",

    }))


class ApplicationForm(forms.ModelForm):
    class Meta:
        model = Application
        exclude = ["program"]


class JoinUsForm(forms.ModelForm):
    class Meta:
        model = Application
        fields = "__all__"


class SliderForm(forms.ModelForm):
    class Meta:
        model = Slider
        fields = "__all__"


class OrganizationForm(forms.ModelForm):
    class Meta:
        model = Organization
        fields = "__all__"


class ProgramForm(forms.ModelForm):
    class Meta:
        model = Program
        fields = "__all__"


class SemesterForm(forms.ModelForm):
    class Meta:
        model = Semester
        fields = "__all__"


class SubjectForm(forms.ModelForm):
    class Meta:
        model = Subject
        fields = "__all__"


class TeacherForm(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = "__all__"


class FacilityForm(forms.ModelForm):
    class Meta:
        model = Facility
        fields = "__all__"


class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = "__all__"


class TestimonialsForm(forms.ModelForm):
    class Meta:
        model = Testimonials
        fields = "__all__"
