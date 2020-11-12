from django.db import models

# Create your models here.
class MedicineData(models.Model):
    username = models.CharField(max_length=50)
    medicine_name = models.CharField(max_length=100)
    batch_id = models.CharField(max_length=50)
    mfd = models.DateField()
    number_of_boxes = models.IntegerField()
    exd = models.DateField()
    invoice_no = models.CharField(max_length=50)
    no_of_pieces = models.IntegerField()
    date_of_purchase = models.DateField()
    date_of_added = models.DateTimeField()
    no_of_days_left = models.CharField(max_length=6, default="0")

    def __str__(self):
        return str(self.medicine_name)

