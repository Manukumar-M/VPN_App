
from django.db import models

class CertificateRequest(models.Model):
    server_ip = models.GenericIPAddressField()
    device_type = models.CharField(max_length=100)
    site_id = models.CharField(max_length=100)
    customer_name = models.CharField(max_length=255,unique=True)  
    model_name = models.CharField(max_length=100)
    project_type = models.CharField(max_length=100)
    device_id = models.CharField(max_length=10, blank=True, null=True)
    
    def __str__(self):
        return self.customer_name  

    # @classmethod
    # def generate_unique_customer_name(cls, desired_name):
    #     original_name = desired_name
    #     extension = 1
    #     while cls.objects.filter(customer_name=desired_name).exists():
    #         desired_name = f"{original_name}_{extension}"
    #         extension += 1
    #     return desired_name



class PersonCertificate(models.Model):
    server_ip = models.CharField(max_length=255) 
    person_name = models.CharField(max_length=255, unique=True)
    project_name = models.CharField(max_length=255)

    PROJECT_SCOPE_CHOICES = [
        ('internal', 'Internal'),
        ('external', 'External'),
    ]
    project_scope = models.CharField(max_length=10, choices=PROJECT_SCOPE_CHOICES, default='internal')

    def __str__(self):
        return self.person_name


    # @classmethod
    # def generate_unique_person_name(cls, desired_name1):
    #     original_name1 = desired_name1
    #     extension1 = 1
    #     while cls.objects.filter(person_name=desired_name1).exists():
    #         desired_name1 = f"{original_name1}_{extension1}"
    #         extension1 += 1
    #     return desired_name1





