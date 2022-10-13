N = 100

sum_squares = N * (N + 1) * (2 * N + 1) // 6
squares_sum = (N * (N + 1) // 2) ** 2

print(squares_sum - sum_squares)
