from typing import ContextManager
from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings

from .forms import RegModelForm, ContacForm
from .models import Registrado

# Create your views here.


def inicio(request):

    titulo = "HOLA"

    if request.user.is_authenticated:
        titulo = "Bienvenido %s" % (request.user)

    form = RegModelForm(request.POST or None)

    context = {
        "tituloVar": titulo,
        "formVar": form,

    }

    if form.is_valid():
        instance = form.save(commit=False)
        form_data = form.cleaned_data
        mailVar = form_data.get("email")
        nombreVar = form_data.get("nombre")

        if not instance.nombre:
            instance.nombre = "PERSONA"

        instance.save()

        if not nombreVar:
            context = {
                "tituloVar": "Gracias %s!" % (mailVar)

            }
        else:
            context = {
                "tituloVar": "Gracias %s!" % (nombreVar)

            }

        print(instance)
        print(instance.timeStamp)

    return render(request, "inicio.html", context)


def contact(request):

    titulo = "Enviar un mail como bot: "
    form = ContacForm(request.POST or None)

    context = {
        "tituloVar": titulo,
        "formVar": form,

    }

    if form.is_valid():

        emailVar = form.cleaned_data.get("email")
        mensajeVar = form.cleaned_data.get("mensaje")
        nombreVar = form.cleaned_data.get("nombre")
        asunto = "Asunto del mail!" 
        email_from = settings.EMAIL_HOST_USER
        email_to = [email_from, emailVar]
        mensaje_email = "%s: %s" % (nombreVar, mensajeVar)
        titulo = "Mail enviado!"

        send_mail(asunto,
                  mensaje_email,
                  email_from,
                  email_to,
                  fail_silently=False
                  )

        context = { 
            "tituloVar": titulo,
            "formVar": form,
            
         }

    return render(request, "forms.html", context)
