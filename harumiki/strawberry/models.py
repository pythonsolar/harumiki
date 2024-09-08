from django.db import models

# Create your models here.
class Measurement(models.Model):
    date = models.DateField(null=True, blank=True)  # วันที่

    # ข้อมูลของน้ำ
    water_ph = models.FloatField(null=True, blank=True, default=0.0)  # ค่าความเป็นกรด-ด่างของน้ำ
    water_ec = models.FloatField(null=True, blank=True, default=0.0)  # ค่าการนำไฟฟ้าของน้ำ (EC)

    # ข้อมูลโซน 1
    z1_ph1 = models.FloatField(null=True, blank=True, default=0.0)
    z1_ph2 = models.FloatField(null=True, blank=True, default=0.0)
    z1_ec1 = models.FloatField(null=True, blank=True, default=0.0)
    z1_ec2 = models.FloatField(null=True, blank=True, default=0.0)
    z1_ml = models.FloatField(null=True, blank=True, default=0.0)
    z1_rh = models.FloatField(null=True, blank=True, default=0.0)

    # ข้อมูลโซน 2
    z2_ph1 = models.FloatField(null=True, blank=True, default=0.0)
    z2_ph2 = models.FloatField(null=True, blank=True, default=0.0)
    z2_ec1 = models.FloatField(null=True, blank=True, default=0.0)
    z2_ec2 = models.FloatField(null=True, blank=True, default=0.0)
    z2_ml = models.FloatField(null=True, blank=True, default=0.0)
    z2_rh = models.FloatField(null=True, blank=True, default=0.0)

    # ข้อมูลโซน 3
    z3_ph1 = models.FloatField(null=True, blank=True, default=0.0)
    z3_ph2 = models.FloatField(null=True, blank=True, default=0.0)
    z3_ec1 = models.FloatField(null=True, blank=True, default=0.0)
    z3_ec2 = models.FloatField(null=True, blank=True, default=0.0)
    z3_ml = models.FloatField(null=True, blank=True, default=0.0)
    z3_rh = models.FloatField(null=True, blank=True, default=0.0)

    # ข้อมูลโซน 4
    z4_ph1 = models.FloatField(null=True, blank=True, default=0.0)
    z4_ph2 = models.FloatField(null=True, blank=True, default=0.0)
    z4_ec1 = models.FloatField(null=True, blank=True, default=0.0)
    z4_ec2 = models.FloatField(null=True, blank=True, default=0.0)
    z4_ml = models.FloatField(null=True, blank=True, default=0.0)
    z4_rh = models.FloatField(null=True, blank=True, default=0.0)

    def __str__(self):
        return f"Measurement on {self.date}"
