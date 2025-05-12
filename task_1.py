times = '1h 45m,360s,25m,30m 120s,2h 60s'
seconds_total = 0
for t in times.replace(',', ' ').split():
    n = int(t[:-1])
    if 'h' in t:
        seconds_total += n * 60 * 60
    elif 'm' in t:
        seconds_total += n * 60
    else:
        seconds_total += n
minutes_total = seconds_total // 60
print(minutes_total)
