screen_fade_value = 20
size_max = 30

def setup():
    size(400, 400)    
    background(130, 130, 240)    
    noFill()    

def draw():
    return None

def fade_screen():
    fill(130, 130, 240, screen_fade_value)    
    noStroke()    
    rect(0, 0, width, height)    
    
def paint_shapes(is_dragged):
    
    if (is_dragged):
        noStroke()
        ellipse(mouseX, mouseY, radius_x, radius_y)
    else:
        noFill()
        stroke(random(255))
        rect(mouseX, mouseY, random(size_max), random(size_max))

def mousePressed():
    
    global radius_x, radius_y
    
    fade_screen()
    radius_x = random(size_max)
    radius_y = random(size_max)
    fill(random(255), random(255), random(255), 100)
    
def mouseMoved():
    paint_shapes(False)

def mouseDragged():
    paint_shapes(True)

