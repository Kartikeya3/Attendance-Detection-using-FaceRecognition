from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import user,userface,studentface,attendence
import requests
import csv
import datetime
from PIL import Image
from io import BytesIO
from azure.storage.blob import  BlobServiceClient
import json
import base64
from django.core.files.base import ContentFile
from .models import *
from .forms import *

# Create your views here.
def logout(request):
    if 'email' in request.session and 'faceconfirm' in request.session:
        del request.session['email']
    del request.session['faceconfirm']
    return redirect('login')
def Login(request):
    if 'email' in request.session and 'faceconfirm' in request.session:
        if request.session['faceconfirm']:
            return redirect('dashboard')
    if request.method=='POST':
        if request.POST.get('email') and request.POST.get('password'):
            try:
                User=user.objects.get(email=request.POST.get('email'))
            except:
                User=None
                User=user.objects.filter(email=request.POST.get('email'))
            if User:
                if User.password==request.POST.get('password'):
                    request.session['email']=User.email
                    request.session['faceconfirm']=False
                    return redirect('verifyface')
    return render(request,'login.html')

def SignUP(request):
    if request.method=='POST':
        if request.POST.get('email') and request.POST.get('password') and request.POST.get('confirmpassword'):
            User=user()
            User.email=request.POST.get('email')
            if request.POST.get('password')==request.POST.get('confirmpassword'):
                User.password=request.POST.get('password')
                User.save()
                request.session['email']=User.email
                request.session['faceconfirm']=False
                return redirect('newface')
            else:
                HttpResponse("Confirmpassword is not same as your password.")
        else:
            HttpResponse("Please fill all the details.")
    return render(request,'signup.html')

def newface(request):
    if request.method=="POST":
        img_data=request.POST.get('photodata')
        print(img_data)
        format, imgstr = img_data.split(';base64,')
        ext = format.split('/')[-1]
        data = ContentFile(base64.b64decode(imgstr))
        email=request.session['email']
        email_list=email.split('@')
        file_name=email_list[0]
        connect_str="DefaultEndpointsProtocol=https;AccountName=attendance1;AccountKey=0IulrWo/ZJoSHzIzPozXnghAdOS+O4TApkOfDU60bojmeNHcy553ctS7/LFByYWjZEA4udDeIsbs+ASt3cOQxw==;EndpointSuffix=core.windows.net"

        blob_service_client = BlobServiceClient.from_connection_string(connect_str)
        container_name="attendance1"
        blob_client = blob_service_client.get_blob_client(container=container_name, blob=file_name+'.png')
        blob_client.upload_blob(data)
        print(blob_client.url)
        Userface=userface()
        Userface.email=request.session['email']
        Userface.url=blob_client.url
        Userface.save()
        request.session['faceconfirm']=True
        request.session['loggedinalert']=True
        return redirect("profiles")
    return render(request,"newface.html")

def verifyface(request):
    if request.method=="POST":
        img_data=request.POST.get('photodata')
        format, imgstr = img_data.split(';base64,')
        ext = format.split('/')[-1]
        data = ContentFile(base64.b64decode(imgstr))
        sub_key='d5afc92936094fa58e366633acc54639'
        Userface=userface.objects.get(email=request.session['email'])
        file1=Userface.url
        print(file1)
        response=requests.get(file1)
        img_data1=BytesIO(response.content)
        uri_base="https://facerecognition4.cognitiveservices.azure.com/"
        headers = {
        'Content-Type': 'application/octet-stream',
        'Ocp-Apim-Subscription-Key': sub_key,
        }
        headers2={
            'Content-Type': 'application/json',
            'Ocp-Apim-Subscription-Key': sub_key,
        }
        params = {
            'returnFaceId': 'true',
        }
        img_list=[]
        face_api1='/face/v1.0/detect'
        face_api2='/face/v1.0/verify'
        img_list.append(data)
        img_list.append(img_data1)
        faceid_list=[]
        try:
            for img in img_list:
                response=requests.post(uri_base+face_api1,
                    data=img,
                    headers=headers,
                    params=params
                    )
                parsed=response.json()
                print(parsed)
                json_str=parsed[0]
                faceid_list.append(json_str['faceId'])
        except Exception as e:
            print(e)
        print(faceid_list)
        data={"faceId1":faceid_list[0],"faceId2":faceid_list[1]}
        data_json=json.dumps(data)
        response=requests.post(uri_base + face_api2,data=data_json,headers=headers2)
        parsed=response.json()
        if parsed['isIdentical']:
            request.session['faceconfirm']=True
            request.session['loggedinalert']=True
            return redirect('profiles')
        else:
            del request.session['email']
            return HttpResponse('<h1>Face id doesnt match please try again.</h1>')
    return render(request,"newface.html")

