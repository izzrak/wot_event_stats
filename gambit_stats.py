import urllib.request
import json

# define lists
rank_list = []
acc_list = []
clan_tag_list = []
clan_rank_stats = [0 for x in range(51)]

# calculate multiplier
multiplier_list = [1]
multiplier_list += [7]
multiplier_list += [6.5]
multiplier_list += [6] * 2
multiplier_list += [5.5] * 3
multiplier_list += [5] * 7
multiplier_list += [4] * 7
multiplier_list += [3] * 7
multiplier_list += [2.5] * 7
multiplier_list += [2] * 35
#print(len(multiplier_list))
#print(multiplier_list)

# set urls
clan_rank_url = 'https://api.worldoftanks.com/wot/globalmap/eventrating/?application_id=de8adc67ec8e5376d9bb0344b482c3e6&event_id=event_gambit&front_id=gambit&limit=60'
acc_rank_url = 'https://api.worldoftanks.com/wot/globalmap/eventaccountratings/?application_id=de8adc67ec8e5376d9bb0344b482c3e6&event_id=event_gambit&front_id=gambit&limit=100&page_no='

def get_player_rank(string):
  return int(string)

def get_clan_rank(rank):
  if rank == None:
    ret = 0
  elif rank < 70:
    ret = rank
  else:
    ret = 0 
  return ret

def get_bonds_num(rank):
  if rank <= 67:
    bonds = 1000
  elif rank <= 134:
  	bonds = 950
  elif rank <= 201:
  	bonds = 900
  elif rank <= 335:
  	bonds = 850
  elif rank <= 670:
  	bonds = 800
  elif rank <= 1005:
  	bonds = 750
  elif rank <= 1340:
  	bonds = 700
  elif rank <= 1675:
  	bonds = 600
  elif rank <= 3350:
  	bonds = 500
  else:
  	bonds = 250
  return bonds

data=urllib.request.urlopen(clan_rank_url)
clan_json = json.loads(data.read())
#print(clan_json)
clans = clan_json['data']
clan_tag_list.append('Others')
for clan in clans:
  clan_tag_list.append(clan['tag'])

#print(clan_tag_list)

# define free reward number
free_num = 0

for num in range(30):
  print(num)
  
  url = acc_rank_url + str(num+1)
  data=urllib.request.urlopen(url)
  acc_json = json.loads(data.read())
  #print(acc_json)
  players = acc_json['data']

  for player in players:
    #rank_list.append(player['rank'])
    #acc_list.append(player['account_id'])
    #clan_rank_list.append(player['clan_rank'])
    #print(player['rank'], player['account_id'], player['clan_rank'])
    #print(player['clan_rank'])
    clan_rank = get_clan_rank(player['clan_rank'])
    bonds_num = get_bonds_num(int(player['rank']))
    total_bonds = int(bonds_num * multiplier_list[clan_rank])
    if total_bonds >= 3000:
      free_num += 1
    #print(total_bonds)
print(free_num)
'''
    if player['clan_rank'] == None:
      idx = 51
    else:
      idx = int(player['clan_rank'])

    if idx <= 50:
      clan_rank_stats[idx] += 1
    else:
      clan_rank_stats[0] += 1

  print(clan_rank_stats)

for i in range(61):
  print(clan_tag_list[i], clan_rank_stats[i])
'''