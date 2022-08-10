from django.shortcuts import render,redirect
from .models import Contact
from django.http import HttpResponse
from django.contrib import messages
# Create your views here.

def contact(request):
    if request.method == "POST":
        contact = Contact()
        name = request.POST.get("name")
        email = request.POST.get("email")
        subject = request.POST.get("subject")
        contact.name = name
        contact.email = email
        contact.subject = subject
        contact.save()

        messages.success(request, "Düşüncelerinizi Dikkate Alacağız Şimdiden Teşekkür Ederiz...")
        return redirect("index")
    return render(request,"contact.html")