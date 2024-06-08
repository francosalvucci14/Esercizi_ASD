def bocciati(f, m, d):
    n = len(f)
    print(n)

    OPT = [-1] * (n + 4)
    print(OPT)
    OPT[n + 3] = OPT[n + 2] = OPT[n+1] = OPT[n]= 0
    print(OPT)

    f = f + [0] * 4
    d = d + [0] * 4
    m = m + [0] * 4

    print(f)
    for i in range(n-1, -1, -1):
        OPT[i] = max(
            f[i] + OPT[i + 1],
            m[i] + f[i + 1] + OPT[i + 2],
            d[i] + f[i + 1] + f[i + 2] + f[i + 3] + OPT[i + 4],
        )
    print(OPT)

    # Print solution

    # for i in range(no - 2, -1,- 1):
    #     if OPT[i] == f[i] + OPT[i + 1]:
    #         print("Esame facile")
    #     elif OPT[i] == m[i] + f[i + 1] + OPT[i + 2]:
    #         print("Esame medio")
    #     else:
    #         print("Esame difficile")
    return OPT[0]


f = [2, 4, 1, 3, 5, 2, 2, 3, 4, 1]
m = [5, 6, 5, 4, 7, 4, 4, 6, 7, 3]
d = [10, 8, 10, 6, 9, 9, 6, 7, 8, 8]

print(bocciati(f, m, d))
