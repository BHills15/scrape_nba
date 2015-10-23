import json
import urllib2

import helper

def get_sportvu_data_for_stat(season, season_type, player_or_team, measure_type):
    url = "http://stats.nba.com/stats/leaguedashptstats?College=&Conference=&Country=&DateFrom=&DateTo=&Division=&DraftPick=&DraftYear=&GameScope=&Height=&LastNGames=0&LeagueID=00&Location=&Month=0&OpponentTeamID=0&Outcome=&PORound=0&PerMode=Totals&PlayerExperience=&PlayerOrTeam="+player_or_team+"&PlayerPosition=&PtMeasureType="+measure_type+"&Season="+season+"&SeasonSegment=&SeasonType="+season_type+"&StarterBench=&TeamID=0&VsConference=&VsDivision=&Weight="
    return helper.get_data_from_url(url, 0)
