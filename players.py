from val import valrank

def getPlayers():



    f = open('players.txt', 'r')
    contents = f.read().split('\n')
    f.close()

    valList = []

    for line in contents:
        user, tag = line.split('#')
        current = valrank(user, tag)
        valList.append([user, tag, current, current])

    return valList

    #for person in valList:
        #print(person[2]['elo'], person[2]['mmr_change_to_last_game'])