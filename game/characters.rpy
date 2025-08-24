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
    xsize 1400

init:
    #     Персонажи
    define narrator = Character(None, what_color="#FFFFFF", what_style='centered_text')
    define narrator_creepy = Character(None, kind=nvl, what_color="#FFFFFF", what_style="centered_text")

    # Джопа
    define j = Character("Джопаждек /", who_color="#D2691E", what_color="#CD853F", callback=character_sound, cb_character_name="jopa")
    define j_fast = Character("Джопаждек /", who_color="#D2691E", what_color="#CD853F", callback=character_sound, cb_character_name="jopa", what_slow_cps=50)
    define j_sad = Character("Джопаждек /", who_color="#D2691E", what_color="#CD853F", what_prefix="{i}{w=0.2}", what_suffix="{/i}", what_slow_cps=25, cb_character_name="jopa", callback=character_sound)
    define j_scared = Character("Джопаждек /", who_color="#D2691E", what_color="#CD853F", what_prefix="{i}{w=0.2}{size=-3}{shader=jitter:u__jitter=3.0,3.0}", what_suffix="{/shader}{/size}{/i}", what_slow_cps=55, cb_character_name="jopa", callback=character_sound)
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
    image j = im.FactorScale("sprites/characters/jopa/j_1.png", 0.25)
    image j 2 = im.FactorScale("sprites/characters/jopa/j_2.png", 0.25)
    image j 3 = im.FactorScale("sprites/characters/jopa/j_3.png", 0.25)
    image j_jacket = im.FactorScale("sprites/characters/jopa/j_jacket_1.png", 0.25)
    image j_jacket 2 = im.FactorScale("sprites/characters/jopa/j_jacket_2.png", 0.25)
    image j_jacket 3 = im.FactorScale("sprites/characters/jopa/j_jacket_3.png", 0.25)
    image j_jacket_calling = im.FactorScale("sprites/characters/jopa/j_jacket_calling.png", 0.25)
    image j_jacket_calling_sweat = im.FactorScale("sprites/characters/jopa/j_jacket_calling_sweat.png", 0.25)
    image j_jacket_calling_sweat_very = im.FactorScale("sprites/characters/jopa/j_jacket_calling_sweat_very.png", 0.25)
    image j_jacket_calling_evil = im.FactorScale("sprites/characters/jopa/j_jacket_calling_evil.png", 0.25)
    image j_jacket_angry = im.FactorScale("sprites/characters/jopa/j_jacked_angry.png", 0.25)
    image j_jacket_angry_sweat = im.FactorScale("sprites/characters/jopa/j_jacket_angry_sweat.png", 0.25)
    image j_jacket_scared = im.FactorScale("sprites/characters/jopa/j_jacket_scared.png", 0.25)
    image j_jacket_kind = im.FactorScale("sprites/characters/jopa/j_jacket_kind.png", 0.25)
    image j_jacket_kind_embarrassed = im.FactorScale("sprites/characters/jopa/j_jacket_kind_embrassed.png", 0.25)
    image j_jacket_sweat = im.FactorScale("sprites/characters/jopa/j_jacket_sweat.png", 0.25)
    image j_jacket_sad = im.FactorScale("sprites/characters/jopa/j_jacket_sad.png", 0.25)
    image j_jacket_falling = im.FactorScale("sprites/characters/jopa/j_jacket_falling.png", 0.25)
    image j_sad = im.FactorScale("sprites/characters/jopa/j_sad.png", 0.25)
    image j_sweat = im.FactorScale("sprites/characters/jopa/j_sweat.png", 0.25)
    image j_angry = im.FactorScale("sprites/characters/jopa/j_angry.png", 0.25)
    image j_angry_sweat = im.FactorScale("sprites/characters/jopa/j_angry_sweat.png", 0.25)
    image j_falling = im.FactorScale("sprites/characters/jopa/j_falling.png", 0.25)
    image j_kind = im.FactorScale("sprites/characters/jopa/j_kind.png", 0.25)
    image j_kind_embarrassed = im.FactorScale("sprites/characters/jopa/j_kind_embarrassed.png", 0.25)

    #Дебилыч
    image d = im.FactorScale("sprites/characters/debil/d.png", 0.25)
    image d_crying = im.FactorScale("sprites/characters/debil/d_crying.png", 0.25)
    image d_sad = im.FactorScale("sprites/characters/debil/d_sad.png", 0.25)
    image d_smiling = im.FactorScale("sprites/characters/debil/d_smiling.png", 0.25)
    image d_surprised = im.FactorScale("sprites/characters/debil/d_surprised.png", 0.25)
    image d_touched = im.FactorScale("sprites/characters/debil/d_touched.png", 0.25)
    image d_wipes_face = im.FactorScale("sprites/characters/debil/d_wipes_face.png", 0.25)
    image d_wtf = im.FactorScale("sprites/characters/debil/d_wtf.png", 0.25)