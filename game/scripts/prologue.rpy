# prologue
label start:

    show screen prologue_screen

    play audio prologue_voice

    $ subtitle_text = "One day was all it took. I woke up, and my world had been ripped apart."
    $ renpy.restart_interaction()
    $ renpy.pause(5.0, hard=True)

    $ subtitle_text = "My home, my life — gone, like a cruel joke I wasn’t in on."
    $ renpy.restart_interaction()
    $ renpy.pause(5.2, hard=True)

    $ subtitle_text = "No warnings, no signs, just a void where everything used to be."
    $ renpy.restart_interaction()
    $ renpy.pause(6.0, hard=True)

    $ subtitle_text = "I tried to understand, to make sense of it, but there was nothing left to hold on to."
    $ renpy.restart_interaction()
    $ renpy.pause(6.0, hard=True)

    $ subtitle_text = "Just me, standing in the wreckage of what used to be real."
    $ renpy.restart_interaction()
    $ renpy.pause(4.0, hard=True)

    $ subtitle_text = "Now, all I have are questions. But there are no answers."
    $ renpy.restart_interaction()
    $ renpy.pause(6.0, hard=True)

    hide screen prologue_screen
    stop audio

    # Pub enter scene
    scene bg pub_enter with fade
    call screen pub_enter_screen
