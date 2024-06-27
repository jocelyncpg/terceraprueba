from django.db import models


class Musician(models.Model):
    # id_musician  = models.AutoField(db_column='idMusician', primary_key=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    instrument = models.CharField(max_length=100)
    def __str__(self):
        return str(self.first_name + self.last_name)


class Album(models.Model):
    # id_albun = models.AutoField(db_column='idAlbun', primary_key=True)
    # id_musician = models.ForeignKey('Musician',on_delete=models.CASCADE, db_column='idMusician')  
    artist = models.ForeignKey(Musician, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    release_date = models.DateField()
    num_stars = models.IntegerField()
    image = models.ImageField(upload_to="media/", default=None)
    def __str__(self):
        return str(self.name)