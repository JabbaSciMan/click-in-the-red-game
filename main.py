def determine_winner():
    if Score_A > Score_B:
        basic.show_number(Score_A)
    else:
        basic.show_number(Score_B)

def on_button_pressed_a():
    button_logic(Score_A, True)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    button_logic(Score_B, False)
input.on_button_pressed(Button.B, on_button_pressed_b)

def button_logic(Sc_A: number, bool2: bool):
    global Continue, X, Score_A, Score_B, Begin, R1, Range_A, Range_B
    Continue = False
    if Begin - 0 <= X and X <= Begin + R1 - 0:
        X = 1
        if bool2:
            Score_A += 1
        else:
            Score_B += 1
        Begin += 1
        R1 += -2
        music.play_tone(523, music.beat(BeatFraction.QUARTER))
        for index in range(4):
            strip.show_rainbow(1, 360)
            basic.pause(200)
            strip.clear()
            strip.show()
            basic.pause(200)
        basic.show_number(Sc_A)
        if R1 < 1:
            music.start_melody(music.built_in_melody(Melodies.ENTERTAINER),
                MelodyOptions.ONCE)
            for index2 in range(20):
                strip.show_rainbow(1, 360)
                basic.pause(200)
                strip.clear()
                strip.show()
                basic.pause(200)
            basic.show_number(Sc_A)
    elif Players:
        basic.show_icon(IconNames.SAD)
        music.play_tone(262, music.beat(BeatFraction.WHOLE))
    else:
        music.start_melody(music.built_in_melody(Melodies.FUNERAL),
            MelodyOptions.FOREVER)
        if Players:
            determine_winner()
        else:
            basic.show_number(Sc_A)
        for index3 in range(10):
            if Players:
                Range_A = strip.range(0, Score_A)
                Range_B = strip.range(Length_of_strip - Score_B, Score_B)
            strip.show_color(neopixel.colors(NeoPixelColors.RED))
            basic.pause(200)
            strip.clear()
            strip.show()
            basic.pause(200)
        basic.pause(2000)
        reset()
    Continue = True

def on_logo_pressed():
    global Players
    Players = True
    basic.show_leds("""
        # . . . #
                . . . . .
                . . . . .
                . . . . .
                . . . . .
    """)
input.on_logo_event(TouchButtonEvent.PRESSED, on_logo_pressed)

def reset():
    global Dir, Score_A, X, Length_of_strip, strip, Begin, R1, Continue, Players
    Dir = 1
    Score_A = 0
    X = 1
    Length_of_strip = 60
    strip = neopixel.create(DigitalPin.P13, Length_of_strip, NeoPixelMode.RGB)
    Begin = 20
    R1 = 21
    Continue = True
    music.stop_melody(MelodyStopOptions.ALL)
    Players = False
range2: neopixel.Strip = None
Dir = 0
Length_of_strip = 0
Range_B: neopixel.Strip = None
Range_A: neopixel.Strip = None
strip: neopixel.Strip = None
Players = False
R1 = 0
X = 0
Begin = 0
Continue = False
Score_B = 0
Score_A = 0
music.play_tone(262, music.beat(BeatFraction.WHOLE))
reset()

def on_forever():
    global range2, X, Dir
    if not (input.button_is_pressed(Button.A)) and R1 > 0 and Continue and not (input.button_is_pressed(Button.B)):
        strip.clear()
        range2 = strip.range(Begin, R1)
        range2.show_color(neopixel.colors(NeoPixelColors.RED))
        X += Dir * 2
        strip.set_pixel_color(X, neopixel.colors(NeoPixelColors.GREEN))
        strip.show()
        if X < 0 or X > Length_of_strip:
            Dir = Dir * -1
basic.forever(on_forever)
