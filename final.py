players = [('a', 1), ('b', 0), ('c', 1), ('d', 1),('e', 1),('f', 1)]

def matchmaking(players=[], teams = 3, min_player = 1, max_player = None):

    even = []
    odd = []
    copy = []
    players = [x[0] for x in players if x[1] == 1]
    game = [[] for i in xrange(teams)]

    for list in game:
        if max_player == None:
            for letter in players[:]:

                player_index = players.index(letter)
                if player_index % 2 == 0:
                    if len(list) != max_player:
                        list.append(letter)
                        players.remove(letter)
                elif player_index % 2 == 1:
                    if len(list) != max_player:
                        list.append(letter)
                        players.remove(letter)
        else:
            for letter in players:
                player_index = players.index(letter)
                if player_index % 2 == 0:
                    if len(list) != max_player:
                        list.append(letter)
                        players.remove(letter)
                elif player_index % 2 == 1:
                    if len(list) != max_player:
                        list.append(letter)

    if [i for i in game if i == []]:
        return 'false'
    else:
        return game

print 'players, 1, 1, 1: ' + str(matchmaking(players, 1, 1, 1))
print 'players, 2, 1, 1: ' +  str(matchmaking(players, 2, 1, 1))
print 'players, 2, 1, 2: ' + str(matchmaking(players, 2, 1, 2))
print 'players, 2, 3: ' + str(matchmaking(players, 2, 3))
print 'players, 6, 1: ' + str(matchmaking(players, 6, 1))
print 'players, 1, 1: ' + str(matchmaking(players, 1, 1))
