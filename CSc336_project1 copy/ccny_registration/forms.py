from crispy_forms.helper import FormHelper 
from crispy_forms.layout import Layout, Submit
from django import forms 
from .models import Snippet 
from django.core.validators import RegexValidator

class NameWidget(forms.MultiWidget):

	def __init__(self,attrs=None):
		super().__init__([
			forms.TextInput(),
			forms.TextInput()
			], attrs)

	def decompress(self, value):
		if value:
			return value.split(' ')
		return ['','']

class NameField(forms.MultiValueField):

	widget = NameWidget

	def __init__(self, *args, **kwargs):

		fields = (
				forms.CharField(validators=[
					RegexValidator(r'[a-zA-Z]+',' Enter a valid first name')
				]),
				forms.CharField(validators=[
					RegexValidator(r'[a-zA-Z]+',' Enter a valid last name')
				])
			)

		super().__init__(fields, *args, **kwargs)

	def compress(self, data_list):
		#data_list = ['firstname', 'lastname']
		return f'{data_list[0]} {data_list[1]}'

class RegisterForm(forms.Form):
	first_name_last_name = NameField()
	email = forms.EmailField(label="Contact email")
	major = forms.ChoiceField(choices=[('first', 'Computer Science'),('other','Computer Engineering')])
	emplid = forms.CharField(required=True)
	semester = forms.CharField(required=True)
	gpa = forms.CharField(required=True)
	qpa = forms.CharField(required=True)
	additional_information = forms.CharField(widget=forms.Textarea, required=False) 

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)

		self.helper = FormHelper
		self.helper.form_method = 'post'

		self.helper.layout = Layout (
				'first_name_last_name',
				'email',
				'major',
				'emplid',
				'semester',
				'gpa',
				'qpa',
				'additional_information',
				Submit('submit', 'Submit', css_class = 'btn-success')
			)


class SnippetForm(forms.ModelForm):

	class Meta:
		model = Snippet 
		fields = ('name','body')