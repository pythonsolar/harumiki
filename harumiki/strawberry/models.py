from django.db import models

# Create your models here.
class Measurement(models.Model):
    date = models.DateField(null=True, blank=True)  # วันที่

    # ข้อมูลของน้ำ
    water_ph = models.FloatField(null=True, blank=True)  # ค่าความเป็นกรด-ด่างของน้ำ
    water_ec = models.FloatField(null=True, blank=True)  # ค่าการนำไฟฟ้าของน้ำ (EC)

    # ข้อมูลโซน 1
    z1_ph1 = models.FloatField(null=True, blank=True)
    z1_ph2 = models.FloatField(null=True, blank=True)
    z1_ec1 = models.FloatField(null=True, blank=True)
    z1_ec2 = models.FloatField(null=True, blank=True)
    z1_ml = models.FloatField(null=True, blank=True)
    z1_rh = models.FloatField(null=True, blank=True)  # %RH ความชื้นสัมพัทธ์ (สามารถเป็นค่าว่างได้)

    # ข้อมูลโซน 2
    z2_ph1 = models.FloatField(null=True, blank=True)
    z2_ph2 = models.FloatField(null=True, blank=True)
    z2_ec1 = models.FloatField(null=True, blank=True)
    z2_ec2 = models.FloatField(null=True, blank=True)
    z2_ml = models.FloatField(null=True, blank=True)
    z2_rh = models.FloatField(null=True, blank=True)

    # ข้อมูลโซน 3
    z3_ph1 = models.FloatField(null=True, blank=True)
    z3_ph2 = models.FloatField(null=True, blank=True)
    z3_ec1 = models.FloatField(null=True, blank=True)
    z3_ec2 = models.FloatField(null=True, blank=True)
    z3_ml = models.FloatField(null=True, blank=True)
    z3_rh = models.FloatField(null=True, blank=True)

    # ข้อมูลโซน 4
    z4_ph1 = models.FloatField(null=True, blank=True)
    z4_ph2 = models.FloatField(null=True, blank=True)
    z4_ec1 = models.FloatField(null=True, blank=True)
    z4_ec2 = models.FloatField(null=True, blank=True)
    z4_ml = models.FloatField(null=True, blank=True)
    z4_rh = models.FloatField(null=True, blank=True)

    def __str__(self):
        return f"Measurement on {self.date}"
