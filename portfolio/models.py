from django.db import models

# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    image = models.ImageField(upload_to="projects") #El upload_to="projects" sirve para especificar donde guardar las imagenes en media, esto creara automaticamente una carpeta llamada projects en la carpeta media
    link = models.URLField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "proyecto"
        verbose_name_plural = "proyectos"
        
    def __str__(self):
        return self.title