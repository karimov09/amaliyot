from django.db import models

class TechRes(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        permissions = [
            ("view_techres", "Can view tech resources"),
            ("edit_techres", "Can edit tech resources"),
        ]

    def __str__(self):
        return self.name


class Students(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    registered_date = models.DateField(auto_now_add=True)

    class Meta:
        permissions = [
            ("view_students", "Can view students"),
            ("edit_students", "Can edit students"),
        ]

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
