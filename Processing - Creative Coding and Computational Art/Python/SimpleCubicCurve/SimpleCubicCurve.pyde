curve_fitting_factor = .0001

def setup():
    size(400, 400)
    background(255)
    fill(0)
    
    for i in range(-102, 300):
        x = i
        y = pow(i, 3) *.2 + x * x * -50 + x -100
        ellipse(x + 100, y * curve_fitting_factor + 200, 2, 2)