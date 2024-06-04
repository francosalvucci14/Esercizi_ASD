# def massimo_punteggio(n, ni, bi):
#     if n == 0:
#         return 0
#     elif n == 1:
#         return max(ni[0], bi[0])
    
#     # Inizializzazione delle tabelle dp
#     dp_no_white = [0] * n
#     dp_one_white = [0] * n
    
#     # Inizializzazione del primo elemento
#     dp_no_white[0] = ni[0]
#     dp_one_white[0] = bi[0]

#     if n > 1:
#         dp_no_white[1] = max(ni[1], dp_no_white[0])
#         dp_one_white[1] = max(bi[1], dp_no_white[0] + bi[1])

#     # Riempimento della tabella dp
#     for i in range(2, n):
#         dp_no_white[i] = max(dp_no_white[i-1], dp_no_white[i-2] + ni[i])
#         dp_one_white[i] = max(dp_one_white[i-1], dp_no_white[i-2] + bi[i], dp_one_white[i-2] + ni[i])

#     # Il massimo punteggio sarà il massimo tra dp_no_white[n-1] e dp_one_white[n-1]
#     return max(dp_no_white[n-1], dp_one_white[n-1])

def massimo_punteggio(n, ni, bi):
    dp_no_white = [0]*(n+1)
    dp_one_white = [0]*(n+1)

    dp_no_white[1] = ni[0]
    dp_one_white[1] = bi[0]

    for i in range(2, n+1):
        dp_no_white[i] = max(dp_no_white[i-1], dp_no_white[i-2] + ni[i-1])
        dp_one_white[i] = max(dp_one_white[i-1], dp_no_white[i-2] + bi[i-1],dp_one_white[i-2] + ni[i-1])

    return max(dp_no_white[n], dp_one_white[n])
# Esempio di utilizzo:
n = 3
bi = [1,10,25.01]
ni = [10,4,2]
print(massimo_punteggio(n, ni, bi))  # Output atteso: 15
