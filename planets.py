from collections import defaultdict

testcases = int(input())
for testcase in range(testcases):
    planets = list(map(int, input().split()))
    orbits = list(map(int, input().split()))
    dictionary = defaultdict(int)
    for orbit in orbits:
        dictionary[orbit] += 1
    answer = 0
    for key, value in dictionary.items():
        if value >= planets[1]:
            answer += planets[1]
        else:
            answer += value
            
    print(answer)
