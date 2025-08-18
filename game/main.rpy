
label start:
    scene bg room

    show j
    j "Эх. Как же хочеться свежего и горячего писюнчика"
    hide j
    show j_sad at center
    j_sad "Вспоминаю те времена с моим бывшим..."
    hide j_sad
    show j_angry at center
    j_angry "Да как он только мог?"
    hide j_angry
    show j at center
    j "Эх. Как же хочеться свежего и горячего писюнчика"
    hide j
    show d_unknown at center
    d_unknown "я типо неизвесный инвалид"
    hide d_unknown
    show d_semidead at center
    d_semidead "я типо полумёртвый инвалид"
    hide d_semidead
    show d at center
    d "Эх. Как же хочеться свежего и горячего писюнчика"
    hide d
    show d_sad at center
    d_sad "Вспоминаю те времена с моим бывшим..."
    hide d_sad
    show d_angry at center
    d_angry "Да как он только мог?"

    return

init python:

    def sound(character_name: str) -> None:
        renpy.sound.play("characters_voice")
