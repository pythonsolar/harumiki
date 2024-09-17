from django.shortcuts import render
from .models import *
import json
from django.utils.dateparse import parse_date
from django.db.models import Q
import requests

# Create your views here.
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
    # รับค่า start-date และ end-date จาก URL parameters
    start_date = request.GET.get('start-date')
    end_date = request.GET.get('end-date')

    # ถ้ามีการกรองวันที่ ให้ทำการกรองข้อมูล
    if start_date and end_date:
        start_date = parse_date(start_date)
        end_date = parse_date(end_date)
        measurements = Measurement.objects.filter(date__range=[start_date, end_date])
    else:
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

def GHpage(request):
    measurements = MeasurementTwo.objects.all()

    # จัดเตรียมข้อมูลสำหรับกราฟ
    dates = [m.date.strftime('%Y-%m-%d') for m in measurements]
    
    # GH1 ข้อมูล pH
    gh1_ph_be_values = [m.gh1_ph_be for m in measurements]
    gh1_ph_mid_values = [m.gh1_ph_mid for m in measurements]
    gh1_ph_end_values = [m.gh1_ph_end for m in measurements]

    # GH1 ข้อมูล EC
    gh1_ec_be_values = [m.gh1_ec_be for m in measurements]
    gh1_ec_mid_values = [m.gh1_ec_mid for m in measurements]
    gh1_ec_end_values = [m.gh1_ec_end for m in measurements]

    # GH1 ข้อมูล ml
    gh1_ml_be_values = [m.gh1_ml_be for m in measurements]
    gh1_ml_mid_values = [m.gh1_ml_mid for m in measurements]
    gh1_ml_end_values = [m.gh1_ml_end for m in measurements]

    # GH2 ข้อมูล pH
    gh2_ph_be_values = [m.gh2_ph_be for m in measurements]
    gh2_ph_mid_values = [m.gh2_ph_mid for m in measurements]
    gh2_ph_end_values = [m.gh2_ph_end for m in measurements]

    # GH2 ข้อมูล EC
    gh2_ec_be_values = [m.gh2_ec_be for m in measurements]
    gh2_ec_mid_values = [m.gh2_ec_mid for m in measurements]
    gh2_ec_end_values = [m.gh2_ec_end for m in measurements]

    # GH1 ข้อมูล ml
    gh2_ml_be_values = [m.gh2_ml_be for m in measurements]
    gh2_ml_mid_values = [m.gh2_ml_mid for m in measurements]
    gh2_ml_end_values = [m.gh2_ml_end for m in measurements]

    context = {
        'dates': json.dumps(dates),
        
        'gh1_ph_be_values': json.dumps(gh1_ph_be_values),
        'gh1_ph_mid_values': json.dumps(gh1_ph_mid_values),
        'gh1_ph_end_values': json.dumps(gh1_ph_end_values),
        'gh1_ec_be_values': json.dumps(gh1_ec_be_values),
        'gh1_ec_mid_values': json.dumps(gh1_ec_mid_values),
        'gh1_ec_end_values': json.dumps(gh1_ec_end_values),
        'gh1_ml_be_values': json.dumps(gh1_ml_be_values),
        'gh1_ml_mid_values': json.dumps(gh1_ml_mid_values),
        'gh1_ml_end_values': json.dumps(gh1_ml_end_values),

        'gh2_ph_be_values': json.dumps(gh2_ph_be_values),
        'gh2_ph_mid_values': json.dumps(gh2_ph_mid_values),
        'gh2_ph_end_values': json.dumps(gh2_ph_end_values),
        'gh2_ec_be_values': json.dumps(gh2_ec_be_values),
        'gh2_ec_mid_values': json.dumps(gh2_ec_mid_values),
        'gh2_ec_end_values': json.dumps(gh2_ec_end_values),
        'gh2_ml_be_values': json.dumps(gh2_ml_be_values),
        'gh2_ml_mid_values': json.dumps(gh2_ml_mid_values),
        'gh2_ml_end_values': json.dumps(gh2_ml_end_values),
    }

    return render(request, 'strawberry/ghpage.html', context)

def get_latest_nonzero_value(field_name):
    """ดึงค่าสุดท้ายที่ไม่ใช่ None หรือ 0 ของฟิลด์ที่กำหนด"""
    measurement = Measurement.objects.exclude(**{field_name: 0}).exclude(**{field_name: None}).order_by('-date').first()
    if measurement:
        return getattr(measurement, field_name, 0)
    return 0

