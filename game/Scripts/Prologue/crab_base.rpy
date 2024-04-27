label crab_base:

    scene crab_room

    "Я вынириваю из той темной тягучей реальности, которую люди называют сном и оглянулась."

    "В незнакомой мне комнате пахнет горелым мясом и сыростью. Сумрачный свет, падающий из маленькой лампочки над потолком являет мне кучу смятых гамбургеров на старом, испачканном темной жижей столе."

    "Помещение похоже на кухню, если бы не провода, свисающие с потолка вдоль стены словно мертвые змеи."

    "И цепи. Их мерный звон, вызванный слабым ветерком, убаюкивает и пугает меня. Зачем они здесь?!"

    "Я закрываю глаза и пытаюсь вспомнить, что вообще со мной произошло. Голова звонко гудит, мысли путаются. Я едва вспоминаю, как меня зовут."

    "Кое-как поднимаюсь с пола, за что расплачиваюсь острою болью в затвердевших мышцах."

    show CrabQueen with dissolve

    crab_queen "Крххх, наконец-то твой бренный разум выбрался из глубин сновидений. Жалкая человеческая функция."

    me "Если вы хотите убить меня - то давайте без разговоров!"

    crab_queen "Крххх, это было бы слишком просто, а я не создана для простых решений."

    crab_queen "Крххх, я обещала рассказать тебе всё, прежде чем растоптать твою душу на части, но потом поняла, что в этом не было никакого смысла."

    me "Что? Тогда зачем вы меня здесь держите?"
    
    crab_queen "Крххх, потому что я хочу использовать тебя, жалкую марионетку из мяса и дурных мыслей."

    me "Для чего?"

    crab_queen "Крххх, для желаний - моих и моего народа."

    me "Но почему именно я?"

    crab_queen "Крххх, потому что по какой-то неведомной мне причине ты слишком важна для этой вселенной. Убивать тебя, значит обречь существование моей расы на страдание. А раз так, то ты вполне пригодна в качестве рабыни."

    crab_queen "Крххх, в конце концов ты была рабыней Королевы Енотов, так что тебе не привыкать!"

    me "А если я откажусь, что ты сделаешь? Мне то уже все равно нечего терять, раз убить ты меня не можешь."

    crab_queen "Крххх, синапсы твоего разума настолько предсказуемы, что я подготовилась!"

    hide CrabQueen with dissolve

    play music "audio/music/HorrorMusic.mp3"

    if is_talking_again == True:

        scene yulia_sleeps

        me "ЮЛЯ!!!!"

        crab_queen "Крххх, наконец-то в твой блеклый разум пришло осознание."

        me "Она... Она..."

        crab_queen "Крххх, всего лишь в сонном царстве. И если ты посмеешь нарушить мои приказы, её пребывание там станет вечным."

        me "Сволочь..."

        crab_queen "Крххх, твои ругательства для меня всё равно, что пыль."

    else:

        scene boss_chains

        me "ЭДУАРД!!!!"

        crab_queen "Крххх, как ожидалось, любовь можно использовать, как инструмент для достижения целей."

        me "Что ты с ним сделала?!"

        crab_queen "Крххх, ничего такого, что могло бы его убить. Но он будет жить лишь благодаря моей безграничной воле. Все зависит от тебя!"

    scene crab_room

    show CrabQueen with dissolve

    crab_queen "Крххх, сомнения твои теперь не имеют никакого смысла! Пожчиняйся, или твои близкие пострадают!"

    "Она не блефует. Если я соглашусь мои близкие будут живы. По-крайней мере, шанс на это был велик."

    "С другой, подчиняться её правилам? Наплевать на собственные принципы? Продать свое мужество за иллюзорный шанс, что эта крабовая бестия сдержит своё слово? Дело было даже не в риске, что всё обернется в худшую сторону. Дело было во мне. В моих идеалах, в моей независимости..."

    menu:
        "Согласиться на сотрудничество":

            "Нет... Я не могу так рисковать..."

            me "Я согласна..."

            crab_queen "Крххх, другого и не ожидалось. Человеческое нутро всего тянется спасать себе подобных. Потому вы и слабы по сравнению с нашим крабовым гением!"

            crab_queen "Крххх, но я принимаю твою жертву. Можешь спать!"

            "Никаких ударов, никаких дешевых слов. Лишь сонливость, что обрушилась на меня лавиной. Я и подумать ни о чем не успела, как уже видела сны..."

        "Послать её к черту":
            jump bad_ending    

    return

