# University of Chicago Masters Program in Computer Science - Placement Exam 2014/15


n = input()
lst = map(int, raw_input().split())
tot = 0
for i in lst:
    if i < 0:
        tot += 1
print tot