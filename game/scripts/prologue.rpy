# prologue
define p = Character("player", color="#20703fff")
define v = Character("Viktor", color="#7804bbff", image="viktor")
define s = Character("Scarlet", color="#2e356dff", image="vakt")
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
    # scene bg car_1 with fade
    # pause 1.5

    # scene bg car_2
    # street_boss "Раз ты сел в машину, значит, хочешь изменить свою жизнь."
    # street_boss "Жить, как человек, а не выживать, как дворовая крыса?"

    # scene bg car_3
    # player "Иногда крысы честнее людей."

    # scene bg car_4
    # street_boss "…Согласен. Но крыса без стаи долго не протянет."
    # street_boss "Я могу дать тебе шанс. Крышу над головой, работу."

    # scene bg car_5
    # player "Что за работа?"
    # street_boss "Я держу паб.\n{p}{cps=50}Мне нужен человек, который не боится грязной и тяжёлой работы. {w}Который всегда на месте.{/cps}"

    # scene bg car_6
    # player "Я голоден. Не спал несколько дней. {w}Это всё равно лучше, чем улица."
    # player "Где я буду жить?"

    # scene bg car_4
    # street_boss "В подвале под пабом. {p}Лучше, чем картонка в переулке, не так ли?"

    # scene bg car_7
    # player "…Да."

    # scene bg car_8
    # pause 1.5

    # scene bg car_4
    # street_boss "Мы скоро выезжаем."
    # street_boss "У тебя есть кто-то? Семья? Любимый человек?"

    # scene bg car_6
    # player "Нет. {w}Я сам по себе."

    # scene bg car_5
    # street_boss "Может, это ещё можно исправить. Но мне нужна твоя полная отдача."
    # street_boss "Я предлагаю тебе вторую жизнь, но ты должен оправдать моё доверие."

    # scene bg car_3
    # player "Я не хочу возвращаться на улицу."

    # scene bg car_4
    # street_boss "Тогда всё зависит только от тебя."

    # scene bg car_8
    # pause 1
    # scene bg car_9
    # pause 1
    # street_boss "У нас мало времени! Поехали. Нам нужно закончить это сегодня."
    
    scene bg pub_enter with fade

    show viktor n
    with dissolve

    v @ n t '''
    Мы на месте. Это твой будущий дом

    Какое у тебя имя?

    '''
    p "Меня зовут Игрок"

    v @ n t '''
    Меня Виктор, с этого дня я твой босс!
    
    Я тебе сейчас все покажу!
    '''
    show viktor n at right
    with move

    show vakt 
    with easeinleft
    s @ a '''
    ШЕФ!
    
    Что это за помойная крыса, опять попрошайка, мне её выкинуть отсюда? 
    
    '''
    show viktor n at default
    with move
    show vakt at left
    with move
    v @ n t ''' 
    Успокойся Скарлет, теперь Игрок работает в моём пабе. 

    Так что запомни его и не перепутай с каким-то мусором в следующий раз!

    Думаю, Игрок будет выглядеть лучше в скором времени 

    '''
    s @ a "Что, он распугает всех гостей своим видом"
    v @ n t '''
    Сейчас только ты распугиваешь мой персонал!

    Успокойся, и относись с уважением к нашему новому колеге
    '''
    s @ a "Я Скарлет, я здесь охраняю твою жопу, от наших любимых гостей"
    v @ n t "Иди работай хватит болтать!"
    s @ a "Хммa, не силино и хотелось"
    hide vakt 
    with moveoutleft
    v @ n t "Пошли во внутрь, у меня не так много времени"
    hide viktor with dissolve
    
    # Pub enter scene
    scene bg pub_enter
    call screen pub_enter_screen

