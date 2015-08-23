import pandas as pd

class ShotLogsPbp:
    def __init__(self, shot_log_data, pbp_data):
        self.shot_log_data = shot_log_data
        self.pbp_data = pbp_data

    def combine_pbp_and_shot_logs_for_player_for_period(self, player_id, period, game_id):
        # return player_id, game_id, shot_number, eventnum
        shot_log_event_num = []
        pbp_player_period = self.pbp_data[(self.pbp_data['PERIOD'] == period) & (self.pbp_data['PLAYER1_ID'] == player_id)]
        shot_logs_player_period = self.shot_log_data[(self.shot_log_data['PERIOD'] == period) & (self.shot_log_data['PLAYER_ID'] == player_id)]
        if len(pbp_player_period.index) == len(shot_logs_player_period.index):
            pbp_split = pbp_player_period['PCTIMESTRING'].str.split(":")
            pbp_player_period['seconds'] = pbp_split.map(lambda x: int(x[0])*60 + int(x[1]))

            shot_logs_split = shot_logs_player_period['GAME_CLOCK'].str.split(":")
            shot_logs_player_period['seconds'] = shot_logs_split.map(lambda x: int(x[0])*60 + int(x[1]))

            pbp_player_period = pbp_player_period.sort('seconds', ascending=False)
            shot_logs_player_period = shot_logs_player_period.sort('seconds', ascending=False)

            pbp_player_period = pbp_player_period.reset_index(drop=True)
            shot_logs_player_period = shot_logs_player_period.reset_index(drop=True)

            for i, row in shot_logs_player_period.iterrows():
                if abs(row['seconds'] - pbp_player_period['seconds'].iloc[i]) <= 5:
                    shot_log_event_num.append({"GAME_ID": game_id, "PLAYER_ID": player_id, "SHOT_NUMBER": row['SHOT_NUMBER'], "PBP_EVENTNUM": pbp_player_period['EVENTNUM'].iloc[i]})

        return shot_log_event_num
