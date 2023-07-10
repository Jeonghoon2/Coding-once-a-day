def solution(players, callings):

    p = dict()

    for i, player in enumerate(players):
        p[player] = i

    for c_p in callings:
        idx = p.get(c_p)

        players[idx - 1], players[idx] = players[idx], players[idx - 1]

        p[c_p] = idx-1
        p[players[idx]] = idx

    return players


players = ["memu", "soe", "poe", "kai", "mine"]
callings = ["kai", "kai", "mine", "mine"]

print(solution(players, callings))
