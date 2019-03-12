from django.db import models
from django.contrib.auth.models import User
from django import forms

# Create your models here.
class WeaponList(models.Model):
    name = models.CharField(max_length=100)
    minLevel = models.IntegerField(default=1)
    paBonus = models.IntegerField(default=1)
    maBonus = models.IntegerField(default=1)

    def __str__(self):
        return self.name

class ArmourList(models.Model):
    name = models.CharField(max_length=100)
    minLevel = models.IntegerField(default=1)
    pdBonus = models.IntegerField(default=1)
    mdBonus = models.IntegerField(default=1)

    def __str__(self):
        return self.name

class OffHandList(models.Model):
    name = models.CharField(max_length=100)
    minLevel = models.IntegerField(default=1)
    pdBonus = models.IntegerField(default=1)
    mdBonus = models.IntegerField(default=1)

    def __str__(self):
        return self.name

class AccessoryList(models.Model):
    name = models.CharField(max_length=100)
    minLevel = models.IntegerField(default=1)

    bonusType1 = models.CharField(max_length=100, null=True,blank=True) #ex: str
    bonus1 = models.IntegerField(default=1,null=True,blank=True) #ex +1

    bonusType2 = models.CharField(max_length=100, null=True, blank=True)  # ex: str
    bonus2 = models.IntegerField(default=1,null=True,blank=True)  # ex +1

    bonusType3 = models.CharField(max_length=100, null=True, blank=True)  # ex: str
    bonus3 = models.IntegerField(default=1,null=True,blank=True)  # ex +1

    def __str__(self):
        return self.name


#lets put our base stats in a database
class BaseCharacterList(models.Model):
    job_name = models.CharField(max_length=100, null=True)
    hp = models.IntegerField(default=1)
    mp = models.IntegerField(default=1)

    physA = models.IntegerField(default=1)
    physD = models.IntegerField(default=1)
    magA = models.IntegerField(default=1)
    magD = models.IntegerField(default=1)

    mainE = models.ForeignKey(WeaponList, on_delete = models.SET_NULL,null=True, blank=True)
    offE = models.ForeignKey(OffHandList, on_delete = models.SET_NULL,null=True, blank=True)
    armorE = models.ForeignKey(ArmourList, on_delete = models.SET_NULL,null=True, blank=True)
    accE = models.ForeignKey(AccessoryList, on_delete = models.SET_NULL,null=True, blank=True)

    def __str__(self):
        return self.job_name

class Character(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    gender = models.CharField(max_length=10)
    level = models.IntegerField(default=1)

    job = models.ForeignKey(BaseCharacterList, on_delete = models.SET_NULL,null=True)

    hp = models.IntegerField(default = 1)
    mp = models.IntegerField(default = 1)

    physA = models.IntegerField(default = 1)
    physD = models.IntegerField(default = 1)
    magA = models.IntegerField(default = 1)
    magD = models.IntegerField(default = 1)

    mainE = models.ForeignKey(WeaponList, on_delete = models.SET_NULL,null=True, blank=True)
    offE = models.ForeignKey(OffHandList, on_delete = models.SET_NULL,null=True, blank=True)
    armorE = models.ForeignKey(ArmourList, on_delete = models.SET_NULL,null=True, blank=True)
    accE = models.ForeignKey(AccessoryList, on_delete = models.SET_NULL,null=True, blank=True)

    def __str__(self):
        return self.user.username

class Position(models.Model):
    character = models.ForeignKey(Character, on_delete=models.CASCADE)
    posx = models.IntegerField(default=16)
    posy = models.IntegerField(default=16)
    mapseed = models.IntegerField(default=1)
    timestamp = models.IntegerField(default = 1)

    def __str__(self):
        return self.character.user.username+" - "+str(self.posx)+" - "+str(self.posy)


JOBS= (
    ('Knight','Knight'),
    ('Mage', 'Mage'),
)
GENDER=(
    ('Male','Male'),
    ('Female','Female')
)
class CharacterModel(models.Model):
  job = models.CharField(max_length=6, choices=JOBS, default='Knight')
  gender = models.CharField(max_length=6, choices=GENDER, default='Male')
