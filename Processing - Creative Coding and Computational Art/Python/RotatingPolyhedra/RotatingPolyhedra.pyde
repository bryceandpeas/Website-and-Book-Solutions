rot_x = 0
rot_y = 0

def setup():
    size(400, 400, P3D)
    frameRate(30)

def draw():
    
    global rot_x, rot_y
    
    background(255)
    translate(width / 2, height / 2, mouseY - 100)
    
    rotateY(rot_y += 0.05)
    rotateX(rot_x += 0.1)

    sphereDetail(mouseX / 32)
    fill(0)
    stroke(255)

    sphere(30)
    fill(50, 50, 50, 175)
    noStroke()

    box(80)
    noFill()
    sphereDetail(8)
    stroke(0)
  
    sphere(80)
