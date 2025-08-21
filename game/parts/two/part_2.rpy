
define slow_fade = Fade(1.5, 2, 3)

label start_part2:
    scene entrance
    $ renpy.music.play("bg/entrance/noise.ogg", channel="music", loop=True)
    pause 2

    narrator "Свет ламп накаливания..."
    narrator "Зелёная, пыльная краска на стенах..."
    narrator "Запахи ухода за домашними животными доносятся из соседних квартир."
    narrator "Типичная хрущевка"

    j "Когда ж я уже перееду..."
    show j_jacket with dissolve
    j "Хотя вопрос скорее... {w=0.2}\n{i}\"Когда эту хрущевку отдадут под снос чтобы у меня больше не было причин откладывать этот момент\"{/i}"
    hide j_jacket

    scene entrance
    show j_jacket with slow_fade
    $ renpy.music.stop(channel='music', fadeout=0.6)

    j "Так что ж мне нужно было..."

    $ renpy.sound.play("sfx/echo_walk.ogg", channel="sound", loop=True)
    hide j_jacket
    pause 5.0

    $ renpy.sound.stop(channel='sound', fadeout=1)

    narrator_small "Под ногами что-то оказалось и джек споткнулся"

    show j_falling with hpunch
    j_fast "А-А-А"
    hide j_fast with fade

    scene entrance porch
    $ renpy.sound.play("bg/flicker.mp3", channel="sound", loop=True, relative_volume=0.2)
    pause 2

    show j_jacket_scared with dissolve
    j_fast "Твою мать!{w=0.5} Кто это!"
    narrator_small "Джек поднялся на ноги и рассмотрел тело внимательней"
    hide j_jacket_scared with dissolve

    narrator_small "То было тело человека ещё живого, судя по наличию у него дыхания... \n{w=1.0}И пьяным.. {w=0.3}судя по запаху..."
    narrator_small "Самым пугающим было скорее то, что он был одет не по погоде. \n{w=0.3}Если слово \"Одет\" тут вообще применимо. учитывая погоду."
    narrator_small "Пара сланцев, шорты, да дебильная футболка. {w=0.3}Ну и неряшливый вид немытых длинных волос наводит не на самые приятные мысли о его состоянии."
    narrator_small "Хуже всего было только то, что он был бледный и холодный и то,\n что он близок к обморожению."

    show j_jacket_scared with dissolve
    j_fast "Охренеть! Он же тут замерзнет... \n{w=0.5}Не хватало ещё чтобы перед домом кто-то умер!"
    $ renpy.sound.stop(channel='sound', fadeout=5)
    j "Н-но что же мне делать?"
    jump what_jack_wil_do_omg


label what_jack_wil_do_omg:
    show j_jacket_scared with dissolve
    scene entrance porch

    menu:
        "Позвонить в скорую":
            jump part1_call_an_ambulance

        "Попытаться разбудить":
            jump part1_try_wake_up

        "Пнуть чтобы разбудить":
            jump part1_kick_wake_up

        "Проигнорировать и пойти дальше по своим делам":
            jump part1_ignore

        "Помочь Человеку занеся его домой":
            jump part1_help_to_home

