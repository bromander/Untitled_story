

label part2_help_to_home:
    scene bliss with dissolve
    hide j_jacket_scared with dissolve
    show j_jacket 3 at show_jack_at_right with dissolve
    j "Делать нечего, придётся помогать."
    'Джек поднял почти полностью обмороженное тело, закинув его руку себе на плечо, и понёс его в дом.'
    $ renpy.music.stop(channel='music', fadeout=2)
    $ renpy.music.play("bg/entrance/noise.ogg", channel="music", loop=True, relative_volume=2)
    scene bg entrance with fade
    show j_jacket_angry at show_jack_at_right with dissolve
    'Сколько бы Джек не тыкал кнопки, двери лифта не открывались, а привода не гудели!'
    j_angry 'ДА ТВОЮ МАТЬ! \nЕЩЁ И ЛИФТ НЕ РАБОТАЕТ!'
    j_angry 'Дрыхнешь, да?! \n{w=0.3}Ты как бы тяжёлый! \n{w=0.2}ЭЭЭЭЭЭХ!'
    'Смирившись со своей участью, Джек поднялся на свой этаж с жертвой общества потребления на своих могучих плечах.'
    jump start_part3