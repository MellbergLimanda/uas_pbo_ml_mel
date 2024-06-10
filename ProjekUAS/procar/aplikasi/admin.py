from django.contrib import admin
from .models import Merek, Jenis, Mobil

class JenisAdmin(admin.ModelAdmin):
    list_display = ('name', 'merek')
    search_fields = ('name', 'merek__name'  )

class MobilAdmin(admin.ModelAdmin):
    list_display = ('merek', 'jenis', 'Penggerakroda', 'tahun', 'odometer', 'bahanbakar', 'transmisi', 'kapasitas_mesin', 'warna', 'harga')
    search_fields = ('merek__name', 'jenis__name', 'tahun', 'odometer', 'bahanbakar', 'transmisi', 'kapasitas_mesin', 'warna', 'harga')

    class Media:
        js = ('js/admin.js',) 

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "jenis":
            if request.user.is_superuser:
                kwargs["queryset"] = Jenis.objects.all()
            else:
                kwargs["queryset"] = Jenis.objects.filter(merek__in=Merek.objects.all())
        return super().formfield_for_foreignkey(db_field, request, **kwargs)

admin.site.register(Merek)
admin.site.register(Jenis, JenisAdmin)
admin.site.register(Mobil, MobilAdmin)
