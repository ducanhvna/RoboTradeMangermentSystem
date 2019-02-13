from django.shortcuts import render
from django.shortcuts import render
from robos.models import Plugin, Setting
from backtests.models import TestSetting, BackTest, TestResult
from django.contrib.auth.models import User
from datetime import datetime
import openpyxl

# Create your views here.
def FindBacktestitembyName(ten):
    """ Tìm kiếm backtestitem bởi tên
    return None nếu không tìm thấy tao lun project moi
    Ngược lại trả về một object
    """
    objects = BackTest.objects.filter(name=ten)
    if objects.count() == 0:
        newtestitem = BackTest()
        newtestitem.name = ten
        newtestitem.created_by = User.objects.get(pk=1)
        newtestitem.save()
        return newtestitem
    return objects[0]

def FindPluginByName(plugin):
    objects = Plugin.objects.filter(name=plugin)
    if objects.count() == 0:
        return None
    return objects[0]

def AddBackTest(row_data):
    """
    create Backtest từ một row data trong file
    """
    print('add backtestitem')
    #Name	Plugin	Setting	Value

    ten = row_data[0]
    plugin = row_data[1]
    settingname = row_data[2]
    settingvalue = row_data[3]

    # Kiem tra thong tin cua bo phan

    testitem = FindBacktestitembyName(ten)
    if testitem is None:
        return
    ispluginvalid = (plugin == None) or (plugin == "") or (plugin == 'None')
    
    if not ispluginvalid:
        pluginobject = FindPluginByName(plugin)
        if pluginobject is None:
            pluginobject = Plugin()
            pluginobject.name = plugin
            pluginobject.created_by = User.objects.get(pk=1)
            pluginobject.save()

        # tao setting
        
        settings = Setting.objects.filter(plugin = pluginobject, name = settingname)
        if settings.count() > 0:
            setting = settings[0]
        else:

            setting = Setting()
            setting.plugin = pluginobject
            setting.name = settingname
            setting.save()

        # tạo testsetting
        testitem.backtest_settings.create(setting = setting, settingvalue = settingvalue)

#####################################################
# Vùng import timeline
#####################################################
def ImportTimeline(request):
    if "GET" == request.method:
        return render(request, 'import_testitem.html', {})
    else:
        excel_file = request.FILES["excel_file"]

        # you may put validations here to check extension or file size

        wb = openpyxl.load_workbook(excel_file)

        # getting a particular sheet by name out of many sheets
        worksheet = wb["Sheet1"]
        print(worksheet)

        excel_data = list()
        # iterating over the rows and
        # getting value from each cell in row
        index = 0
        for row in worksheet.iter_rows():
            row_data = list()
            for cell in row:
                row_data.append(str(cell.value))
            if index >0:
                AddBackTest(row_data)
            index = index+1
            excel_data.append(row_data)

        return render(request, 'import_testitem.html', {"excel_data":excel_data})