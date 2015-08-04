import json
import urllib2

import helper

class SynergyData:
    def __init__(self):
        self.renamed_columns = {"FGm":"FG_m", "FGmG":"FG_mG", "PlayerIDSID":"PLAYER_ID", "TeamIDSID":"TEAM_ID"}
        self.transition_team_url = "http://stats.nba.com/js/data/playtype/team_Transition.js"
        self.transition_url = "http://stats.nba.com/js/data/playtype/player_Transition.js"
        self.isolation_team_url = "http://stats.nba.com/js/data/playtype/team_Isolation.js"
        self.isolation_url = "http://stats.nba.com/js/data/playtype/player_Isolation.js"
        self.pr_ball_handler_team_url = "http://stats.nba.com/js/data/playtype/team_PRBallHandler.js"
        self.pr_ball_handler_url = "http://stats.nba.com/js/data/playtype/player_PRBallHandler.js"
        self.pr_roll_man_team_url = "http://stats.nba.com/js/data/playtype/team_PRRollMan.js"
        self.pr_roll_man_url = "http://stats.nba.com/js/data/playtype/player_PRRollMan.js"
        self.post_up_team_url = "http://stats.nba.com/js/data/playtype/team_Postup.js"
        self.post_up_url = "http://stats.nba.com/js/data/playtype/player_Postup.js"
        self.spot_up_team_url = "http://stats.nba.com/js/data/playtype/team_Spotup.js"
        self.spot_up_url = "http://stats.nba.com/js/data/playtype/player_Spotup.js"
        self.handoff_team_url = "http://stats.nba.com/js/data/playtype/team_Handoff.js"
        self.handoff_url = "http://stats.nba.com/js/data/playtype/player_Handoff.js"
        self.cut_team_url = "http://stats.nba.com/js/data/playtype/team_Cut.js"
        self.cut_url = "http://stats.nba.com/js/data/playtype/player_Cut.js"
        self.off_screen_team_url = "http://stats.nba.com/js/data/playtype/team_OffScreen.js"
        self.off_screen_url = "http://stats.nba.com/js/data/playtype/player_OffScreen.js"
        self.put_back_team_url = "http://stats.nba.com/js/data/playtype/team_OffRebound.js"
        self.put_back_url = "http://stats.nba.com/js/data/playtype/player_OffRebound.js"
        self.misc_team_url = "http://stats.nba.com/js/data/playtype/team_Misc.js"
        self.misc_url = "http://stats.nba.com/js/data/playtype/player_Misc.js"

    def transition_team_offense(self):
        return helper.get_data_from_url_rename_columns(self.transition_team_url, self.renamed_columns, 0)

    def transition_team_defense(self):
        return helper.get_data_from_url_rename_columns(self.transition_team_url, self.renamed_columns, 1)

    def transition_offense(self):
        return helper.get_data_from_url_rename_columns(self.transition_url, self.renamed_columns, 0)

    def isolation_team_offense(self):
        return helper.get_data_from_url_rename_columns(self.isolation_team_url, self.renamed_columns, 0)

    def isolation_team_defense(self):
        return helper.get_data_from_url_rename_columns(self.isolation_team_url, self.renamed_columns, 1)

    def isolation_offense(self):
        return helper.get_data_from_url_rename_columns(self.isolation_url, self.renamed_columns, 0)

    def isolation_defense(self):
        return helper.get_data_from_url_rename_columns(self.isolation_url, self.renamed_columns, 1)

    def pr_ball_handler_team_offense(self):
        return helper.get_data_from_url_rename_columns(self.pr_ball_handler_team_url, self.renamed_columns, 0)

    def pr_ball_handler_team_defense(self):
        return helper.get_data_from_url_rename_columns(self.pr_ball_handler_team_url, self.renamed_columns, 1)

    def pr_ball_handler_offense(self):
        return helper.get_data_from_url_rename_columns(self.pr_ball_handler_url, self.renamed_columns, 0)

    def pr_ball_handler_defense(self):
        return helper.get_data_from_url_rename_columns(self.pr_ball_handler_url, self.renamed_columns, 1)

    def pr_roll_man_team_offense(self):
        return helper.get_data_from_url_rename_columns(self.pr_roll_man_team_url, self.renamed_columns, 0)

    def pr_roll_man_team_defense(self):
        return helper.get_data_from_url_rename_columns(self.pr_roll_man_team_url, self.renamed_columns, 1)

    def pr_roll_man_offense(self):
        return helper.get_data_from_url_rename_columns(self.pr_roll_man_url, self.renamed_columns, 0)

    def pr_roll_man_defense(self):
        return helper.get_data_from_url_rename_columns(self.pr_roll_man_url, self.renamed_columns, 1)

    def post_up_team_offense(self):
        return helper.get_data_from_url_rename_columns(self.post_up_team_url, self.renamed_columns, 0)

    def post_up_team_defense(self):
        return helper.get_data_from_url_rename_columns(self.post_up_team_url, self.renamed_columns, 1)

    def post_up_offense(self):
        return helper.get_data_from_url_rename_columns(self.post_up_url, self.renamed_columns, 0)

    def post_up_defense(self):
        return helper.get_data_from_url_rename_columns(self.post_up_url, self.renamed_columns, 1)

    def spot_up_team_offense(self):
        return helper.get_data_from_url_rename_columns(self.spot_up_team_url, self.renamed_columns, 0)

    def spot_up_team_defense(self):
        return helper.get_data_from_url_rename_columns(self.spot_up_team_url, self.renamed_columns, 1)

    def spot_up_offense(self):
        return helper.get_data_from_url_rename_columns(self.spot_up_url, self.renamed_columns, 0)

    def spot_up_defense(self):
        return helper.get_data_from_url_rename_columns(self.spot_up_url, self.renamed_columns, 1)

    def handoff_team_offense(self):
        return helper.get_data_from_url_rename_columns(self.handoff_team_url, self.renamed_columns, 0)

    def handoff_team_defense(self):
        return helper.get_data_from_url_rename_columns(self.handoff_team_url, self.renamed_columns, 1)

    def handoff_offense(self):
        return helper.get_data_from_url_rename_columns(self.handoff_url, self.renamed_columns, 0)

    def handoff_defense(self):
        return helper.get_data_from_url_rename_columns(self.handoff_url, self.renamed_columns, 1)

    def cut_team_offense(self):
        return helper.get_data_from_url_rename_columns(self.cut_team_url, self.renamed_columns, 0)

    def cut_team_defense(self):
        return helper.get_data_from_url_rename_columns(self.cut_team_url, self.renamed_columns, 1)

    def cut_offense(self):
        return helper.get_data_from_url_rename_columns(self.cut_url, self.renamed_columns, 0)

    def off_screen_team_offense(self):
        return helper.get_data_from_url_rename_columns(self.off_screen_team_url, self.renamed_columns, 0)

    def off_screen_team_defense(self):
        return helper.get_data_from_url_rename_columns(self.off_screen_team_url, self.renamed_columns, 1)

    def off_screen_offense(self):
        return helper.get_data_from_url_rename_columns(self.off_screen_url, self.renamed_columns, 0)

    def off_screen_defense(self):
        return helper.get_data_from_url_rename_columns(self.off_screen_url, self.renamed_columns, 1)

    def put_back_team_offense(self):
        return helper.get_data_from_url_rename_columns(self.put_back_team_url, self.renamed_columns, 0)

    def put_back_team_defense(self):
        return helper.get_data_from_url_rename_columns(self.put_back_team_url, self.renamed_columns, 1)

    def put_back_offense(self):
        return helper.get_data_from_url_rename_columns(self.put_back_url, self.renamed_columns, 0)

    def misc_team_offense(self):
        return helper.get_data_from_url_rename_columns(self.misc_team_url, self.renamed_columns, 0)

    def misc_team_defense(self):
        return helper.get_data_from_url_rename_columns(self.misc_team_url, self.renamed_columns, 1)

    def misc_offense(self):
        return helper.get_data_from_url_rename_columns(self.misc_url, self.renamed_columns, 0)
