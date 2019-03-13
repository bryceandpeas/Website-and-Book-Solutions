y = 0
angle = 0
amplitude = 5
wave_gap = 24
frequency = 5

def setup():
    size(400, 400)
    background(255)
    noFill()
    frameRate(30)

def draw():
    
    global y, angle, amplitude, wave_gap, frequency
    
    if (y < height):
        py = 0
        
        for i in range(0, width):
            py = y + sin(radians(angle)) * amplitude
            point(i, py)
            angle += frequency

        y += wave_gap
