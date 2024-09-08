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

def Dashboard(request):
    return render(request, 'strawberry/dashboard.html')