from pure_pagination import Paginator, EmptyPage, PageNotAnInteger


def paging(content, request):
    print("你好")
    try:
        all_articles = content.page(request.GET.get('page', 1))
    except PageNotAnInteger:
        all_articles = content.page(1)
    except EmptyPage:
        print("wps", content.num_pages)
        # 页码超出范围，返回最后一页
        all_articles = content.page(content.num_pages)
    return all_articles
