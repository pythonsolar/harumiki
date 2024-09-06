from django.core.management.base import BaseCommand
import os
import pandas as pd
from django.conf import settings
from strawberry.models import Measurement

class Command(BaseCommand):
    help = 'Import data from CSV file into the Measurement model'

    def handle(self, *args, **kwargs):
        # กำหนด path ไปยังไฟล์ CSV
        csv_file_path = os.path.join(settings.BASE_DIR, 'database.csv')

        # อ่านข้อมูลจากไฟล์ CSV
        data = pd.read_csv(csv_file_path)

        # บันทึกข้อมูลลงในฐานข้อมูล
        for index, row in data.iterrows():
            Measurement.objects.create(
                date=row['Date'],
                water_ph=row['Water_pH'],
                water_ec=row['Water_EC'],

                z1_ph1=row['Z1_pH1'],
                z1_ph2=row['Z1_pH2'],
                z1_ec1=row['Z1_EC1'],
                z1_ec2=row['Z1_EC2'],
                z1_ml=row['Z1_ml'],
                z1_rh=row['Z1_%RH'],

                z2_ph1=row['Z2_pH1'],
                z2_ph2=row['Z2_pH2'],
                z2_ec1=row['Z2_EC1'],
                z2_ec2=row['Z2_EC2'],
                z2_ml=row['Z2_ml'],
                z2_rh=row['Z2_%RH'],

                z3_ph1=row['Z3_pH1'],
                z3_ph2=row['Z3_pH2'],
                z3_ec1=row['Z3_EC1'],
                z3_ec2=row['Z3_EC2'],
                z3_ml=row['Z3_ml'],
                z3_rh=row['Z3_%RH'],

                z4_ph1=row['Z4_pH1'],
                z4_ph2=row['Z4_pH2'],
                z4_ec1=row['Z4_EC1'],
                z4_ec2=row['Z4_EC2'],
                z4_ml=row['Z4_ml'],
                z4_rh=row['Z4_%RH'],
            )
            print(f"Added record for {row['Date']}")
