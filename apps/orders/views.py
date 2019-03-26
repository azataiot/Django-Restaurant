from datetime import datetime,timedelta
from django.shortcuts import render
from django.views.generic.base import View
from tables.forms import TableFilterForm
from tables.models import Tables
from .models import TableOrder
from deskreserve.models import DeskOrder
# Create your views here.

def OrdersView(request):
    if request.method == 'GET':
        #GET
        all_orders = DeskOrder.objects.all()
        content = {
            'all_orders': all_orders
        }
        return render(request,'orders.html',content)
    elif request.method == 'POST':
        # POST
        or_name = request.POST.get('deskordername',None)
        DeskOrder.objects.filter(name=or_name).delete()
        all_orders = DeskOrder.objects.all()
        content = {
            'deleteditem':or_name,
            'deletemsg':'Сәтті жойылды!',
            'all_orders': all_orders
        }
        return render(request,'orders.html',content)



class BronView(View):
    def get(self,request):
        table_filter_form = TableFilterForm
        return render(request, 'bron.html',{'table_filter_form':table_filter_form})
    def post(self,request):
        table_filter_form = TableFilterForm
        all_available_tables = Tables.objects.filter(table_is_available=True)
        if table_filter_form.is_valid():
            return render(request, 'bron.html',{'all_available_tables':all_available_tables})
            print("idnisd")
        else:
            print("unvalid")



class ReservationView(View):
    def get(self,request):
        delta = timedelta(minutes=90)
        tables = Tables()
        all_tables = Tables.objects.all()
        table_order = TableOrder()
        now = datetime.now()
        all_table_orders = TableOrder.objects.all()
        for each_order in all_table_orders:
            print(each_order)
        if all_table_orders:
            print("not black")
        for each in all_tables:
            if(now-each.table_occ_end):
                each.table_is_available = True
            elif(each.table_occ_end-now>delta):
                each.table_is_available = True
            else:
                each.table_is_available = False
        tables.save()
        after_filter = Tables.objects.all()
        return render(request, 'reservation.html',{'all_tables':after_filter,'current_time':now})

    def post(self,request):
        table_filter_form = TableFilterForm
        table_order = TableOrder()
        tables = Tables()
        rdate = request.POST.get('rdate')
        rtime = request.POST.get('rtime')
        selected_table = request.POST.get('table_id')
        if selected_table:
            now = datetime.now()
            current_day = now.strftime("%Y-%m-%d")
            current_time = now.strftime("%H:%M")
            if rdate:
                pass
            else:
                rdate = current_day
            if rtime:
                pass
            else:
                rtime = current_time
            return render(request, 'bron-act.html',{'selected_table':selected_table,'rdate':rdate,'rtime':rtime})
        if rdate and rtime:
            # 这里会有一段查询的代码
            # 大于时间开始时间,小于时间结束时间根据这个并集选择.
            delta = timedelta(minutes=90)
            t_str = rdate+' '+rtime
            d_time = datetime.strptime(t_str, '%Y-%m-%d %H:%M')
            tables.table_occ_start = d_time
            after_delta = d_time +delta
            tables.table_occ_end = d_time +delta
            print(d_time)
            print(after_delta)
            print(type(d_time))
            # table_order.save()
            return render(request,'reservation.html',{'error':"ok"})
        else:
            if rdate:
                return render(request,'reservation.html',{'error':"Тапсырыс берілетін Үстелні тексеру үшін уақытты таңдаңыз!",'rdate':rdate})
            else:
                return render(request,'reservation.html',{'error':"Тапсырыс берілетін Үстелні тексеру үшін күнні таңдаңыз!",'rtime':rtime})



class BronActView(View):
    def get(self,request):
        return render(request,'bron-act.html',{})
    def post(self,request):
        delta = timedelta(minutes=90)
        table  = Tables()
        table_order = TableOrder()
        order_client_name = request.POST.get('order_client_name')
        order_client_mobile = request.POST.get('order_client_mobile')
        order_client_number = request.POST.get('order_client_number')
        rdate = request.POST.get('rdate')
        rtime = request.POST.get('rtime')
        selected_table = request.POST.get('selected_table')
        d_time = datetime.now()
        order_name = str(rdate)+str(rtime)+"Table: N0."+str(selected_table)+str(order_client_name)
        table_order.order_name = order_name
        TableOrder.ordered_tabel = selected_table
        TableOrder.order_client_name = order_client_name
        TableOrder.order_client_mobile = order_client_mobile
        TableOrder.order_client_number = order_client_number
        TableOrder.order_start_time = d_time
        Tables.table_is_available = False
        Tables.table_occ_start = d_time
        Tables.table_occ_end = d_time+delta
        table.save()
        table_order.save()
        return render(request,'message.html',{'msg':"Сіздің брондау қабылданды! \nҚолдауыңызға рахмет! \n"})