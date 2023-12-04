import pandas as pd

data_df = pd.read_csv('2019_kbo_for_kaggle_v2.csv')

data_df_2015 = data_df[data_df['p_year'] == 2015]
data_df_2016 = data_df[data_df['p_year'] == 2016]
data_df_2017 = data_df[data_df['p_year'] == 2017]
data_df_2018 = data_df[data_df['p_year'] == 2018]

top_10_players_2015_hits = data_df_2015.sort_values(by='H', ascending=False).head(10)
top_10_players_2015_batting_average = data_df_2015.sort_values(by='avg', ascending=False).head(10)
top_10_players_2015_homerun = data_df_2015.sort_values(by='HR', ascending=False).head(10)
top_10_players_2015_on_base_percentage = data_df_2015.sort_values(by='OBP', ascending=False).head(10)

top_10_players_2016_hits = data_df_2016.sort_values(by='H', ascending=False).head(10)
top_10_players_2016_batting_average = data_df_2016.sort_values(by='avg', ascending=False).head(10)
top_10_players_2016_homerun = data_df_2016.sort_values(by='HR', ascending=False).head(10)
top_10_players_2016_on_base_percentage = data_df_2016.sort_values(by='OBP', ascending=False).head(10)

top_10_players_2017_hits = data_df_2017.sort_values(by='H', ascending=False).head(10)
top_10_players_2017_batting_average = data_df_2017.sort_values(by='avg', ascending=False).head(10)
top_10_players_2017_homerun = data_df_2017.sort_values(by='HR', ascending=False).head(10)
top_10_players_2017_on_base_percentage = data_df_2017.sort_values(by='OBP', ascending=False).head(10)

top_10_players_2018_hits = data_df_2018.sort_values(by='H', ascending=False).head(10)
top_10_players_2018_batting_average = data_df_2018.sort_values(by='avg', ascending=False).head(10)
top_10_players_2018_homerun = data_df_2018.sort_values(by='HR', ascending=False).head(10)
top_10_players_2018_on_base_percentage = data_df_2018.sort_values(by='OBP', ascending=False).head(10)

print('2015 top 10 players in hits')
print(top_10_players_2015_hits['batter_name'])

print('2015 top 10 players in batting average')
print(top_10_players_2015_batting_average['batter_name'])

print('2015 top 10 players in homerun')
print(top_10_players_2015_homerun['batter_name'])

print('2015 top 10 players in on-base percentage')
print(top_10_players_2015_on_base_percentage['batter_name'])

print('2016 top 10 players in hits')
print(top_10_players_2016_hits['batter_name'])

print('2016 top 10 players in batting average')
print(top_10_players_2016_batting_average['batter_name'])

print('2016 top 10 players in homerun')
print(top_10_players_2016_homerun['batter_name'])

print('2016 top 10 players in on-base percentage')
print(top_10_players_2016_on_base_percentage['batter_name'])

print('2017 top 10 players in hits')
print(top_10_players_2017_hits['batter_name'])

print('2017 top 10 players in batting average')
print(top_10_players_2017_batting_average['batter_name'])

print('2017 top 10 players in homerun')
print(top_10_players_2017_homerun['batter_name'])

print('2017 top 10 players in on-base percentage')
print(top_10_players_2017_on_base_percentage['batter_name'])

print('2018 top 10 players in hits')
print(top_10_players_2018_hits['batter_name'])

print('2018 top 10 players in batting average')
print(top_10_players_2018_batting_average['batter_name'])

print('2018 top 10 players in homerun')
print(top_10_players_2018_homerun['batter_name'])

print('2018 top 10 players in on-base percentage')
print(top_10_players_2018_on_base_percentage['batter_name'])

positions = ['포수', '1루수', '2루수', '3루수', '유격수', '좌익수', '중견수', '우익수']
highest_war_players = {}

for position in positions:
    position_data = data_df_2018[data_df_2018['cp'] == position]
    highest_war_player = position_data.loc[position_data['war'].idxmax()]
    highest_war_players[position] = highest_war_player['batter_name']

print('the player with the highest war by position in 2018')
for position, player in highest_war_players.items():
    print(f'{position}: {player}')

selected_columns = ['R', 'H', 'HR', 'RBI', 'SB', 'war', 'avg', 'OBP', 'SLG', 'salary']
selected_data = data_df[selected_columns]
correlation_matrix = selected_data.corr()
correlation_with_salary = correlation_matrix['salary']
highest_correlation = correlation_with_salary.abs().nlargest(2).index[1]
print(f'the highest correlation with salary: {highest_correlation}')
