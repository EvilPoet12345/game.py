def paint_1():
    import turtle
    #название самой игры крсаного вета
    turtle.pencolor('red')
    turtle.speed(1)
    turtle.write('Квест в темной комнате!',align = 'center', move = True, font = ('Arial', 22, 'italic'))
    turtle.clear()
    turtle.reset()
    return paint_1


def paint_2():
    #нарисованная дверь
    import turtle
    turtle.forward(250)
    turtle.right(90)
    turtle.forward(500)
    turtle.right(90)
    turtle.forward(250)
    turtle.right(90)
    turtle.forward(500)
    turtle.clear()
    turtle.reset()
    return paint_2


def paint_3():
    #нарисовать лестницу
    import turtle
    turtle.forward(50)
    turtle.right(90)
    turtle.forward(25)
    turtle.left(90)
    turtle.forward(50)
    turtle.right(90)
    turtle.forward(25)
    turtle.left(90)
    turtle.forward(50)
    turtle.right(90)
    turtle.forward(25)
    turtle.left(90)
    turtle.forward(50)
    turtle.right(90)
    turtle.forward(25)
    turtle.left(90)
    turtle.forward(50)
    turtle.right(90)
    turtle.forward(25)
    turtle.left(90)
    turtle.forward(50)
    turtle.right(90)
    turtle.forward(25)
    turtle.left(90)
    turtle.forward(50)
    turtle.right(90)
    turtle.forward(25)
    turtle.left(90)
    turtle.forward(50)
    turtle.right(90)
    turtle.forward(25)
    turtle.left(90)
    turtle.forward(50)
    turtle.right(90)
    turtle.forward(25)
    turtle.left(90)
    turtle.forward(50)
    turtle.clear()
    turtle.reset()
    return paint_3


def paint_4():
    #нарисовать холодильник
    import turtle
    turtle.forward(150)
    turtle.right(90)
    turtle.forward(250)
    turtle.rt(90)
    turtle.forward(150)
    turtle.rt(90)
    turtle.forward(350)
    turtle.rt(90)
    turtle.fd(150)
    turtle.rt(90)
    turtle.fd(225)
    turtle.rt(90)
    turtle.fd(35)
    turtle.lt(90)
    turtle.fd(50)
    turtle.lt(90)
    turtle.fd(35)
    turtle.clear()
    turtle.reset()
    return paint_4


def paint_5():
    #заголовок о конце игры
    import turtle
    turtle.pencolor('Blue')
    turtle.speed(1)
    turtle.write('Конец игры!',align = 'center', move = True, font = ('Arial', 22, 'italic'))
    return paint_5








print("Привет мой друг, скажи мне как тебя зовут?")
name = str(input())
print(name + " Готов ли ты начать наще увлекательное путешествие?")
print("Если - да, то введи -1 и мы начинаем, ну а если же - нет, тогда введи - 2 и в следующий раз.")
def questions ():
    return int(input())
a = questions()

if a == 1:
    paint_1()
    print("Начинаем!!!")
    print("""Ты открываешь глаза и понимаешь что лежишь на деревянном полу.
В комнате темно, как у кошки в заднице. Садишся, достаешь из кармана джинсов
свой сотовый и...""")
    print("Что же ты сделаешь?", "Если включишь фонарик. нажми 1, если позвонишь в службу спасения то 2")
    a = questions()
    if a ==2:
        print(""" Ты включил фонарик и теб сожрало чудовище, которое прятолось в темноте""")
        input()
    elif a == 1:
        print("Ты включил фонарик и начал осматривать комнату")
        print("""Молча встал и с затаенным дыханием увидел, что тут было все из дерева. 
Сама же комната была пустая и кроме тебя в ней не было ничего. В одном из углов, ты увидел дверь, 
а на противоположной стороне, окно. Куда же ты пойдешь?
В окно, напечатай - Моя идти в квадратный штук
В дверь, напечатай - Моя идти в прямоугольный штук
Что решишь """, name,)
        input()
        print("Хотя все решили за тебя...")
        paint_2()
        print("""Ты выходишь в коридор и осматриваешся. смотришь в право и влево.
Куда же ты пойдешь, если на право то жми 1, если на лево то жми 2""")
        a = questions()
        if a == 1:
            print("""Ты ушел далеко в темноту и так и не вернулся обратно, долго бродя и в конце
концнов умер от голода""")
            input()
        elif a == 2:
            print("""Ты пошел  на лево и нашел лестницу, и подумал что лучше будет...
Пойти дальше  - 1 или спуститься полестнице - 2""")
            paint_3()
            a = questions()
            if a == 1:
                print("""Идя дальше ты спотыкаешся о чейто труп, который тебя и съедает""")
                input()
            elif a == 2:
                print("""Ты спускаешся на кухню, там стоит только холодильник, а за ним какая-то дыра в стене. куда двинешь""", name,)
                paint_4()
                print("В холодиьник, жмякай - 1, в дырку - жмякай - 2")
                a = questions()
                if a == 2:
                    print("ты полез в дуырку и застрял, и потом тебя кто-то съел пока ты обессиленный был в дырке")
                    input()
                elif a == 1:
                    print("""Ты долго спускался по лестнице внутри холодильника, пока не наткнулся на еще дну дверь.
Откроешь ли ты ее""", name, """да - 1 или нет - 2?""")
                    a = questions()
                    if a == 2:
                        print("ты так и не открыл дверь, стоял и ждал пока тьма тебя не поглотила")
                        input()
                    elif a == 1:
                        print("""Ты открыл дверь и вышел на свет, режущий глаза. Осмотрелся и понял, что ты на улице и в безопасности.
Ты победил, """, name, "млодчинка")
                        paint_5()
                        print("END GAME")
                        input()
elif a == 2:
    print("***** ответ")
    print("game over")
    input()
else:
    print("Чето не то нажал ты, давай все сначала")
    input()
