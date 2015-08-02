import json
import urllib2

class GameData:
    def __init__(self, game_id):
        self.game_id = game_id
        
        self.pbp_url = "http://stats.nba.com/stats/playbyplayv2?EndPeriod=10&EndRange=55800&GameID=" + game_id + "&RangeType=2&Season=2014-15&SeasonType=Regular+Season&StartPeriod=1&StartRange=0"
        self.pbp_response = urllib2.urlopen(self.pbp_url)
        self.pbp_data = json.loads(self.pbp_response.read())

        self.player_tracking_boxscore_url = "http://stats.nba.com/stats/boxscoreplayertrackv2?GameId="+game_id
        self.player_tracking_boxscore_response = urllib2.urlopen(self.player_tracking_boxscore_url)
        self.player_tracking_boxscore_data = json.loads(self.player_tracking_boxscore_response.read())

        self.traditional_boxscore_url = "http://stats.nba.com/stats/boxscoretraditionalv2?GameId="+game_id+"&StartPeriod=0&EndPeriod=10&RangeType=2&StartRange=0&EndRange=55800"
        self.traditional_boxscore_response = urllib2.urlopen(self.traditional_boxscore_url)
        self.traditional_boxscore_data = json.loads(self.traditional_boxscore_response.read())

        self.advanced_boxscore_url = "http://stats.nba.com/stats/boxscoreadvancedv2?GameId="+game_id+"&StartPeriod=0&EndPeriod=10&RangeType=2&StartRange=0&EndRange=55800"
        self.advanced_boxscore_response = urllib2.urlopen(self.advanced_boxscore_url)
        self.advanced_boxscore_data = json.loads(self.advanced_boxscore_response.read())

        self.scoring_boxscore_url = "http://stats.nba.com/stats/boxscorescoringv2?GameId="+game_id+"&StartPeriod=0&EndPeriod=10&RangeType=2&StartRange=0&EndRange=55800"
        self.scoring_boxscore_response = urllib2.urlopen(self.scoring_boxscore_url)
        self.scoring_boxscore_data = json.loads(self.scoring_boxscore_response.read())

        self.misc_boxscore_url = "http://stats.nba.com/stats/boxscoremiscv2?GameId="+game_id+"&StartPeriod=0&EndPeriod=10&RangeType=2&StartRange=0&EndRange=55800"
        self.misc_boxscore_response = urllib2.urlopen(self.misc_boxscore_url)
        self.misc_boxscore_data = json.loads(self.misc_boxscore_response.read())

        self.usage_boxscore_url = "http://stats.nba.com/stats/boxscoreusagev2?GameId="+game_id+"&StartPeriod=0&EndPeriod=10&RangeType=2&StartRange=0&EndRange=55800"
        self.usage_boxscore_response = urllib2.urlopen(self.usage_boxscore_url)
        self.usage_boxscore_data = json.loads(self.usage_boxscore_response.read())

        self.four_factors_boxscore_url = "http://stats.nba.com/stats/boxscorefourfactorsv2?GameId="+game_id+"&StartPeriod=0&EndPeriod=10&RangeType=2&StartRange=0&EndRange=55800"
        self.four_factors_boxscore_response = urllib2.urlopen(self.four_factors_boxscore_url)
        self.four_factors_boxscore_data = json.loads(self.four_factors_boxscore_response.read())

        self.teams = [self.player_tracking_boxscore_team()[0]['TEAM_ID'], self.player_tracking_boxscore_team()[1]['TEAM_ID']]

    def pbp(self):
        headers = self.pbp_data['resultSets'][0]['headers']
        rows = self.pbp_data['resultSets'][0]['rowSet']
        return [dict(zip(headers, row)) for row in rows]

    def shots(self):
        game_shots = []
        for team in self.teams:
            shots_url = "http://stats.nba.com/stats/shotchartdetail?Season=2014-15&SeasonType=Regular+Season&LeagueID=00&TeamID="+str(team)+"&PlayerID=0&GameID="+self.game_id+"&Outcome=&Location=&Month=0&SeasonSegment=&DateFrom=&DateTo=&OpponentTeamID=0&VsConference=&VsDivision=&Position=&RookieYear=&GameSegment=&Period=0&LastNGames=0&ContextFilter=&ContextMeasure=FG_PCT&display-mode=performance&zone-mode=zone&zoneOverlays=false&zoneDetails=false&viewShots=true"
            shots_response = urllib2.urlopen(shots_url)
            shots_data = json.loads(shots_response.read())
            headers = shots_data['resultSets'][0]['headers']
            rows = shots_data['resultSets'][0]['rowSet']
            game_shots += [dict(zip(headers, row)) for row in rows]
        return game_shots

    def player_tracking_boxscore(self):
        headers = self.player_tracking_boxscore_data['resultSets'][0]['headers']
        rows = self.player_tracking_boxscore_data['resultSets'][0]['rowSet']
        return [dict(zip(headers, row)) for row in rows]

    def player_tracking_boxscore_team(self):
        headers = self.player_tracking_boxscore_data['resultSets'][1]['headers']
        rows = self.player_tracking_boxscore_data['resultSets'][1]['rowSet']
        return [dict(zip(headers, row)) for row in rows]

    def traditional_boxscore(self):
        headers = self.traditional_boxscore_data['resultSets'][0]['headers']
        rows = self.traditional_boxscore_data['resultSets'][0]['rowSet']
        return [dict(zip(headers, row)) for row in rows]

    def traditional_boxscore_team(self):
        headers = self.traditional_boxscore_data['resultSets'][1]['headers']
        rows = self.traditional_boxscore_data['resultSets'][1]['rowSet']
        return [dict(zip(headers, row)) for row in rows]

    def advanced_boxscore(self):
        headers = self.advanced_boxscore_data['resultSets'][0]['headers']
        rows = self.advanced_boxscore_data['resultSets'][0]['rowSet']
        return [dict(zip(headers, row)) for row in rows]

    def advanced_boxscore_team(self):
        headers = self.advanced_boxscore_data['resultSets'][1]['headers']
        rows = self.advanced_boxscore_data['resultSets'][1]['rowSet']
        return [dict(zip(headers, row)) for row in rows]

    def scoring_boxscore(self):
        headers = self.scoring_boxscore_data['resultSets'][0]['headers']
        rows = self.scoring_boxscore_data['resultSets'][0]['rowSet']
        return [dict(zip(headers, row)) for row in rows]

    def scoring_boxscore_team(self):
        headers = self.scoring_boxscore_data['resultSets'][1]['headers']
        rows = self.scoring_boxscore_data['resultSets'][1]['rowSet']
        return [dict(zip(headers, row)) for row in rows]

    def misc_boxscore(self):
        headers = self.misc_boxscore_data['resultSets'][0]['headers']
        rows = self.misc_boxscore_data['resultSets'][0]['rowSet']
        return [dict(zip(headers, row)) for row in rows]

    def misc_boxscore_team(self):
        headers = self.misc_boxscore_data['resultSets'][1]['headers']
        rows = self.misc_boxscore_data['resultSets'][1]['rowSet']
        return [dict(zip(headers, row)) for row in rows]

    def usage_boxscore(self):
        headers = self.usage_boxscore_data['resultSets'][0]['headers']
        rows = self.usage_boxscore_data['resultSets'][0]['rowSet']
        return [dict(zip(headers, row)) for row in rows]

    def usage_boxscore_team(self):
        headers = self.usage_boxscore_data['resultSets'][1]['headers']
        rows = self.usage_boxscore_data['resultSets'][1]['rowSet']
        return [dict(zip(headers, row)) for row in rows]

    def four_factors_boxscore(self):
        headers = self.four_factors_boxscore_data['resultSets'][0]['headers']
        rows = self.four_factors_boxscore_data['resultSets'][0]['rowSet']
        return [dict(zip(headers, row)) for row in rows]

    def four_factors_boxscore_team(self):
        headers = self.four_factors_boxscore_data['resultSets'][1]['headers']
        rows = self.four_factors_boxscore_data['resultSets'][1]['rowSet']
        return [dict(zip(headers, row)) for row in rows]
