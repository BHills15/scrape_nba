import json
import urllib2

import helper

def get_sportvu_data_for_stat(season, season_type, player_or_team, measure_type, start_date="", end_date=""):
    url = "http://stats.nba.com/stats/leaguedashptstats?College=&Conference=&Country=&DateFrom="+start_date+"&DateTo="+end_date+"&Division=&DraftPick=&DraftYear=&GameScope=&Height=&LastNGames=0&LeagueID=00&Location=&Month=0&OpponentTeamID=0&Outcome=&PORound=0&PerMode=Totals&PlayerExperience=&PlayerOrTeam="+player_or_team+"&PlayerPosition=&PtMeasureType="+measure_type+"&Season="+season+"&SeasonSegment=&SeasonType="+season_type+"&StarterBench=&TeamID=0&VsConference=&VsDivision=&Weight="
    return helper.get_data_from_url(url, 0)

def add_game_id_to_game_log_for_player(daily_data, date, storage, player_game_map):
    games = storage.query('select GAME_ID from game_summary where GAME_DATE_EST = "' + date + 'T00:00:00"')
    to_return = []
    for row in daily_data:
        player_id = str(row["PLAYER_ID"])
        for game in games:
            game_id = game[0]
            if game_id in player_game_map[player_id].keys():
                row["GAME_ID"] = game_id
                row["TEAM_ID"] = player_game_map[player_id][game_id]
                to_return.append(row)
                break
    return to_return

def add_game_id_to_game_log_for_team(daily_data, date, storage, team_game_map):
    games = storage.query('select GAME_ID from game_summary where GAME_DATE_EST = "' + date + 'T00:00:00"')
    to_return = []
    for row in daily_data:
        team_id = str(row["TEAM_ID"])
        for game in games:
            game_id = game[0]
            if game_id in team_game_map[team_id].keys():
                row["GAME_ID"] = game_id
                to_return.append(row)
                break
    return to_return