def DesignUI(request):

    # รับค่า start-date และ end-date จาก URL parameters
    start_date = request.GET.get('start-date')
    end_date = request.GET.get('end-date')

    # ถ้ามีการกรองวันที่ ให้ทำการกรองข้อมูล
    if start_date and end_date:
        start_date = parse_date(start_date)
        end_date = parse_date(end_date)
        measurements = Measurement.objects.filter(date__range=[start_date, end_date])
    else:
        measurements = Measurement.objects.all()
    
    # ดึงข้อมูลล่าสุดที่ไม่ใช่ None หรือ 0
    latest_measurement = Measurement.objects.filter(
        ~Q(water_ph=0), 
        ~Q(water_ph=None), 
        ~Q(water_ec=0), 
        ~Q(water_ec=None)
        ).order_by('-date').first()

    if latest_measurement:
        water_ph = latest_measurement.water_ph
        water_ec = latest_measurement.water_ec
    else:
        water_ph = 0
        water_ec = 0

    dates = [m.date.strftime('%Y-%m-%d') for m in measurements]
    water_ph_values = [measurement.water_ph for measurement in measurements]
    water_ec_values = [measurement.water_ec for measurement in measurements]

    context = {
        'water_ph': water_ph,
        'water_ec': water_ec,
        'dates': json.dumps(dates),
        'water_ph_values': json.dumps(water_ph_values),
        'water_ec_values': json.dumps(water_ec_values),
    }

    return render(request, 'strawberry/designui.html', context)

def get_latest_nonzero_value(field_name):
    """ดึงค่าสุดท้ายที่ไม่ใช่ None หรือ 0 ของฟิลด์ที่กำหนด"""
    measurementtwo = MeasurementTwo.objects.exclude(**{field_name: 0}).exclude(**{field_name: None}).order_by('-date').first()
    if measurementtwo:
        return getattr(measurementtwo, field_name, 0)
    return 0

def Home(request):

    measurementtwos = MeasurementTwo.objects.all()

    latest_measurementtwo = MeasurementTwo.objects.filter(
        ~Q(gh1_ec_be=0), ~Q(gh1_ec_be=None), 
        ~Q(gh1_ec_mid=0), ~Q(gh1_ec_mid=None),
        ~Q(gh1_ec_end=0), ~Q(gh1_ec_end=None),
        ~Q(gh1_ph_be=0), ~Q(gh1_ph_be=None),
        ~Q(gh1_ph_mid=0), ~Q(gh1_ph_mid=None),
        ~Q(gh1_ph_end=0), ~Q(gh1_ph_end=None),
        ~Q(gh1_ml_be=0), ~Q(gh1_ml_be=None),
        ~Q(gh1_ml_mid=0), ~Q(gh1_ml_mid=None),
        ~Q(gh1_ml_end=0), ~Q(gh1_ml_end=None)
        ).order_by('-date').first()
    
    if latest_measurementtwo:
        gh1_ec_be = latest_measurementtwo.gh1_ec_be
        gh1_ec_mid = latest_measurementtwo.gh1_ec_mid
        gh1_ec_end = latest_measurementtwo.gh1_ec_end
        gh1_ph_be = latest_measurementtwo.gh1_ph_be
        gh1_ph_mid = latest_measurementtwo.gh1_ph_mid
        gh1_ph_end = latest_measurementtwo.gh1_ph_end
        gh1_ml_be = latest_measurementtwo.gh1_ml_be
        gh1_ml_mid = latest_measurementtwo.gh1_ml_mid
        gh1_ml_end = latest_measurementtwo.gh1_ml_end
    else:
        gh1_ec_be = 0
        gh1_ec_mid = 0
        gh1_ec_end = 0
        gh1_ph_be = 0
        gh1_ph_mid = 0
        gh1_ph_end = 0
        gh1_ml_be = 0
        gh1_ml_mid = 0
        gh1_ml_end = 0

    context = {
        'gh1_ec_be': gh1_ec_be,
        'gh1_ec_mid': gh1_ec_mid,
        'gh1_ec_end': gh1_ec_end,
        'gh1_ph_be': gh1_ph_be,
        'gh1_ph_mid': gh1_ph_mid,
        'gh1_ph_end': gh1_ph_end,
        'gh1_ml_be': gh1_ml_be,
        'gh1_ml_mid': gh1_ml_mid,
        'gh1_ml_end': gh1_ml_end,
    }

    return render(request, 'strawberry/home.html', context)

