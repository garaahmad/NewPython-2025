
# -OR-
temp = 50
is_raining = False
if temp > 35 or temp < 0 or is_raining:
    print('The outdoor event is cancelled')
else:
    print('the outdoor event is still scheduled')
    
temp = 25
is_sunny = True
if temp >= 28 and is_sunny:
    print('it is HOT outside')
    print('it is SUNNY')
elif temp <= 0 and is_sunny:
    print('It is COLD outside')
    print('it is SUNNY')
elif temp <28 and temp > 0 and is_sunny:
    print('It is WARM outside')
    print('it is SUNNY')
elif temp >= 28 and not is_sunny:
    print('it is HOT outside')
    print('it is CLOUDY')
elif temp <= 0 and not is_sunny:
    print('It is COLD outside')
    print('it is CLOUDY')
elif temp <28 and temp > 0 and not is_sunny:
    print('It is WARM outside')
    print('it is CLOUDY')