def hateville(D):
    DP = [0, D[0]]
    for i in range(1, len(D)):
        DP.append(max(DP[-1], DP[-2] + D[i]))
    return DP[-1]


D = [10, 5, 5, 10]
print(hateville(D))
