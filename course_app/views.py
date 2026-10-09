from django.shortcuts import render
from rest_framework import generics
from django.db.models import Count
from .models import Course,Stage,Chapter,Section
from .serializers import CourseSerializers,StageSerializers,ChapterSerializers,SectionSerializers,StageDateSerializers
from rest_framework.pagination import PageNumberPagination
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page

# Create your views here.

'''
redis缓存 不频繁变更 公开查询  读多少写的公共数据

'''



# 设置分页器类 rest_framework中的
class RestfulPage(PageNumberPagination):
    # 前端默认显示多少条数据
    page_size=2
    # 前端控制时最多显示多少条数据
    max_page_size=5
    # 页码参数
    page_query_param='page'


# 这里没有写他会添加数据的接口 只有查询数据接口 那就先默认是 不变更的数据


# 获取课程分类所有数据
@method_decorator(
    cache_page(60 * 3, key_prefix="course_list"),
    name="dispatch",
)
class CourseView(generics.ListAPIView):
    # 指定查询及
    # queryset=Course.objects.all()
    # 统计分类中有多少个阶段 多少个章节 多少个小节 需要注意 使用annotate时在去使用Count统计完成之后 需要使用values去进行查询（相当于原先的
    # 查询所有内容）
    queryset=Course.objects.annotate(
        # 统计有多少个阶段 distinct=True避免放大计数
        stage_count=Count('stage',distinct=True),
        # 统计有多少个章节
        chapter_count=Count('stage__chapter',distinct=True),
        # 统计用多少个小结
        section_count=Count("stage__chapter__sction",distinct=True)
        # 查询所有字段
    ).values(
          'id','name','learn_info','learn_style','learn_time','supervision','icon',
          'brief','level',"stage_count","chapter_count",'section_count'
    )

    # 指定序列器
    serializer_class=CourseSerializers
    # 指定分页器
    pagination_class=RestfulPage
    '''
    指定分页器后不用在路由传递 参数 generics.ListAPIView已经封装好了
    
    '''





# 获取课程阶段所有对应数据
class StageView(generics.ListAPIView):
    # 指定查询及
    queryset=Stage.objects.all()
    # 指定序列器
    serializer_class=StageSerializers
    # 设置过滤字段 
    '''
    设置过滤 给前端添加筛选功能
    '''
    filterset_fields=('course')



# 获取课程章节所有数据 以及添加内容 以及过滤
class ChapterView(generics.ListAPIView):
    queryset=Chapter.objects.all()
    serializer_class=ChapterSerializers
    filterset_fields=('stage')




# 获取所有小节列表
class SectionView(generics.ListAPIView):
    queryset=Section.objects.all()
    serializer_class=SectionSerializers
    filterset_fields=('chapter')



# 获取某个阶段以及其中对应的章节以及对应的小节
class StageAllView(generics.RetrieveAPIView):
     queryset=Stage.objects.all()
     serializer_class=StageDateSerializers



 












'''

复习如何手写分页器 而在项目中 一般不用手写分页器
直接使用 rest_framework中自带的分页功能就可以了



'''

# from django.conf import settings
# from django.core.paginator import Paginator
# # 设置分页  自定义函数
# def get_pages(request):
#     # 获取要分页的数据
#     courses=Course.objects.all()
#     # 设置分多少页数 settings.PAGE_SIEZ
#     # 初始化分页器
#     paginator=Paginator(courses,settings.PAGE_SIZE)
#     # 获取指定页码
#     page=request.GET.get("page")
#     # 返回指定页码的数据
#     data=paginator.get_page(page)
#     #设置底层显示 设置默认为
#     current_page= page if page is not None else 1
    



# # 自定义页码显示
# def get_page_data(page,max_page,num=4):
#     """
#     get_page_data 的 Docstring
    
#     :param page: 当前页码
#     :param max_page: 总页码数
#     :param num: 前后显示多少页码
#     """
#     # 最小页码数
#     min=int(page)-num
#     min=min if min>1 else 1
#     # 最大页码数
#     max=int(page)+num-1
#     max=max if max<max_page else max_page
#     return range(min,max+1)

    