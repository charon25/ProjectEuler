# This solves the system :
# O = P0 + (P1 - P0) * s + (P2 - P0) * t
# If 0 <= s <= 1, 0 <= t <= 1 and s + t <= 1, then O is in the triangle (P0, P1, P2)
def is_in_triangle(x0, y0, x1, y1, x2, y2):
    s_num = x2 * y0 - x0 * y2
    s_denom = x0 * (y1 - y2) + x1 * (y2 - y0) + x2 * (y0 - y1)
    t_num = x1 * y0 - x0 * y1
    t_denom = -s_denom

    s, t = s_num / s_denom, t_num / t_denom

    return 0.0 <= s <= 1.0 and 0.0 <= t <= 1.0 and s + t <= 1.0

triangles = []
with open('102.txt', 'r') as fi:
    for line in fi:
        triangles.append(list(map(int, line.strip().split(','))))

print(sum(is_in_triangle(*triangle) for triangle in triangles))
