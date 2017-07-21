# University of Chicago Masters Program in Computer Science - Placement Exam 2014/15


n = raw_input()
from itertools import groupby
print ''.join([x[0] for x in groupby(list(n))])