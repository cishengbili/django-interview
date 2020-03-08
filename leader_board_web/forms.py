# coding:utf-8


from django import forms
from django.forms import ValidationError

from leader_board_web.models import PlayerPoint



class PlayerPointForm(forms.ModelForm):

    class Meta:
        model = PlayerPoint
        exclude = ("update_time",)
    
    def clean_point(self):
        """
        验证分数是否符合要求
        """
        point = self.cleaned_data.get("point")
        try:
            point = int(point)
            if not 1 <= point <= 10000000:
                raise ValidationError("point大小范围为1-10000000")
        except ValueError:
            raise ValidationError("point必须为整型")
        return point
