def max_score_with_pieces(n, b, g, n_score):
    if n == 0:
        return 0, []

    # Initialize DP arrays
    dp = [[float('-inf')] * 3 for _ in range(n)]
    prev = [[-1] * 3 for _ in range(n)]
    dp[0][0] = b  # The first piece must be white
    dp[0][1] = float('-inf')  # Invalid state
    dp[0][2] = float('-inf')  # Invalid state

    for i in range(1, n):
        # If we place a white piece at position i
        dp[i][0] = b
        prev[i][0] = -1

        # If we place a gray piece at position i
        if dp[i-1][0] != float('-inf'):
            dp[i][1] = dp[i-1][0] + g
            prev[i][1] = 0
        else:
            dp[i][1] = g
            prev[i][1] = -1

        # If we place a black piece at position i
        if dp[i-1][1] != float('-inf') and dp[i-1][0] != float('-inf'):
            if dp[i-1][1] + n_score > dp[i-1][0] + n_score:
                dp[i][2] = dp[i-1][1] + n_score
                prev[i][2] = 1
            else:
                dp[i][2] = dp[i-1][0] + n_score
                prev[i][2] = 0
        elif dp[i-1][1] != float('-inf'):
            dp[i][2] = dp[i-1][1] + n_score
            prev[i][2] = 1
        elif dp[i-1][0] != float('-inf'):
            dp[i][2] = dp[i-1][0] + n_score
            prev[i][2] = 0
        else:
            dp[i][2] = n_score
            prev[i][2] = -1

    # Maximum score at the end of the board
    max_score = max(dp[n-1][0], dp[n-1][1], dp[n-1][2])
    final_choice = dp[n-1].index(max_score)

    # Recover the sequence of pieces
    sequence = []
    i = n - 1
    while i >= 0:
        if final_choice == 0:
            sequence.append('bianco')
        elif final_choice == 1:
            sequence.append('grigio')
        else:
            sequence.append('nero')
        
        final_choice = prev[i][final_choice]
        i -= 1

    sequence.reverse()  # Reverse the sequence to get the correct order

    return max_score, sequence

# Example usage:
n = 5
b = 1
g = 2
n_score = 3
score, sequence = max_score_with_pieces(n, b, g, n_score)
print("Max Score:", score)
print("Sequence of Pieces:", sequence)