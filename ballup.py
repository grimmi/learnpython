'''
You throw a ball vertically upwards with an initial speed v (in km per hour).
The height h of the ball at each time t is given by h = v*t - 0.5*g*t*t
where g is Earth's gravity (g ~ 9.81 m/s**2). A device is recording at every
tenth of second the height of the ball. For example with v = 15 km/h the device gets
something of the following form: (0, 0.0), (1, 0.367...), (2, 0.637...), (3, 0.808...), (4, 0.881..)
where the first number is the time in tenth of second and the second number the height in meter.

Task

Write a function max_ball with parameter v (in km per hour) that returns the time in tenth of
second of the maximum height recorded by the device.

Examples:

max_ball(15) should return 4

max_ball(25) should return 7

Notes

Remember to convert the velocity from km/h to m/s or from m/s in km/h when necessary.
The maximum height recorded by the device is not necessarily the maximum height reached by the ball.
'''

# km/h -> 1000m / 3600s -> 1/3.6 m/s
# 10 km/h -> 10 * (1000m / 3600s) -> 10'000m/3600s -> 10/3.6 m/s

def max_ball(v0):

    tenth = 0
    max_height = 0
    for x in iter(int, 1):
        tenth += 1
        t = tenth / 10
        step_height = ((v0 / 3.6) * t) - (0.5 * 9.81 * t * t)
        if step_height < max_height:
            break
        else:
            max_height = step_height
    
    return tenth - 1

    # def to_kmh(ms):
    #     return ms * 3.6

    # def to_ms(kmh):
    #     return kmh / 3.6
    
    # for t in range(0, 6):
    #     s = t / 10
    #     vt = to_ms(v0) * s
    #     gt = 0.5 * (9.81) * s * s
    #     h = vt - gt
    #     print("t: " + str(t))
    #     print("vt: " + str(vt))
    #     print("gt: " + str(gt))
    #     print("h: " + str(h))

print(max_ball(15))

