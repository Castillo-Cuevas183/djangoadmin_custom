from django.contrib import admin
from .models import Producto 

class ProductAdmin(admin.ModelAdmin):
    readonly_fields = ('fecha_creacion', 'fecha_modificacion') #  readonly_fields: solo lectura usuario no puede modificar. 
    ordering = ('fecha_modificacion') 
    list_filter = ('valoracion' 'fecha_modificacion') 
    list_display = ('nombre', 'color_precio', 'stock', 'valoracion', 'fecha_creacion')
    
    
# Register your models here.
