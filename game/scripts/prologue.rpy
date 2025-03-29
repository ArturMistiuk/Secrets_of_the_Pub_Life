# prologue
label start:

    #show screen prologue_screen

    #play audio prologue_voice

    # Block for showing prologue subtitles
    #$ show_subtitles(subtitles="One day was all it took. I woke up, and my world had been ripped apart.", sec=5.0)
    #$ show_subtitles(subtitles="My home, my life — gone, like a cruel joke I wasn’t in on.", sec=5.2)
    #$ show_subtitles(subtitles="No warnings, no signs, just a void where everything used to be.", sec=6.0)
    #$ show_subtitles(subtitles="I tried to understand, to make sense of it, but there was nothing left to hold on to.", sec=6.0)
    #$ show_subtitles(subtitles="Just me, standing in the wreckage of what used to be real.", sec=4.0)
    #$ show_subtitles(subtitles="Now, all I have are questions. But there are no answers.", sec=6.0)

    #hide screen prologue_screen
    #stop audio

    # Block of dialogue in the car
    scene bg car_1 with fade
    "............................................................................................................"

    scene bg car_2
    street_boss "Since you got in the car, you must have hit rock bottom."
    street_boss "Tired of eating scraps, huh?\nYou want to live like a man, not like a stray rat?"

    scene bg car_3
    player "Sometimes rats are more honest than people."

    scene bg car_4
    street_boss "Maybe.\nBut a rat without a pack is just prey."
    street_boss "I can give you a chance. A roof over your head, food, work. Choose."

    scene bg car_5
    player "What kind of work?"
    street_boss "Dirty. Hard. No days off."
    street_boss "I need someone who doesn’t ask questions and doesn’t ask for favors."

    scene bg car_6
    player "I'm starving. Haven't slept for days."
    player "This is still better than the streets.\nWhere will I live?"

    scene bg car_4
    street_boss "In the basement under the pub. Consider it your new home."

    scene bg car_7
    player "…Better than a dumpster."

    scene bg car_8
    "He checks his watch, shaking his head."

    scene bg car_4
    street_boss "Time’s running out."
    street_boss "Do you have any family? Anyone who cares about you?"

    scene bg car_6
    player "No. I’m on my own."

    scene bg car_5
    street_boss "Good. That means no one will miss you."
    street_boss "From now on, you’re my guy. And if you don’t mess up, maybe you’ll get a shot at something bigger."

    scene bg car_3
    player "I don’t want to go back to the streets."

    scene bg car_4
    street_boss "Then don’t make me regret this decision."

    scene bg car_9
    "He glances at his watch again, then suddenly knocks on the glass."
    street_boss "Let’s go. We don’t have time to waste."

    # Pub enter scene
    scene bg pub_enter with fade
    call screen pub_enter_screen

