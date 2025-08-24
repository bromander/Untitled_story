
# спрайты фонов у которых значение размера 0.5325 - неверного формата. Я уже сказал художнику и их дорисуют

init:
    image bg test_room = im.FactorScale("images/sprites/scenes/jopa_home/bg test_room.png", 1)

    image bg entrance = im.FactorScale("images/sprites/scenes/jopa_home/bg entrance.jpg", 0.5325)
    image bg entrance porch = im.FactorScale("images/sprites/scenes/jopa_home/bg entrance porch.jpg", 0.5325)
    image bg entrance light_on = im.FactorScale("images/sprites/scenes/jopa_home/bg entrance light_on.jpg", 0.5325)
    image bg entrance 2 = im.FactorScale("images/sprites/scenes/jopa_home/bg entrance 2.jpg", 0.5325)

    image bg entrance porch = im.FactorScale("images/sprites/scenes/jopa_home/bg entrance porch.jpg", 0.5325)

    image bg hall = im.FactorScale("images/sprites/scenes/jopa_home/bg hall.jpg", 0.5325)
    image bg hall light_on = im.FactorScale("images/sprites/scenes/jopa_home/bg hall light_on.jpg", 0.5325)
    image bg hall 2 = im.FactorScale("images/sprites/scenes/jopa_home/bg hall 2.jpg", 0.5325)
    image bg hall 2 light_on = im.FactorScale("images/sprites/scenes/jopa_home/bg hall 2 light_on.jpg", 0.5325)

    image bg bathroom = im.FactorScale("images/sprites/scenes/jopa_home/bg bathroom.jpg", 0.5325)
    image bg bathroom light_on = im.FactorScale("images/sprites/scenes/jopa_home/bg bathroom light_on.jpg", 0.5325)
    image bg bathroom bath = im.FactorScale("images/sprites/scenes/jopa_home/bg bathroom bath.png", 0.5325)
    image bg bathroom cleared = im.FactorScale("images/sprites/scenes/jopa_home/bg bathroom cleared.jpg", 0.5325)
    image bg bathroom cleared light_on = im.FactorScale("images/sprites/scenes/jopa_home/bg bathroom cleared light_on.jpg", 0.5325)

    image bg jopa_room = im.FactorScale("images/sprites/scenes/jopa_home/bg jopa_room.jpg", 0.5325)
    image bg jopa_room light_on = im.FactorScale("images/sprites/scenes/jopa_home/bg jopa_room light_on.jpg",  0.5325)
    image bg jopa_room bed = im.FactorScale("images/sprites/scenes/jopa_home/bg jopa_room bed.jpg",  0.5325)
    image bg jopa_room bed light_on = im.FactorScale("images/sprites/scenes/jopa_home/bg jopa_room bed light_on.jpg",  0.5325)

    image bg kitchen = im.FactorScale("images/sprites/scenes/jopa_home/bg kitchen.jpg", 0.5325)
    image bg kitchen light_on = im.FactorScale("images/sprites/scenes/jopa_home/bg kitchen light_on.jpg", 0.5325)
    image bg kitchen fridge = im.FactorScale("images/sprites/scenes/jopa_home/bg kitchen fridge.png", 0.5325)
    image bg kitchen fridge light_on = im.FactorScale("images/sprites/scenes/jopa_home/bg kitchen fridge light_on.png", 0.5325)
    image bg kitchen fridge open = im.FactorScale("images/sprites/scenes/jopa_home/bg kitchen fridge open.png", 0.5325)
    image bg kitchen fridge open light_on = im.FactorScale("images/sprites/scenes/jopa_home/bg kitchen fridge open light_on.png", 0.5325)

    image bg exit = im.FactorScale("images/sprites/scenes/jopa_home/bg exit.jpg", 0.5325)
    image bg exit light_on = im.FactorScale("images/sprites/scenes/jopa_home/bg exit light_on.jpg", 0.5325)



################################################################################
## Экран переключателя
################################################################################

init python:
    def get_scene_state(room: str):

        if not hasattr(persistent, "switch_toggles"):
            persistent.switch_toggles = {}
        if str(room) not in persistent.switch_toggles.keys():
            persistent.switch_toggles[str(room)] = True
        if type(persistent.switch_toggles) is not dict:
            persistent.switch_toggles = {}



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
    transform image_toggle_size(_zoom, _xzoom):
        xzoom _xzoom
        zoom _zoom


screen show_scene(_xpos, _ypos, room, is_reflected): # WIP
    tag show_scene
    python:
        print(list(renpy.get_showing_tags(layer='master'))[0])
        _xzoom = 1
        if is_reflected:
            _xzoom = -1

        _state = get_scene_state(room)

        if _state == 1:
            renpy.show(f"bg {room} light_on")
        else:
            renpy.show(f"bg {room}")

    vbox:
        imagebutton:
            idle f"images/sprites/light_switch/switch_{_state}.png"
            xpos _xpos
            ypos _ypos
            action [
                Function(edit_switch_state, room),
                SetScreenVariable("_state", get_scene_state(room))
            ]
            at image_toggle_size(0.8, _xzoom)