from django.db import models

class Teachers(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.name


class Students(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    registered_date = models.DateField(auto_now_add=True)


    def __str__(self):
        return f"{self.first_name} {self.last_name}"