def dashboard(request):
    if 'email' in request.session and 'faceconfirm' in request.session:
        if request.session['faceconfirm']:
            if request.method=="POST":
                studentid=request.POST.get('studentid')
                print(studentid)
                if request.POST.get("action")=="upload":
                    img_data=request.POST.get('photodata')
                    format, imgstr = img_data.split(';base64,')
                    ext = format.split('/')[-1]
                    data = ContentFile(base64.b64decode(imgstr))
                    file_name=studentid
                    connect_str="DefaultEndpointsProtocol=https;AccountName=attendance1;AccountKey=bm1YoAjtiyRMrdUFr/4DZBXOOgjgVAPcLCVQTSLdavYDa0qnOX7haRx9X3oHSyk7DpSASlh3OXXf+AStKjML8A==;EndpointSuffix=core.windows.net"

                    blob_service_client = BlobServiceClient.from_connection_string(connect_str)
                    container_name="attendance1"
                    blob_client = blob_service_client.get_blob_client(container=container_name, blob=file_name+'.png')
                    blob_client.upload_blob(data)
                    print(blob_client.url)
                    Studentface=studentface()
                    Studentface.studentid=studentid
                    Studentface.url=blob_client.url
                    Studentface.save()
                    return redirect('dashboard')
                if request.POST.get("action")=="take":
                    img_data=request.POST.get('photodata')
                    format, imgstr = img_data.split(';base64,')
                    ext = format.split('/')[-1]
                    data = ContentFile(base64.b64decode(imgstr))
                    sub_key='d5afc92936094fa58e366633acc54639'
                    try:
                        Studentface=studentface.objects.get(studentid=studentid)
                    except:
                        return HttpResponse("Student id not found!")
                    file1=Studentface.url
                    print(file1)
                    response=requests.get(file1)
                    img_data1=BytesIO(response.content)
                    uri_base="https://facerecognition4.cognitiveservices.azure.com/"
                    headers = {
                    'Content-Type': 'application/octet-stream',
                    'Ocp-Apim-Subscription-Key': sub_key,
                    }
                    headers2={
                        'Content-Type': 'application/json',
                        'Ocp-Apim-Subscription-Key': sub_key,
                    }
                    params = {
                        'returnFaceId': 'true',
                    }
                    img_list=[]
                    face_api1='/face/v1.0/detect'
                    face_api2='/face/v1.0/verify'
                    img_list.append(data)
                    img_list.append(img_data1)
                    faceid_list=[]
                    try:
                        for img in img_list:
                            response=requests.post(uri_base+face_api1,
                                data=img,
                                headers=headers,
                                params=params
                                )
                            parsed=response.json()
                            print(parsed)
                            json_str=parsed[0]
                            faceid_list.append(json_str['faceId'])
                    except Exception as e:
                        print(e)
                    print(faceid_list)
                    data={"faceId1":faceid_list[0],"faceId2":faceid_list[1]}
                    data_json=json.dumps(data)
                    response=requests.post(uri_base + face_api2,data=data_json,headers=headers2)
                    parsed=response.json()
                    if parsed['isIdentical']:
                        Attendence=attendence()
                        Attendence.studentid=studentid
                        x = datetime.datetime.now()
                        str1 = x.strftime('%m/%d/%y-%H:%M:%S')
                        Attendence.datetime=str1
                        Attendence.status="present"
                        Attendence.save()
                        return redirect("dashboard")
                    else:
                        return HttpResponse("Student Face not identical!")
            return render(request,"dashboard.html")
        else:
            return redirect('verifyface')
    else:
        return redirect('login')

def download_csv(request, queryset):
    opts = queryset.model._meta
    model = queryset.model
    response = HttpResponse(content_type='text/csv')
    # force download.
    response['Content-Disposition'] = 'attachment;filename=export.csv'
    # the csv writer
    writer = csv.writer(response)
    field_names = [field.name for field in opts.fields]
    # Write a first row with header information
    writer.writerow(field_names)
    # Write data rows
    for obj in queryset:
            writer.writerow([getattr(obj, field) for field in field_names])
    return response

def download(request):
    if 'email' in request.session and 'faceconfirm' in request.session:
        if request.session['faceconfirm']:
            data = download_csv(request, attendence.objects.all())
            return HttpResponse (data, content_type='text/csv')
        else:
            return redirect('verifyface')
    else:
        return redirect('login')

def add_profile(request):
    form = ProfileForm
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('profiles')
    context = {'form': form}
    return render(request, 'add_profiles.html', context)

# @login_required(login_url = 'login')
def profiles(request):
    profiles = Profile.objects.all()
    context = {
        'profiles': profiles,

        'loggedinalert': request.session['loggedinalert']
    }
    request.session['loggedinalert']=False
    return render(request, 'profiles.html', context)

# @login_required(login_url = 'login')
def edit_profile(request, id):
    profile = Profile.objects.get(id=id)
    form = ProfileForm(instance=profile)
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profiles')
    context = {'form': form}
    return render(request, 'add_profiles.html', context)


# @login_required(login_url = 'login')
def delete_profile(request, id):
    profile = Profile.objects.get(id=id)
    profile.delete()
    return redirect('profiles')
