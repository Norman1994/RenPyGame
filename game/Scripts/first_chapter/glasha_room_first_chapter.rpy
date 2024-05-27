label glasha_room_first_chapter:

    play music "audio/music/RoomMusic.mp3"

    scene glasha_room with dissolve

    "Ох... Голова... Сон... Какой же он был реальный!"

    "Крабо-люди, ранение Эдуарда Семеновича, похищение..."

    "Как будто я пережила события дешевого фантастического фильма."

    "Мне плохо... Но ничего, сейчас в комнату зайдет Юля и все будет, как раньше!"

    if is_talking_again == True:
        "О нет... Юля..."

    show Father with dissolve

    father "Привет, доча!"

    me "Папа! Ты... ты настоящий!"

    father "Что за глупости?! Конечно я настоящий! Ты в порядке? Сама не своя?"

    me "Папенька... А где я вчера была?!"

    father "Что? Что за вопросы? Ну, дома наверное. Я так то гулял вчера с одной юной... поклонницей!"

    father "Поэтому, меня не было вчера дома. Я только что пришел."

    "На мгновение мне хотелось рассказать ему обо всех ужасах, что приключились со мной минувшим вечером."

    "Но решила, что оно того не стоит. Я не хочу впутывать в это отца."

    if is_talking_again == True:
        "Хватило и Юли..."

    "Хотя, стоп! Этого же не было! Это же был сон!"

    "Нужно немедленно позвонить Эдуарду Семеновичу, чтобы во всем разобраться!"

    father "Хм. Ладно, доча, я пойду наверное. Ты сама не своя. Спи почаще!"

    hide Father with dissolve

    "Несмотря на сонливость, я бросаюсь к телефону и обессилившими пальцами пытаюсь набрать номер Эдуарда."

    "Гудки... Долгие, растянутые гудки."

    "Нет... Неужели, это был не сон!"

    "Ладно, нужно вести себя естественно! Пойти на работу, поругаться с жабой секретаршей... Если она жива."

    play sound "audio/music/PhoneSound.mp3"

    "Ой... Наверное, Эдуард!"

    stop sound fadeout 1.0

    crab_queen "Крххх, открой свой email!!!"

    "Ну конечно это был не сон. А как иначе?"

    "Чудовище в виде крабовой королевы возложила на меня какую-то бредовую миссию."

    "Если у королевы Енотов я невольно была на побегушках, то здесь меня реально собирались использовать, как секс-куклу!"

    "Что же делать? Куда идти? К кому обращаться?!"

    if is_talking_again == True:
        "Может, все-таки позвонить Эдуарду?! Мне больше не на кого положиться!"
    else:
        "Может, все-таки поговорить с Юлей?!"

    "Нет... Это слишком рискованно..."

    "Ладно, что там с письмом?"

    show glasha_monitor

    "И правда письмо... Поначалу я ничего не понимала, от волнения расплывалось перед глазами."

    "Но вскоре я различила таблицу. Четыре мужчины, их имена, адреса и должности."

    "Хорошие новости: все они жили в моем городе."

    "Плохие новости: все они были олигархами."

    "Один директор фирмы, другой какой-то биржевой брокер, третий какой-то магнат, четвертый - ведущий ученый."

    "И имена какие то странные."

    "Радолев Бздыхович, Ауф Вульфович, Кукис Никнак, Жабжаб Кваров."

    "Люди с деньгами, статусом, собственным местом под солнцем."

    "И мне нужно их соблазнить? Мне, простой девчонке, которая ничего дороже брюк по дисконту ничего не носила?"

    "Да я еле Эдурда Семеновича охмурила..."

    show glasha_room with dissolve

    "От осознания собственной беспомощности хотелось кричать во весь голос, но какой смысл?"

    "Ладно... В конце концов от меня зависела жизнь дорогого мне человека, а это многого стоит."

    "Пойду на работу."

    return