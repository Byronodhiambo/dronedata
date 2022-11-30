from django.contrib import admin
from .models import Rpas, Flights

# Register your models here.

class RpasAdmin(admin.ModelAdmin):
    list_display = ('rpas_type', 'rpas_reg', 'airframe_bf')



class FlightsAdmin(admin.ModelAdmin):
    list_display = ('flight_no', 'date','rpas','location_dep','location_arr','flight_type', 'pilot')


admin.site.register(Rpas,RpasAdmin)
admin.site.register(Flights,FlightsAdmin)