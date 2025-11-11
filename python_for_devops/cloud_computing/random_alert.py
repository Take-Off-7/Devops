from random import choice


hours = range(1, 25)
status = ["Alert", "No Alert"]

for hour in hours:
    alert = choice(status)
    print(f"Hour: {hour} -- {alert}")

