label mansion_first_chapter:

    play music "audio/music/mansion_music.mp3"

    scene mansion

    "Ого... Какая невероятная роскошь!"

    "Если бы не Краболева, я бы чувствовала себя настоящей принцессой, в честь которой устроили пышный бал!"

    "Невероятно..."

    show Jojo with dissolve

    jojo "Ух ты, тут здорово!"

    me "Здорово?! Да здесь великолепно!"

    jojo "Ха-ха, рада, что тебе стало легче."

    "На самом деле мою душу по-прежнему драли бешеные коты, но я решила промолчать об этом."

    jojo "Ладненько, пойдем-ка. Не будем заставлять гостей ждать!"

    me "Ой... Ой... А как же... А кем же я представлюсь? Меня же туда просто так не пустят."

    jojo "Точно! Совсем забыла! Мы же должны дать тебе имя, достойное твоего величественного облика!"

    jojo "В общем, вот тебе на выбор несколько имен."

    me "А как же список?"

    jojo "Эти имена есть у них в списке! Поверь мне!"

    me "Хм. Ладно."

    jojo "Короче, выбирай!"

    menu:
        "Вингира Топоровна":
            $glasha_name = "Вингира Топоровна"
        "Альбина Кексова":
            $glasha_name = "Альбина Кексова"
        "Чебуреня Начинковна":
            $glasha_name = "Чебуреня Начинковна"
        "Стульина Ножкова":
            $glasha_name = "Стульина Ножкова"

    me "Хм... Ну пусть будет [glasha_name]."

    jojo "Великолепно! Тебе очень подходит!"

    me "Правда? Я глупо себя чувствую."

    jojo "Выше нос, подруга! Возможно, тебя ждет самый лучший вечер в твоей жизни!"

    "Хотела бы я ей сказать не называть меня подругой - права не имела! - но сдержалась."

    jojo "Ладно, пошли внутрь, уверена там ещё лучше!"

    scene grand_hall

    "У меня дыхание перехватило от такой красоты..."

    "Теперь я была уверена, что это сон. Я бы в жизни не оказалась в таком месте просто так."

    "А люди... Сколько тут людей! Все таки важные, нарядные, надменные."

    "Всем своим видом они показывали превосходство над низшим классом."

    "Заговорить с такими означало заговорить с самими Богами..."

    show Jojo with dissolve

    jojo "Мама-мия! Хорошо, что Краболева послала меня сюда!"

    jojo "О, а вот и Радолев!"

    hide Jojo with dissolve

    show Radolev at left with dissolve
    show Jojo at right with dissolve

    radolev "Так-так-так! Какие красавицы решили придти на мой сегодняшний бал!"

    "Господи, такого горячего самца я в жизни не видела. Клянусь, от него веяло жаром, как от печки."

    "И пах он старым советским одеколоном."

    jojo "Ох... Я вся в восхищении!"

    radolev "Правда? Я рад. Мое тело - результат долгих тренеровок и борьбы с собственными комплексами и недостатками."

    radolev "Чтобы достичь такого великолепия мне пришлось в буквальном смысле идеализировать себя изнутри."

    jojo "Я щас умру!!!"

    radolev "Хаха, ррр, не стоит! А кто ваша подруга? Такая тихая, стеснительная. И пленительная!"

    me "Я... Я... Я [glasha_name]."

    radolev "Ох... Какое будоражещее имя!"

    "И его мне нужно было соблазнить? Да он сам был готов кинуться на меня, стоит ему только разрешить..."

    "То, как он на меня смотрел, было за гранью простого человеческого желания."

    "Он меня хотел. Прямо здесь, прямо сейчас!!!"

    "Мое сердце сжалось..."

    me "Спасибо..."

    jojo "Ой, ну ладненько, оставлю вас двоих наедине! Удачи!"

    hide Jojo with dissolve
    hide Radolev with dissolve

    show Radolev with dissolve

    radolev "Хаха, вы такая стеснительная. Мне это нравится."

    radolev "Но, прошу вас, расскажите мне о себе!"

    "Что я могла рассказать? Что я обычный клерк, у которого все интересы ограничиваются интернетом и чтением книг?"

    "Нет, такое ему точно не подойдет. Я должна соответствовать новому образу."

    "Но и перебарщивать нельзя. Одна ошибка - и я ошибусь!"

    menu:
        "Я - дочь нефтенного магната":

            $radolev_scores += 3

            radolev "Охохо, сильно!"
        
        "Мой отец - крупный бизнесмен, входит в топ 200 Forbes":

            $radolev_scores += 5

            radolev "Охохохох! Вот это уже интересно! Коллега мой, получается!"

        "Я - ведущий журналист крупного женского журнала":

            $radolev_scores += 2

            radolev "Правда? Жаль, что я не умею читать..."

        "Да ничего особенного. В конторе одной крупной работаю...":

            $radolev_scores += 1

            radolev "Как то безвкусно вы это сказали..."

    radolev "Ладно, а чем вы интересуетесь?"

    menu:
        "Люблю сидеть на окне, писать стихи и смотреть на проливной дождь за окном":

            $radolev_scores += 1

            radolev "Хм..."

        "Люблю проводить вечера на балах и кататься на порше по ночной Москве": 

            $radolev_scores += 5

            radolev "Да, люблю скорость!!!"

        "Все свое свободное время трачу на чтение книг по ведению бизнеса": 

            $radolev_scores += 3

            radolev "Хрр, полезно, наверное!"

        "Люблю сидеть с подругами и говорить о проблемах социума": 

            $radolev_scores += 2

            radolev "А у него есть проблемы?"

    radolev "Хех, допустим, а какие напитки вы предпочитаете?"

    menu:
        "Красное вино шато-морто 1899 года":

            $radolev_scores += 5

            radolev "Своеобразно!"

        "Шампанское. И побольше!": 

            $radolev_scores += 3

            radolev "Оно такое шипучее, хрр!"

        "Кофе. И только кофе. Лучше дома, на диване с пледиком": 

            $radolev_scores += 1

            radolev "Хм, не мое..."

        "Ароматный чай, лучше всего индийский": 

            $radolev_scores += 2

            radolev "О, наверное, оно того стоит? Хехе."

    radolev "Так, а кто ваш идеал человека? На кого вы ориентируетесь по жизни?!"

    menu:
        "Маргарет Тетчер":

            $radolev_scores += 2

            radolev "Сильная была женщина, однако!"

        "Илон Маск": 

            $radolev_scores += 5

            radolev "О да, великий человек, одобряю!!!"

        "Роберт Кийосаки":

            $radolev_scores += 3

            radolev "Я слышал, что он жулик, но богатый и самоуверенный жулик!"

        "Сергей Есенин":

            $radolev_scores += 1

            radolev "А кто это?"

    if radolev_scores >= 15:

        radolev "Ух, [glasha_name], не хочу вас смущать... Но вы только что разожгли во мне костер сладострастного искушения!"

        jump radolev_evening

    if 10 <= radolev_scores <= 14:

        radolev "Слушайте, а вы не хотите познакомиться поближе?"

    if  5 <= radolev_scores <= 9:

        radolev "Хм... Что то таки в вас есть, но я не могу понять, что..."

    if radolev_scores <= 4:

        radolev "О, нам с тобой не по пути!"

    return

label radolev_evening:

    "Он пуще прежнего начал пожирать меня глазами. Моё сердце нервно забилось..."

    radolev "Я не смутил вас? У вас по лицу пот покатился."

    "Я силилась успокоиться, но это всё равно, что попытаться остановить движущийся на тебя поезд."

    "Главное помнить, что я здесь ради Эдуарда Семеновича."

    "Чертова краболева!"

    radolev "Может, поднимемся ко мне?! Я успокою вас."

    "Его голос стал низким и бархатным, отчего у меня невольно затрепетала душа."

    me "Д-да... Давайте"

    

    return