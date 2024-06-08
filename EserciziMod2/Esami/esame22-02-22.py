def massimo_guadagno(v):
    n = len(v)

    # Aggiungi un valore 0 alla posizione iniziale per facilitare gli indici
    v = [0] + v

    # Inizializza l'array dp con 0
    dp = [0] * (n + 1)

    # Condizioni iniziali
    if n >= 1:
        dp[1] = 0
    if n >= 2:
        dp[2] = v[2]

    # Calcola dp[i] per i >= 3
    for i in range(3, n + 1):
        dp[i] = max(dp[i - 3] + v[i], dp[i - 2] + v[i])
    # print(dp)
    return dp[n]


def massimo_guadagno_inv(v):
    n = len(v)

    # Aggiungiamo tre elementi 0 alla fine per gestire gli indici fuori dai limiti
    v = v + [0, 0, 0]

    # Inizializziamo l'array dp con 0
    dp = [0] * (n + 3)

    # Calcoliamo dp[i] partendo dalla fine verso l'inizio
    for i in range(n - 1, -1, -1):
        if i + 3 <= n:
            prima_di_tre = v[i] + dp[i + 3]
        else:
            prima_di_tre = 0

        if i + 2 <= n:
            seconda_di_due = v[i + 1] + dp[i + 2]
        else:
            seconda_di_due = 0

        dp[i] = max(prima_di_tre, seconda_di_due)
    # print(dp)
    # Il massimo guadagno partendo dalla moneta 0
    return dp[0]


# Esempio di utilizzo
v = [10, 2, 5, 7, 11, 20]
print(massimo_guadagno(v))  # Output atteso: 55
print(massimo_guadagno_inv(v))  # Output atteso: 55
