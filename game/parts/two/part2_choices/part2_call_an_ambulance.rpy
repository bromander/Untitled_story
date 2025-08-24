

label part2_call_an_ambulance:
    scene bg entrance porch
    hide j_jacket_scared with dissolve
    show j_jacket_calling with dissolve

    $ beeps = renpy.random.randint(2, 5)
    $ index = 0
    while index < beeps:
        $ index += 1
        $ renpy.sound.play("sfx/phone/calling.ogg", channel="sound", loop=False, relative_volume=0.5)
        narrator "{i}*идут гудки*{/i}"
        python:
            if renpy.random.randint(0, 1) == 1:
                is_sweat = True
            else:
                is_sweat = False
        if is_sweat:
            hide j_jacket_calling
            show j_jacket_calling_sweat

    $ renpy.sound.play("sfx/phone/reset.mp3", channel="sound", loop=False, relative_volume=0.5)

    hide j_jacket_calling_sweat
    hide j_jacket_calling
    show j_jacket_calling_sweat_very

    j_fast "Да черт бы побрал бурю и связь!"

    hide j_jacket_calling_sweat_very
    show j_jacket_calling_evil

    $ renpy.sound.stop(channel='sound')

    j_fast "Ну тогда..."
    jump what_jack_wil_do_omg

