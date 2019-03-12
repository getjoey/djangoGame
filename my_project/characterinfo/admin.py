from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(Character)
admin.site.register(BaseCharacterList)
admin.site.register(WeaponList)
admin.site.register(ArmourList)
admin.site.register(AccessoryList)
admin.site.register(OffHandList)
admin.site.register(Position)