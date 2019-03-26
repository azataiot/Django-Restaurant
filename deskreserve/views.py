from django.shortcuts import render
from .models import DeskOrder,Desk
from datetime import datetime,date,time, timedelta
from django.db.models import Q
# Create your views here.


def DeskShow(request):
    if request.method == 'GET':
        # DESKS_ID = []
        # DESK_OCC_ID = []
        # all_desks = Desk.objects.all()
        # for each in all_desks:
        #     DESKS_ID.append(each.id)
        # today = date.today()
        # rdate_date = today
        # # print(rdate_date)
        # # print(type(rdate_date))
        # rtime_time =datetime.now().time()
        # # print(rtime_time)
        # # desk_free = Desk.objects.filter(order__client_name__contains=rdate_date)  # desk is free that day
        # # desk_occ_in_date = Desk.objects.filter(order__order_date = rdate_date)
        # for each in desk_occ_in_date:
        #     DESK_OCC_ID.append(each.id)
        # desks_free_in_date = [item for item in DESKS_ID if item not in DESK_OCC_ID]
        content = {
            'msg': "Күн мен уақытты таңдаңыз!",
            # 'desks_free_in_date':desks_free_in_date,
            # 'desk_occ_in_date':desk_occ_in_date,
            # 'rdate_date':rdate_date,
            # 'rtime_time':rtime_time
        }

        return render(request, 'deskshow.html',content)

    elif request.method == 'POST':
        desk_order = DeskOrder()
        rdate = request.POST.get('rdate',None)
        rtime = request.POST.get('rtime',None)
        if rdate:
            if rtime:
                # everything is ok
                sess_id = request.session.session_key
                msg=''
                today = date.today()
                rdate_date = datetime.strptime(rdate,"%Y-%m-%d").date()
                rtime_time = datetime.strptime(rtime,"%H:%M").time()
                # desk_occ_in_date = Desk.objects.filter(order__order_date=rdate_date)
                dtcombined = datetime.combine(rdate_date,rtime_time)
                if today>rdate_date:
                    msg = "Өткен уақытты таңдау болмайды!"
                    content = {
                        'msg': msg
                    }
                    return render(request, 'deskshow.html', content)
                else:
                    dtcombined_end = dtcombined + timedelta(minutes=90)
                    not_ok_order = DeskOrder.objects.filter(Q(order_dt__gt=dtcombined) & Q(order_dt__lt=dtcombined_end))
                    all_desks = Desk.objects.all()
                    content = {
                        'not_ok_order':not_ok_order,
                        'rdate_date':rdate,
                        'rtime_time':rtime,
                        'dtcombined':dtcombined,
                        'all_desks':all_desks
                    }
                    return render(request,'deskshow.html',content)
            else:
                msg = "Күн мен уақытты таңдаңыз!"
                content = {
                    'msg':msg
                }
                return render(request, 'deskshow.html', content)
        else:
            # date is not filled
            msg = "Күн мен уақытты таңдаңыз!"
            content = {
                'msg': msg
            }
            return render(request, 'deskshow.html', content)

def DeskOrderView(request):
    if request.method == 'GET':
        content = {
        }
        return render(request, 'bron-act.html',content)
    if request.method == 'POST':
        desk = request.POST.get('desk',None)
        desk_date = request.POST.get('rdate',None)
        desk_time = request.POST.get('rtime',None)
        content = {
            'desk': desk,
            'rdate':desk_date,
            'rtime':desk_time
        }
        deskfororder = desk
        sess_id = request.session.session_key
        desk_for_order = Desk.objects.filter(id=desk)
        # desk_will_be_ordered = DeskOrder.objects.filter(desk__name=desk)
        rdate_date = datetime.strptime(desk_date, "%Y-%m-%d").date()
        rtime_time = datetime.strptime(desk_time, "%H:%M").time()
        dt_dt = datetime.combine(rdate_date, rtime_time)
        DeskOrder.objects.create(desktop_id = deskfororder, name= desk_date+desk_time ,order_date=rdate_date, order_time=rtime_time, order_dt=dt_dt)
        return render(request, 'bron-act.html',content)




def DeskOrderHandle(request):
    if request.method == 'GET':
        return render(request, 'message.html',{'msg':"Ok!"})
    if request.method == 'POST':
        desk_id = request.POST.get('desk1')
        desss = request.POST.get('desss')
        print(desss)
        order_client_name = request.POST.get('order_client_name',None)
        print(order_client_name)
        order_client_mobile = request.POST.get('order_client_mobile',None)
        print(order_client_mobile)
        order_client_number = request.POST.get('order_client_number',None)
        print(order_client_number)
        # dt = request.POST.get('dt',None)
        rdate = request.POST.get('rdate',None)
        rtime = request.POST.get('rtime',None)
        print(rdate+rtime)
        rdate_date = datetime.strptime(rdate, "%Y-%m-%d").date()
        rtime_time = datetime.strptime(rtime, "%H:%M").time()
        dt_dt= datetime.combine(rdate_date,rtime_time)

        DeskOrder.objects.filter(order_dt= dt_dt).update( client_name = order_client_name, mobile = order_client_mobile , num_client = order_client_number )

        content = {
            # 'msg':'Біз сіздің броньызызды алдық және сіздің пайдалануыңызға рахмет!',
            'msg':"Табысты жұмыс!"
        }
        return render(request,'message.html',content)