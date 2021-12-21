from django.contrib import admin
from .models import *


class StoneShapeAdmin(admin.TabularInline):
    model = StoneShape


class StoneTypeAdmin(admin.TabularInline):
    model = StoneType


class GenderAdmin(admin.TabularInline):
    model = Gender


class MetalTypeAdmin(admin.TabularInline):
    model = MetalType


class JewelryShapeAdmin(admin.TabularInline):
    model = JewelryShape


class JewelryAdmin(admin.ModelAdmin):
    inlines = [StoneShapeAdmin, StoneTypeAdmin, GenderAdmin, MetalTypeAdmin, JewelryShapeAdmin]


admin.site.register(StoneShape)
admin.site.register(StoneType)
admin.site.register(Gender)
admin.site.register(MetalType)
admin.site.register(JewelryShape)
admin.site.register(Jewelry)
