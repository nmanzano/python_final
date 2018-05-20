players = [('a', 1), ('b', 0), ('c', 1), ('d', 1),('e', 1),('f', 1)]

def matchmaking(players=[], teams = 3, min_player = 1, max_player = None):


    even = []
    odd = []
    copy = []


    players = [x for x in players if x[1] == 1]

    for x in players:
        copy.append(x[0])
    players = copy

    game = [[] for i in xrange(teams)]


    for x in game:
        for y in players:
            player_index = players.index(y)

            if player_index % 2 == 0:
                if len(x) != max_player:
                    x.append(y)
                    players.pop(player_index)
            elif player_index % 2 == 1:
                if len(x) != max_player:
                    x.append(y)


    print game, 'game'

matchmaking(players, 2, 1, 1)
