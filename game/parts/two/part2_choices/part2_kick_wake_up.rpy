

label part2_kick_wake_up:
    scene bg entrance porch
    hide j_jacket_scared with dissolve
    show j_jacket_angry at show_jack_at_right with dissolve
    $ renpy.music.stop(channel='music', fadeout=5)
    'Джек пинает тело... \nтело отзывается звуками лёгкого хруста и задыхающегося человека'
    j_angry 'Проснись дебил! Ты тут сдохнуть хочешь?!'
    $ renpy.music.play("bg/Tinnitus.ogg", channel="music", loop=True, relative_volume=0.8, fadein=25)
    hide j_jacket_angry
    '\"Тут дальше должна быть сцена или несколько кадров, изображающие дебилыча, нападающего на джека\"'
    'Хочешь забавный факт? \nОт удушения ты не чувствуешь боль, скорее всего это от начинающегося кислородного голодания.'
    'Отчасти ты ловишь себя на мысли что это когда-нибудь закончится. \nТы вновь почувствуешь облегчение и даже небольшое удовольствие от осознания что ты жив, но скоро ощущаешь жуткую боль в шее и в спине.'
    narrator_creepy '{cps=5}{size=+60}{color=#ff0000}{b}... НО       ЭТО       НЕ        КОНЧАЕТСЯ ...{/b}{/color}{/size}{/cps}'
    narrator_creepy '{alpha=0.9}{cps=14}{color=#CF0000}{b}Теперь тебя окутывает страх от потемнения в глазах. \nБлеклая виньетка закрывает твой обзор фокусируя его на глазах того кто держит тебя сейчас за горло.{/b}{/color}{/cps}{/alpha}'
    narrator_creepy '{alpha=0.7}{cps=12}{color=#A80000}{b}Никак не вдохнуть? \nСтрах перетекает в панику? \nПаника переходит в судороги? \nВ тебя вцепились не руки а холодная сталь, которую нельзя убрать.{/b}{/color}{/cps}{/alpha}'
    narrator_creepy '{alpha=0.5}{cps=10}{color=#5C0000}{b}То что ты чувствуешь - нельзя назвать болью... \nЭто первобытный ужас вызванный твоей же беспомощностью... \nУже ничто не беспокоит тебя кроме воздуха... \nВсё кончено...{/b}{/color}{/cps}{/alpha}'
    narrator_creepy '{alpha=0.5}{cps=5}{size=+40}{color=#2B0000}{b}Ты... Ничто...{/b}{/color}{/size}{/cps}{/alpha}'
    $ renpy.sound.play("sfx/ominous.mp3", channel="sound", loop=False, relative_volume=1)
    narrator_creepy '{alpha=0.5}{cps=5}{size=+40}{color=#5C1515}{b}КОНЕЦ{/b}{/color}{/size}{/cps}{/alpha}'