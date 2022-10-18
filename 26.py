
def recurring_cycle_length(n):
    m = 1
    modulos = []
    while not m in modulos:
        modulos.append(m)
        m *= 10
        m %= n

    if m == 0:
        return 0

    return len(modulos) - modulos.index(m)

print(max((recurring_cycle_length(n), n) for n in range(1, 1000))[1])
