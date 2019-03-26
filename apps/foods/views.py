from django.shortcuts import render
from cafe.models import Sanat,Tamaq
from .forms import ImageUploadForm
from django.core.files.base import ContentFile
# Create your views here.
def MenusView(request):
    if request.method == 'GET':
        # while get method
        all_tamaq = Tamaq.objects.all()
        content = {
            'all_tamaq':all_tamaq
        }
        return render(request,'menus.html',content)
    elif request.method == 'POST':
        all_tamaq = Tamaq.objects.all()
        item_id = request.POST.get('item_id',None)
        if item_id:
            Tamaq.objects.filter(id = item_id).delete()
        content = {
            'delsucc':"Табысты жойылды!",
            'all_tamaq': all_tamaq
        }
        return render(request, 'menus.html', content)

def FoodsView(request):
    if request.method == 'GET':
        all_sanat = Sanat.objects.all()
        #
        content = {
            'all_sanat':all_sanat
        }
        return render(request,'addmenu.html',content)


    elif request.method == 'POST':
        all_tamaq = Tamaq.objects.all()
        form = ImageUploadForm(request.POST, request.FILES)
        if request.FILES.get('photo'):
            # file_content = ContentFile(photo.read())
            # tamaq_add.suret.save(file_content)
            # suret = form.cleaned_data['photo']
            suret = request.FILES.get('photo')
            tamaq =request.POST.get('name',None)
            sanat = request.POST.get('menu',None)
            salmagi = request.POST.get('gramm',None)
            baga = request.POST.get('price',None)
            actiontype = request.POST.get('action_type','ADD')
            if actiontype == 'ADD':
                tamaq_add =Tamaq()
                tamaq_add.sanat_id = sanat
                tamaq_add.aty = tamaq
                tamaq_add.salmagi = salmagi
                tamaq_add.baga = baga
                tamaq_add.suret = suret
                tamaq_add.save()
                content = {
                    'addsucc': 'Жаңа тағам сәтті қосылды!',
                    'all_tamaq': all_tamaq
                }
                return render(request, 'menus.html', content)
            elif actiontype == 'EDIT':
                pass
        else:
            content = {
                'msg':'Ұсынылған деректер дұрыс екендігін тексеріңіз!'
            }

            return render(request,'addmenu.html',content)


def EditFoodView(request):
    all_sanat = Sanat.objects.all()
    if request.method == 'GET':
        return render(request, 'editmenu.html', content)
    if request.method == 'POST':
        item_id = request.POST.get('item_id',None)
        item_name = request.POST.get('item_name',None)
        item_salmagi = request.POST.get('item_salmagi',None)
        item_baga = request.POST.get('item_salmagi',None)
        item_suret = request.POST.get('item_salmagi',None)
        content = {
            'msg':'үшін ақпаратты өзгертіп жатырсыз',
            'all_sanat': all_sanat,
            'item_id':item_id,
            'item_name':item_name,
            'item_salmagi':item_salmagi,
            'item_baga':item_baga,
            'item_suret':item_suret
        }

        return render(request,'editmenu.html', content)