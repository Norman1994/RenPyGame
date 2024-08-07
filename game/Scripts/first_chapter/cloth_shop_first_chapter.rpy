label cloth_shop_first_chapter:

    scene cloth_shop with dissolve

    play music "audio/music/shop_music.mp3"

    "Жожо привела меня в самый пафосный бутик города."

    "То, что он пафосный было видно не только по ценам, но и по обстановке. Все такое яркое, величественное."

    "Атмосфера могущества, чувство прекрасного."

    "Пока я стояла и глазела на многочисленные шкафы, забитые невероятно красивыми костюмами, Жожо уже передавала мне какое-то красное бархатное платье."

    "Даже касаться его было страшно. Казалось, что под моими пальцами, пропитанными потом и бедностью, ткань разойдется, превратится в пыль."

    show Jojo with dissolve

    jojo "О, этот тебе точно подойдет!"

    "Только сейчас я поняла, что Жожо пыталась во всю быть похожей на Юлю."

    "Поведение, мимика, беззаботность."

    if is_talking_again == False:
        "Интересно, где она сейчас?!"
    else:
        "Чертова Краболева!!"

    jojo "Ну что, будешь мерить? Время не ждет!"

    "Делать нечего..."

    scene glasha_reflection with dissolve

    me "Господи... Это же я!"

    "Впервые за всю свою жизнь я чувствовала себя богиней, утонченной изысканной женщиной!"

    "Как будто вся моя жизнь прошла в водовороте балов и путешествий."

    "У меня даже дыхание перехватило..."

    "Я была прекрасна!"

    scene cloth_shop with dissolve

    show Jojo with dissolve

    jojo "Хах, видела бы ты свое лицо!"

    "Мне даже ответить было нечем..."

    jojo "Ладненько, давай, плати, буду ждать тебя на улице!"

    hide Jojo with dissolve

    "Хоть на секунду она оставила меня в одиночестве."

    "И в эту секунду мне хотелось убраться восвояси."

    "Заплатить за платье и покинуть магазин через черный ход."

    "Подальше от неё и этого кошмара!"

    "Может, и правда так сделать?!"

    menu:
        "Сбежать от Жожанны":
            jump glasha_escapes

        "Пойти на бал":
            jump glasha_staying

    return