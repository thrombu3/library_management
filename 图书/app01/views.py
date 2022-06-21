from django.shortcuts import render,HttpResponse,redirect
from app01 import models

# Create your views here.

def index(request):
    return render(request,'index.html')

def see_book(request):
    res = models.Book.objects.filter()
    return render(request,'seebook.html',{'res_list': res})

def create_book(request):
    if request.method == 'POST':
        b_name = request.POST.get('book_name')
        b_price = int(request.POST.get('book_price'))
        b_xiaoliang = int(request.POST.get('book_xiaoliang'))
        b_kucun = int(request.POST.get('book_kucun'))
        # b_author = request.POST.get('zuozhe')
        b_chubanshe = request.POST.get('chubanshe')
        outh = models.Publish.objects.filter(name=b_chubanshe).first()
        if not outh:
            return HttpResponse('该出版社不存在')
        b_chubanshe_id = models.Publish.objects.filter(name=b_chubanshe).values('pk')
        b_chubanshe_id_a =b_chubanshe_id[0].get('pk')
        flag = models.Book.objects.filter(title=b_name).first()
        if flag:
            return HttpResponse('该书籍已经存在')
        request.body

        models.Book.objects.create(title=b_name,
                                   price=b_price,
                                   xiaoliang=b_xiaoliang,
                                   kucun=b_kucun,
                                   publish_id=b_chubanshe_id_a)
        return redirect('see_view')
    msg = models.Publish.objects.filter()
    res = models.Author.objects.filter()
    return render(request,'createbook.html',{'res_list':res,'msg_list':msg})

def modify_book(request,update_id):
    update_obj = models.Book.objects.filter(id=update_id).first()
    if not update_obj:
        return HttpResponse('当前书籍不存在')
    if request.method =='POST':
        b_price = int(request.POST.get('book_price'))
        b_xiaoliang = int(request.POST.get('book_xiaoliang'))
        b_kucun = int(request.POST.get('book_kucun'))
        models.Book.objects.filter(id=update_id).update(price=b_price,
                                                        xiaoliang=b_xiaoliang,
                                                        kucun=b_kucun)
        return redirect('see_view')

    return render(request,'modifybook.html',{'update_list': update_obj})

def drop_book(request,delect_id):
    delect_obj = models.Book.objects.filter(id=delect_id)
    if not delect_obj:
        return HttpResponse('该书籍不存在')
    delect_obj.delete()
    return redirect('caozuo_view')

def caozuo_book(request):
    res = models.Book.objects.filter()
    return render(request, 'caozuo.html', {'res_list': res})


from django.db.models import Max
def max_xiaoliang(request):
    res = models.Book.objects.aggregate(Max('price'))
    # msg = models.Book.objects.filter(price=res).values('title')
    # msg = res.key()
    msg = res.get('price__max')
    outh = models.Book.objects.filter(price=msg).first()
    return render(request,'max_title.html',{'outh_list':outh})


def test(request):
    return render(request,'test.html')