import numpy as np
import pandas as pd
import math
import scipy.linalg as lin

u = 0; v = 0
uv = np.array([[0], [0]])
# eta = 0.01
for i in range(5):
    du = math.exp(u)+v*math.exp(u*v)+2*u-2*v-3
    dv = 2*math.exp(2*v)+u*math.exp(u*v)-2*u+4*v-2
    # u -= eta*du
    # v -= eta*dv
    du2 = math.exp(u)+v**2*math.exp(u*v)+2
    dv2 = 4*math.exp(2*v)+u**2*math.exp(u*v)+4
    dudv = math.exp(u*v)+v*u*math.exp(u*v)-2
    ddE = np.array([[du2, dudv], [dudv, dv2]])
    dE = np.array([[du], [dv]])
    uv = uv-lin.inv(ddE).dot(dE)
    u = uv[0, 0]
    v = uv[1, 0]
print('u and v: ',uv.T)
E = math.exp(u)+math.exp(2*v)+math.exp(u*v)+u**2-2*u*v+2*v**2-3*u-2*v
print('E: ',E)
