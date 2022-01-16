from cmu_graphics import*

#Background#
app.background = 'black'


#Race Track#
Circle(200, 200, 230, fill='gray')

# Finish Line #
a = Rect(200, 0, 20, 20, fill='gainsboro')
b = Rect(180, 0, 20, 20)
c = Rect(200, 20, 20, 20)
d = Rect(180, 20, 20, 20, fill='gainsboro')
e = Rect(200, 40, 20, 20, fill='gainsboro')
f = Rect(180, 40, 20, 20)
g = Rect(180, 60, 20, 20, fill='gainsboro')
h = Rect(200, 60, 20, 20)
i = Rect(180, 80, 20, 20)
j = Rect(200, 80, 20, 20, fill='gainsboro')
k = Rect(180, 100, 20, 20, fill='gainsboro')
l = Rect(200, 100, 20, 20)

# Finish Line Group #
finishLine = Group()
finishLine.add(a)
finishLine.add(b)
finishLine.add(c)
finishLine.add(d)
finishLine.add(e)
finishLine.add(f)
finishLine.add(g)
finishLine.add(h)
finishLine.add(i)
finishLine.add(j)
finishLine.add(k)
finishLine.add(l)

# Race Track Middle Circle #
Circle(200, 200, 80)


# Blue Car #
body1 = Rect(20, 140, 70, 150, fill='navy')
bumper1 = Oval(55, 140, 90, 20, fill='navy')
frontwheel1 = Oval(100, 170, 20, 40)
frontwheel2 = Oval(10, 170, 20, 40)
backwheel1 = Oval(10, 260, 20, 40)
backwheel2 = Oval(100, 260, 20, 40)
windshield1 = Rect(25, 160, 60, 30, fill='dimGray', border='black')
windshield2 = Oval(55, 192, 80, 10, fill='navy')
backshield1 = Rect(30, 240, 50, 35, fill='dimGray', border='black')
backshield2 = Oval(55, 240, 80, 10, fill='navy')
backshield3 = Oval(55, 280, 80, 10, fill='navy')
mirror1 = Oval(10, 200, 30, 10, fill='lightGray')
mirror2 = Oval(100, 200, 30, 10, fill='lightGray')

# Red Car #
redbody2 = Rect(140, 310, 150, 70, fill='red')
redbumper2 = Oval(140, 345, 20, 80, fill='red')
redfrontwheel1 = Oval(170, 300, 40, 20)
redfrontwheel2 = Oval(250, 300, 40, 20)
redbackwheel1 = Oval(170, 389, 40, 20)
redbackwheel2 = Oval(250, 389, 40, 20)
redwindshield1 = Rect(160, 320, 30, 50, fill='dimGray', border='black')
redwindshield2 = Oval(190, 345, 10, 80, fill='red')
redbackshield1 = Rect(240, 320, 35, 50, fill='dimGray', border='black')
redbackshield2 = Oval(230, 345, 10, 80, fill='red')
redbackshield3 = Oval(275, 345, 10, 80, fill='red')
redmirror1 = Oval(200, 300, 10, 30, fill='lightGray')
redmirror2 = Oval(200, 390, 10, 30, fill='lightGray')


# Red Car Group #
cars1 = Group()
cars1.add(body1)
cars1.add(bumper1)
cars1.add(frontwheel1)
cars1.add(frontwheel2)
cars1.add(backwheel1)
cars1.add(backwheel2)
cars1.add(windshield1)
cars1.add(windshield2)
cars1.add(backshield1)
cars1.add(backshield2)
cars1.add(backshield3)
cars1.add(mirror1)
cars1.add(mirror2)


# Red Car Group #
cars2 = Group()
cars2.add(redbody2)
cars2.add(redbumper2)
cars2.add(redfrontwheel1)
cars2.add(redfrontwheel2)
cars2.add(redbackwheel1)
cars2.add(redbackwheel2)
cars2.add(redwindshield1)
cars2.add(redwindshield2)
cars2.add(redbackshield1)
cars2.add(redbackshield2)
cars2.add(redbackshield3)
cars2.add(redmirror1)
cars2.add(redmirror2)


#Invisible Line#
invisibleLine = Line(350, 200, 50, 200, fill=None, lineWidth=5)
invisibleLine2 = Line(200, 50, 200, 350, fill=None, lineWidth=5)
invisibleLine2.rotateSpeed = 5


# Lap Counter #
lapRect = Rect(145, 165, 110, 70, fill=None, border='white')
lap = Label("Lap: ", 180, 200, fill='white', size=25)
counter = Label(0, 225, 200, fill='white', size=25)


def onStep():

    invisibleLine.rotateAngle += 8
    cars1.rotateAngle += 8
    cars1.centerX = invisibleLine.x2
    cars1.centerY = invisibleLine.y2

    invisibleLine2.rotateAngle += 8
    cars2.rotateAngle += 8
    cars2.centerX = invisibleLine2.x2
    cars2.centerY = invisibleLine2.y2

    if bumper1.hitsShape(b):
        counter.value = counter.value + 1
    elif counter.value == 20:
        app.paused = True
        Rect(0, 0, 400, 400, fill='black', opacity=50)
        Label("Blue Wins!", 200, 200, size=80, fill='white')
    elif redbumper2.hitsShape(b):
        counter.value += 0
    elif counter.value == 2:
        invisibleLine2.rotateAngle += 8
        cars2.rotateAngle += 8
    elif counter.value == 8:
        invisibleLine.rotateAngle += 8
        cars1.rotateAngle += 8
    elif counter.value == 14:
        invisibleLine2.rotateAngle += 8
        cars2.rotateAngle += 8
    elif counter.value == 16:
        invisibleLine.rotateAngle += 8
        cars1.rotateAngle += 8
    elif counter.value == 18:
        invisibleLine2.rotateAngle += 8
        cars2.rotateAngle += 8


def onMousePress(mouseX, mouseY):

    if cars1.hits(mouseX, mouseY):
        app.paused = True
    elif cars2.hits(mouseX, mouseY):
        app.paused = True
    else:
        app.paused = False


def onKeyPress(key):
    if key == 'right':
        invisibleLine2.rotateAngle += 10
        cars2.rotateAngle += 10


cmu_graphics.run()
