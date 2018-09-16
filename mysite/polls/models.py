from django.db import models

# Create your models here.


# 创建数据模型：投票的问题
# 每个类必须继承自models.Model
class Question(models.Model):
    # 创建问题的内容
    # 每个属性的类型必须是models.xxxField()
    # 其中models.CharField类型必须使用max_length参数指明长度
    question_text = models.CharField(max_length=200)
    # 创建发布日期
    # models.DateTimeField是日期类型
    pub_date = models.DateTimeField('date published')

    # 当对象作为字符串时返回问题的文本内容
    def __str__(self):
        return self.question_text


# 创建数据模型：投票的选项和相应的票数
class Choice(models.Model):
    # models.ForeignKey()方法创建外键，关联Queston
    # on_delete = models.CASCADE设置同步删除
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    # 创建选项的内容
    choice_text = models.CharField(max_length=200)
    # 创建票数，default设置默认值
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text
