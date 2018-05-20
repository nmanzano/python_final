players = [('a', 1), ('b', 0), ('c', 1), ('d', 1),('e', 1),('f', 1)]

def matchmaking(players=[], teams = 3, min_player = 1, max_player = None):

    game = []
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
            print y, 'y'
            player_index = players.index(y)
            if player_index % 2 == 0 and len(x) != max_player:
                x.append(y)
                print x, 'x'
            elif len(x) == max_player:
                pass
            
    # for x in players:
    #     # print game, 'game again'
    #     if len(game) == max_player:
    #         print game, 'game'
    #     player_index = players.index(x)
    #     if player_index % 2 == 0:
    #         print x, 'even'
    #         if len(even) == 0:
    #             even.append(x)
    #         elif len(even) == max_player:
    #             game.append(even)
    #             even = []
    #             even.append(x)
    #         else:
    #             even.append(x)
    #     elif player_index % 2 == 1:
    #         if len(even) == 0:
    #             even.append(x)
    #         elif len(even) == max_player:
    #             game.append(even)
    #             even = []
    #             even.append(x)
    #         else:
    #             even.append(x)
    #
    # print even, 'even'
    # print game, ''

matchmaking(players, 2, 1, 1)
