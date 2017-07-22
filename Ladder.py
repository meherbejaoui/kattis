# Spotify Challenge 2010


from math import sin, radians, ceil
h, v = map(int, raw_input().split())
print int(ceil(h/sin(radians(v))))