label bad_ending:

    "Нет... Нельзя ей верить..."

    me "Пошла ты!"

    crab_queen "Крххх, жалкое подобие человека как всегда идет по пути своих никчемных принципов. Я разочарована..."

    me "Да мне плевать! Отпусти моих близких, или я клянусь, я тебя уничтожу!"

    crab_queen "Крххх, как же ты собираешься это сделать? Ты даже пошевелиться не можешь!"

    "Я с ужасом понимаю, что она права. Я не чувствую ни рук, ни ног, вообще ничего. Будто мое тело стало неосязаемым, ненастоящим. В панике я пытаюсь сделать хоть что-нибудь, но бесполезно. Я парализована."

    crab_queen "Крххх, узри последствие своего выбора!"

    if is_talking_again == True:

        scene yulia_sleeps

        me "НЕТ!!!!"

        "Внезапно, капсула внутри темнеет и огоньки на панели затихают. Лицо Юли практически не меняется, разве что оно становится бледным и безразличным, как маска."

    else:

        scene boss_chains

        me "ЭДУАРД!!!!"

        "Он не слышит меня. Но слышит, как позади него раздается механический гул. Из тьмы выниривает устройство, похожее на огромный пылесос. Из того места, откуда обычно свисает труба, торчит нечто похожее на женский самотык."

        "На его гладкой металической поверхности весело пляшут огоньки."

        "Но как только робот вплотную приближается к Эдуарду, самотык начинает бешено вибрировать и увеличиваться в размерах. За жалкую долю секунды оно становится похожим на переспелый баклажан."

        "Эдвард в панике. Осознает, что через секунду его упругая попа превратится в бесформенную кашу, и поэтому начинает барахтаться на цепях, как рыба, брошенная на сушу."

        "Но то ли слабость берет вверх, то ли цепи слишком сильно сжимают его тело, он может лишь беспорядочно вращать головой."

        "Тем временем, из корпуса робота выныривает металическая клешня, которая быстрым и точным движением стаскивает с него тряпку, а затем звонко шлепает его выпирающую ягодицу."

        "Шлепок звонко разносится по комнате."

        "Я ловлю себя на том, что смотрю на экзекуцию с медленно нарастающим внутри меня возбуждением. И от стыда закрываю глаза."

        play sound "audio/music/BossSoundSlow.mp3"

        "Эдуард кричит..."

        "Открыв один глаз, я вижу, как самотык ровным механическим движением трахает его, как перекаченный негр из порно."

        "Эдуард барахтается, вопит во весь голос, но с каждой секундой его тон становится более мягким и в конце концов раздается в такт механизированного проникновения."

        "Его глаза закатываются... И, это невероятно, на лице медленно проявляется наслаждение. Ему нравится!! Черт, ему нравится!!!"

        stop sound fadeout 1.0

        crab_queen "Крххх, ненадолго. Совсем скоро силы его иссякнут, а вместе с ними и жизнь. Он умрет, изнасилованный моим рукотворным шедевром 'Брежнев-101'."

        crab_queen "Но ты этого не увидишь. Ты уже вообще ничего не увидишь."

    scene crab_room

    show CrabQueen with dissolve

    crab_queen "Крххх, прощай. Эта комната станет твоей вечной могилой, пока я не решу использовать тебя для чего-то ещё!"

    hide CrabQueen with dissolve

    "От увиденного меня окутывает тонкая ткань оцепенения. Не вижу смысла что либо говорить, что либо думать..."

    "Думаю, что осознание моего неправильного выбора ещё скоро аукнется мне."

    "На это мне отведена целая вечность..."

    jump bad_title

    return