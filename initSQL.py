import os, django

os.environ["DJANGO_SETTINGS_MODULE"] = "Django_Blog.settings"
django.setup()
from blog.models import Site

print("开始创建网站信息")
name = input("请输入您的网站名:")
keywords = input("请输入您的网站关键字:")
head = input("请输入您的头像链接:")
site = Site.objects.create(site_name=name, keywords=keywords, logo=head)
site.save()
print("创建默认网站成功")
