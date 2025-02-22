screen prologue_screen():

    add Movie(play="video/prologue.webm", fit="contain")

    text subtitle_text style "video_subtitles"


screen pub_enter_screen():
    imagebutton:
        xalign(0.5325)
        yalign(0.9424)
        idle "images/prologue/door_btn_idle.png"
        hover "images/prologue/door_btn_hover.png"
        hover_sound "audio/door_opens_sound.mp3"
        #hovered (Function(renpy.music.play, "audio/door_opens_sound.mp3", channel="sound", loop=False))
        action Jump("mock")