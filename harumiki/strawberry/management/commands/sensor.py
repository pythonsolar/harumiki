import os
from django.core.management.base import BaseCommand
import pandas as pd

class Command(BaseCommand):
    help = 'Organize and save sensor data from CSV'

    def handle(self, *args, **kwargs):
        base_dir = os.path.dirname(os.path.abspath(__file__))  # เอา path ของไฟล์ปัจจุบัน
        input_file = os.path.join(base_dir, 'sensor_data_with_date_time.csv')
        output_file = os.path.join(base_dir, 'sensor_data_cleaned.csv')

        # อ่านข้อมูลจากไฟล์ CSV
        try:
            df = pd.read_csv(input_file)
        except FileNotFoundError:
            self.stdout.write(self.style.ERROR(f"File '{input_file}' not found."))
            return

        # ตรวจสอบโครงสร้างข้อมูลเบื้องต้น
        self.stdout.write(self.style.SUCCESS("Reading data from CSV..."))
        self.stdout.write(self.style.SUCCESS(df.head().to_string()))  # แสดงข้อมูลตัวอย่างใน console

        # จัดกลุ่มข้อมูลตาม sensor โดยจัดเรียงตามวันที่และเวลา
        df_pivot = df.pivot_table(index=['date', 'time'], columns='sensor', values='value', aggfunc='first')

        # ลบ MultiIndex เพื่อทำให้เป็นรูปแบบปกติ
        df_pivot.reset_index(inplace=True)

        # บันทึกข้อมูลที่จัดเรียงแล้วเป็นไฟล์ CSV ใหม่
        df_pivot.to_csv(output_file, index=False)

        self.stdout.write(self.style.SUCCESS(f"Data has been organized and saved to '{output_file}'"))
