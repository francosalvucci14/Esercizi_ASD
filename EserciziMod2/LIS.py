def lis_with_elements(arr):
    if not arr:
        return 0, []

    n = len(arr)
    dp = [1] * n
    prev = [-1] * n

    for i in range(1, n):
        for j in range(i):
            if arr[i] > arr[j] and dp[i] < dp[j] + 1:
                dp[i] = dp[j] + 1
                prev[i] = j

    # Trova l'indice dell'elemento massimo in dp
    max_index = 0
    for i in range(n):
        if dp[i] > dp[max_index]:
            max_index = i

    # Ricostruisci la LIS utilizzando l'array prev
    lis = []
    while max_index != -1:
        lis.append(arr[max_index])
        max_index = prev[max_index]

    lis.reverse()  # La sequenza è stata costruita in ordine inverso
    print(dp)
    return dp[max_index], lis


# Esempio di utilizzo
# arr = [10, 9, 2, 5, 3, 7, 101, 18]
arr = [4, 1, 8, 3, 4, 8, 2, 7, 5, 6, 9, 8]
length, lis = lis_with_elements(arr)
print("La lunghezza della Longest Increasing Subsequence è:", length)
print("Gli elementi della Longest Increasing Subsequence sono:", lis)
