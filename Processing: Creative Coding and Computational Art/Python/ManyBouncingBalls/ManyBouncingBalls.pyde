ballcount = 500
ballsize = 8
ballspeed = 3
xspeed = []
yspeed = []
xpos = []
ypos = []
wdth = []
ht = []

def setup():
    size(500, 500)
    background(0)
    
    for i in range(0, ballcount):
        xspeed.append(random(1, ballspeed))
        yspeed.append(random(-ballspeed, ballspeed))
        wdth.append(random(1, ballsize))
        ht.append(wdth[i])
        xpos.append(width / 2 + random(-width / 3,  width / 3))
        ypos.append(height / 2 + random(-height / 3,  height / 3))

    noStroke()
    frameRate(30)
    
def draw():
    
    global ballcount, xpos, ypos, wdth, ht
    
    background(0)
    
    for i in range(0, ballcount):
        ellipse(xpos[i], ypos[i], wdth[i], ht[i])
        xpos[i] += xspeed[i]
        ypos[i] += yspeed[i]

        if (xpos[i] + wdth[i] / 2 >= width or xpos[i] <= wdth[i] / 2):
            xspeed[i] *= -1

        if (ypos[i] + ht[i] / 2 >= height or ypos[i] <= ht[i] / 2):
            yspeed[i] *= -1

    
