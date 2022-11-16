import challonge

def API(Name, API, ID):
    challonge.set_credentials(Name, API)
    tournament = challonge.tournaments.show(ID)
    matches = challonge.matches.index(tournament['id'])
    participants = challonge.participants.index(tournament['id'])
    i = 0
    matchCardId = {}
    matchCardname = {}
    for game in matches:
        if game['state'] == 'open':

            for playerName in participants:
                if playerName['id'] == game['player1_id']:
                    player1_name = playerName['name']
                elif playerName['id'] == game['player2_id']:
                    player2_name = playerName['name']
                    
            player_id = {'identifier':game['identifier'], 'player1_id':game['player1_id'], 'player2_id':game['player2_id']}
            player_name = {'identifier':game['identifier'], 'player1_name':player1_name, 'player2_nema':player2_name}
            matchCardId[i] = player_id
            matchCardname[i] = player_name
            i += 1

    return(matchCardname)