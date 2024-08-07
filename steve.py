from sense_hat import SenseHat

sense = SenseHat()

h = (139,69,19)
s = (255,228,196)
n = (160,82,45)
e = (255,255,255)
b = (0,0,255)

steve_matrix = [
  h,h,h,h,h,h,h,h,
  h,h,h,h,h,h,h,h,
  h,s,s,s,s,s,s,h,
  s,s,s,s,s,s,s,s,
  s,e,b,s,s,b,e,s,
  s,s,s,n,n,s,s,s,
  s,s,h,s,s,h,s,s,
  s,s,h,h,h,h,s,s,
]

sense.set_pixels(steve_matrix)