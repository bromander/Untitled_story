
label start:
    python:
        if not hasattr(persistent, "is_sees_tut"):
            persistent.is_sees_tut = False
    if not persistent.is_sees_tut:
        scene bg tutor 1
        $ renpy.pause()
        scene bg tutor 2
        $ renpy.pause()
        scene bg tutor 3
        $ renpy.pause()
        $ persistent.is_sees_tut = True

    jump start_part1

    $ renpy.sound.play("bg/silent_hill_2_Akira Yamaoka - A World Of Madness.mp3", channel="music", loop=True, relative_volume=0.1)
    #show screen note("note2")
    show screen show_scene(50, 50, "jack_room", True)



    j_sad "Вспоминаю те времена с моим бывшим..."
    j "У лукоморья дуб зелёный;
Златая цепь на дубе том:
И днём и ночью кот учёный
Всё ходит по цепи кругом;
Идёт направо - песнь заводит,
Налево - сказку говорит.
Там чудеса: там леший бродит,
Русалка на ветвях сидит;
Там на неведомых дорожках
Следы невиданных зверей;
Избушка там на курьих ножках
Стоит без окон, без дверей;
Там лес и дол видений полны;
Там о заре прихлынут волны
На брег песчаный и пустой,
И тридцать витязей прекрасных
Чредой из вод выходят ясных,
И с ними дядька их морской;
Там королевич мимоходом
Пленяет грозного царя;
Там в облаках перед народом
Через леса, через моря
Колдун несёт богатыря;
В темнице там царевна тужит,
А бурый волк ей верно служит;
Там ступа с Бабою Ягой
Идёт, бредёт сама собой,
Там царь Кащей над златом чахнет;
Там русский дух... там Русью пахнет!
И там я был, и мёд я пил;
У моря видел дуб зелёный;
Под ним сидел, и кот учёный
Свои мне сказки говорил."
    j "У лукоморья дуб зелёный;
Златая цепь на дубе том:
И днём и ночью кот учёный
Всё ходит по цепи кругом;
Идёт направо - песнь заводит,
Налево - сказку говорит.
Там чудеса: там леший бродит,
Русалка на ветвях сидит;
Там на неведомых дорожках
Следы невиданных зверей;
Избушка там на курьих ножках
Стоит без окон, без дверей;
Там лес и дол видений полны;
Там о заре прихлынут волны
На брег песчаный и пустой,
И тридцать витязей прекрасных
Чредой из вод выходят ясных,
И с ними дядька их морской;
Там королевич мимоходом
Пленяет грозного царя;
Там в облаках перед народом
Через леса, через моря
Колдун несёт богатыря;
В темнице там царевна тужит,
А бурый волк ей верно служит;
Там ступа с Бабою Ягой
Идёт, бредёт сама собой,
Там царь Кащей над златом чахнет;
Там русский дух... там Русью пахнет!
И там я был, и мёд я пил;
У моря видел дуб зелёный;
Под ним сидел, и кот учёный
Свои мне сказки говорил."
    d_unknown "я типо неизвесный инвалид"
    d_semidead "я типо полумёртвый инвалид"
    d_sad "Вспоминаю те времена с моим бывшим..."
    d_angry "Да как он только мог?"

    return

label sigma_masturbistor:
    image pompa = "sprites/sigma_masturbistor/unnamed.jpg"
    image sticker1 = "sprites/sigma_masturbistor/sticker1.png"
    image sticker2 = "sprites/sigma_masturbistor/sticker2.webp"
    image sticker3 = "sprites/sigma_masturbistor/sticker3.webp"
    image sticker4 = "sprites/sigma_masturbistor/sticker4.jpg"
    image sticker5 = "sprites/sigma_masturbistor/sticker5.webp"
    image sticker6 = "sprites/sigma_masturbistor/sticker6.webp"
    image sticker7 = "sprites/sigma_masturbistor/sticker7.webp"
    image sticker8 = "sprites/sigma_masturbistor/sticker8.jpg"
    image sticker9 = "sprites/sigma_masturbistor/sticker9.png"
    image sticker10 = "sprites/sigma_masturbistor/sticker10.jpg"
    image sticker11 = "sprites/sigma_masturbistor/sticker11.png"
    image sticker12 = "sprites/sigma_masturbistor/sticker12.jpg"

    init python:
        def play_skala():
            import random
            files = ["vine-boom.mp3", "lobotomy-sound-effect.mp3"]

            renpy.sound.play(f"sigma_masturbistor/{random.choice(files)}", channel="sound", loop=False, relative_volume=0.4)

    $ renpy.sound.play("sigma_masturbistor/hopen.mp3", channel="music", loop=False)

    transform scream:
        xalign 0.5
        yalign 0.5
        zoom 0.0
        linear 2.0 zoom 20.0


    init python:
        def get_randoms():
            import random
            _xalign = random.randint(1, 10) / 10
            _yalign = random.randint(0, 10) / 10
            _zoom = random.randint(3, 6) / 10
            return _xalign, _yalign, _zoom

    transform random_small_image(_xalign, _yalign, _zoom):
        xalign _xalign
        yalign _yalign
        zoom 0.0
        linear 2 zoom _zoom


    scene bg room
    $ renpy.sound.play("sigma_masturbistor/half-life-skrimer.ogg", channel="sound", loop=False)

    show pompa at scream

    pause 2.0


    $ play_skala()
    show sticker1 at random_small_image(*get_randoms())
    pause 1
    $ play_skala()
    show sticker2 at random_small_image(*get_randoms())
    pause 1
    $ play_skala()
    show sticker3 at random_small_image(*get_randoms())
    pause 1
    $ play_skala()
    show sticker4 at random_small_image(*get_randoms())
    pause 1
    $ play_skala()
    show sticker5 at random_small_image(*get_randoms())
    pause 1
    $ play_skala()
    show sticker6 at random_small_image(*get_randoms())
    pause 1
    $ play_skala()
    show sticker7 at random_small_image(*get_randoms())
    pause 1
    $ play_skala()
    show sticker8 at random_small_image(*get_randoms())
    pause 1
    $ play_skala()
    show sticker9 at random_small_image(*get_randoms())
    pause 1
    $ play_skala()
    show sticker10 at random_small_image(*get_randoms())
    pause 1
    $ play_skala()
    show sticker11 at random_small_image(*get_randoms())
    pause 1
    $ play_skala()
    show sticker12 at random_small_image(*get_randoms())
    pause 1

    ""

    $ renpy.quit()