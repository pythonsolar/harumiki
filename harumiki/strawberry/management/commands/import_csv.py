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

        # อ่านข้อมูลจากไฟล์ CSV และแทนที่ค่าที่เป็น None หรือ NaN ด้วย 0
        data = pd.read_csv(csv_file_path)
        data = data.fillna(0)

        # บันทึกข้อมูลลงในฐานข้อมูล
        for index, row in data.iterrows():
            Measurement.objects.create(
                date=row.get('Date', None),  # ในกรณีวันที่อาจต้องการให้ None
                water_ph=row.get('Water_pH', 0),
                water_ec=row.get('Water_EC', 0),

                z1_ph1=row.get('Z1_pH1', 0),
                z1_ph2=row.get('Z1_pH2', 0),
                z1_ec1=row.get('Z1_EC1', 0),
                z1_ec2=row.get('Z1_EC2', 0),
                z1_ml=row.get('Z1_ml', 0),
                z1_rh=row.get('Z1_%RH', 0),

                z2_ph1=row.get('Z2_pH1', 0),
                z2_ph2=row.get('Z2_pH2', 0),
                z2_ec1=row.get('Z2_EC1', 0),
                z2_ec2=row.get('Z2_EC2', 0),
                z2_ml=row.get('Z2_ml', 0),
                z2_rh=row.get('Z2_%RH', 0),

                z3_ph1=row.get('Z3_pH1', 0),
                z3_ph2=row.get('Z3_pH2', 0),
                z3_ec1=row.get('Z3_EC1', 0),
                z3_ec2=row.get('Z3_EC2', 0),
                z3_ml=row.get('Z3_ml', 0),
                z3_rh=row.get('Z3_%RH', 0),

                z4_ph1=row.get('Z4_pH1', 0),
                z4_ph2=row.get('Z4_pH2', 0),
                z4_ec1=row.get('Z4_EC1', 0),
                z4_ec2=row.get('Z4_EC2', 0),
                z4_ml=row.get('Z4_ml', 0),
                z4_rh=row.get('Z4_%RH', 0),
            )
            print(f"Added record for {row['Date']}")
