from django.db import models

# Create your models here.
class information(models.Model):
    name=models.CharField(max_length=200, blank=False)
    email=models.EmailField(max_length=100, blank=False)
    subject=models.CharField(max_length=500)
    content=models.CharField(max_length=20000)
    created_at=models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table="information"

    def __str__(self):
        return self.subject