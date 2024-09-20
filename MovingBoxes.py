import pgzrun
WIDTH=500
HEIGHT=500
Box1=Rect((20,20),(50,50))
Box2=Rect((20,20),(50,50))


def draw():
    screen.clear()
    screen.fill('light blue')
    screen.draw.filled_rect(Box1,'red')
    screen.draw.filled_rect(Box2,'green')

def update():
    Box1.x=Box1.x+10
    if Box1.x > WIDTH:
        Box1.x=0
    Box2.y=Box2.y+10
    if Box2.y > HEIGHT:
        Box2.y=0


    


    



























pgzrun.go()