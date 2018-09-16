# 自建的路由文件
# 导入path来匹配url
from django.urls import path
# 导入当前目录下的views
from . import views


# 确定命名空间
app_name = 'polls'
# 子路由表
urlpatterns = [
    # path()负责绑定业务功能
    # 第一个参数是url,url里的参数用'< >'包裹
    # 第二个参数是绑定的业务功能，xxx.as_view()把xxx类作为业务功能
    # 第三个参数代表该条url的名字
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
]
