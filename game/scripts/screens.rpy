screen prologue_screen():

    add Movie(play="video/prologue.webm", fit="contain")

    text subtitle_text style "video_subtitles"


screen pub_enter_screen():
    imagebutton:
        xalign(DOOR_BTN_XALIGN)
        yalign(DOOR_BTN_YALIGN)
        idle "images/prologue/door_btn_idle.jpg"
        hover "images/prologue/door_btn_hover.jpg"
        hover_sound "audio/door_opens_sound.mp3"
        action [Stop("music"), Jump("ch_1")]
        