label ch_1:
    play music playlist_1 volume 0.8 loop
    scene black
    show text "Chapter 1: The Pub!" with fade
    pause 2.0

    play audio inside_pub_sounds volume 0.3 loop
    scene bg main_ch1
    
    pause 50.0
    stop music
    return 