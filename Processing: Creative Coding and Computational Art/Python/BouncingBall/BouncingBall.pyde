xspeed = 3
yspeed = 6

wdth = 10
ht = 10

xpos = 500 / 2
ypos = 500 / 2



def setup():
    size(500, 500)
    background(0)
    noStroke()
    frameRate(30)

def draw():
    
    global xpos, ypos, wdth, ht, xspeed, yspeed
    
    background(0)
    ellipse(xpos, ypos, wdth, ht)
    
    xpos += xspeed
    ypos += yspeed
    
    if (xpos >= width - wdth / 2 or xpos <= wdth / 2):
        xspeed *= -1

    if (ypos >= height - ht / 2 or ypos <= ht / 2):
        yspeed *= -1
