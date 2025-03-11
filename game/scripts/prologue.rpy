# prologue
label start:

    show screen prologue_screen

    play audio prologue_voice

    # Block for showing prologue subtitles
    $ show_subtitles(subtitles="One day was all it took. I woke up, and my world had been ripped apart.", sec=5.0)
    $ show_subtitles(subtitles="My home, my life — gone, like a cruel joke I wasn’t in on.", sec=5.2)
    $ show_subtitles(subtitles="No warnings, no signs, just a void where everything used to be.", sec=6.0)
    $ show_subtitles(subtitles="I tried to understand, to make sense of it, but there was nothing left to hold on to.", sec=6.0)
    $ show_subtitles(subtitles="Just me, standing in the wreckage of what used to be real.", sec=4.0)
    $ show_subtitles(subtitles="Now, all I have are questions. But there are no answers.", sec=6.0)

    hide screen prologue_screen
    stop audio

    # Pub enter scene
    scene bg pub_enter with fade
    call screen pub_enter_screen

