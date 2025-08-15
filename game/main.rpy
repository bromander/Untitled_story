
label start:
    scene bg room

    show j
    j "sosaldfgnfddnhfhrhgnhfrgdgnfgh?"
    j_sad "nethfdghmfghwagrhdgfnh"
    j_angry "pohemuszfdngmfhrwaghgdfmhhradgfn?"

    return

init python:

    def sound(character_name: str) -> None:
        renpy.sound.play("characters_voice")
