from django.shortcuts import render
from .models import *
import json

# Create your views here.
def Home(request):
    query_date = request.GET.get('date', None)

    if query_date:
        measurements = Measurement.objects.filter(date=query_date)
    else:
        measurements = Measurement.objects.all()

    # จัดเตรียมข้อมูลสำหรับกราฟ
    dates = [measurement.date.strftime('%Y-%m-%d') for measurement in measurements]
    water_ph_values = [measurement.water_ph for measurement in measurements]
    water_ec_values = [measurement.water_ec for measurement in measurements]
    
    z1_ph1_values = [measurement.z1_ph1 for measurement in measurements]
    z1_ph2_values = [measurement.z1_ph2 for measurement in measurements]
    z1_ec1_values = [measurement.z1_ec1 for measurement in measurements]
    z1_ec2_values = [measurement.z1_ec2 for measurement in measurements]
    z1_ml_values = [measurement.z1_ml for measurement in measurements]
    z1_rh_values = [measurement.z1_rh for measurement in measurements]

    context = {
        'measurements': measurements,  # ส่งข้อมูลไปแสดงในตาราง
        'dates': json.dumps(dates),  # แปลงเป็น JSON เพื่อส่งไปยังกราฟ
        'water_ph_values': json.dumps(water_ph_values),
        'water_ec_values': json.dumps(water_ec_values),
        'z1_ph1_values': json.dumps(z1_ph1_values),
        'z1_ph2_values': json.dumps(z1_ph2_values),
        'z1_ec1_values': json.dumps(z1_ec1_values),
        'z1_ec2_values': json.dumps(z1_ec2_values),
        'z1_ml_values': json.dumps(z1_ml_values),
        'z1_rh_values': json.dumps(z1_rh_values),
    }

    return render(request, 'strawberry/home.html', context)

def get_zone_data(measurements, prefix):
    """ฟังก์ชันดึงข้อมูลจาก Measurement ตามโซน"""
    return {
        f'{prefix}_ph1_values': json.dumps([getattr(m, f'{prefix}_ph1', 0) for m in measurements]),
        f'{prefix}_ph2_values': json.dumps([getattr(m, f'{prefix}_ph2', 0) for m in measurements]),
        f'{prefix}_ec1_values': json.dumps([getattr(m, f'{prefix}_ec1', 0) for m in measurements]),
        f'{prefix}_ec2_values': json.dumps([getattr(m, f'{prefix}_ec2', 0) for m in measurements]),
        f'{prefix}_ml_values': json.dumps([getattr(m, f'{prefix}_ml', 0) for m in measurements]),
        f'{prefix}_rh_values': json.dumps([getattr(m, f'{prefix}_rh', 0) for m in measurements]),
    }

def Dashboard(request):
    measurements = Measurement.objects.all()

    # จัดเตรียมข้อมูลสำหรับกราฟ
    dates = [m.date.strftime('%Y-%m-%d') for m in measurements]
    water_ph_values = [m.water_ph for m in measurements]
    water_ec_values = [m.water_ec for m in measurements]

    context = {
        'measurements': measurements,
        'dates': json.dumps(dates),
        'water_ph_values': json.dumps(water_ph_values),
        'water_ec_values': json.dumps(water_ec_values),
    }

    # ดึงข้อมูลโซน Z1 ถึง Z4
    for zone in range(1, 5):
        zone_data = get_zone_data(measurements, f'z{zone}')
        context.update(zone_data)

    return render(request, 'strawberry/dashboard.html', context)