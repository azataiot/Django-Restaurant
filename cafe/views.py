from django.shortcuts import render

# Create your views here.
from djreservation.views import ProductReservationView
from .models import Tamaq, Sanat, SebetModel

class MyObjectReservation(ProductReservationView):
    base_model = Tamaq  # required
    amount_field = 'quantity'  # required
    # extra_display_field = ['measurement_unit']  # not required


def ShowMenus(request):
        all_sanat = Sanat.objects.all()
        all_tamaq = Tamaq.objects.all()
        tamaq_1 = Tamaq.objects.filter(sanat_id=1)
        tamaq_2 = Tamaq.objects.filter(sanat_id=2)
        tamaq_3 = Tamaq.objects.filter(sanat_id=3)
        tamaq_4 = Tamaq.objects.filter(sanat_id=4)
        tamaq_5 = Tamaq.objects.filter(sanat_id=5)
        tamaq_6 = Tamaq.objects.filter(sanat_id=6)
        tamaq_7 = Tamaq.objects.filter(sanat_id=7)
        sanat_1 = Sanat.objects.filter(id=1)
        sanat_2 = Sanat.objects.filter(id=2)
        sanat_3 = Sanat.objects.filter(id=3)
        sanat_4 = Sanat.objects.filter(id=4)
        sanat_5 = Sanat.objects.filter(id=5)
        sanat_6 = Sanat.objects.filter(id=6)
        sanat_7 = Sanat.objects.filter(id=7)
        content = {
            'tamaq_1':tamaq_1,
            'tamaq_2':tamaq_2,
            'tamaq_3':tamaq_3,
            'tamaq_4':tamaq_4,
            'tamaq_5':tamaq_5,
            'tamaq_6':tamaq_6,
            'tamaq_7':tamaq_7,
            'sanat_1':sanat_1,
            'sanat_2':sanat_2,
            'sanat_3':sanat_3,
            'sanat_4':sanat_4,
            'sanat_5':sanat_5,
            'sanat_6':sanat_6,
            'sanat_7':sanat_7,
            'all_sanat':all_sanat,
            'all_tamaq':all_tamaq
        }

        return render(request,'menu.html',content)

