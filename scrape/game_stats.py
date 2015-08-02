import json
import urllib2
import pandas as pd

class GameData:
    def __init__(self, game_id):
        self.game_id = game_id
        self.pbp_url = "http://stats.nba.com/stats/playbyplayv2?EndPeriod=10&EndRange=55800&GameID=" + game_id + "&RangeType=2&Season=2014-15&SeasonType=Regular+Season&StartPeriod=1&StartRange=0"
        self.pbp_response = urllib2.urlopen(self.pbp_url)
        self.pbp_data = json.loads(self.pbp_response.read())

        self.player_tracking_boxscore_url = "http://stats.nba.com/stats/boxscoreplayertrackv2?GameId="+game_id
        self.player_tracking_boxscore_response = urllib2.urlopen(self.player_tracking_boxscore_url)
        self.player_tracking_boxscore_data = json.loads(self.player_tracking_boxscore_response.read())

        self.teams = [self.player_tracking_boxscore_team()[0]['TEAM_ID'], self.player_tracking_boxscore_team()[1]['TEAM_ID']]

    def pbp(self):
        headers = self.pbp_data['resultSets'][0]['headers']
        rows = self.pbp_data['resultSets'][0]['rowSet']
        return [dict(zip(headers, row)) for row in rows]

    def player_tracking_boxscore(self):
        headers = self.player_tracking_boxscore_data['resultSets'][0]['headers']
        rows = self.player_tracking_boxscore_data['resultSets'][0]['rowSet']
        return [dict(zip(headers, row)) for row in rows]

    def player_tracking_boxscore_team(self):
        headers = self.player_tracking_boxscore_data['resultSets'][1]['headers']
        rows = self.player_tracking_boxscore_data['resultSets'][1]['rowSet']
        return [dict(zip(headers, row)) for row in rows]


    def shots(self):
        shots = []
        for team in self.teams:
            shots_url = "http://stats.nba.com/stats/shotchartdetail?Season=2014-15&SeasonType=Regular+Season&LeagueID=00&TeamID="+str(team)+"&PlayerID=0&GameID="+self.game_id+"&Outcome=&Location=&Month=0&SeasonSegment=&DateFrom=&DateTo=&OpponentTeamID=0&VsConference=&VsDivision=&Position=&RookieYear=&GameSegment=&Period=0&LastNGames=0&ContextFilter=&ContextMeasure=FG_PCT&display-mode=performance&zone-mode=zone&zoneOverlays=false&zoneDetails=false&viewShots=true"
            shots_response = urllib2.urlopen(shots_url)
            shots_data = json.loads(shots_response.read())
            headers = shots_data['resultSets'][0]['headers']
            rows = shots_data['resultSets'][0]['rowSet']
            shots += [dict(zip(headers, row)) for row in rows]
        return shots
