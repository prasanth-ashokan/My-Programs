from itertools import permutations,combinations
for ii in range(1):
    n=int(input())
    cl=[[[(0, 1), (0, 2), (1, 2)]], [[(0, 1), (0, 2), (0, 3), (1, 2), (1, 3), (2, 3)], [(0, 1, 2), (0, 1, 3), (0, 2, 3), (1, 2, 3)]], [[(0, 1), (0, 2), (0, 3), (0, 4), (1, 2), (1, 3), (1, 4), (2, 3), (2, 4), (3, 4)], [(0, 1, 2), (0, 1, 3), (0, 1, 4), (0, 2, 3), (0, 2, 4), (0, 3, 4), (1, 2, 3), (1, 2, 4), (1, 3, 4), (2, 3, 4)], [(0, 1, 2, 3), (0, 1, 2, 4), (0, 1, 3, 4), (0, 2, 3, 4), (1, 2, 3, 4)]], [[(0, 1), (0, 2), (0, 3), (0, 4), (0, 5), (1, 2), (1, 3), (1, 4), (1, 5), (2, 3), (2, 4), (2, 5), (3, 4), (3, 5), (4, 5)], [(0, 1, 2), (0, 1, 3), (0, 1, 4), (0, 1, 5), (0, 2, 3), (0, 2, 4), (0, 2, 5), (0, 3, 4), (0, 3, 5), (0, 4, 5), (1, 2, 3), (1, 2, 4), (1, 2, 5), (1, 3, 4), (1, 3, 5), (1, 4, 5), (2, 3, 4), (2, 3, 5), (2, 4, 5), (3, 4, 5)], [(0, 1, 2, 3), (0, 1, 2, 4), (0, 1, 2, 5), (0, 1, 3, 4), (0, 1, 3, 5), (0, 1, 4, 5), (0, 2, 3, 4), (0, 2, 3, 5), (0, 2, 4, 5), (0, 3, 4, 5), (1, 2, 3, 4), (1, 2, 3, 5), (1, 2, 4, 5), (1, 3, 4, 5), (2, 3, 4, 5)], [(0, 1, 2, 3, 4), (0, 1, 2, 3, 5), (0, 1, 2, 4, 5), (0, 1, 3, 4, 5), (0, 2, 3, 4, 5), (1, 2, 3, 4, 5)]], [[(0, 1), (0, 2), (0, 3), (0, 4), (0, 5), (0, 6), (1, 2), (1, 3), (1, 4), (1, 5), (1, 6), (2, 3), (2, 4), (2, 5), (2, 6), (3, 4), (3, 5), (3, 6), (4, 5), (4, 6), (5, 6)], [(0, 1, 2), (0, 1, 3), (0, 1, 4), (0, 1, 5), (0, 1, 6), (0, 2, 3), (0, 2, 4), (0, 2, 5), (0, 2, 6), (0, 3, 4), (0, 3, 5), (0, 3, 6), (0, 4, 5), (0, 4, 6), (0, 5, 6), (1, 2, 3), (1, 2, 4), (1, 2, 5), (1, 2, 6), (1, 3, 4), (1, 3, 5), (1, 3, 6), (1, 4, 5), (1, 4, 6), (1, 5, 6), (2, 3, 4), (2, 3, 5), (2, 3, 6), (2, 4, 5), (2, 4, 6), (2, 5, 6), (3, 4, 5), (3, 4, 6), (3, 5, 6), (4, 5, 6)], [(0, 1, 2, 3), (0, 1, 2, 4), (0, 1, 2, 5), (0, 1, 2, 6), (0, 1, 3, 4), (0, 1, 3, 5), (0, 1, 3, 6), (0, 1, 4, 5), (0, 1, 4, 6), (0, 1, 5, 6), (0, 2, 3, 4), (0, 2, 3, 5), (0, 2, 3, 6), (0, 2, 4, 5), (0, 2, 4, 6), (0, 2, 5, 6), (0, 3, 4, 5), (0, 3, 4, 6), (0, 3, 5, 6), (0, 4, 5, 6), (1, 2, 3, 4), (1, 2, 3, 5), (1, 2, 3, 6), (1, 2, 4, 5), (1, 2, 4, 6), (1, 2, 5, 6), (1, 3, 4, 5), (1, 3, 4, 6), (1, 3, 5, 6), (1, 4, 5, 6), (2, 3, 4, 5), (2, 3, 4, 6), (2, 3, 5, 6), (2, 4, 5, 6), (3, 4, 5, 6)], [(0, 1, 2, 3, 4), (0, 1, 2, 3, 5), (0, 1, 2, 3, 6), (0, 1, 2, 4, 5), (0, 1, 2, 4, 6), (0, 1, 2, 5, 6), (0, 1, 3, 4, 5), (0, 1, 3, 4, 6), (0, 1, 3, 5, 6), (0, 1, 4, 5, 6), (0, 2, 3, 4, 5), (0, 2, 3, 4, 6), (0, 2, 3, 5, 6), (0, 2, 4, 5, 6), (0, 3, 4, 5, 6), (1, 2, 3, 4, 5), (1, 2, 3, 4, 6), (1, 2, 3, 5, 6), (1, 2, 4, 5, 6), (1, 3, 4, 5, 6), (2, 3, 4, 5, 6)], [(0, 1, 2, 3, 4, 5), (0, 1, 2, 3, 4, 6), (0, 1, 2, 3, 5, 6), (0, 1, 2, 4, 5, 6), (0, 1, 3, 4, 5, 6), (0, 2, 3, 4, 5, 6), (1, 2, 3, 4, 5, 6)]], [[(0, 1), (0, 2), (0, 3), (0, 4), (0, 5), (0, 6), (0, 7), (1, 2), (1, 3), (1, 4), (1, 5), (1, 6), (1, 7), (2, 3), (2, 4), (2, 5), (2, 6), (2, 7), (3, 4), (3, 5), (3, 6), (3, 7), (4, 5), (4, 6), (4, 7), (5, 6), (5, 7), (6, 7)], [(0, 1, 2), (0, 1, 3), (0, 1, 4), (0, 1, 5), (0, 1, 6), (0, 1, 7), (0, 2, 3), (0, 2, 4), (0, 2, 5), (0, 2, 6), (0, 2, 7), (0, 3, 4), (0, 3, 5), (0, 3, 6), (0, 3, 7), (0, 4, 5), (0, 4, 6), (0, 4, 7), (0, 5, 6), (0, 5, 7), (0, 6, 7), (1, 2, 3), (1, 2, 4), (1, 2, 5), (1, 2, 6), (1, 2, 7), (1, 3, 4), (1, 3, 5), (1, 3, 6), (1, 3, 7), (1, 4, 5), (1, 4, 6), (1, 4, 7), (1, 5, 6), (1, 5, 7), (1, 6, 7), (2, 3, 4), (2, 3, 5), (2, 3, 6), (2, 3, 7), (2, 4, 5), (2, 4, 6), (2, 4, 7), (2, 5, 6), (2, 5, 7), (2, 6, 7), (3, 4, 5), (3, 4, 6), (3, 4, 7), (3, 5, 6), (3, 5, 7), (3, 6, 7), (4, 5, 6), (4, 5, 7), (4, 6, 7), (5, 6, 7)], [(0, 1, 2, 3), (0, 1, 2, 4), (0, 1, 2, 5), (0, 1, 2, 6), (0, 1, 2, 7), (0, 1, 3, 4), (0, 1, 3, 5), (0, 1, 3, 6), (0, 1, 3, 7), (0, 1, 4, 5), (0, 1, 4, 6), (0, 1, 4, 7), (0, 1, 5, 6), (0, 1, 5, 7), (0, 1, 6, 7), (0, 2, 3, 4), (0, 2, 3, 5), (0, 2, 3, 6), (0, 2, 3, 7), (0, 2, 4, 5), (0, 2, 4, 6), (0, 2, 4, 7), (0, 2, 5, 6), (0, 2, 5, 7), (0, 2, 6, 7), (0, 3, 4, 5), (0, 3, 4, 6), (0, 3, 4, 7), (0, 3, 5, 6), (0, 3, 5, 7), (0, 3, 6, 7), (0, 4, 5, 6), (0, 4, 5, 7), (0, 4, 6, 7), (0, 5, 6, 7), (1, 2, 3, 4), (1, 2, 3, 5), (1, 2, 3, 6), (1, 2, 3, 7), (1, 2, 4, 5), (1, 2, 4, 6), (1, 2, 4, 7), (1, 2, 5, 6), (1, 2, 5, 7), (1, 2, 6, 7), (1, 3, 4, 5), (1, 3, 4, 6), (1, 3, 4, 7), (1, 3, 5, 6), (1, 3, 5, 7), (1, 3, 6, 7), (1, 4, 5, 6), (1, 4, 5, 7), (1, 4, 6, 7), (1, 5, 6, 7), (2, 3, 4, 5), (2, 3, 4, 6), (2, 3, 4, 7), (2, 3, 5, 6), (2, 3, 5, 7), (2, 3, 6, 7), (2, 4, 5, 6), (2, 4, 5, 7), (2, 4, 6, 7), (2, 5, 6, 7), (3, 4, 5, 6), (3, 4, 5, 7), (3, 4, 6, 7), (3, 5, 6, 7), (4, 5, 6, 7)], [(0, 1, 2, 3, 4), (0, 1, 2, 3, 5), (0, 1, 2, 3, 6), (0, 1, 2, 3, 7), (0, 1, 2, 4, 5), (0, 1, 2, 4, 6), (0, 1, 2, 4, 7), (0, 1, 2, 5, 6), (0, 1, 2, 5, 7), (0, 1, 2, 6, 7), (0, 1, 3, 4, 5), (0, 1, 3, 4, 6), (0, 1, 3, 4, 7), (0, 1, 3, 5, 6), (0, 1, 3, 5, 7), (0, 1, 3, 6, 7), (0, 1, 4, 5, 6), (0, 1, 4, 5, 7), (0, 1, 4, 6, 7), (0, 1, 5, 6, 7), (0, 2, 3, 4, 5), (0, 2, 3, 4, 6), (0, 2, 3, 4, 7), (0, 2, 3, 5, 6), (0, 2, 3, 5, 7), (0, 2, 3, 6, 7), (0, 2, 4, 5, 6), (0, 2, 4, 5, 7), (0, 2, 4, 6, 7), (0, 2, 5, 6, 7), (0, 3, 4, 5, 6), (0, 3, 4, 5, 7), (0, 3, 4, 6, 7), (0, 3, 5, 6, 7), (0, 4, 5, 6, 7), (1, 2, 3, 4, 5), (1, 2, 3, 4, 6), (1, 2, 3, 4, 7), (1, 2, 3, 5, 6), (1, 2, 3, 5, 7), (1, 2, 3, 6, 7), (1, 2, 4, 5, 6), (1, 2, 4, 5, 7), (1, 2, 4, 6, 7), (1, 2, 5, 6, 7), (1, 3, 4, 5, 6), (1, 3, 4, 5, 7), (1, 3, 4, 6, 7), (1, 3, 5, 6, 7), (1, 4, 5, 6, 7), (2, 3, 4, 5, 6), (2, 3, 4, 5, 7), (2, 3, 4, 6, 7), (2, 3, 5, 6, 7), (2, 4, 5, 6, 7), (3, 4, 5, 6, 7)], [(0, 1, 2, 3, 4, 5), (0, 1, 2, 3, 4, 6), (0, 1, 2, 3, 4, 7), (0, 1, 2, 3, 5, 6), (0, 1, 2, 3, 5, 7), (0, 1, 2, 3, 6, 7), (0, 1, 2, 4, 5, 6), (0, 1, 2, 4, 5, 7), (0, 1, 2, 4, 6, 7), (0, 1, 2, 5, 6, 7), (0, 1, 3, 4, 5, 6), (0, 1, 3, 4, 5, 7), (0, 1, 3, 4, 6, 7), (0, 1, 3, 5, 6, 7), (0, 1, 4, 5, 6, 7), (0, 2, 3, 4, 5, 6), (0, 2, 3, 4, 5, 7), (0, 2, 3, 4, 6, 7), (0, 2, 3, 5, 6, 7), (0, 2, 4, 5, 6, 7), (0, 3, 4, 5, 6, 7), (1, 2, 3, 4, 5, 6), (1, 2, 3, 4, 5, 7), (1, 2, 3, 4, 6, 7), (1, 2, 3, 5, 6, 7), (1, 2, 4, 5, 6, 7), (1, 3, 4, 5, 6, 7), (2, 3, 4, 5, 6, 7)], [(0, 1, 2, 3, 4, 5, 6), (0, 1, 2, 3, 4, 5, 7), (0, 1, 2, 3, 4, 6, 7), (0, 1, 2, 3, 5, 6, 7), (0, 1, 2, 4, 5, 6, 7), (0, 1, 3, 4, 5, 6, 7), (0, 2, 3, 4, 5, 6, 7), (1, 2, 3, 4, 5, 6, 7)]], [[(0, 1), (0, 2), (0, 3), (0, 4), (0, 5), (0, 6), (0, 7), (0, 8), (1, 2), (1, 3), (1, 4), (1, 5), (1, 6), (1, 7), (1, 8), (2, 3), (2, 4), (2, 5), (2, 6), (2, 7), (2, 8), (3, 4), (3, 5), (3, 6), (3, 7), (3, 8), (4, 5), (4, 6), (4, 7), (4, 8), (5, 6), (5, 7), (5, 8), (6, 7), (6, 8), (7, 8)], [(0, 1, 2), (0, 1, 3), (0, 1, 4), (0, 1, 5), (0, 1, 6), (0, 1, 7), (0, 1, 8), (0, 2, 3), (0, 2, 4), (0, 2, 5), (0, 2, 6), (0, 2, 7), (0, 2, 8), (0, 3, 4), (0, 3, 5), (0, 3, 6), (0, 3, 7), (0, 3, 8), (0, 4, 5), (0, 4, 6), (0, 4, 7), (0, 4, 8), (0, 5, 6), (0, 5, 7), (0, 5, 8), (0, 6, 7), (0, 6, 8), (0, 7, 8), (1, 2, 3), (1, 2, 4), (1, 2, 5), (1, 2, 6), (1, 2, 7), (1, 2, 8), (1, 3, 4), (1, 3, 5), (1, 3, 6), (1, 3, 7), (1, 3, 8), (1, 4, 5), (1, 4, 6), (1, 4, 7), (1, 4, 8), (1, 5, 6), (1, 5, 7), (1, 5, 8), (1, 6, 7), (1, 6, 8), (1, 7, 8), (2, 3, 4), (2, 3, 5), (2, 3, 6), (2, 3, 7), (2, 3, 8), (2, 4, 5), (2, 4, 6), (2, 4, 7), (2, 4, 8), (2, 5, 6), (2, 5, 7), (2, 5, 8), (2, 6, 7), (2, 6, 8), (2, 7, 8), (3, 4, 5), (3, 4, 6), (3, 4, 7), (3, 4, 8), (3, 5, 6), (3, 5, 7), (3, 5, 8), (3, 6, 7), (3, 6, 8), (3, 7, 8), (4, 5, 6), (4, 5, 7), (4, 5, 8), (4, 6, 7), (4, 6, 8), (4, 7, 8), (5, 6, 7), (5, 6, 8), (5, 7, 8), (6, 7, 8)], [(0, 1, 2, 3), (0, 1, 2, 4), (0, 1, 2, 5), (0, 1, 2, 6), (0, 1, 2, 7), (0, 1, 2, 8), (0, 1, 3, 4), (0, 1, 3, 5), (0, 1, 3, 6), (0, 1, 3, 7), (0, 1, 3, 8), (0, 1, 4, 5), (0, 1, 4, 6), (0, 1, 4, 7), (0, 1, 4, 8), (0, 1, 5, 6), (0, 1, 5, 7), (0, 1, 5, 8), (0, 1, 6, 7), (0, 1, 6, 8), (0, 1, 7, 8), (0, 2, 3, 4), (0, 2, 3, 5), (0, 2, 3, 6), (0, 2, 3, 7), (0, 2, 3, 8), (0, 2, 4, 5), (0, 2, 4, 6), (0, 2, 4, 7), (0, 2, 4, 8), (0, 2, 5, 6), (0, 2, 5, 7), (0, 2, 5, 8), (0, 2, 6, 7), (0, 2, 6, 8), (0, 2, 7, 8), (0, 3, 4, 5), (0, 3, 4, 6), (0, 3, 4, 7), (0, 3, 4, 8), (0, 3, 5, 6), (0, 3, 5, 7), (0, 3, 5, 8), (0, 3, 6, 7), (0, 3, 6, 8), (0, 3, 7, 8), (0, 4, 5, 6), (0, 4, 5, 7), (0, 4, 5, 8), (0, 4, 6, 7), (0, 4, 6, 8), (0, 4, 7, 8), (0, 5, 6, 7), (0, 5, 6, 8), (0, 5, 7, 8), (0, 6, 7, 8), (1, 2, 3, 4), (1, 2, 3, 5), (1, 2, 3, 6), (1, 2, 3, 7), (1, 2, 3, 8), (1, 2, 4, 5), (1, 2, 4, 6), (1, 2, 4, 7), (1, 2, 4, 8), (1, 2, 5, 6), (1, 2, 5, 7), (1, 2, 5, 8), (1, 2, 6, 7), (1, 2, 6, 8), (1, 2, 7, 8), (1, 3, 4, 5), (1, 3, 4, 6), (1, 3, 4, 7), (1, 3, 4, 8), (1, 3, 5, 6), (1, 3, 5, 7), (1, 3, 5, 8), (1, 3, 6, 7), (1, 3, 6, 8), (1, 3, 7, 8), (1, 4, 5, 6), (1, 4, 5, 7), (1, 4, 5, 8), (1, 4, 6, 7), (1, 4, 6, 8), (1, 4, 7, 8), (1, 5, 6, 7), (1, 5, 6, 8), (1, 5, 7, 8), (1, 6, 7, 8), (2, 3, 4, 5), (2, 3, 4, 6), (2, 3, 4, 7), (2, 3, 4, 8), (2, 3, 5, 6), (2, 3, 5, 7), (2, 3, 5, 8), (2, 3, 6, 7), (2, 3, 6, 8), (2, 3, 7, 8), (2, 4, 5, 6), (2, 4, 5, 7), (2, 4, 5, 8), (2, 4, 6, 7), (2, 4, 6, 8), (2, 4, 7, 8), (2, 5, 6, 7), (2, 5, 6, 8), (2, 5, 7, 8), (2, 6, 7, 8), (3, 4, 5, 6), (3, 4, 5, 7), (3, 4, 5, 8), (3, 4, 6, 7), (3, 4, 6, 8), (3, 4, 7, 8), (3, 5, 6, 7), (3, 5, 6, 8), (3, 5, 7, 8), (3, 6, 7, 8), (4, 5, 6, 7), (4, 5, 6, 8), (4, 5, 7, 8), (4, 6, 7, 8), (5, 6, 7, 8)], [(0, 1, 2, 3, 4), (0, 1, 2, 3, 5), (0, 1, 2, 3, 6), (0, 1, 2, 3, 7), (0, 1, 2, 3, 8), (0, 1, 2, 4, 5), (0, 1, 2, 4, 6), (0, 1, 2, 4, 7), (0, 1, 2, 4, 8), (0, 1, 2, 5, 6), (0, 1, 2, 5, 7), (0, 1, 2, 5, 8), (0, 1, 2, 6, 7), (0, 1, 2, 6, 8), (0, 1, 2, 7, 8), (0, 1, 3, 4, 5), (0, 1, 3, 4, 6), (0, 1, 3, 4, 7), (0, 1, 3, 4, 8), (0, 1, 3, 5, 6), (0, 1, 3, 5, 7), (0, 1, 3, 5, 8), (0, 1, 3, 6, 7), (0, 1, 3, 6, 8), (0, 1, 3, 7, 8), (0, 1, 4, 5, 6), (0, 1, 4, 5, 7), (0, 1, 4, 5, 8), (0, 1, 4, 6, 7), (0, 1, 4, 6, 8), (0, 1, 4, 7, 8), (0, 1, 5, 6, 7), (0, 1, 5, 6, 8), (0, 1, 5, 7, 8), (0, 1, 6, 7, 8), (0, 2, 3, 4, 5), (0, 2, 3, 4, 6), (0, 2, 3, 4, 7), (0, 2, 3, 4, 8), (0, 2, 3, 5, 6), (0, 2, 3, 5, 7), (0, 2, 3, 5, 8), (0, 2, 3, 6, 7), (0, 2, 3, 6, 8), (0, 2, 3, 7, 8), (0, 2, 4, 5, 6), (0, 2, 4, 5, 7), (0, 2, 4, 5, 8), (0, 2, 4, 6, 7), (0, 2, 4, 6, 8), (0, 2, 4, 7, 8), (0, 2, 5, 6, 7), (0, 2, 5, 6, 8), (0, 2, 5, 7, 8), (0, 2, 6, 7, 8), (0, 3, 4, 5, 6), (0, 3, 4, 5, 7), (0, 3, 4, 5, 8), (0, 3, 4, 6, 7), (0, 3, 4, 6, 8), (0, 3, 4, 7, 8), (0, 3, 5, 6, 7), (0, 3, 5, 6, 8), (0, 3, 5, 7, 8), (0, 3, 6, 7, 8), (0, 4, 5, 6, 7), (0, 4, 5, 6, 8), (0, 4, 5, 7, 8), (0, 4, 6, 7, 8), (0, 5, 6, 7, 8), (1, 2, 3, 4, 5), (1, 2, 3, 4, 6), (1, 2, 3, 4, 7), (1, 2, 3, 4, 8), (1, 2, 3, 5, 6), (1, 2, 3, 5, 7), (1, 2, 3, 5, 8), (1, 2, 3, 6, 7), (1, 2, 3, 6, 8), (1, 2, 3, 7, 8), (1, 2, 4, 5, 6), (1, 2, 4, 5, 7), (1, 2, 4, 5, 8), (1, 2, 4, 6, 7), (1, 2, 4, 6, 8), (1, 2, 4, 7, 8), (1, 2, 5, 6, 7), (1, 2, 5, 6, 8), (1, 2, 5, 7, 8), (1, 2, 6, 7, 8), (1, 3, 4, 5, 6), (1, 3, 4, 5, 7), (1, 3, 4, 5, 8), (1, 3, 4, 6, 7), (1, 3, 4, 6, 8), (1, 3, 4, 7, 8), (1, 3, 5, 6, 7), (1, 3, 5, 6, 8), (1, 3, 5, 7, 8), (1, 3, 6, 7, 8), (1, 4, 5, 6, 7), (1, 4, 5, 6, 8), (1, 4, 5, 7, 8), (1, 4, 6, 7, 8), (1, 5, 6, 7, 8), (2, 3, 4, 5, 6), (2, 3, 4, 5, 7), (2, 3, 4, 5, 8), (2, 3, 4, 6, 7), (2, 3, 4, 6, 8), (2, 3, 4, 7, 8), (2, 3, 5, 6, 7), (2, 3, 5, 6, 8), (2, 3, 5, 7, 8), (2, 3, 6, 7, 8), (2, 4, 5, 6, 7), (2, 4, 5, 6, 8), (2, 4, 5, 7, 8), (2, 4, 6, 7, 8), (2, 5, 6, 7, 8), (3, 4, 5, 6, 7), (3, 4, 5, 6, 8), (3, 4, 5, 7, 8), (3, 4, 6, 7, 8), (3, 5, 6, 7, 8), (4, 5, 6, 7, 8)], [(0, 1, 2, 3, 4, 5), (0, 1, 2, 3, 4, 6), (0, 1, 2, 3, 4, 7), (0, 1, 2, 3, 4, 8), (0, 1, 2, 3, 5, 6), (0, 1, 2, 3, 5, 7), (0, 1, 2, 3, 5, 8), (0, 1, 2, 3, 6, 7), (0, 1, 2, 3, 6, 8), (0, 1, 2, 3, 7, 8), (0, 1, 2, 4, 5, 6), (0, 1, 2, 4, 5, 7), (0, 1, 2, 4, 5, 8), (0, 1, 2, 4, 6, 7), (0, 1, 2, 4, 6, 8), (0, 1, 2, 4, 7, 8), (0, 1, 2, 5, 6, 7), (0, 1, 2, 5, 6, 8), (0, 1, 2, 5, 7, 8), (0, 1, 2, 6, 7, 8), (0, 1, 3, 4, 5, 6), (0, 1, 3, 4, 5, 7), (0, 1, 3, 4, 5, 8), (0, 1, 3, 4, 6, 7), (0, 1, 3, 4, 6, 8), (0, 1, 3, 4, 7, 8), (0, 1, 3, 5, 6, 7), (0, 1, 3, 5, 6, 8), (0, 1, 3, 5, 7, 8), (0, 1, 3, 6, 7, 8), (0, 1, 4, 5, 6, 7), (0, 1, 4, 5, 6, 8), (0, 1, 4, 5, 7, 8), (0, 1, 4, 6, 7, 8), (0, 1, 5, 6, 7, 8), (0, 2, 3, 4, 5, 6), (0, 2, 3, 4, 5, 7), (0, 2, 3, 4, 5, 8), (0, 2, 3, 4, 6, 7), (0, 2, 3, 4, 6, 8), (0, 2, 3, 4, 7, 8), (0, 2, 3, 5, 6, 7), (0, 2, 3, 5, 6, 8), (0, 2, 3, 5, 7, 8), (0, 2, 3, 6, 7, 8), (0, 2, 4, 5, 6, 7), (0, 2, 4, 5, 6, 8), (0, 2, 4, 5, 7, 8), (0, 2, 4, 6, 7, 8), (0, 2, 5, 6, 7, 8), (0, 3, 4, 5, 6, 7), (0, 3, 4, 5, 6, 8), (0, 3, 4, 5, 7, 8), (0, 3, 4, 6, 7, 8), (0, 3, 5, 6, 7, 8), (0, 4, 5, 6, 7, 8), (1, 2, 3, 4, 5, 6), (1, 2, 3, 4, 5, 7), (1, 2, 3, 4, 5, 8), (1, 2, 3, 4, 6, 7), (1, 2, 3, 4, 6, 8), (1, 2, 3, 4, 7, 8), (1, 2, 3, 5, 6, 7), (1, 2, 3, 5, 6, 8), (1, 2, 3, 5, 7, 8), (1, 2, 3, 6, 7, 8), (1, 2, 4, 5, 6, 7), (1, 2, 4, 5, 6, 8), (1, 2, 4, 5, 7, 8), (1, 2, 4, 6, 7, 8), (1, 2, 5, 6, 7, 8), (1, 3, 4, 5, 6, 7), (1, 3, 4, 5, 6, 8), (1, 3, 4, 5, 7, 8), (1, 3, 4, 6, 7, 8), (1, 3, 5, 6, 7, 8), (1, 4, 5, 6, 7, 8), (2, 3, 4, 5, 6, 7), (2, 3, 4, 5, 6, 8), (2, 3, 4, 5, 7, 8), (2, 3, 4, 6, 7, 8), (2, 3, 5, 6, 7, 8), (2, 4, 5, 6, 7, 8), (3, 4, 5, 6, 7, 8)], [(0, 1, 2, 3, 4, 5, 6), (0, 1, 2, 3, 4, 5, 7), (0, 1, 2, 3, 4, 5, 8), (0, 1, 2, 3, 4, 6, 7), (0, 1, 2, 3, 4, 6, 8), (0, 1, 2, 3, 4, 7, 8), (0, 1, 2, 3, 5, 6, 7), (0, 1, 2, 3, 5, 6, 8), (0, 1, 2, 3, 5, 7, 8), (0, 1, 2, 3, 6, 7, 8), (0, 1, 2, 4, 5, 6, 7), (0, 1, 2, 4, 5, 6, 8), (0, 1, 2, 4, 5, 7, 8), (0, 1, 2, 4, 6, 7, 8), (0, 1, 2, 5, 6, 7, 8), (0, 1, 3, 4, 5, 6, 7), (0, 1, 3, 4, 5, 6, 8), (0, 1, 3, 4, 5, 7, 8), (0, 1, 3, 4, 6, 7, 8), (0, 1, 3, 5, 6, 7, 8), (0, 1, 4, 5, 6, 7, 8), (0, 2, 3, 4, 5, 6, 7), (0, 2, 3, 4, 5, 6, 8), (0, 2, 3, 4, 5, 7, 8), (0, 2, 3, 4, 6, 7, 8), (0, 2, 3, 5, 6, 7, 8), (0, 2, 4, 5, 6, 7, 8), (0, 3, 4, 5, 6, 7, 8), (1, 2, 3, 4, 5, 6, 7), (1, 2, 3, 4, 5, 6, 8), (1, 2, 3, 4, 5, 7, 8), (1, 2, 3, 4, 6, 7, 8), (1, 2, 3, 5, 6, 7, 8), (1, 2, 4, 5, 6, 7, 8), (1, 3, 4, 5, 6, 7, 8), (2, 3, 4, 5, 6, 7, 8)], [(0, 1, 2, 3, 4, 5, 6, 7), (0, 1, 2, 3, 4, 5, 6, 8), (0, 1, 2, 3, 4, 5, 7, 8), (0, 1, 2, 3, 4, 6, 7, 8), (0, 1, 2, 3, 5, 6, 7, 8), (0, 1, 2, 4, 5, 6, 7, 8), (0, 1, 3, 4, 5, 6, 7, 8), (0, 2, 3, 4, 5, 6, 7, 8), (1, 2, 3, 4, 5, 6, 7, 8)]]]
    l=[int(i) for i in input().split()]
    ml=max(l)
    bm=len(bin(ml)[2:])
    bc=[]
    ac=[]
    c=0
    to=0
    ao=0
    for i in l:
        b=bin(i)[2:]
        oc=(b).count('1')
        cc=abs(len(b)-oc)+bm-len(b)
        to=to+oc
        ao=ao+cc
        if oc==cc:
            c=c+1
        bc.append(oc)
        ac.append(cc)
    if to==ao:
        c=c+1
    if n>2 and n<=10:
        for i in cl[n-3]:
            for j in (i):
                x=0
                y=0
                for k in j:
                    x=x+(bc[k])
                    y=y+(ac[k])
                if (x==y):
                    c=c+1
    la=len(bin(c)[2:])
    print((bm-la)*'0'+bin(c)[2:])
        
    