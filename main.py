cache = {}
def can_win(stones,depth):
    if (stones, depth) in cache:
        return cache[(stones, depth)]

    if stones >= 35:
        return [False, ["opponent already won"],depth,depth]
        return cache[(stones,depth)]


    wins = []
    losses = []

    depth += 1

    plus2 = can_win(stones+2,depth)
    if plus2[0] ==False:
        wins.append([True, [f"+2 = {stones+2}"]+ plus2[1],plus2[2],plus2[3]])
    else:
        losses.append([False, [f"+2 = {stones + 2}"] + plus2[1],plus2[2],plus2[3]])
    plus4 = can_win(stones + 4,depth)
    if plus4[0]==False:
        wins.append([True, [f"+4 = {stones+4}"]+ plus4[1],plus4[2],plus4[3]])
    else:
        losses.append([False, [f"+4 = {stones + 4}"] + plus4[1],plus4[2],plus4[3]])
    by2 = can_win(stones * 2,depth)
    if by2[0]==False:
        wins.append([True, [f"*2 = {stones*2}"]+by2[1], by2[2], by2[3]])
    else:
        losses.append([False, [f"*2 = {stones * 2}"] + by2[1], by2[2], by2[3]])
    by3 = can_win(stones * 3,depth)
    if by3[0]==False:
        wins.append([True, [f"*3 = {stones*3}"]+ by3[1],by3[2],by3[3]])
    else:
        losses.append([False, [f"*3 = {stones*3}"]+ by3[1],by3[2],by3[3]])

    if len(wins)>0:
        minwin_idx= 0
        for i in range(len(wins)):
             if wins[minwin_idx][2] > wins[i][2]:
                 minwin_idx = i
        return wins[minwin_idx]

    minloss_idx = 0
    maxloss_idx = 0

    for i in range(len(losses)):
        if losses[minloss_idx][2] > losses[i][2]:
            minloss_idx = i
        if losses[maxloss_idx][3] < losses[i][3]:
            maxloss_idx = i

    cache[(stones,depth)] = [False,
            [[f"even if +2 = {stones+2}, opponent will"]+ [plus2[1]]]+
            [[f"even if +4 = {stones+4}, opponent will"]+ [plus4[1]]]+
            [[f"even if *2 = {stones * 2}, opponent will"]+ [by2[1]]]+
            [[f"even if *3 = {stones * 3}, opponent will"]+ [by3[1]]],
            losses[minloss_idx][2],
            losses[maxloss_idx][3]]
    return cache[(stones,depth)]

for stones in range(1,35):
    print(stones,can_win(stones,0), '\n')