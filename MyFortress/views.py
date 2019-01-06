from django.shortcuts import render, HttpResponse, redirect
import json
from MyFortress import models
from MyFortress import pagination
from MyFortress import add_hosts_modelform
from MyFortress import change_hosts_modelform
from django.views.decorators.csrf import csrf_exempt
# Create your views here.

def index(request):
    role_list = models.Roles.objects.all()
    isp_list = models.ISP.objects.all()
    group_list = models.dev_group.objects.all()
    curent_page = 1
    field_list = ['hostname', 'ipaddr', 'role', 'isp', 'status', 'group']
    search_condition = {}
    if request.GET.get('page', None):
        curent_page = request.GET.get('page')

    for field in field_list:
        if request.GET.get(field, None):
            search_condition[field] = request.GET.get(field)

    host_list = models.HostList.objects.filter(**search_condition)
    curent_content, code_str = pagination.pagination(curent_page, host_list, page_num=7, page_content=20, **search_condition)
    return render(request, 'index.html',
                  {'host_list': curent_content, 'code_str': code_str, 'role_list': role_list, 'isp_list': isp_list,
                   'group_list': group_list})

@csrf_exempt
def add_host(request):
    if request.method == 'POST':
        add_host_form = add_hosts_modelform.add_form(request.POST)
        if add_host_form.is_valid():
            add_host_form.save()
            ret = {'status': True}
            return HttpResponse(json.dumps(ret))
        else:
            ret = add_host_form.errors.as_json()
            return HttpResponse(ret)

from django.core import serializers
@csrf_exempt
def get_host(request):
    hid = request.POST.get('host_id')
    host_info = models.HostList.objects.filter(id=hid)
    json_data = serializers.serialize("json", host_info)

    return HttpResponse(json_data)

@csrf_exempt
def change_host(request):
    if request.method == 'POST':
        host_obj = models.HostList.objects.filter(id=request.POST.get('id')).first()
        change_host_form = change_hosts_modelform.change_form(request.POST, instance=host_obj)
        if change_host_form.is_valid():
            change_host_form.save()
            ret = {'status': True}
            return HttpResponse(json.dumps(ret))
        else:
            ret = change_host_form.errors.as_json()
            return HttpResponse(ret)