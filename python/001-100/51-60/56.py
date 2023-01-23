print(max(max(sum(map(int, str(a**b))) for b in range(1, 100)) for a in range(1, 100)))
