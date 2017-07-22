# Croatian Open Competition in Informatics 2016/2017


x = int(raw_input()) # X megabytes to surf the internet per month
n = int(raw_input()) # N months of using the plan
consumption = []
for i in range(n):
    consumption.append(x - int(raw_input()))
print sum(consumption)+x