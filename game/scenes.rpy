
# спрайты фонов у которых значение размера 0.5325 - неверного формата. Я уже сказал художнику и их дорисуют

init:
    image bg test_room = im.FactorScale("images/sprites/scenes/jopa_home/bg entrance.jpg", 1)

    image bg entrance = im.FactorScale("images/sprites/scenes/jopa_home/bg entrance.jpg", 0.5325)
    image bg entrance porch = im.FactorScale("images/sprites/scenes/jopa_home/bg entrance porch.jpg", 0.5325)

    image bg hall = im.FactorScale("images/sprites/scenes/jopa_home/bg hall.jpg", 0.5325)
    image bg hall 2 = im.FactorScale("images/sprites/scenes/jopa_home/bg hall 2.jpg", 0.5325)

    image bg bathroom = im.FactorScale("images/sprites/scenes/jopa_home/bg bathroom.jpg", 0.5325)
    image bg bathroom bath = im.FactorScale("images/sprites/scenes/jopa_home/bg bathroom bath.jpg", 0.5325)

    image bg hallway = im.FactorScale("images/sprites/scenes/jopa_home/bg hallway.jpg", 0.5325)

    image bg jack_room = im.FactorScale("images/sprites/scenes/jopa_home/bg jack_room.jpg", 0.5325)
    image bg jack_room light_on = im.FactorScale("images/sprites/scenes/jopa_home/bg jack_room light_on.jpg", 1)

    image bg kitchen = im.FactorScale("images/sprites/scenes/jopa_home/bg kitchen.jpg", 0.5325)
    image bg kitchen fridge = im.FactorScale("images/sprites/scenes/jopa_home/bg kitchen fridge.jpg", 0.5325)
    image bg kitchen fridge opened = im.FactorScale("images/sprites/scenes/jopa_home/bg kitchen fridge opened.jpg", 0.5325)




################################################################################
## Экран переключателя
################################################################################

init python:
    def get_scene_state(room: str):

        if not hasattr(persistent, "switch_toggles"):
            persistent.switch_toggles = {}
        if str(room) not in persistent.switch_toggles.keys():
            persistent.switch_toggles[str(room)] = True

        if persistent.switch_toggles[room]:
            _state = 1
        else:
            _state = 0

        return _state

    def edit_switch_state(room: str):
        if persistent.switch_toggles.get(room, False):
            persistent.switch_toggles[room] = False
            renpy.show(f"bg {room}")
        else:
            persistent.switch_toggles[room] = True
            renpy.show(f"bg {room} light_on")

init:
    transform image_toggle_size(_zoom, _yzoom):
        xzoom _yzoom
        zoom _zoom


screen show_scene(_xpos, _ypos, room, is_reflected):
    python:
        _yzoom = 1
        if is_reflected:
            _yzoom = -1
    python:
        if persistent.switch_toggles[room]:
            renpy.show(f"bg {room} light_on")
        else:
            renpy.show(f"bg {room}")
    $ _state = get_scene_state(room)
    vbox:
        imagebutton:
            idle f"images/sprites/light_switch/switch_{_state}.png"
            xpos _xpos
            ypos _ypos
            action [
                Function(edit_switch_state, room),
                SetScreenVariable("_state", get_scene_state(room))
            ]
            at image_toggle_size(0.8, _yzoom)
        $ print(_yzoom)