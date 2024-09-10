from django.core.management.base import BaseCommand
import os
import pandas as pd
from django.conf import settings
from strawberry.models import MeasurementTwo

class Command(BaseCommand):
    help = 'Import data from CSV file into the MeasurementTwo model'

    def handle(self, *args, **kwargs):
        # กำหนด path ไปยังไฟล์ CSV
        csv_file_path = os.path.join(settings.BASE_DIR, 'databasetwo.csv')

        # อ่านข้อมูลจากไฟล์ CSV และแทนที่ค่าที่เป็น None หรือ NaN ด้วย 0
        data = pd.read_csv(csv_file_path)
        # data = data.fillna(0)

        # บันทึกข้อมูลลงในฐานข้อมูล
        for index, row in data.iterrows():
            MeasurementTwo.objects.create(
                date=row.get('Date', None),

                gh1_ec_be=row.get('GH1-EC-BE', 0),
                gh1_ec_mid=row.get('GH1-EC-MID', 0),
                gh1_ec_end=row.get('GH1-EC-END', 0),

                gh1_ph_be=row.get('GH1-pH-BE', 0),
                gh1_ph_mid=row.get('GH1-pH-MID', 0),
                gh1_ph_end=row.get('GH1-pH-END', 0),

                gh1_ml_be=row.get('GH1-ml-BE', 0),
                gh1_ml_mid=row.get('GH1-ml-MID', 0),
                gh1_ml_end=row.get('GH1-ml-END', 0),

                gh2_ec_be=row.get('GH2-EC-BE', 0),
                gh2_ec_mid=row.get('GH2-EC-MID', 0),
                gh2_ec_end=row.get('GH2-EC-END', 0),

                gh2_ph_be=row.get('GH2-pH-BE', 0),
                gh2_ph_mid=row.get('GH2-pH-MID', 0),
                gh2_ph_end=row.get('GH2-pH-END', 0),

                gh2_ml_be=row.get('GH2-ml-BE', 0),
                gh2_ml_mid=row.get('GH2-ml-MID', 0),
                gh2_ml_end=row.get('GH2-ml-END', 0),
            )
            print(f"Added record for {row['Date']}")
