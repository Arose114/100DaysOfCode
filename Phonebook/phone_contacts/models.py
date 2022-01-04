from django.db import models

# Create your models here.
class Contacts(models.Model):
    CATEGORY=(
        ('Family','Family'),
        ('Friends','Friends'),
        ('Work','Work'),
        ('Home','Home'),
        ('School','School'),
    )
    phone_number=models.CharField(null=True, max_length=50)
    contact_name=models.CharField(null=True, max_length=50)
    contact_address=models.CharField(null=True, max_length=50)
    category=models.CharField(null=True, max_length=50, choices=CATEGORY)
    profile_pic=models.ImageField(null=True, blank=True)
    date_created =models.DateTimeField(auto_now_add=True, null=True)




    

    def __str__(self):
        return self.name

  


