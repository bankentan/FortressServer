from django.forms import widgets as Fwidgets
from django.forms import fields as Ffields
from django.forms import ModelForm
from MyFortress import models
from django.core.exceptions import ValidationError

class change_form(ModelForm):
    class Meta:
        model = models.HostList
        fields = '__all__'
        labels = {
            'hostname': '主机名',
            'ipaddr': 'ip地址',
            'role': '角色',
            'group': '设备组',
            'isp': '运营商',
            'status': '状态',
            'remarks': '备注'
        }


        error_messages = {
            'hostname': {'required': '请输入主机名'},
            'ipaddr': {'required': '请输入ip'},
            'role': {'required': '请选择角色'},
            'isp': {'required': '请选择运营商'},
            'group': {'required': '请选择设备组'},
        }

    def clean_hostname(self):
        hostname = self.cleaned_data['hostname']
        hid = getattr(self.instance, 'id')
        has_host = self.Meta.model.objects.exclude(id=hid).filter(hostname=hostname).count()
        print(has_host)
        if not has_host:
            return hostname
        else:
            raise ValidationError('设备名已经存在', code='invalid')

    def clean_ipaddr(self):
        ipaddr = self.cleaned_data['ipaddr']
        hid = getattr(self.instance, 'id')
        has_ip = self.Meta.model.objects.exclude(id=hid).filter(ipaddr=ipaddr).count()
        if not has_ip:
            return ipaddr
        else:
            raise ValidationError('ip地址已经存在', code='invalid')