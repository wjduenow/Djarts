from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import *
# Create your views here.




   
def index(request):
    return HttpResponse("Hello, world. You're at the Djart index.")
    




    # context = ({'gym_slots_today': gym_slots_today, 'gym_slots_other': gym_slots_other, 'active_games': active_games, 
    #             'active_sessions': active_sessions, 'ps_win_ratio': ps_win_ratio, 'ps_point_differential': ps_point_differential, 
    #             'best_tandem_point_differential': best_tandem_point_differential, 'best_tandem_win_ratio': best_tandem_win_ratio, 
    #             'ps_win_ratio_bad': ps_win_ratio_bad, 'ps_point_differential_bad': ps_point_differential_bad, 
    #             'best_tandem_point_differential_bad': best_tandem_point_differential_bad,
    #             'best_tandem_win_ratio_bad': best_tandem_win_ratio_bad,
    #             'best_opponent_point_differential':best_opponent_point_differential,
    #             'best_opponent_win_ratio':best_opponent_win_ratio,
    #             'best_opponent_point_differential_bad':best_opponent_point_differential_bad,
    #             'best_opponent_win_ratio_bad':best_opponent_win_ratio_bad,
    #             'score_lifters':score_lifters,
    #             'score_draggers':score_draggers,
    #             'win_lifters':win_lifters,
    #             'win_draggers':win_draggers})

    # return HttpResponse(template.render(context, request))

