# Takes two arguments, start date and end date. Date format YYYY-MM-DD. If no dates entered gets yesterday
import json
import sys
import datetime
from dateutil.rrule import rrule, DAILY
import logging
import re

from process import pbp
import storage.db
import scrape.helper

def main():
    if len(sys.argv) < 3:
        start_date = datetime.date.today() - datetime.timedelta(1)
        end_date = datetime.date.today() - datetime.timedelta(1)
    elif len(sys.argv) > 3:
        print "Too many arguments. Enter a start and end date with format YYYY-MM-DD"
        sys.exit(0)
    else:
        start = sys.argv[1]
        end = sys.argv[2]
        # validate dates
        try:
            datetime.datetime.strptime(start, '%Y-%m-%d')
        except:
            print 'invalid format for start date'
            sys.exit(0)

        try:
            datetime.datetime.strptime(end, '%Y-%m-%d')
        except:
            print 'invalid format for end date'
            sys.exit(0)

        start_split = start.split("-")
        end_split = end.split("-")

        start_date = datetime.date(int(start_split[0]), int(start_split[1]), int(start_split[2]))
        end_date = datetime.date(int(end_split[0]), int(end_split[1]), int(end_split[2]))

    logging.basicConfig(filename='games.log',level=logging.DEBUG, format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
    config=json.loads(open('config.json').read())

    season = config["season"]
    # make sure season is valid format
    season_pattern = re.compile('\d{4}[-]\d{2}$')
    if season_pattern.match(season) == None:
        print "Invalid Season format. Example format: 2014-15"
        sys.exit(0)

    db_storage = storage.db.Storage(config['host'], config['username'], config['password'], config['database'])

    for dt in rrule(DAILY, dtstart=start_date, until=end_date):
        games = scrape.helper.get_game_ids_for_date(dt.strftime("%Y-%m-%d"))
        for game_id in games:
            if game_id[:3] == "002" or game_id[:3] == "004":
                try:
                    query = "select * from pbp where GAME_ID = '"+game_id+"'"
                    pbp_data = db_storage.query_df(query)

                    game_data = pbp.Lineups(pbp_data)
                    pbp_with_lineups =  game_data.get_players_on_floor_for_game()
                    db_storage.insert(pbp_with_lineups, "pbp")

                    db_storage.commit()
                except:
                    logging.error('game %s not stored', game_id)

    db_storage.close()

if __name__ == '__main__':
    main()
