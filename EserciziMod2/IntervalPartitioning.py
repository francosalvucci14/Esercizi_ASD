def IP(lectures: list) -> list:
    lectures.sort(
        key=lambda x: x[0]
    )  # ordino gli intervalli in base allo starting time

    d = []  # classrooms
    for lect in lectures:
        room_found = False
        for room in d:
            if room[-1][1] <= lect[0]:
                room.append(lect)
                room_found = True
                break
        if not room_found:
            d.append([lect])  # se non ci sono classrooms disponibili, ne creo una nuova
    dn = len(d)
    print(f"Il numero di classi usate è {dn}")
    return d


lect = [
    (0, 3, "A"),
    (0, 7, "B"),
    (0, 3, "C"),
    (4, 7, "D"),
    (4, 10, "E"),
    (8, 11, "F"),
    (8, 11, "G"),
    (10, 15, "H"),
    (12, 15, "I"),
    (12, 15, "J"),
]
classi = IP(lect)
n = len(classi)
print("I job vengono schedulati con queste classi:\n")
for i in range(n):
    print(i + 1, classi[i])
