from django.db import models

# Create your models here.
class Measurement(models.Model):
    date = models.DateField(null=True, blank=True)

    water_ph = models.FloatField(null=True, blank=True, default=0.0)
    water_ec = models.FloatField(null=True, blank=True, default=0.0)

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

class MeasurementTwo(models.Model):
    date = models.DateField(null=True, blank=True)

    # GH1 ข้อมูล EC
    gh1_ec_be = models.FloatField(null=True, blank=True, default=0.0)
    gh1_ec_mid = models.FloatField(null=True, blank=True, default=0.0)
    gh1_ec_end = models.FloatField(null=True, blank=True, default=0.0)

    # GH1 ข้อมูล pH
    gh1_ph_be = models.FloatField(null=True, blank=True, default=0.0)
    gh1_ph_mid = models.FloatField(null=True, blank=True, default=0.0)
    gh1_ph_end = models.FloatField(null=True, blank=True, default=0.0)

    # GH1 ข้อมูล ml
    gh1_ml_be = models.FloatField(null=True, blank=True, default=0.0)
    gh1_ml_mid = models.FloatField(null=True, blank=True, default=0.0)
    gh1_ml_end = models.FloatField(null=True, blank=True, default=0.0)

    # GH2 ข้อมูล EC
    gh2_ec_be = models.FloatField(null=True, blank=True, default=0.0)
    gh2_ec_mid = models.FloatField(null=True, blank=True, default=0.0)
    gh2_ec_end = models.FloatField(null=True, blank=True, default=0.0)

    # GH2 ข้อมูล pH
    gh2_ph_be = models.FloatField(null=True, blank=True, default=0.0)
    gh2_ph_mid = models.FloatField(null=True, blank=True, default=0.0)
    gh2_ph_end = models.FloatField(null=True, blank=True, default=0.0)

    # GH2 ข้อมูล ml
    gh2_ml_be = models.FloatField(null=True, blank=True, default=0.0)
    gh2_ml_mid = models.FloatField(null=True, blank=True, default=0.0)
    gh2_ml_end = models.FloatField(null=True, blank=True, default=0.0)

    def __str__(self):
        return f"MeasurementTwo on {self.date}"
