from django.shortcuts import render

# Create your views here.


# 导入通用视图
from django.views import generic
# 导入要用到的数据模型
from .models import Question, Choice
# 导入时区模块
from django.utils import timezone
# 导入自动生成404的快捷函数,生成HttpResponse对象的快捷函数
from django.shortcuts import get_object_or_404, render
# 导入页面重定向模块
from django.http import HttpResponseRedirect
# 导入反向解析函数
from django.urls import reverse


# 创建索引视图
# 必须继承字generic的一个子类,这样才能自动实现一些功能
# 类名直接对应urls.py里path()的第二个参数
# 也就是URLs和Views是通过类名或者函数名进行区别绑定的
class IndexView(generic.ListView):
    # model属性绑定数据模型
    model = Question
    # template_name属性绑定页面模板
    template_name = 'polls/index.html'
    # context_object_name 用于对传给页面模板的变量进行命名
    context_object_name = 'question_list'


# 创建问题详情视图
class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'

    # get_queryset()用于筛选model得到数据,结果返回给model
    def get_queryset(self):
        # 返回出版时间小于现在的
        # Question.objects.filter(pub_date__lte=timezone.now())
        # 是Django提供的数据库API的写法
        return Question.objects.filter(pub_date__lte=timezone.now())


# 创建投票结果视图
class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'


# 创建投票功能视图,是函数视图,实现投票业务
def vote(request, question_id):
    # 获取主键pk等于参数question_id的Question
    # get_object_or_404()实现:要么获取成功,要么自动返回Http404
    # 第一个参数表示要获取的数据模型
    # 第二个参数是获取条件
    question = get_object_or_404(Question, pk=question_id)
    try:
        # 获取投票选项
        # question.choice_set.get()是数据库API的写法
        # request.POST[]以字符串形式返回选择的Choice的ID
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    # 如果在request.POST['choice']数据中没有提供choice,POST将引发一个KeyError
    except (KeyError, Choice.DoesNotExist):
        # 如果choice不存在引发KeyError,就返回polls/detail.html页面
        # render()用于返回HttpResponse对象
        # 第一个参数request是固定且必要的
        # 第二个参数是绑定的页面模板
        # 第三个参数是传到模板中的参数,是一个字典类型
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        # 选票加一
        selected_choice.votes += 1
        # 保存选票数据
        selected_choice.save()
        # 重定向到polls:results的链接,参数是url
        # reverse()用于对url反向解析:把名字变为链接
        # 第一个参数是url的名字,路由urls.py里面命名的
        # 第二个参数是url的参数,是一个元组类型
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))
