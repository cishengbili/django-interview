# coding:utf-8




from django.db import models



class PlayerPoint(models.Model):
    """
    玩家评分表
    """

    # 客户端号
    client_number = models.CharField(max_length=50, unique=True)
    # 玩家评分
    point = models.IntegerField()
    # 更新时间
    update_time = models.DateField(auto_now=True)

    def __str__(self):
        return "%s:%s" % (self.client_number, self.point)

    class Meta:
        db_table =  "player_point"
