import numpy as np
import pandas as pd

from nba_api.stats.static import teams
# get_teams returns a list of 30 dictionaries, each an NBA team.
nba_teams = teams.get_teams()
print('Number of teams fetched: {}'.format(len(nba_teams)))
mavs = [team for team in nba_teams
         if team['full_name'] == 'Dallas Mavericks'][0]

from nba_api.stats.endpoints import teamyearbyyearstats
mavs_yby_stats = teamyearbyyearstats.TeamYearByYearStats(team_id=mavs['id']).get_data_frames()[0]
reg_season_df = pd.DataFrame(columns=mavs_yby_stats)

for team in nba_teams :
    lockout_year_index = mavs_yby_stats[mavs_yby_stats['YEAR'] == '2011-12'].index.values[0]
    mavs_yby_stats = mavs_yby_stats[(mavs_yby_stats.index > lockout_year_index) & (mavs_yby_stats['GP'] > 69)]