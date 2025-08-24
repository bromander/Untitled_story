
define slow_fade = Fade(1.5, 2, 3)

transform show_jack_at_right:
    ypos 160
    xalign 0.85
    xzoom -1


label start_part2:
    scene bg entrance light_on with fade
    $ renpy.music.play("bg/entrance/noise.ogg", channel="music", loop=True, relative_volume=2)
    pause 2

    narrator "Свет ламп накаливания..."
    narrator "Синяя, пыльная краска на стенах..."
    narrator "Запахи ухода за домашними животными доносятся из соседних квартир."
    narrator "Типичная хрущёвка."

    j "Когда ж я уже перееду..."
    scene bg entrance 2 with dissolve
    show j_jacket at show_jack_at_right with dissolve
    j "Хотя вопрос скорее... {w=0.2}\n{i}\"Когда эту хрущёвку отдадут под снос чтобы у меня больше не было причин откладывать этот момент\"{/i}."
    hide j_jacket

    scene bg entrance porch with slow_fade
    show j_jacket 2 at show_jack_at_right
    $ renpy.music.stop(channel='music', fadeout=0.6)
    $ renpy.sound.play("bg/Glowing_Snow.ogg", channel="music", loop=True, relative_volume=0.2)

    j "Так что ж мне нужно было..."

    hide j_jacket 2 with fade

    narrator "Под ногами что-то оказалось, и Джек споткнулся."

    show j_jacket_falling at show_jack_at_right with hpunch
    j_fast "А-А-А"
    hide j_jacket_falling with fade

    pause 2

    show j_jacket_sweat at show_jack_at_right with dissolve
    j_fast "Твою мать!{w=0.5} Кто это?"
    hide j_jacket_sweat with dissolve
    narrator "Джек поднялся на ноги и рассмотрел тело внимательней."

    narrator "То было тело человека ещё живого, судя по наличию у него дыхания... \n{w=1.0} и пьяного.. {w=0.3}судя по его запаху..."
    narrator "Самым пугающим было скорее то, что он был одет не по погоде. \n{w=0.3}Если слово \"одет\" тут вообще применимо. Учитывая погоду."
    narrator "Пара сланцев, шорты, да дебильная футболка. {w=0.3}Ну и неряшливый вид немытых длинных волос наводит не на самые приятные мысли о его состоянии."
    narrator "Хуже было только то, что он был бледный и холодный и то,\n что он близок к обморожению."

    show j_jacket_scared with dissolve
    j_fast "Охренеть! Он же тут замёрзнет... \n{w=0.5}Не хватало ещё чтобы перед домом кто-то умер!"
    $ renpy.sound.stop(channel='sound', fadeout=5)
    j "Н-но что же мне делать?"
    jump what_jack_wil_do_omg

define try_part2_call_an_ambulance = False
define try_part2_try_wake_up = False
define try_part2_kick_wake_up = False
define try_part2_ignore = False

label what_jack_wil_do_omg:
    show j_jacket_scared with dissolve
    scene bg entrance porch
    menu:
        "Н-но что же мне делать?"
        "Позвонить в скорую" if not try_part2_call_an_ambulance:
            $ try_part2_call_an_ambulance = True
            jump part2_call_an_ambulance

        "Попытаться разбудить" if not try_part2_try_wake_up:
            $ try_part2_try_wake_up = True
            jump part2_try_wake_up

        "Пнуть чтобы разбудить" if not try_part2_kick_wake_up and try_part2_try_wake_up:
            $ try_part2_kick_wake_up = True
            jump part2_kick_wake_up

        "Проигнорировать и пойти дальше по своим делам" if not try_part2_ignore and try_part2_try_wake_up and try_part2_call_an_ambulance:
            $ try_part2_ignore = True
            jump part2_ignore

        "Помочь человеку, занеся его домой" if try_part2_try_wake_up and try_part2_call_an_ambulance:
            jump part2_help_to_home


