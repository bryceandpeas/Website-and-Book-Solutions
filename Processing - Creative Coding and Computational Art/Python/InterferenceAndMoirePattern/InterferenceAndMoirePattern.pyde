angle = 0
amplitude = 0.05
wave_gap = 10
frequency = 0.1
ring_growth_rate = 0.5
is_inactive = True

interval = 400 * 0.03
spacer = interval

def setup():
    size(400, 400)
    noFill()
    frameRate(30)

def draw():
    
    global angle, amplitude, wave_gap, frequency
    global ring_growth_rate, is_inactive, spacer, interval
    
    background(0)
    stroke(255)
    
    py = 0

    for i in range(0, height, wave_gap):
        for j in range(0, width):
            py = i + sin(radians(angle)) * mouseY * amplitude
            point(j, py)
            angle += mouseX * frequency

    for i in range(0, int(width / 2 * spacer / interval)):
        ellipse(mouseX, mouseY, 10 + i, 10 + i)
  
    if (mousePressed):
        angle = 0
        is_inactive = False
        if (spacer < interval * 2):
            spacer += ring_growth_rate

    if (is_inactive):
        if (spacer > interval):
            spacer -= ring_growth_rate
            
def mouseReleased():
    is_inactive = True
