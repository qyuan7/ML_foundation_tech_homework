import numpy as np
import pandas as pd
import math
import scipy.linalg as lin

u = 0; v = 0
eta = 0.01
for i in range(5):
    du = math.exp(u)+v*math.exp(u*v)+2*u-2*v-3
    dv = 2*math.exp(2*v)+u*math.exp(u*v)-2*u+4*v-2
    u -= eta*du
    v -= eta*dv
print('u=',u,'v=',v)
E = math.exp(u)+math.exp(2*v)+math.exp(u*v)+u**2-2*u*v+2*v**2-3*u-2*v
print(E)
