from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.forms import RadioSelect
from Futura_App.models import Login,Trainer,Student,Evaluation,Schedule,Slot,Technologies,Sections,Person
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit



YEAR_CHOICES = [(str(year), str(year)) for year in range(2023, 1990, -1)]

class DateInput(forms.DateInput):
    input_type = 'date'


class TimeInput(forms.TimeInput):
    input_type = 'time'


class LoginForm(UserCreationForm):
    username = forms.CharField()
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput, )
    password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput, )

    class Meta:
        model = Login
        fields = ('username', 'password1', 'password2')


class StudentForm(forms.ModelForm):
    year_of_passout = forms.ChoiceField(choices=YEAR_CHOICES, widget=forms.Select(
        attrs={'class': 'year-dropdown'}))
    internship_project = forms.ChoiceField(widget=RadioSelect,
                                           choices=[('Internship', 'Internship'), ('Project', 'Project')])
    mod_of_class = forms.ChoiceField(widget=RadioSelect,
                                     choices=[('Online', 'Online'), ('Offline', 'Offline')])

    # technology = forms.ChoiceField(widget=RadioSelect,
    #                                  choices=[('React Js', 'React Js'), ('Digital Marketing', 'Digital Marketing'),
    #                                           ('Data Science', 'Data Science'),('Mern Stack', 'Mern Stack'),('Flutter', 'Flutter'),
    #                                           ('Python', 'Python'),('UI UX Designing', 'UI UX Designing'),
    #                                           ('PHP(Laravel Framework)', 'PHP(Laravel Framework)'),('.NET', '.NET'),
    #                                           ('Python', 'Python'),('Software Testing', 'Software Testing')])
    #


    class Meta:
        model = Student
        fields = (
        'date','name', 'location','district','qualification','branch', 'college', 'year_of_passout','university','phone_no', 'whatsapp_no','email_id',  'guardian_name', 'guardian_phno', 'mod_of_class','internship_project',
          'technology', 'duration', 'How_do_you_reach_us')

class Trainerform(forms.ModelForm):
    class Meta:
        model = Trainer
        fields = ('name', 'phone_no','technology')

class Sectionsform(forms.ModelForm):
    class Meta:
        model = Sections
        fields = ('technology','name',)

class Evaluationform(forms.ModelForm):
    class Meta:
        model = Evaluation
        fields = ('evaluation_date','mcq','machine_test','evaluation')


class Slotform(forms.ModelForm):
    date = forms.DateField(widget=DateInput)
    start_time = forms.TimeField(widget=TimeInput)
    end_time = forms.TimeField(widget=TimeInput)
    class Meta:
        model = Slot
        fields = ('date','start_time','end_time')

class Technologyform(forms.ModelForm):
    class Meta:
        model = Technologies
        fields = ('name',)



class Scheduleform(forms.ModelForm):
    date = forms.DateField(widget=DateInput)
    # students = forms.ModelMultipleChoiceField(queryset=Student.objects.all(), required=False)
    #

    class Meta:
        model = Schedule
        fields = ('date','technology','trainers','students','slot')


class Activeform(forms.ModelForm):
    class Meta:
        model = Person
        fields = ('name', 'mod', 'technology', 'join_date', 'duration', 'staff', 'month')

