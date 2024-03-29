import datetime
from django.db import models
from app_machine.models import Station, Pallet, Camera
from app_reference.models import Reference


"""
Model Relation:

    PRODUCT +
            |
            + PROCESS   +
            + ...       |
                        + PROCESS VALUE -> PROCES DATA FIELD
                        + PROCESS VALUE -> PROCES DATA FIELD
                        + ...
"""


class Product(models.Model):
    """
    Opis elementu scalającego obiekty klasy 'Process' w całościowy produkt linii produkcyjnej
    """
    PART_STATUS = [
        (0, '-'),
        (2, 'OK'),
        (3, 'NOK'),
    ]
    id = models.BigAutoField(primary_key=True)
    reference = models.ForeignKey(Reference, on_delete=models.SET_NULL, null=True, blank=True, related_name='products')
    status = models.SmallIntegerField(choices=PART_STATUS, default=0)
    start = models.DateTimeField(default=datetime.datetime.now(), blank=True, null=True)
    end = models.DateTimeField(default=datetime.datetime.now(), blank=True, null=True)
    def __str__(self):
        return str('PRODUCT #') + str(self.id)


class Process(models.Model):
    """
    Opis części procesu produkcyjnego - wykonywanego na danym stanowisku/stacji
    """
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="process2",)
    station = models.ForeignKey(Station, on_delete=models.SET_NULL, null=True, )# related_name="process",)
    pallet = models.ForeignKey(Pallet, on_delete=models.SET_NULL, null=True, )# related_name="process",)
    start_process = models.DateTimeField(default=datetime.datetime.now())
    end_process = models.DateTimeField(default=datetime.datetime.now())
    operator = models.IntegerField(null=True, blank=True)
    PROCESS_STATUS = [
        ('0', '---'),
        ('1', 'POMIŃ'),
        ('2', 'OK'),
        ('3', 'NOK'),
        ('4', 'ANULUJ'),
    ]
    status = models.CharField(max_length=1, choices=PROCESS_STATUS, default='0')
    def __str__(self):
        return " (" + str(self.station) + ") - " + str(self.product)


class ProcessDataField(models.Model):
    """
    Opis pola dodatkowej wartości procesowej np.: "CAM1-Ciśnienie" / "ST6-Wysokość_magnesu_4"
    """
    station = models.ForeignKey(Station, on_delete=models.SET_NULL, null=True, related_name="process_data_field")
    name = models.CharField(max_length=25)
    FIELD_TYPE = [
        ('B', 'BOOL'),
        ('I', 'INT'),
        ('R', 'REAL'),
        ('S', 'STRING'),
        ('DT', 'DATE-TIME'),
        ('D', 'DATE'),
        ('T', 'TIME'),
    ]
    type = models.CharField(max_length=2, choices=FIELD_TYPE, default='R')

    def __str__(self):
        return str(self.station) + str('- (') + str(self.name) + str(')')


class ProcessDataValue(models.Model):
    """
    Opis wartości procesowej wybranego pola -> ProcesDataField
    """
    process = models.ForeignKey(Process, on_delete=models.CASCADE, related_name="process_data_value", null=True)
    field = models.ForeignKey(ProcessDataField, on_delete=models.CASCADE, )#related_name="process_data_value")
    value = models.CharField(max_length=50)

    def __str__(self):
        return str(self.field)


class Image(models.Model):
    """
    Opis zdjęć z kamer
    """
    image = models.ImageField(upload_to='image/product/', null=True, blank=True, )
    inspection = models.ImageField(upload_to='image/product/', null=True, blank=True, )
    camera = models.ForeignKey(Camera, on_delete=models.SET_NULL, null=True, related_name="image")
    process = models.ForeignKey(Process, on_delete=models.SET_NULL, null=True, related_name="image")
    status = models.BooleanField(default=False)
    save_time = models.DateTimeField(default=datetime.datetime.now())

    def __str__(self):
        return str(self.camera)
