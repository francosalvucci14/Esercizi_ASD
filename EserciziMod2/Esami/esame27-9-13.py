import pprint as pp


def max_gain(board):
    n = len(board[0])
    if n == 1:
        return max(board[0][0], board[1][0])

    dp = [[0] * n for _ in range(2)]
    dp[0] = board[0][:]
    dp[1] = board[1][:]
    
    for j in range(1, n):
        for i in range(2):
            dp[i][j] = (
                max(
                    dp[i - 1][j - 1],
                    dp[i - 1][j - 2] if j >= 2 else 0,
                    dp[i - 1][j - 3] if j >= 3 else 0,
                )
                + board[i][j]
            )

    pp.pprint(dp)
    return max(dp[0][-1], dp[1][-1])


# board = [[1, 5, 3, 28, 1000, 14, 3, 6], [56, 8, 1, 3, 74, 2, 60, 4]]
# board = [[8, 25, 32, 1, 65, 4, 1, 63], [0, 1, 0, 0, 2, 0, 1, 0]]
board = [[3, 10, 10, 15, 6, 5, 30, 2, 1], [7, 2, 10, 1, 1, 2, 1, 3, 1000]]

pp.pprint(board)

print(max_gain(board))
