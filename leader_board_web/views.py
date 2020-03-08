# coding:utf-8





from django.shortcuts import render, redirect

from leader_board_web.models import PlayerPoint
from leader_board_web.forms import PlayerPointForm
from leader_board_web.shortcuts.ajax import ajax_success, ajax_error

def check_args(args):
    """
    检查参数
    """
    client_number = args.get("client_number")
    rank_start = args.get("rank_start")
    rank_end = args.get("rank_end")
    if not (client_number and rank_start and rank_end):
        return False
    try:
        rank_start = int(rank_start)
        rank_end = int(rank_end)
    except ValueError:
        return False
    return True

def push_point(request):
    """
    玩家终端上传分数, 可重复提交
    """
    if request.method != "GET":
        return ajax_error("请求方法不支持")
    data = request.GET
    client_number = data.get("client_number")
    point = data.get("point")
    form_data = {"client_number": client_number, "point": point}
    try: 
        player_point_obj = PlayerPoint.objects.get(client_number=client_number)
        form = PlayerPointForm(form_data, instance=player_point_obj)
    except PlayerPoint.DoesNotExist:
        form = PlayerPointForm(form_data)
    if form.is_valid():
        form.save()
        return ajax_success()
    print(form.errors)
    return ajax_error(form.errors)


def get_player_rank(request):
    """
    某个终端玩家查询排名区间的玩家信息
    """
    if request.method != "GET":
        return ajax_error("请求方法不支持")
    args = request.GET
    check_res = check_args(args)
    if not check_res:
        return ajax_error("请检查参数是否正确")
    client_number = args.get("client_number") 
    rank_start = int(args.get("rank_start"))
    rank_end = int(args.get("rank_end"))

    get_rank_data = PlayerPoint.objects.order_by('-point')[rank_start-1:rank_end]
    rank = []
    for player_point in get_rank_data:
        data = {
                "rank": rank_start,
                "client_number": player_point.client_number,
                "point": player_point.point
                }
        rank.append(data)
        rank_start = rank_start + 1
    try:
        request_player_point = PlayerPoint.objects.get(client_number=client_number)
        request_player_rank = PlayerPoint.objects.filter(point__gt=request_player_point.point).count()
        rank.append({"rank": request_player_rank + 1, 
                     "client_number": client_number, 
                     "point": request_player_point.point})
    except PlayerPoint.DoesNotExist:
        pass
    return ajax_success(rank)
