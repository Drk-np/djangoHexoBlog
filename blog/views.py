from django.shortcuts import render
import datetime
from django.views.generic.base import View
from .models import Article, Link, Category, Tag, Notice, Valine, About, Site, Social, Skill
import mistune
from pure_pagination import Paginator, EmptyPage, PageNotAnInteger
from .tools.tools import paging #分页工具


def index(request):
    """首页展示"""
    # 取出所有博客文章
    all_articles = Article.objects.all().order_by('-add_time')
    # 取出要推荐的博客文章
    top_articles = Article.objects.filter(is_recommend=1)
    notices = Notice.objects.all()
    #分页
    p = Paginator(all_articles, 9, request=request)
    all_articles =  paging(p,request)
    # 需要传递给模板（templates）的对象
    context = {
        'all_articles': all_articles,
        'top_articles': top_articles,
        'notices': notices
    }
    # render函数：载入模板，并返回context对象
    return render(request, 'index.html', context)


def article_detail(request, id):
    """文章详情页"""
    # 取出相应的文章
    article = Article.objects.get(id=id)
    # 增加阅读数
    article.click_count += 1
    article.save(update_fields=['click_count'])
    valine = Valine.objects.first()  # 取第一条数据
    # 前台mK解析
    mk = mistune.Markdown()
    output = mk(article.content)
    # 需要传递给模板的对象
    context = {
        'valine': valine,
        'article': article,
        'article_detail_html': output,
    }
    # 载入模板，并返回context对象
    return render(request, 'article_detail.html', context)


def member(request):
    '''成员详情页'''
    links = Link.objects.all()
    context = {'links': links, }
    return render(request, 'member.html', context)


def category_tag(request):
    '''分类和标签页'''
    categories = Category.objects.all()
    tags = Tag.objects.all()
    context = {
        'categories': categories,
        'tags': tags,
    }
    return render(request, 'category_tag.html', context)


def article_category(request, id):
    '''文章分类详情页'''
    categories = Category.objects.all()
    articles = Category.objects.get(id=id).article_set.all()  # 获取该id对应的所有的文章
    # 分页
    p = Paginator(articles, 12, request=request)
    articles = paging(p, request)
    context = {
        'categories': categories,
        'id': id,
        'articles': articles
    }
    return render(request, 'article_category.html', context)


def article_tag(request, id):
    '''文章标签详情页'''
    tags = Tag.objects.all()
    articles = Tag.objects.get(id=id).article_set.all()
    # 分页
    p = Paginator(articles, 12, request=request)
    articles = paging(p, request)
    context = {
        'tags': tags,
        'id': id,
        'articles': articles
    }
    print("context", context)
    return render(request, 'article_tag.html', context)


def archive(request):
    """
       文章归档
    """
    all_articles = Article.objects.all().order_by('-add_time')

    all_date = all_articles.values('add_time')
    latest_date = all_date[0]['add_time']
    all_date_list = []
    for i in all_date:
        all_date_list.append(i['add_time'].strftime("%Y-%m-%d"))

    # 遍历1年的日期
    end = datetime.date(latest_date.year, latest_date.month, latest_date.day)
    begin = datetime.date(latest_date.year - 1, latest_date.month, latest_date.day)
    d = begin
    date_list = []
    temp_list = []

    delta = datetime.timedelta(days=1)
    while d <= end:
        day = d.strftime("%Y-%m-%d")
        if day in all_date_list:
            temp_list.append(day)
            temp_list.append(all_date_list.count(day))
        else:
            temp_list.append(day)
            temp_list.append(0)
        d += delta
        date_list.append(temp_list)
        temp_list = []

    # 文章归档分页
    try:
        page = request.GET.get('page', 1)
    except PageNotAnInteger:
        page = 1
    except EmptyPage:
        # 页码超出范围，返回最后一页
        page = Paginator.num_pages

    print(all_articles[0])
    p = Paginator(all_articles, 10, request=request)
    articles = p.page(page)
    return render(request, 'archive.html', {
        'all_articles': articles,
        'date_list': date_list,
        'end': str(end),
        'begin': str(begin),
    })


def add_nav(request):
    '''导航栏'''
    category_nav = Category.objects.filter(add_menu=True).order_by('index')
    context = {
        'category_nav': category_nav,
    }
    return render(request, 'layout/header.html', context)


def about(request):
    articles = Article.objects.all().order_by('-add_time')
    categories = Category.objects.all()
    tags = Tag.objects.all()

    about = About.objects.first()
    skill = Skill.objects.all()

    all_date = articles.values('add_time')

    latest_date = all_date[0]['add_time']
    end_year = latest_date.strftime("%Y")
    end_month = latest_date.strftime("%m")
    date_list = []
    for i in range(int(end_month), 13):
        date = str(int(end_year) - 1) + '-' + str(i)
        date_list.append(date)

    for j in range(1, int(end_month) + 1):
        date = end_year + '-' + str(j)
        date_list.append(date)

    value_list = []
    all_date_list = []
    for i in all_date:
        all_date_list.append(i['add_time'].strftime("%Y-%m"))

    for i in date_list:
        value_list.append(all_date_list.count(i))

    temp_list = []  # 临时集合
    tags_list = []  # 存放每个标签对应的文章数

    tags = Tag.objects.all()
    for tag in tags:
        temp_list.append(tag.name)
        temp_list.append(len(tag.article_set.all()))
        tags_list.append(temp_list)
        temp_list = []

    tags_list.sort(key=lambda x: x[1], reverse=True)  # 根据文章数排序

    top10_tags = []
    top10_tags_values = []
    for i in tags_list[:10]:
        top10_tags.append(i[0])
        top10_tags_values.append(i[1])

    return render(request, 'about.html', {
        'articles': articles,
        'categories': categories,
        'tags': tags,
        'about': about,
        'skill': skill,
        'date_list': date_list,
        'value_list': value_list,
        'top10_tags': top10_tags,
        'top10_tags_values': top10_tags_values,

    })


def global_params(request):
    """全局变量"""
    # 分类是否增加到导航栏
    category_nav = Category.objects.filter(add_menu=True).order_by('index')
    site_name = Site.objects.first().site_name
    logo = Site.objects.first().logo
    keywords = Site.objects.first().keywords
    desc = Site.objects.first().desc
    slogan = Site.objects.first().slogan
    dynamic_slogan = Site.objects.first().dynamic_slogan
    bg_cover = Site.objects.first().bg_cover
    icp_number = Site.objects.first().icp_number
    icp_url = Site.objects.first().icp_url
    social = Social.objects.all()
    return {
        'category_nav': category_nav,
        'SITE_NAME': site_name,
        'LOGO': logo,
        'KEYWORDS': keywords,
        'DESC': desc,
        'SLOGAN': slogan,
        'DYNAMIC_SLOGAN': dynamic_slogan,
        'BG_COVER': bg_cover,
        'ICP_NUMBER': icp_number,
        'ICP_URL': icp_url,
        'social': social,
    }
