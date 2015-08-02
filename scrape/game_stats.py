import json
import urllib2
import pandas as pd

class GameData:
    def __init__(self, game_id):
        self.game_id = game_id
        self._pbp_url = "http://stats.nba.com/stats/playbyplayv2?EndPeriod=10&EndRange=55800&GameID=" + game_id + "&RangeType=2&Season=2014-15&SeasonType=Regular+Season&StartPeriod=1&StartRange=0"
        self._pbp_response = urllib2.urlopen(self._pbp_url)
        self._pbp_data = json.loads(self._pbp_response.read())

        self._player_tracking_boxscore_url = "http://stats.nba.com/stats/boxscoreplayertrackv2?GameId="+game_id
        self._player_tracking_boxscore_response = urllib2.urlopen(self._player_tracking_boxscore_url)
        self._player_tracking_boxscore_data = json.loads(self._player_tracking_boxscore_response.read())

        self._teams = [self.player_tracking_boxscore_team()[0]['TEAM_ID'], self.player_tracking_boxscore_team()[1]['TEAM_ID']]

    def pbp(self):
        _headers = self._pbp_data['resultSets'][0]['headers']
        _rows = self._pbp_data['resultSets'][0]['rowSet']
        return [dict(zip(_headers, row)) for row in _rows]

    def player_tracking_boxscore(self):
        _headers = self._player_tracking_boxscore_data['resultSets'][0]['headers']
        _rows = self._player_tracking_boxscore_data['resultSets'][0]['rowSet']
        return [dict(zip(_headers, row)) for row in _rows]

    def player_tracking_boxscore_team(self):
        _headers = self._player_tracking_boxscore_data['resultSets'][1]['headers']
        _rows = self._player_tracking_boxscore_data['resultSets'][1]['rowSet']
        return [dict(zip(_headers, row)) for row in _rows]


    def shots(self):
        _shots = []
        for team in self._teams:
            _shots_url = "http://stats.nba.com/stats/shotchartdetail?Season=2014-15&SeasonType=Regular+Season&LeagueID=00&TeamID="+str(team)+"&PlayerID=0&GameID="+self.game_id+"&Outcome=&Location=&Month=0&SeasonSegment=&DateFrom=&DateTo=&OpponentTeamID=0&VsConference=&VsDivision=&Position=&RookieYear=&GameSegment=&Period=0&LastNGames=0&ContextFilter=&ContextMeasure=FG_PCT&display-mode=performance&zone-mode=zone&zoneOverlays=false&zoneDetails=false&viewShots=true"
            _shots_response = urllib2.urlopen(_shots_url)
            _shots_data = json.loads(_shots_response.read())
            _headers = _shots_data['resultSets'][0]['headers']
            _rows = _shots_data['resultSets'][0]['rowSet']
            _shots += [dict(zip(_headers, row)) for row in _rows]
        return _shots
