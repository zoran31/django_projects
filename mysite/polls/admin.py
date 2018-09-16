from django.contrib import admin

# Register your models here.


# 导入Question模型
from .models import Question, Choice


# # 注册Question，这样就可以被管理
# admin.site.register(Question)


# 创建自定义的Choice管理类
# 但必须继承自admin的某个类，这样才能使用它的功能
class ChioceInline(admin.TabularInline):
    # 关联Choice模型
    model = Choice
    # 定义可添加数目
    extra = 3


# 创建自定义的Question管理类
class QuestionAdmin(admin.ModelAdmin):
    # 定义显示格式：问题文本，发布日期
    list_display = ('question_text', 'pub_date')
    # 定义筛选器，按发布日期筛选
    list_filter = ['pub_date']
    # 定义查找器，按问题文本查找
    search_fields = ['question_text']
    # 关联ChoiceInline对象
    inlines = [ChioceInline]

# 注册Question，按照QuestionAdmin定义的内容
admin.site.register(Question, QuestionAdmin)
