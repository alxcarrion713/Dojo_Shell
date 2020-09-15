from django.db import models

# Create your models here.
class Dojo(models.Model):
    name= models.CharField(max_length=255)
    city= models.CharField(max_length=255)
    state= models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def_repr_(self):
        return f"<Dojo Object {self.name} {self.id}>"

class Ninjas(models.Model):
    school= models.ForeignKey(Dojo, related_name= 'students_attend', on_delete= models.CASCADE)
    first_name= models.CharField(max_length=255)
    last_name= models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
