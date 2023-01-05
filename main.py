def doSomething():
    global x, y, targetx, targety
    music.play_sound_effect(music.create_sound_effect(WaveShape.SQUARE,
            5000,
            0,
            255,
            0,
            500,
            SoundExpressionEffect.NONE,
            InterpolationCurve.LINEAR),
        SoundExpressionPlayMode.UNTIL_DONE)
    basic.pause(1000)
    x = randint(0, 4)
    y = randint(0, 4)
    targetx = randint(0, 4)
    targety = randint(0, 4)
    led.plot(targetx, targety)
    led.plot(x, y)
accy = 0
accx = 0
targety = 0
targetx = 0
y = 0
x = 0
samexy = 1
doSomething()

def on_forever():
    global samexy, targetx, targety, accx, accy, x, y
    samexy = 1
    while targetx == 2 and targety == 2:
        targetx = randint(0, 4)
        targety = randint(0, 4)
    accx = input.acceleration(Dimension.X)
    accy = input.acceleration(Dimension.Y)
    if targetx == x and targety == y:
        basic.clear_screen()
        samexy = 0
        doSomething()
    if accx > 300 and x > 0:
        x += -1
    if accx < -300 and x < 4:
        x += 1
    if accy > 300 and y > 0:
        y += -1
    if accy < -300 and y < 4:
        y += 1
    if samexy:
        basic.clear_screen()
        led.plot(x, y)
        led.plot(targetx, targety)
    basic.pause(300)
basic.forever(on_forever)

