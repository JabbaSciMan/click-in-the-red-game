input.onButtonPressed(Button.A, function () {
    button_logic(Score_A, true)
})
function clearShow () {
    basic.pause(200)
    strip.clear()
    strip.show()
    basic.pause(200)
}
input.onButtonPressed(Button.B, function () {
    button_logic(Score_B, false)
})
function button_logic (Sc_A: number, bool2: boolean) {
    Continue = false
    if (Begin - 0 <= X && X <= Begin + R1 - 0) {
        X = 1
        if (bool2) {
            Score_A += 1
        } else {
            Score_B += 1
        }
        Begin += 1
        R1 += -2
        music.playTone(523, music.beat(BeatFraction.Quarter))
        for (let index = 0; index < 4; index++) {
            strip.showRainbow(1, 360)
            clearShow()
        }
        basic.showNumber(Sc_A)
        if (R1 < 1) {
            music.startMelody(music.builtInMelody(Melodies.Entertainer), MelodyOptions.Once)
            for (let index = 0; index < 20; index++) {
                strip.showRainbow(1, 360)
                clearShow()
            }
            if (Players) {
                Range_A = strip.range(0, Score_A)
                Range_B = strip.range(Length_of_strip - Score_B, Score_B)
                Range_A.showColor(neopixel.colors(NeoPixelColors.Red))
                Range_B.showColor(neopixel.colors(NeoPixelColors.Red))
                basic.pause(5000)
            }
            reset()
        }
    } else if (Players) {
        basic.showIcon(IconNames.Sad)
        music.playTone(262, music.beat(BeatFraction.Whole))
    } else {
        music.startMelody(music.builtInMelody(Melodies.Funeral), MelodyOptions.Forever)
        if (Players) {
            if (Score_A > Score_B) {
                basic.showNumber(Score_A)
            } else {
                basic.showNumber(Score_B)
            }
        } else {
            basic.showNumber(Sc_A)
        }
        for (let index = 0; index < 10; index++) {
            strip.showColor(neopixel.colors(NeoPixelColors.Red))
            clearShow()
        }
        reset()
    }
    Continue = true
}
input.onLogoEvent(TouchButtonEvent.Pressed, function () {
    Players = true
    basic.showLeds(`
        # . . . #
        . . . . .
        . . . . .
        . . . . .
        . . . . .
        `)
})
function reset () {
    Dir = 1
    Score_A = 0
    X = 1
    Length_of_strip = 60
    strip = neopixel.create(DigitalPin.P13, Length_of_strip, NeoPixelMode.RGB)
    Begin = 20
    R1 = 21
    Continue = true
    music.stopMelody(MelodyStopOptions.All)
    Players = false
}
let range2: neopixel.Strip = null
let Dir = 0
let Length_of_strip = 0
let Range_B: neopixel.Strip = null
let Range_A: neopixel.Strip = null
let Players = false
let R1 = 0
let X = 0
let Begin = 0
let Continue = false
let Score_B = 0
let strip: neopixel.Strip = null
let Score_A = 0
music.playTone(262, music.beat(BeatFraction.Whole))
reset()
basic.forever(function () {
    if (!(input.buttonIsPressed(Button.A)) && R1 > 0 && Continue && !(input.buttonIsPressed(Button.B))) {
        strip.clear()
        range2 = strip.range(Begin, R1)
        range2.showColor(neopixel.colors(NeoPixelColors.Red))
        X += Dir * 2
        strip.setPixelColor(X, neopixel.colors(NeoPixelColors.Green))
        strip.show()
        if (X < 0 || X > Length_of_strip) {
            Dir = Dir * -1
        }
    }
})
