
label part2_try_wake_up:
    scene bg entrance porch
    hide j_jacket_scared with dissolve
    show j_jacket_sweat at show_jack_at_right with dissolve
    'Джек пытается дёргать за плечо, чтобы разбудить перегарное тело. Оно невероятно холодное.'
    j 'Ээээй... \nУважаемый... \nпроснитесь!'
    j "..."
    hide j_jacket_sweat
    show j_jacket_angry at show_jack_at_right
    j_angry 'ТВОЮ МАТЬ! ЧЕЛ ПРОСНИСЬ! ТЫ Ж ТАК ЗАМЁРЗНЕШЬ И СДОХНЕШЬ!'
    'От тела ноль реакции, зато Джек успел заметить, что сердцебиение сильно замедлилось.'
    j 'Времени всё меньше, и он скоро замёрзнет...'
    jump what_jack_wil_do_omg