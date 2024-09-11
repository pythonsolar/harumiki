# from django.core.management.base import BaseCommand
# import pandas as pd
# import os

# class Command(BaseCommand):
#     help = 'Convert epoch time to human-readable datetime'

#     def handle(self, *args, **kwargs):
#         # ระบุเส้นทางเต็มสำหรับไฟล์ output
#         base_dir = os.path.dirname(os.path.abspath(__file__))  # เอา path ของไฟล์ปัจจุบัน
#         input_file = os.path.join(base_dir, 'sensor_data.csv')
#         output_file = os.path.join(base_dir, 'sensor_data_with_datetime.csv')

#         # อ่านข้อมูลจากไฟล์ CSV
#         df = pd.read_csv(input_file)

#         # แปลงค่า epoch ให้เป็น datetime
#         df['datetime'] = pd.to_datetime(df['epoch'], unit='ms')

#         # แสดงข้อมูลหลังจากแปลงแล้ว
#         self.stdout.write(self.style.SUCCESS(df.head().to_string()))  # แสดงผลข้อมูลในเทอร์มินัล

#         # บันทึกข้อมูลที่แปลงแล้วลงในไฟล์ CSV ใหม่
#         df.to_csv(output_file, index=False)

#         # แสดงข้อความยืนยันการบันทึกข้อมูล
#         self.stdout.write(self.style.SUCCESS(f'Data has been saved to {output_file}'))
from django.core.management.base import BaseCommand
import pandas as pd
import os

class Command(BaseCommand):
    help = 'Convert epoch time to human-readable datetime and separate date and time columns'

    def handle(self, *args, **kwargs):
        # ระบุเส้นทางเต็มสำหรับไฟล์ output
        base_dir = os.path.dirname(os.path.abspath(__file__))  # เอา path ของไฟล์ปัจจุบัน
        input_file = os.path.join(base_dir, 'sensor_data.csv')
        output_file = os.path.join(base_dir, 'sensor_data_with_date_time.csv')

        # อ่านข้อมูลจากไฟล์ CSV
        df = pd.read_csv(input_file)

        # แปลงค่า epoch ให้เป็น datetime
        df['datetime'] = pd.to_datetime(df['epoch'], unit='ms')

        # แยก datetime ออกเป็น date และ time
        df['date'] = df['datetime'].dt.date  # สร้างคอลัมน์สำหรับ date
        df['time'] = df['datetime'].dt.time  # สร้างคอลัมน์สำหรับ time

        # ลบคอลัมน์ datetime เดิมถ้าไม่ต้องการเก็บ
        # df.drop('datetime', axis=1, inplace=True)  # Uncomment ถ้าคุณไม่ต้องการคอลัมน์ 'datetime'

        # แสดงข้อมูลหลังจากแปลงแล้ว
        self.stdout.write(self.style.SUCCESS(df.head().to_string()))  # แสดงผลข้อมูลในเทอร์มินัล

        # บันทึกข้อมูลที่แปลงแล้วลงในไฟล์ CSV ใหม่
        df.to_csv(output_file, index=False)

        # แสดงข้อความยืนยันการบันทึกข้อมูล
        self.stdout.write(self.style.SUCCESS(f'Data has been saved to {output_file}'))

