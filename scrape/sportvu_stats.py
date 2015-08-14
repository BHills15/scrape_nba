import json
import urllib2

import helper

class SportVuData:
    def __init__(self, season, season_type=""):
        # season type = "" for regular season, "Post" for playoffs
        self.touches_team_url = "http://stats.nba.com/js/data/sportvu/"+season+"/touchesTeamData"+season_type+".json"
        self.defense_team_url = "http://stats.nba.com/js/data/sportvu/"+season+"/defenseTeamData"+season_type+".json"
        self.drives_team_url = "http://stats.nba.com/js/data/sportvu/"+season+"/drivesTeamData"+season_type+".json"
        self.passing_team_url = "http://stats.nba.com/js/data/sportvu/"+season+"/passingTeamData"+season_type+".json"
        self.pull_up_shoot_team_url = "http://stats.nba.com/js/data/sportvu/"+season+"/pullUpShootTeamData"+season_type+".json"
        self.rebounding_team_url = "http://stats.nba.com/js/data/sportvu/"+season+"/reboundingTeamData"+season_type+".json"
        self.shooting_team_url = "http://stats.nba.com/js/data/sportvu/"+season+"/shootingTeamData"+season_type+".json"
        self.speed_team_url = "http://stats.nba.com/js/data/sportvu/"+season+"/speedTeamData"+season_type+".json"
        self.catch_shoot_team_url = "http://stats.nba.com/js/data/sportvu/"+season+"/catchShootTeamData"+season_type+".json"
        self.touches_url = "http://stats.nba.com/js/data/sportvu/"+season+"/touchesData"+season_type+".json"
        self.defense_url = "http://stats.nba.com/js/data/sportvu/"+season+"/defenseData"+season_type+".json"
        self.drives_url = "http://stats.nba.com/js/data/sportvu/"+season+"/drivesData"+season_type+".json"
        self.passing_url = "http://stats.nba.com/js/data/sportvu/"+season+"/passingData"+season_type+".json"
        self.pull_up_shoot_url = "http://stats.nba.com/js/data/sportvu/"+season+"/pullUpShootData"+season_type+".json"
        self.rebounding_url = "http://stats.nba.com/js/data/sportvu/"+season+"/reboundingData"+season_type+".json"
        self.shooting_url = "http://stats.nba.com/js/data/sportvu/"+season+"/shootingData"+season_type+".json"
        self.speed_url = "http://stats.nba.com/js/data/sportvu/"+season+"/speedData"+season_type+".json"
        self.catch_shoot_url = "http://stats.nba.com/js/data/sportvu/"+season+"/catchShootData"+season_type+".json"

    def touches_team(self):
        return helper.get_data_from_url(self.touches_team_url, 0)

    def defense_team(self):
        return helper.get_data_from_url(self.defense_team_url, 0)

    def drives_team(self):
        return helper.get_data_from_url(self.drives_team_url, 0)

    def passing_team(self):
        return helper.get_data_from_url(self.passing_team_url, 0)

    def pull_up_shoot_team(self):
        return helper.get_data_from_url(self.pull_up_shoot_team_url, 0)

    def rebounding_team(self):
        return helper.get_data_from_url(self.rebounding_team_url, 0)

    def shooting_team(self):
        return helper.get_data_from_url(self.shooting_team_url, 0)

    def speed_team(self):
        return helper.get_data_from_url(self.speed_team_url, 0)

    def catch_shoot_team(self):
        return helper.get_data_from_url(self.catch_shoot_team_url, 0)

    def touches(self):
        return helper.get_data_from_url(self.touches_url, 0)

    def defense(self):
        return helper.get_data_from_url(self.defense_url, 0)

    def drives(self):
        return helper.get_data_from_url(self.drives_url, 0)

    def passing(self):
        return helper.get_data_from_url(self.passing_url, 0)

    def pull_up_shoot(self):
        return helper.get_data_from_url(self.pull_up_shoot_url, 0)

    def rebounding(self):
        return helper.get_data_from_url(self.rebounding_url, 0)

    def shooting(self):
        return helper.get_data_from_url(self.shooting_url, 0)

    def speed(self):
        return helper.get_data_from_url(self.speed_url, 0)

    def catch_shoot(self):
        return helper.get_data_from_url(self.catch_shoot_url, 0)
