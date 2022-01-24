from django.db import models

# model lié a la table des preferences
class Preferences(models.Model):
    libele = models.CharField(max_length=100)

    class Meta:
        ordering = ['libele']

    def __str__(self):
        return self.libele

# model lié a la table des parrain
class Godfather(models.Model):
    preferences = models.ManyToManyField(Preferences)
    lastname = models.CharField(max_length=100)
    firstname = models.CharField(max_length=100)
    photo = models.ImageField(upload_to="media/godfather", blank=True, null = True)

    def __str__(self):
        return self.lastname +" "+ self.firstname


# model lié a la table des fieul
class Goddaughter(models.Model):
    preferences = models.ManyToManyField(Preferences)
    lastname = models.CharField(max_length=100)
    firstname = models.CharField(max_length=100)
    photo = models.ImageField(upload_to="media/goddaughter", blank=True, null = True)

    def __str__(self):
        return self.lastname +" "+ self.firstname


# model lié a la table des association
class Association(models.Model):
    godfather = models.ForeignKey(Godfather, on_delete=models.CASCADE)
    goddaughter = models.ForeignKey(Goddaughter, on_delete=models.CASCADE)

