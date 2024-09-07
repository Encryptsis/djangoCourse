from django.db import models

# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=200, verbose_name="Título")  # A string field for the project title with a max length
    description = models.TextField(verbose_name="Descripción")  # A text field for a detailed project description
    image = models.ImageField(verbose_name="Imagen", upload_to="projects")  # An image field to upload images to a specific folder
    link = models.URLField(null=True, blank=True, verbose_name="Dirección Web")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")  # A datetime field to automatically set the creation date
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de Edición")  # A datetime field to automatically update when the record is saved
    

    class Meta:
        verbose_name = "proyecto"
        verbose_name_plural = "proyectos"
        ordering = ["-created"]
        
    
    def __str__(self):
        return self.title