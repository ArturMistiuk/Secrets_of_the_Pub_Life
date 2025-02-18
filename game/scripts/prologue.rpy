# prologue

label start:

    show screen prologue_screen

    play audio prologue_voice

    $ subtitle_text = "How did it come to this? I had a job. A home. People who cared."
    $ renpy.restart_interaction()
    $ renpy.pause(6.0, hard=True)

    $ subtitle_text = "Or at least, I thought they did."
    $ renpy.restart_interaction()
    $ renpy.pause(4.0, hard=True)

    # $ subtitle_text = "One wrong turn. One bad decision. And now?"
    # $ renpy.restart_interaction()
    # $ renpy.pause(4.0, hard=True)

    # $ subtitle_text = "Now I’m just another shadow on the sidewalk."
    # $ renpy.restart_interaction()
    # $ renpy.pause(3.0, hard=True)

    # $ subtitle_text = "Do they even see me? Do they even care? I don’t think so. I am a mess."
    # $ renpy.restart_interaction()
    # $ renpy.pause(6.0, hard=True)
    
    return
