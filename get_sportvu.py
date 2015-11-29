import json
import logging
import sys
import re

from scrape import sportvu_stats
import storage.db

def main():
    logging.basicConfig(filename='sportvu.log',level=logging.DEBUG, format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
    config=json.loads(open('config.json').read())

    season = config["season"]
    is_regular_season = config["is_regular_season"]
    # make sure season is valid format
    season_pattern = re.compile('\d{4}[-]\d{2}$')
    if season_pattern.match(season) == None:
        print "Invalid Season format. Example format: 2014-15"
        sys.exit(0)
    year = season.split("-")[0]

    if is_regular_season == 0:
        season_type = "Playoffs"
    elif is_regular_season == 1:
        season_type = "Regular Season"
    else:
        print "Invalid is_regular_season value. Use 0 for regular season, 1 for playoffs"

    db_storage = storage.db.Storage(config['host'], config['username'], config['password'], config['database'])

    try:
        db_storage.insert_with_date_and_season_type(sportvu_stats.get_sportvu_data_for_stat(season, season_type, "Player", "CatchShoot"), "sportvu_catch_shoot", is_regular_season)
        db_storage.insert_with_date_and_season_type(sportvu_stats.get_sportvu_data_for_stat(season, season_type, "Team", "CatchShoot"), "sportvu_catch_shoot_team", is_regular_season)

        db_storage.insert_with_date_and_season_type(sportvu_stats.get_sportvu_data_for_stat(season, season_type, "Player", "Defense"), "sportvu_defense", is_regular_season)
        db_storage.insert_with_date_and_season_type(sportvu_stats.get_sportvu_data_for_stat(season, season_type, "Team", "Defense"), "sportvu_defense_team", is_regular_season)

        db_storage.insert_with_date_and_season_type(sportvu_stats.get_sportvu_data_for_stat(season, season_type, "Player", "Drives"), "sportvu_drives", is_regular_season)
        db_storage.insert_with_date_and_season_type(sportvu_stats.get_sportvu_data_for_stat(season, season_type, "Team", "Drives"), "sportvu_drives_team", is_regular_season)

        db_storage.insert_with_date_and_season_type(sportvu_stats.get_sportvu_data_for_stat(season, season_type, "Player", "Passing"), "sportvu_passing", is_regular_season)
        db_storage.insert_with_date_and_season_type(sportvu_stats.get_sportvu_data_for_stat(season, season_type, "Team", "Passing"), "sportvu_passing_team", is_regular_season)

        db_storage.insert_with_date_and_season_type(sportvu_stats.get_sportvu_data_for_stat(season, season_type, "Player", "PullUpShot"), "sportvu_pull_up_shoot", is_regular_season)
        db_storage.insert_with_date_and_season_type(sportvu_stats.get_sportvu_data_for_stat(season, season_type, "Team", "PullUpShot"), "sportvu_pull_up_shoot_team", is_regular_season)

        db_storage.insert_with_date_and_season_type(sportvu_stats.get_sportvu_data_for_stat(season, season_type, "Player", "Rebounding"), "sportvu_rebounding", is_regular_season)
        db_storage.insert_with_date_and_season_type(sportvu_stats.get_sportvu_data_for_stat(season, season_type, "Team", "Rebounding"), "sportvu_rebounding_team", is_regular_season)

        db_storage.insert_with_date_and_season_type(sportvu_stats.get_sportvu_data_for_stat(season, season_type, "Player", "Efficiency"), "sportvu_shooting", is_regular_season)
        db_storage.insert_with_date_and_season_type(sportvu_stats.get_sportvu_data_for_stat(season, season_type, "Team", "Efficiency"), "sportvu_shooting_team", is_regular_season)

        db_storage.insert_with_date_and_season_type(sportvu_stats.get_sportvu_data_for_stat(season, season_type, "Player", "SpeedDistance"), "sportvu_speed", is_regular_season)
        db_storage.insert_with_date_and_season_type(sportvu_stats.get_sportvu_data_for_stat(season, season_type, "Team", "SpeedDistance"), "sportvu_speed_team", is_regular_season)

        db_storage.insert_with_date_and_season_type(sportvu_stats.get_sportvu_data_for_stat(season, season_type, "Player", "ElbowTouch"), "sportvu_elbow_touches", is_regular_season)
        db_storage.insert_with_date_and_season_type(sportvu_stats.get_sportvu_data_for_stat(season, season_type, "Team", "ElbowTouch"), "sportvu_elbow_touches_team", is_regular_season)

        db_storage.insert_with_date_and_season_type(sportvu_stats.get_sportvu_data_for_stat(season, season_type, "Player", "PostTouch"), "sportvu_post_touches", is_regular_season)
        db_storage.insert_with_date_and_season_type(sportvu_stats.get_sportvu_data_for_stat(season, season_type, "Team", "PostTouch"), "sportvu_post_touches_team", is_regular_season)

        db_storage.insert_with_date_and_season_type(sportvu_stats.get_sportvu_data_for_stat(season, season_type, "Player", "PaintTouch"), "sportvu_paint_touches", is_regular_season)
        db_storage.insert_with_date_and_season_type(sportvu_stats.get_sportvu_data_for_stat(season, season_type, "Team", "PaintTouch"), "sportvu_paint_touches_team", is_regular_season)

        db_storage.insert_with_date_and_season_type(sportvu_stats.get_sportvu_data_for_stat(season, season_type, "Player", "Possessions"), "sportvu_possessions", is_regular_season)
        db_storage.insert_with_date_and_season_type(sportvu_stats.get_sportvu_data_for_stat(season, season_type, "Team", "Possessions"), "sportvu_possessions_team", is_regular_season)

        db_storage.commit()
    except:
        logging.error('sportvu not stored')
    db_storage.close()

if __name__ == '__main__':
    main()
