curve_fitting_factor = .03
      
def setup():
    size(400, 400)
    background(255)
    fill(0)
    
    for i in range(-102, 124):
        x = i
        y = pow(i, 2) - 20 * x + 200
        ellipse(x + 200, y * curve_fitting_factor, 4, 4)
