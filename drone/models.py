from django.db import models

# Create your models here.

class Rpas(models.Model):
    rpas_type = models.CharField(max_length=30)
    rpas_reg = models.CharField(max_length=30)
    airframe_bf = models.DurationField()
    airframe_hrs = models.DurationField(null=True, blank=True)


class Flights(models.Model):
    flight_no = models.CharField(max_length=30)
    date = models.DateField()
    rpas = models.ForeignKey("Rpas", on_delete=models.CASCADE)
    location_dep = models.CharField(max_length=30)
    location_arr = models.CharField(max_length=30)
    flight_type = models.CharField(max_length=30)
    pilot = models.CharField(max_length=30)
    crew = models.CharField(max_length=30)
    dep_time = models.DurationField()
    arr_time = models.DurationField()
    @property
    def flight_time(self):        
        dep_time = self.dep_time
        arr_time = self.arr_time
        flight_time = arr_time - dep_time
        return flight_time 
    @property
    def airframe_hrs(self):    
        flight_time = self.flight_time
        if (self.rpas.airframe_hrs==None):
            self.rpas.airframe_hrs = self.flight_time + self.rpas.airframe_bf
            return flight_time + self.rpas.airframe_bf
        return flight_time + self.rpas.airframe_hrs

        
    fuel_start =  models.IntegerField()
    fuel_end =  models.IntegerField()   
    batt = models.IntegerField()
    signature = models.CharField(max_length=30)


    @property
    def rpas_reg(self):
        return self.rpas.rpas_reg
    @property
    def rpas_type(self):
        return self.rpas.rpas_type


    

    
        

    



    
    

