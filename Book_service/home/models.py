from django.db import models

# Create your models here.

# migrate- apply the pending changes created by makegrations
# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=122)
    mail = models.CharField(max_length=122)
    phone = models.CharField(max_length=12)
    desc = models.TextField()
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name
class Search(models.Model):
    title=models.CharField(max_length=122)
    description=models.TextField()
    def __str__(self):
        return self.title