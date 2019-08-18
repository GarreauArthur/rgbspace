import numpy as np
from PIL import Image


def rgb_to_hsv(r, g, b):
    r, g, b = r/255.0, g/255.0, b/255.0
    mx = max(r, g, b)
    mn = min(r, g, b)
    df = mx-mn
    if mx == mn:
        h = 0
    elif mx == r:
        h = (60 * ((g-b)/df) + 360) % 360
    elif mx == g:
        h = (60 * ((b-r)/df) + 120) % 360
    elif mx == b:
        h = (60 * ((r-g)/df) + 240) % 360
    if mx == 0:
        s = 0
    else:
        s = (df/mx)*100
    v = mx*100
    return h, s, v


def np_conv(x):

  shape = x.shape
  color = np.zeros((shape[0],1))
  for i in range(shape[0]):
    h,s,v = rgb_to_hsv(x[i,0],x[i,1],x[i,2])
    if h < 61: # red
      color[i] = 0
    elif h < 121: # yellow
      color[i] = 1
    elif h < 181: # green
      color[i] = 2
    elif h < 241: # cyan
      color[i] = 3
    elif h < 301: # blue
      color[i] = 4
    elif h < 361: # magenta
      color[i] = 5
  return color

a = np.random.randint(0,256, (10000,3))
colors = np_conv(a)
res = np.concatenate([a, colors], axis=1)
np.savetxt("data.csv", res, fmt='%.18e', delimiter=",")

