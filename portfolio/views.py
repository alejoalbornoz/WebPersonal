from django.shortcuts import render
from .models import Project

# Create your views here.
def portfolio(request):
    projects = Project.objects.all() #Nos devuelve los Todos los projectos de nuestra db de nuestro models Project
    return render(request, "portfolio/portfolio.html", {"projects":projects}) #Este diccionario es el contexto: un diccionario que pasa datos al template. Aquí, se pasa la variable projects al template, permitiendo que se usen los datos de los proyectos en el archivo HTML.

