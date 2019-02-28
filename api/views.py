from django.shortcuts import render
from .models import DemoEntries, Device, UserPin, UserInfo, CrashLog
from django.http import HttpResponse
from django.views.decorators.http import require_http_methods
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect

from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse

from django.contrib.auth.models import User

import pdb
import json

@csrf_exempt
@require_http_methods(["POST",])
def demo(request):
    entry = DemoEntries()
    entry.text = request.body.decode('utf-8')
    entry.save()

    return HttpResponse(status=204)


@csrf_exempt
@require_http_methods(["POST",])
def get_user_list(request):
    data = json.loads(request.body)
    serial = data.get("serial")
    users = []
    device = Device.objects.filter(serial=serial).first()
    if device:
        for user_pin in device.user_pin_entries.all():
            users.append(user_pin.user.username)

    return JsonResponse({"users": users})

@csrf_exempt
@require_http_methods(["POST",])
def get_emergency_contacts(request):
    #pdb.set_trace()
    data = json.loads(request.body)
    username = data.get("user")
    contacts = ""
    user = User.objects.filter(username=username).first()
    if user:
        for contact in user.userinfo.contacts:
            contacts += contact["name"] + " " + contact["phone_number"] + ","

    if contacts.endswith(","):
        contacts = contacts[:-1]
    
    return HttpResponse(contacts)

@require_http_methods(["POST",])
@login_required
def add_device(request):
    serial = request.POST.get("serial")
    pin = request.POST.get("pin")
    device, created = Device.objects.get_or_create(serial=serial)
    #if new device created, or if a user-device relationship exists doesn't exist, create the new entry
    if created or not UserPin.objects.filter(device=device, user=request.user).exists():
        serial_pin_entry = UserPin(device=device, user=request.user, pin=pin)
        serial_pin_entry.save()
    
    return redirect("/")


@require_http_methods(["POST",])
@login_required
def add_emergency_contact(request):
    name = request.POST.get("name")
    phone_number = request.POST.get("phone_number")
    user_info = UserInfo.objects.filter(user=request.user).first()
    #if new device created, or if a user-device relationship exists doesn't exist, create the new entry
    if user_info:
        #pdb.set_trace()
        user_info.contacts.append({'name': name, 'phone_number': phone_number})
        user_info.save()
    
    return redirect("/")


@csrf_exempt
@require_http_methods(["POST",])
def login_device(request):
    data = json.loads(request.body)
    serial = data.get("serial")
    username = data.get("username")
    pin = data.get("pin")

    device = Device.objects.filter(serial=serial).first()
    user_pin_entry = UserPin.objects.filter(user__username=username, device=device).first()
    if user_pin_entry and user_pin_entry.pin == pin:
        return HttpResponse(status=200)
    else:
        return HttpResponse(status=403)

@csrf_exempt
@require_http_methods(["POST",])
def log_crash(request):
    #pdb.set_trace()
    data = json.loads(request.body)
    username = data.get("username")
    log = data.get("log")
    recorded_crash = data.get("crash_public_id")
    user = User.objects.filter(username=username).first()
    if user:
        new_log = CrashLog.objects.create(user=user, log=log, recorded_crash=recorded_crash)
        return HttpResponse(status=200)
    else:
        return HttpResponse(status=400)