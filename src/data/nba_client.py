from nba_api.stats.static import players
from nba_api.stats.endpoints import playergamelog

# playerfullname has space between first and last name
# CANNOT BE MISSPELLED!
# gets id for player
def get_id(PlayerFullName):
    playerdict = players.find_players_by_full_name(PlayerFullName)
    return playerdict[0]['id']
# print(get_id('LeBron James')) --> test


# gets stats for player
# season MUST be informat 20XX - XX
def get_stats(PlayerFullName, season):
   gamelog = playergamelog.PlayerGameLog(season, player_id = get_id(PlayerFullName))
   # convert to data frame
   df_gamelog = gamelog.get_data_frames()[0]
   df_gamelog = df_gamelog.iloc[:10]
   last_twenty_player_betting_stats = df_gamelog[['PTS', 'REB', 'AST', 'STL', 'BLK', 'FG3M', 'TOV']]
   return last_twenty_player_betting_stats


# function wrapper
def stat_information(PlayerFullName, season, stat_category):
# standardize stat category
    stat_category = stat_category.lower()
    stat_category = stat_category.replace(' ', '')
    if stat_category == 'points':
        return get_stats(PlayerFullName, season)['PTS'].tolist()
    elif stat_category == 'rebounds':
        return get_stats(PlayerFullName, season)['REB'].tolist()
    elif stat_category == 'assists':
        return get_stats(PlayerFullName, season)['AST'].tolist()
    elif stat_category == 'steals':
        return get_stats(PlayerFullName, season)['STL'].tolist()
    elif stat_category == 'blocks':
        return get_stats(PlayerFullName, season)['BLK'].tolist()
    elif stat_category == 'threes':
        return get_stats(PlayerFullName, season)['FG3M'].tolist()
    elif stat_category == 'turnovers':
        return get_stats(PlayerFullName, season)['TOV'].tolist()
    else:
        raise ValueError('Only categories are points, rebounds, assists, steals, block, threes, or turnovers. Please try again.')