def APIPage(request):
    # URL ของ API ทั้ง 3
    url1 = "https://magellan.ais.co.th/asgardpullmessagesapis/api/listen/thing?Key=43C5EEC426F28564A0DBFEB84588180E"
    url2 = "https://magellan.ais.co.th/asgardpullmessagesapis/api/listen/thing?Key=68F1140AF50FD5AD4ED1E3FBF2199452"
    url3 = "https://magellan.ais.co.th/asgardpullmessagesapis/api/listen/thing?Key=14C0883E815D76F64AA08344A7EEE824"
    url4 = "https://magellan.ais.co.th/asgardpullmessagesapis/api/listen/thing?Key=43C5EEC426F28564A0DBFEB84588180E"
    url5 = "https://magellan.ais.co.th/asgardpullmessagesapis/api/listen/thing?Key=68F1140AF50FD5AD4ED1E3FBF2199452"
    url6 = "https://magellan.ais.co.th/asgardpullmessagesapis/api/listen/thing?Key=14C0883E815D76F64AA08344A7EEE824"

    # Factor สำหรับการปรับค่า PM2.5
    factor1 = 1.0  # Factor สำหรับ API ที่ 1
    factor2 = 1.0  # Factor สำหรับ API ที่ 2
    factor3 = 50 # Factor สำหรับ API ที่ 3
    factor4 = 60
    factor5 = 101325.0
    factor6 = 700

    # ดึงข้อมูลจาก API ที่ 1
    response1 = requests.get(url1)
    if response1.status_code == 200:
        data1 = response1.json()
        pm25_1 = data1.get('Sensor', {}).get('pm25_ma', 0)  # ดึงค่า pm25_ma จาก API 1
        pm25_1 = pm25_1 * factor1  # ปรับค่าด้วย factor
    else:
        pm25_1 = 0

    # ดึงข้อมูลจาก API ที่ 2
    response2 = requests.get(url2)
    if response2.status_code == 200:
        data2 = response2.json()
        pm25_2 = data2.get('Sensor', {}).get('pm25_ma', 0)  # ดึงค่า pm25_ma จาก API 2
        pm25_2 = pm25_2 * factor2  # ปรับค่าด้วย factor
    else:
        pm25_2 = 0

    # ดึงข้อมูลจาก API ที่ 3
    response3 = requests.get(url3)
    if response3.status_code == 200:
        data3 = response3.json()
        pm25_3 = data3.get('Sensor', {}).get('pm25_ma', 0)  # ดึงค่า pm25_ma จาก API 3
        pm25_3 = pm25_3 + factor3  # ปรับค่าด้วย factor
    else:
        pm25_3 = 0

    # ดึงข้อมูลจาก API ที่ 4
    response4 = requests.get(url4)
    if response4.status_code == 200:
        data4 = response4.json()
        pm25_4 = data3.get('Sensor', {}).get('pm25_ma', 0)  # ดึงค่า pm25_ma จาก API 4
        pm25_4 = pm25_4 + factor4  # ปรับค่าด้วย factor
    else:
        pm25_4 = 0

    # ดึงข้อมูลจาก API ที่ 5
    response5 = requests.get(url5)
    if response5.status_code == 200:
        data5 = response5.json()
        pm25_5 = data5.get('Sensor', {}).get('pm25_ma', 0)  # ดึงค่า pm25_ma จาก API 5
        pm25_5 = pm25_5 + factor5  # ปรับค่าด้วย factor
    else:
        pm25_5 = 0

    # ดึงข้อมูลจาก API ที่ 3
    response6 = requests.get(url6)
    if response6.status_code == 200:
        data6 = response6.json()
        pm25_6 = data3.get('Sensor', {}).get('pm25_ma', 0)  # ดึงค่า pm25_ma จาก API 6
        pm25_6 = pm25_6 + factor6  # ปรับค่าด้วย factor
    else:
        pm25_6 = 0

    # ส่งค่าผ่าน context ไปยัง HTML template
    context = {
        'pm25_1': pm25_1,
        'pm25_2': pm25_2,
        'pm25_3': pm25_3,
        'pm25_4': pm25_4,
        'pm25_5': pm25_5,
        'pm25_6': pm25_6,
    }

    return render(request, 'strawberry/apipage.html', context)