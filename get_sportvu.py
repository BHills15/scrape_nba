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
        season_type = "Post"
    elif is_regular_season == 1:
        season_type = ""
    else:
        print "Invalid is_regular_season value. Use 0 for regular season, 1 for playoffs"

    db_storage = storage.db.Storage(config['host'], config['username'], config['password'], config['database'])

    try:
        sportvu_data = sportvu_stats.SportVuData(year, season_type)

        db_storage.insert_with_date_and_season_type(sportvu_data.touches(), "sportvu_touches", is_regular_season)
        db_storage.insert_with_date_and_season_type(sportvu_data.touches_team(), "sportvu_touches_team", is_regular_season)

        db_storage.insert_with_date_and_season_type(sportvu_data.speed(), "sportvu_speed", is_regular_season)
        db_storage.insert_with_date_and_season_type(sportvu_data.speed_team(), "sportvu_speed_team", is_regular_season)

        db_storage.insert_with_date_and_season_type(sportvu_data.shooting(), "sportvu_shooting", is_regular_season)
        db_storage.insert_with_date_and_season_type(sportvu_data.shooting_team(), "sportvu_shooting_team", is_regular_season)

        db_storage.insert_with_date_and_season_type(sportvu_data.rebounding(), "sportvu_rebounding", is_regular_season)
        db_storage.insert_with_date_and_season_type(sportvu_data.rebounding_team(), "sportvu_rebounding_team", is_regular_season)

        db_storage.insert_with_date_and_season_type(sportvu_data.pull_up_shoot(), "sportvu_pull_up_shoot", is_regular_season)
        db_storage.insert_with_date_and_season_type(sportvu_data.pull_up_shoot_team(), "sportvu_pull_up_shoot_team", is_regular_season)

        db_storage.insert_with_date_and_season_type(sportvu_data.passing(), "sportvu_passing", is_regular_season)
        db_storage.insert_with_date_and_season_type(sportvu_data.passing_team(), "sportvu_passing_team", is_regular_season)

        db_storage.insert_with_date_and_season_type(sportvu_data.drives(), "sportvu_drives", is_regular_season)
        db_storage.insert_with_date_and_season_type(sportvu_data.drives_team(), "sportvu_drives_team", is_regular_season)

        db_storage.insert_with_date_and_season_type(sportvu_data.defense(), "sportvu_defense", is_regular_season)
        db_storage.insert_with_date_and_season_type(sportvu_data.defense_team(), "sportvu_defense_team", is_regular_season)

        db_storage.insert_with_date_and_season_type(sportvu_data.catch_shoot(), "sportvu_catch_shoot", is_regular_season)
        db_storage.insert_with_date_and_season_type(sportvu_data.catch_shoot_team(), "sportvu_catch_shoot_team", is_regular_season)

        db_storage.commit()
    except:
        logging.error('sportvu not stored')
    db_storage.close()

if __name__ == '__main__':
    main()