def SelectMenu(request,cat):
    tamaq_1 = Tamaq.objects.filter(sanat_id=1)
    tamaq_2 = Tamaq.objects.filter(sanat_id=2)
    tamaq_3 = Tamaq.objects.filter(sanat_id=3)
    tamaq_4 = Tamaq.objects.filter(sanat_id=4)
    tamaq_5 = Tamaq.objects.filter(sanat_id=5)
    tamaq_6 = Tamaq.objects.filter(sanat_id=6)
    tamaq_7 = Tamaq.objects.filter(sanat_id=7)
    all_sanat = Sanat.objects.all()
    content = {
        'msg':"Сіз кірген мәзір жоқ!"
    }
    if request.method == 'GET':
        # response for get request
        if(cat == 1):
            tamaq = tamaq_1
            if request.session.get('sebet', False):
                pass
            else:
                request.session['sebet'] = True
            return render(request, 'menus/1.html' ,{'tamaq':tamaq})
        elif(cat == 2):
            tamaq = tamaq_2
            if request.session.get('sebet', False):
                pass
            else:
                request.session['sebet'] = True
            return render(request, 'menus/2.html', {'tamaq': tamaq})
        elif(cat == 3):
            tamaq = tamaq_3
            if request.session.get('sebet', False):
                pass
            else:
                request.session['sebet'] = True
            return render(request, 'menus/3.html', {'tamaq': tamaq})
        elif(cat == 4):
            tamaq = tamaq_4
            if request.session.get('sebet', False):
                pass
            else:
                request.session['sebet'] = True
            return render(request, 'menus/4.html', {'tamaq': tamaq})
        elif(cat == 5):
            tamaq = tamaq_5
            if request.session.get('sebet', False):
                pass
            else:
                request.session['sebet'] = True
            return render(request, 'menus/5.html', {'tamaq': tamaq})
        elif(cat == 6):
            tamaq = tamaq_6
            if request.session.get('sebet', False):
                pass
            else:
                request.session['sebet'] = True
            return render(request, 'menus/6.html', {'tamaq': tamaq})
        elif(cat == 7):
            tamaq = tamaq_7
            if request.session.get('sebet', False):
                pass
            else:
                request.session['sebet'] = True
            return render(request, 'menus/7.html', {'tamaq': tamaq})
        else:
            return render(request, 'menu.html', content)
    elif request.method == 'POST':
        inCart = 0
        sebet_model = SebetModel()
        tamaq_model = Tamaq()
        if (cat == 1):
            tamaq = tamaq_1
            content = {
                'cartmsg': "себетке қосылды !",
                'tamaq':tamaq
            }
            if request.session.get('sebet', False): #if has the session
                sess_id = request.session.session_key
                product = request.POST.get('tamaq',None)
                in_sebet = SebetModel.objects.filter(nameoo=sess_id)
                inCart =  SebetModel.objects.filter(nameoo=sess_id).count()

                if product:
                    inCart += 1
                content = {
                    'cartmsg': "себетке қосылды !",
                    'tamaq': tamaq,
                    'product':product,
                    'inCart' : inCart,
                    'in_sebet':in_sebet,
                    # 'all_in_sebet_food':all_in_sebet_food
                }
                to_cart = Tamaq.objects.get(aty__exact=product)
                sebet_model.nameoo = sess_id
                sebet_model.save()
                sebet_model.foods.add(to_cart)
                return render(request, 'menus/1.html', content)
            else:

                request.session['sebet'] = True
            return render(request, 'menus/1.html', content)
        elif (cat == 2):
            tamaq = tamaq_2
            if request.session.get('sebet', False):  # if has the session
                sess_id = request.session.session_key
                product = request.POST.get('tamaq', None)
                in_sebet = SebetModel.objects.filter(nameoo=sess_id)
                inCart = SebetModel.objects.filter(nameoo=sess_id).count()

                if product:
                    inCart += 1
                content = {
                    'cartmsg': "себетке қосылды !",
                    'tamaq': tamaq,
                    'product': product,
                    'inCart': inCart,
                    'in_sebet': in_sebet,
                    # 'all_in_sebet_food':all_in_sebet_food
                }
                to_cart = Tamaq.objects.get(aty__exact=product)
                sebet_model.nameoo = sess_id
                sebet_model.save()
                sebet_model.foods.add(to_cart)
                return render(request, 'menus/2.html', content)
            else:
                request.session['sebet'] = True
            return render(request, 'menus/2.html', {'tamaq': tamaq})
        elif (cat == 3):
            tamaq = tamaq_3
            if request.session.get('sebet', False):  # if has the session
                sess_id = request.session.session_key
                product = request.POST.get('tamaq', None)
                in_sebet = SebetModel.objects.filter(nameoo=sess_id)
                inCart = SebetModel.objects.filter(nameoo=sess_id).count()

                if product:
                    inCart += 1
                content = {
                    'cartmsg': "себетке қосылды !",
                    'tamaq': tamaq,
                    'product': product,
                    'inCart': inCart,
                    'in_sebet': in_sebet,
                    # 'all_in_sebet_food':all_in_sebet_food
                }
                to_cart = Tamaq.objects.get(aty__exact=product)
                sebet_model.nameoo = sess_id
                sebet_model.save()
                sebet_model.foods.add(to_cart)
                return render(request, 'menus/3.html', content)
            else:
                request.session['sebet'] = True
            return render(request, 'menus/3.html', {'tamaq': tamaq})
        elif (cat == 4):
            tamaq = tamaq_4
            if request.session.get('sebet', False):  # if has the session
                sess_id = request.session.session_key
                product = request.POST.get('tamaq', None)
                in_sebet = SebetModel.objects.filter(nameoo=sess_id)
                inCart = SebetModel.objects.filter(nameoo=sess_id).count()

                if product:
                    inCart += 1
                content = {
                    'cartmsg': "себетке қосылды !",
                    'tamaq': tamaq,
                    'product': product,
                    'inCart': inCart,
                    'in_sebet': in_sebet,
                    # 'all_in_sebet_food':all_in_sebet_food
                }
                to_cart = Tamaq.objects.get(aty__exact=product)
                sebet_model.nameoo = sess_id
                sebet_model.save()
                sebet_model.foods.add(to_cart)
                return render(request, 'menus/4.html', content)
            else:
                request.session['sebet'] = True
            return render(request, 'menus/4.html', {'tamaq': tamaq})
        elif (cat == 5):
            tamaq = tamaq_5
            if request.session.get('sebet', False):  # if has the session
                sess_id = request.session.session_key
                product = request.POST.get('tamaq', None)
                in_sebet = SebetModel.objects.filter(nameoo=sess_id)
                inCart = SebetModel.objects.filter(nameoo=sess_id).count()

                if product:
                    inCart += 1
                content = {
                    'cartmsg': "себетке қосылды !",
                    'tamaq': tamaq,
                    'product': product,
                    'inCart': inCart,
                    'in_sebet': in_sebet,
                    # 'all_in_sebet_food':all_in_sebet_food
                }
                to_cart = Tamaq.objects.get(aty__exact=product)
                sebet_model.nameoo = sess_id
                sebet_model.save()
                sebet_model.foods.add(to_cart)
                return render(request, 'menus/5.html', content)
            else:
                request.session['sebet'] = True
            return render(request, 'menus/5.html', {'tamaq': tamaq})
        elif (cat == 6):
            tamaq = tamaq_6
            if request.session.get('sebet', False):  # if has the session
                sess_id = request.session.session_key
                product = request.POST.get('tamaq', None)
                in_sebet = SebetModel.objects.filter(nameoo=sess_id)
                inCart = SebetModel.objects.filter(nameoo=sess_id).count()

                if product:
                    inCart += 1
                content = {
                    'cartmsg': "себетке қосылды !",
                    'tamaq': tamaq,
                    'product': product,
                    'inCart': inCart,
                    'in_sebet': in_sebet,
                    # 'all_in_sebet_food':all_in_sebet_food
                }
                to_cart = Tamaq.objects.get(aty__exact=product)
                sebet_model.nameoo = sess_id
                sebet_model.save()
                sebet_model.foods.add(to_cart)
                return render(request, 'menus/6.html', content)
            else:
                request.session['sebet'] = True
            return render(request, 'menus/6.html', {'tamaq': tamaq})
        elif (cat == 7):
            tamaq = tamaq_7
            if request.session.get('sebet', False):  # if has the session
                sess_id = request.session.session_key
                product = request.POST.get('tamaq', None)
                in_sebet = SebetModel.objects.filter(nameoo=sess_id)
                inCart = SebetModel.objects.filter(nameoo=sess_id).count()

                if product:
                    inCart += 1
                content = {
                    'cartmsg': "себетке қосылды !",
                    'tamaq': tamaq,
                    'product': product,
                    'inCart': inCart,
                    'in_sebet': in_sebet,
                    # 'all_in_sebet_food':all_in_sebet_food
                }
                to_cart = Tamaq.objects.get(aty__exact=product)
                sebet_model.nameoo = sess_id
                sebet_model.save()
                sebet_model.foods.add(to_cart)
                return render(request, 'menus/7.html', content)
            else:
                request.session['sebet'] = True
            return render(request, 'menus/7.html', {'tamaq': tamaq})
        else:
            return render(request, 'menu.html', content)


def Sebet(request):
    if request.method == 'GET':
        #starts here
        sess_id = request.session.session_key
        qs = Tamaq.objects.filter(sebetmodel__nameoo=sess_id)
        in_Cart = qs.all().count()
        total_baga = 0
        for each in qs:
            total_baga += each.baga
        print(total_baga)
        content = {
            'in_Cart':in_Cart,
            'in_sebet':qs,
            'total_baga':total_baga
        }
        return render(request,'cart.html',content)
    elif request.method == 'POST':
        sess_id = request.session.session_key
        qs = Tamaq.objects.filter(sebetmodel__nameoo=sess_id)
        in_Cart = qs.all().count()
        total_baga = 0
        for each in qs:
            total_baga += each.baga
        # starts here
        del_tam_aty = request.POST.get('tamaq_delete',None)
        SebetModel.objects.filter(foods__aty=del_tam_aty).delete()
        # cor_seb = SebetModel.objects.filter(foods__aty=del_tam_aty)
        # print(cor_seb)
        content = {
            'in_Cart': in_Cart,
            'in_sebet': qs,
            'total_baga': total_baga,
            'del_aty':del_tam_aty,
            'delmsg':'сәтті жойылды!'
        }
        return render(request, 'cart.html', content)


