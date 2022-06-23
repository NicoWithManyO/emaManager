
import random
from Tos.models import CurrentTos

def simple_tos(teams_list):
    for _ in teams_list:
        if not _.is_staff_validated:
            return False
    all_matchs = []
    set_teams_list = set(teams_list)
    print(set_teams_list)
    while len(set_teams_list) > 1:
        current_match = random.sample(set_teams_list, 2)
        all_matchs.append(current_match)
        for _ in current_match:
            set_teams_list.remove(_)
    if set_teams_list:
        o = list(set_teams_list)
        all_matchs.append(o)
    return all_matchs

def save_tos(matchs_list):
    for _ in matchs_list:
        print(_)
        if len(_) > 1:
            new_match = CurrentTos(roster=_[0].roster, for_round=_[0].registered_for_round, tournament=_[0].tournament, home=_[0], opponent=_[1])
            new_match.save()
        else:
            new_match = CurrentTos(roster=_[0].roster, for_round=_[0].registered_for_round, tournament=_[0].tournament, home=_[0])
            new_match.save()