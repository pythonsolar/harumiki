from django.shortcuts import render
from .models import *
import json

# Create your views here.
def Home(request):
    # รับค่าจากการ query วันที่ ถ้าไม่ได้ระบุวันที่จะดึงข้อมูลทั้งหมด
    query_date = request.GET.get('date', None)
    
    if query_date:
        measurements = Measurement.objects.filter(date=query_date)
    else:
        measurements = Measurement.objects.all()  # ดึงข้อมูลทั้งหมด
    
    # จัดเตรียมข้อมูลสำหรับแสดงในกราฟ
    dates = [measurement.date.strftime('%Y-%m-%d') for measurement in measurements]
    ph_values = [measurement.water_ph for measurement in measurements]
    ec_values = [measurement.water_ec for measurement in measurements]
    ml_values = [measurement.z1_ml for measurement in measurements]
    rh_values = [measurement.z1_rh for measurement in measurements]

    context = {
        'measurements': measurements,  # ส่งข้อมูลทั้งหมดไปเพื่อแสดงตาราง
        'dates': json.dumps(dates),  # แปลงเป็น JSON format
        'ph_values': json.dumps(ph_values),  # แปลงเป็น JSON format
        'ec_values': json.dumps(ec_values),  # แปลงเป็น JSON format
        'ml_values': json.dumps(ml_values),  # แปลงเป็น JSON format
        'rh_values': json.dumps(rh_values),  # แปลงเป็น JSON format
    }

    return render(request, 'strawberry/home.html', context)