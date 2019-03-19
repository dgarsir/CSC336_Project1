from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponse
from .forms import RegisterForm, Snippet 

def contact(request):
	if request.method == 'Post':
		form = RegisterForm(request.POST)
		if form.is_valid():
			name = form.cleaned_data['name']
			email = form.cleaned_data['email']
			#print(name)
			return redirect('base.html')
	else:
		form = RegisterForm()

	return render(request,'form.html',{'form':form})


def snippet_detail(request):
	if request.method == 'Post':
		form = RegisterForm(request.POST)
		if form.is_valid():
			form.save()

			return redirect('register-home')
	form = SnippetForm()
	return render(request,'form.html',{'form':form})