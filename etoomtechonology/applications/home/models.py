from django.db import models

# apps terceros
from model_utils.models import TimeStampedModel

class Home(TimeStampedModel):
    """ Modelo de pagina de Home """
    title = models.CharField('nombre', max_length=30)
    descripcion = models.TextField()
    about_title = models.CharField('Acerca del Titulo', max_length=50)
    about_text = models.TextField('Acerca del Texto')
    contact_email = models.EmailField('email de contacto', blank=True, null=True)
    public = models.BooleanField(default=False)
    image = models.ImageField('Imagen', upload_to='Home')
    in_home = models.BooleanField(default=False)
    phone = models.CharField('Telefono de contacto', max_length=20)
    
    class Meta:
        verbose_name = 'Home'
        verbose_name_plural = 'Home'
        
    def __str__(self):
        
        return self.title
    
    
class Suscribers(TimeStampedModel):
    """ Modelo de Suscriptores """
    email = models.EmailField()
    
    class Meta:
        verbose_name = 'Susciptor'
        verbose_name_plural = 'Suscriptores'
        
    def __str__(self):
        return self.email
        

class Contact(TimeStampedModel):
    """ Modelo de Contactos """
    full_name = models.CharField('Nombre Completo', max_length=60)
    email = models.EmailField()
    messagge = models.TextField()
    
    class Meta:
        verbose_name = 'Mensaje'
        verbose_name_plural = 'Mensajes'
        
    def __str__(self):
        return self.full_name


