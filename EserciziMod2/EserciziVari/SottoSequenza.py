def longest_common_substring(str1, str2):
    n = len(str1)
    m = len(str2)

    # Inizializzazione della matrice
    dp = [[0] * (m + 1) for _ in range(n + 1)]
    max_length = 0
    max_i = 0

    # Calcolo della lunghezza della sottostringa comune
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if str1[i - 1] == str2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
                if dp[i][j] > max_length:
                    max_length = dp[i][j]
                    max_i = i
            else:
                dp[i][j] = 0
    print(dp)
    # Ricostruzione della sottostringa comune
    if max_length == 0:
        return ""
    else:
        return str1[max_i - max_length : max_i]


# Esempio di utilizzo
str1 = "tst"
str2 = "test"
print("Stringhe di input str1={} & str2={}".format(str1, str2))
print("La più lunga sottostringa comune è:", longest_common_substring(str1, str2))
