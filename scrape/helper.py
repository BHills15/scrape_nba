import json
import urllib2

def get_data_from_url(url, index):
    response = urllib2.urlopen(url)
    data = json.loads(response.read())
    headers = data['resultSets'][index]['headers']
    rows = data['resultSets'][index]['rowSet']
    return [dict(zip(headers, row)) for row in rows]

def get_data_from_url_add_player_id(url, player_id, index):
    response = urllib2.urlopen(url)
    data = json.loads(response.read())
    headers = data['resultSets'][index]['headers']
    headers = ["PLAYER_ID"] + headers
    rows = data['resultSets'][index]['rowSet']
    return [dict(zip(headers, [player_id] + row)) for row in rows]

def get_data_from_url_add_game_id(url, game_id, index):
    response = urllib2.urlopen(url)
    data = json.loads(response.read())
    headers = data['resultSets'][index]['headers']
    headers = ["GAME_ID"] + headers
    rows = data['resultSets'][index]['rowSet']
    return [dict(zip(headers, [game_id] + row)) for row in rows]

def get_data_from_url_rename_columns(url, renamed_columns, index):
    response = urllib2.urlopen(url)
    data = json.loads(response.read())
    headers = data['resultSets'][index]['headers']
    for key in renamed_columns.keys():
        headers = [renamed_columns[key] if x==key else x for x in headers]
    rows = data['resultSets'][index]['rowSet']
    return [dict(zip(headers, row)) for row in rows]

def get_game_ids_for_date(date):
    # date format YYYY-MM-DD
    game_ids = []
    split = date.split("-")
    url = "http://stats.nba.com/stats/scoreboardV2?DayOffset=0&LeagueID=00&gameDate="+split[1]+"%2F"+split[2]+"%2F"+split[0]
    games = get_data_from_url(url, 1)
    for game in games:
        game_ids.append(game['GAME_ID'])
    return list(set(game_ids))
