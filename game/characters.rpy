#Здесь создаются все персонажи и их спрайты

'''Персонажи:'''
#джек
define j = Character("Джопаждек", who_color="#D2691E", what_color="#CD853F")
define j_sad = Character("Джопаждек", who_color="#D2691E", what_color="#6A5ACD", what_prefix="{i}{w=0.2}", what_suffix="{/i}")
define j_angry = Character("Джопаждек", who_color="#D2691E", what_color="#DC143C", what_prefix="{size=+10}{fast}", what_suffix="{/size}")

#Дебилыч
define d = Character("Дибилыч", who_color="#BDB76B", what_color="#CD853F")
define d_unknown = Character("??ЧЕЛОВЕК??", who_color="#808080", what_color="#808080", what_prefix="{i}", what_suffix="{/i}")
define d_sad = Character("Дибилыч", who_color="#BDB76B", what_color="#6A5ACD", what_prefix="{i}{w=0.2}", what_suffix="{/i}")
define d_angry = Character("Дибилыч", who_color="#BDB76B", what_color="#DC143C", what_prefix="{size=+10}{fast}", what_suffix="{/size}")

'''Спрайты:'''
#джек
image j = "sprites/characters/jopa/jopa.png"
image j_sad = "sprites/characters/jopa/jopa_sad.png"
image j_angry = "sprites/characters/jopa/jopa_angry.png"

#Дебилыч
image d = "sprites/characters/debil/debil.png"
image d_sad = "sprites/characters/debil/debil_sad.png"
image d_angry = "sprites/characters/debil/debil_angry.png"

