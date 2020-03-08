# coding:utf-8



import os


from django.conf.urls import patterns, include, url
from django.conf import settings



PROJECTROOT = os.path.dirname(os.path.abspath(__file__))

urlpatterns = patterns('leader_board_web.views',
    url(r'^push/point/$', "push_point"),
    url(r'^player/rank/$', "get_player_rank")

)
if settings.DEBUG: #在开发时使用django来返回静态文件
    urlpatterns += patterns(
        'django.views.static',
        url(r'^static/(?P<path>.*)$', 'serve', {'document_root': os.path.join(PROJECTROOT, 'static/')})
    )
