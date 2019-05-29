import add
import math


a = 10
b = 3

a1 = 0.01
b1 = 12

a2 = 1
b2 = 3.5

drinkColor = [102,46,12]

def torus(u, v):
    x = (a+b*math.cos(u))*math.cos(v)
    y = b*math.sin(u)
    z = (a+b*math.cos(u))*math.sin(v)
    return ([x,y,z])

def torus1(u, v):
    x = (a1+b1*math.cos(u))*math.cos(v)
    y = b1*math.sin(u) + 40
    z = (a1+b1*math.cos(u))*math.sin(v)
    return ([x,y,z])

def torus2(u, v):
    x = (a2+b2*math.cos(u))*math.cos(v)
    y = b2*math.sin(u) + 54
    z = (a2+b2*math.cos(u))*math.sin(v)
    return ([x,y,z])

add.parametric(torus,0,2*math.pi,20,0,2*math.pi,100,drinkColor)
add.circle([0,-3,0],[0,3,0],10.5,100,drinkColor)
add.cylinder([0,1.5,0],[0,40,0],12,100,drinkColor)
add.cylinder3([0,5,0],[0,38,0],12.05,100,[155, 154, 153])
add.parametric(torus1,0,2*math.pi,20,0,2*math.pi,100,drinkColor)
add.cylinder([0,50,0],[0,60,0],4,100,drinkColor)
add.cylinder([0,60,0],[0,63,0],4,100,[216, 216, 216])
add.cylinder([0,63,0],[0,69,0],4.2,100,[247, 241, 121])
add.cylinder([0,63,0],[0,69,0],4.2,100,[247, 241, 121])
add.parametric(torus2,0,2*math.pi,20,0,4*math.pi,100,drinkColor)



add.off('bonke.off')