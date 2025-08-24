

label part2_kick_wake_up:
    scene bg entrance porch
    hide j_jacket_scared with dissolve
    show j_jacket_angry at show_jack_at_right with dissolve
    $ renpy.music.stop(channel='music', fadeout=5)
    'Джек пинает тело... \nтело отзывается звуками лёгкого хруста и задыхающегося человека.'
    j_angry 'Проснись, дебил! Ты тут сдохнуть хочешь?!'
    hide j_jacket_angry
    
    $ renpy.sound.play ("snow_sound.mp3")
    scene bg fight 1
    $ renpy.pause(delay = 2)
    
    $ renpy.sound.play ("hit.mp3")
    scene bg fight 2
    $ renpy.music.play("bg/Tinnitus.ogg", channel="music", loop=True, relative_volume=0.8, fadein=25)
    $ renpy.pause(delay = 1)

    scene bg fight 3
    $ renpy.sound.play ("snow_sound.mp3")
    $ renpy.pause(delay = 0.5)
    scene bg fight 4 with dissolve
    $ renpy.pause(delay = 0.5)
    scene bg fight 3 with dissolve
    $ renpy.pause(delay = 0.5)


    $ quick_menu = False
    $ _game_menu_screen = None
    scene bg fight 5
    $ renpy.sound.play ("strangled_voice.mp3", relative_volume=0.4)
    'Хочешь забавный факт? \nОт удушения ты не чувствуешь боль, скорее всего это от начинающегося кислородного голодания.'
    'Отчасти ты ловишь себя на мысли что это когда-нибудь закончится. \nТы вновь почувствуешь облегчение и даже небольшое удовольствие от осознания что ты жив, но скоро ощущаешь жуткую боль в шее и в спине.'
    narrator_creepy '{shader=jitter:u__jitter=5.0, 5.0}{cps=5}{size=+60}{color=#ff0000}{b}... НО       ЭТО       НЕ        КОНЧАЕТСЯ ...{/b}{/color}{/size}{/cps}'
    scene bg fight 6
    narrator_creepy '{shader=jitter}{alpha=0.9}{cps=14}{color=#C90000}{b}Теперь тебя окутывает страх от потемнения в глазах. \nБлеклая виньетка закрывает твой обзор фокусируя его на глазах того кто держит тебя сейчас за горло.{/b}{/color}{/cps}{/alpha}'
    nvl clear
    narrator_creepy '{shader=jitter:u__jitter=15.0, 15.0}{fast}{size=+60}{color=#ff0000}{b}{fast}... НО       ЭТО       НЕ        КОНЧАЕТСЯ ...{/b}{/color}{/size}{nw}'
    narrator_creepy '{shader=jitter}{alpha=0.7}{cps=12}{color=#9C0000}{b}Никак не вдохнуть? \nСтрах перетекает в панику? \nПаника переходит в судороги? \nВ тебя вцепились не руки а холодная сталь, которую нельзя убрать.{/b}{/color}{/cps}{/alpha}'
    nvl clear
    scene bg blackscreen with fade
    narrator_creepy '{shader=jitter:u__jitter=25.0, 25.0}{fast}{size=+60}{color=#ff0000}{b}{fast}... НО       ЭТО       НЕ        КОНЧАЕТСЯ ...{/b}{/color}{/size}{nw}'
    narrator_creepy '{shader=jitter}{alpha=0.5}{cps=10}{color=#6E0000}{b}То что ты чувствуешь - нельзя назвать болью... \nЭто первобытный ужас вызванный твоей же беспомощностью... \nУже ничто не беспокоит тебя кроме воздуха... \nВсё кончено...{/b}{/color}{/cps}{/alpha}'
    nvl clear
    narrator_creepy '{shader=jitter:u__jitter=35.0, 35.0}{fast}{size=+60}{color=#ff0000}{b}{fast}... НО       ЭТО       НЕ        КОНЧАЕТСЯ ...{/b}{/color}{/size}{nw}'
    narrator_creepy '{shader=jitter}{alpha=0.5}{cps=5}{size=+40}{color=#4A0000}{b}Ты... Ничто...{/b}{/color}{/size}{/cps}{/alpha}'
    nvl clear
    $ renpy.sound.play("sfx/ominous.mp3", channel="sound", loop=False, relative_volume=1)
    $ my_jitter_strength = 25.0
    while True:
        narrator_creepy '{shader=jitter:u__jitter=[my_jitter_strength], [my_jitter_strength]}{fast}{size=+45}{color=#ff0000}{b}... НО       ЭТО       НЕ        КОНЧАЕТСЯ ...{/b}{/color}{/size}{nw}'
        $ my_jitter_strength += 5