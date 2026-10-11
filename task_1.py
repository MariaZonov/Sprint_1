count_min = 0

a = '1h 45m,360s,25m,30m 120s,2h 60s'
c = a.split(',')
for z in c:
    for time in z.split():
        if 'h' in time:
            count_min += int(time.replace('h', '')) * 60
        elif 'm' in time:
            count_min += int(time.replace('m', ''))
        elif 's' in time:
            count_min += int(time.replace('s', '')) / 60

print(count_min)