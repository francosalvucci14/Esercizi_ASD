def create_oracolo(A):
    n = len(A)
    pref_sum = [0] * (n + 1)

    for i in range(1, n + 1):
        pref_sum[i] = pref_sum[i - 1] + A[i - 1]
    print(pref_sum)
    return pref_sum


def query_difference(oracolo, i, j):
    num_ones = oracolo[j] - oracolo[i - 1]
    num_zeros = (j - i + 1) - num_ones

    print(num_ones)
    print(num_zeros)
    difference_modulo = (
        num_ones - num_zeros if num_ones > num_zeros else num_zeros - num_ones
    )

    return difference_modulo


# Example Usage:
# vettore_A = [1, 0, 1, 1, 0, 1, 0, 0, 1]
vettore_A = [0, 0, 1, 0, 1, 1, 1, 0]
prefix_sums = create_oracolo(vettore_A)
result_query = query_difference(prefix_sums, 0, 2)
print(result_query)
