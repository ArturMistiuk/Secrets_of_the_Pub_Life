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
    pause 1.5

    scene bg car_2
    street_boss "Если ты сел в эту машину — значит, готов начать заново.{p}Жить, как человек, а не выживать, как дворовая крыса?"

    scene bg car_3
    player "Я видел, как поступают люди. {p}{w=0.3}Иногда и крысы выглядят благороднее."

    scene bg car_4
    street_boss "…Есть в этом правда. Но одиночка долго не выживает."
    street_boss "Я могу дать тебе шанс. Крышу над головой, работу."

    scene bg car_5
    player "Что за работа?"
    street_boss "Я держу паб. {w=0.3}Нужен человек, что не бежит от грязной работы. {w=0.3}Тот, кто умеет держать слово."

    scene bg car_6
    player "Я устал. Голоден. Не спал несколько ночей."
    player "Где я буду жить?"

    scene bg car_4
    street_boss "В подвале под пабом. Там не уютно, но теплее чем на улице."

    scene bg car_7
    player "…Да."

    scene bg car_4
    street_boss "Хорошо. Тогда начнём с простого"
    street_boss "Как тебя зовут?"
    $ player_name = renpy.input(prompt="Введите своё имя:")
    $ player_name = player_name.strip()
    if player_name == "":
        $ player_name = "Никто"

    player "[player_name]"

    street_boss "Хм… [player_name]. {w=0.3}Имя говорит больше, чем думаешь. {w=0.2}Запомню."

    scene bg car_8
    pause 1.5

    scene bg car_4
    street_boss "Мы скоро выезжаем."
    street_boss "У тебя есть кто-то? {w=0.3}Семья? {w=0.3}Любимый человек?"

    scene bg car_6
    player "Нет. Я сам по себе."

    scene bg car_5
    street_boss "Может, это ещё можно исправить. Но мне нужна твоя полная отдача."
    street_boss "Я предлагаю тебе вторую жизнь, но ты должен оправдать моё доверие."

    scene bg car_3
    player "Я не хочу возвращаться на улицу."

    scene bg car_4
    street_boss "Тогда всё зависит только от тебя."

    scene bg car_8
    pause 1
    scene bg car_9
    pause 1
    street_boss "У нас мало времени! Поехали. Нам нужно закончить это сегодня."

    # Pub enter scene
    scene bg pub_enter with fade
    call screen pub_enter_screen

