from django.test import TestCase

# Create your tests here.

import os

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "djangosix.settings")
    import django
    django.setup()

    from app01 import models
    # models.Author.objects.create(name='oscar',age=21,author_detail_id=1)
    # models.Author.objects.create(name='jason',age=18,author_detail_id=2)
    # models.Author.objects.create(name='tom',age=36,author_detail_id=3)
    # models.Author.objects.create(name='kevin',age=19,author_detail_id=4)
    # models.Author.objects.create(name='tony',age=31,author_detail_id=5)

    # models.Book.objects.create(title='python',price=8888.21,xiaoliang=1000,kucun=2000,publish_id=1)
    # models.Book.objects.create(title='数据分析',price=9999.21,xiaoliang=1000,kucun=300,publish_id=1)
    # models.Book.objects.create(title='金瓶梅',price=2222.23,xiaoliang=2000,kucun=600,publish_id=2)
    # models.Book.objects.create(title='西游记',price=3333.96,xiaoliang=3000,kucun=900,publish_id=3)
    # models.Book.objects.create(title='红楼梦',price=55555.22,xiaoliang=800,kucun=2000,publish_id=4)
    # models.Book.objects.create(title='三国演义',price=66666.21,xiaoliang=900,kucun=1000,publish_id=5)
    # models.Book.objects.create(title='水浒传',price=7777.21,xiaoliang=4000,kucun=9000,publish_id=1)
    # models.Book.objects.create(title='绿皮书',price=99999.21,xiaoliang=5000,kucun=10000,publish_id=2)
    # models.Book.objects.create(title='疯狂讲义',price=10002.21,xiaoliang=10000,kucun=99000,publish_id=3)
    # models.Book.objects.create(title='资本论',price=11123.21,xiaoliang=200,kucun=88000,publish_id=4)
    # models.Book.objects.create(title='黑猫警长',price=88555.21,xiaoliang=40000,kucun=10000,publish_id=5)
    # models.Book.objects.create(title='葫芦娃',price=66321.21,xiaoliang=30000,kucun=2000,publish_id=1)

    from django.db.models import Max


    res = models.Book.objects.aggregate(Max('price'))
    # msg = models.Book.objects.filter(price=res).values('title')
    # msg = res.key()
    msg = res.get('price__max')
    outh = models.Book.objects.filter(price=msg).first()
    print(outh.price)