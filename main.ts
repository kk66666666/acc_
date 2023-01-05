function doSomething () {
    music.playSoundEffect(music.createSoundEffect(WaveShape.Square, 5000, 0, 255, 0, 500, SoundExpressionEffect.None, InterpolationCurve.Linear), SoundExpressionPlayMode.UntilDone)
    basic.pause(1000)
    x = randint(0, 4)
    y = randint(0, 4)
    targetx = randint(0, 4)
    targety = randint(0, 4)
    led.plot(targetx, targety)
    led.plot(x, y)
}
let accy = 0
let accx = 0
let targety = 0
let targetx = 0
let y = 0
let x = 0
let samexy = 1
doSomething()
basic.forever(function () {
    samexy = 1
    while (targetx == 2 && targety == 2) {
        targetx = randint(0, 4)
        targety = randint(0, 4)
    }
    accx = input.acceleration(Dimension.X)
    accy = input.acceleration(Dimension.Y)
    if (targetx == x && targety == y) {
        basic.clearScreen()
        samexy = 0
        doSomething()
    }
    if (accx > 300 && x > 0) {
        x += -1
    }
    if (accx < -300 && x < 4) {
        x += 1
    }
    if (accy > 300 && y > 0) {
        y += -1
    }
    if (accy < -300 && y < 4) {
        y += 1
    }
    if (samexy) {
        basic.clearScreen()
        led.plot(x, y)
        led.plot(targetx, targety)
    }
    basic.pause(300)
})
