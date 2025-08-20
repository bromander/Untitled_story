#Здесь создаются все персонажи и их спрайты

init python:
    from pathlib import Path
    import os
    import random
    import renpy.exports as renpy_exports
    import threading
    import time

    i = 1
    e = 0

    def random_sounds(character_name):
        import time
        global i
        global e

        base = Path(renpy.config.basedir)
        path = base / "game" / "audio" / f"characters_voice/{character_name}"
        files = os.listdir(path)
        while True:
            if i == 1:
                if renpy.get_screen("say"):
                    e += 1
                    # Выбираем случайный файл
                    if files:
                        file_path = f"audio/characters_voice/{character_name}/{random.choice(files)}"
                        renpy.music.play(str(file_path).replace("\\", "/"), channel='voice', loop=False)
                    else:
                        print("В директории нет подходящих аудиофайлов.")
                    time.sleep(0.15)
            else:
                return None


    def character_sound(event, interact=True, character_name="jopa", **kwargs) -> None:
        global i
        global e
        global thread
        if event == "show_done":
            i = 1
            e = 0
            renpy.invoke_in_thread(random_sounds, character_name)
        elif event == "slow_done":
            renpy.music.stop(channel='voice')
            i = 0
            e = 0

style centered_text:
    yalign 0.5

#     Персонажи
define narrator = Character(None, kind=nvl, what_color="#FFFFFF", what_style='centered_text') #Текст по середине экрана
define narrator_small = Character(None, what_color="#FFFFFF", what_style='centered_text') #Текст внизу экрана (как обычный персонаж)
define j = Character("Джопаждек /", who_color="#D2691E", what_color="#CD853F", callback=character_sound, cb_character_name="jopa")
define j_fast = Character("Джопаждек /", who_color="#D2691E", what_color="#CD853F", callback=character_sound, cb_character_name="jopa", what_slow_cps=50)
define j_sad = Character("Джопаждек /", who_color="#D2691E", what_color="#CD853F", what_prefix="{i}{w=0.2}", what_suffix="{/i}", what_slow_cps=25, cb_character_name="jopa", callback=character_sound)
define j_angry = Character("Джопаждек /", who_color="#D2691E", what_color="#cd863f", what_prefix="{size=+9}", what_suffix="{/size}", what_slow_cps=60, cb_character_name="jopa", callback=character_sound)

#Дебилыч
define d = Character("Дибилыч /", who_color="#BDB76B", what_color="#CD853F", character_name="debil", cb_character_name="debil", callback=character_sound)
define d_unknown = Character("??ЧЕЛОВЕК?? /", who_color="#808080", what_color="#808080", what_prefix="{i}", what_suffix="{/i}", cb_character_name="debil", callback=character_sound)
define d_semidead = Character("??ЧЕЛОВЕК?? /", who_color="#808080", what_color="#808080", what_slow_cps=10, cb_character_name="debil_misunderstood", callback=character_sound)
define d_sad = Character("Дибилыч /", who_color="#BDB76B", what_color="#CD853F", what_prefix="{i}{w=0.2}", what_suffix="{/i}", what_slow_cps=25, cb_character_name="debil", callback=character_sound)
define d_angry = Character("Дибилыч /", who_color="#BDB76B", what_color="#cd863f", what_prefix="{size=+9}", what_suffix="{/size}", what_slow_cps=60, cb_character_name="debil", callback=character_sound)

#Телек
define talking_head = Character("Бошечка из телека", who_color = "#808080", what_color="#808080")

#     Спрайты
#джек
image j = im.FactorScale("sprites/characters/jopa/jopa.png", 8)
image j_jacket = im.FactorScale("sprites/characters/jopa/jopa_jacket.png", 8)
image j_jacket_calling = im.FactorScale("sprites/characters/jopa/jopa_jacket_calling.png", 8)
image j_jacket_calling_sweat = im.FactorScale("sprites/characters/jopa/jopa_jacket_calling_sweat.png", 8)
image j_jacket_calling_sweat_very = im.FactorScale("sprites/characters/jopa/jopa_jacket_calling_sweat_very.png", 8)
image j_jacket_calling_evil = im.FactorScale("sprites/characters/jopa/jopa_jacket_calling_evil.png", 8)
image j_jacket_scared = im.FactorScale("sprites/characters/jopa/jopa_jacket_scared.png", 8)
image j_sad = im.FactorScale("sprites/characters/jopa/jopa_sad.png", 8)
image j_angry = im.FactorScale("sprites/characters/jopa/jopa_angry.png", 8)
image j_falling = im.FactorScale("sprites/characters/jopa/jopa_falling.png", 8)

#Дебилыч
image d = im.FactorScale("sprites/characters/debil/debil.png", 8)
image d_semidead = im.FactorScale("sprites/characters/debil/debil_semidead.png", 8)
image d_unknown = im.FactorScale("sprites/characters/debil/debil_unknown.png", 8)
image d_sad = im.FactorScale("sprites/characters/debil/debil_sad.png", 8)
image d_angry = im.FactorScale("sprites/characters/debil/debil_angry.png", 8)

