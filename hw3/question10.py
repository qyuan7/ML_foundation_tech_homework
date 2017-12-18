import numpy as np
import math
from numpy import linalg
import scipy.linalg as lin
u=0; v=0
uv = np.array([[0],[0]])
for i in range(5):
    du = math.exp(u)+v*math.exp(u*v)+2*u-2*v-3
    dv = 2*math.exp(2*v)+u*math.exp(u*v)-2*u+4*v-2
    du2 = math.exp(u)+v**2*math.exp(u*v)+2
    dv2 = 4*math.exp(2*v)+u**2*math.exp(u*v)+4
    dudv = math.exp(u*v)+u*v*math.exp(u*v)-2
    delta = np.array([[du],[dv]])
    hess = np.array([[du2,dudv],[dudv,dv2]])
    #hess_inv = lin.inv(hess)
    uv = uv-lin.inv(hess).dot(delta)
    u = uv[0,0]
    v = uv[1,0]
    #u = u-lin.inv(hess).dot(delta)[0].item()
    #v = v-lin.inv(hess).dot(delta)[1].item()
E = math.exp(u)+math.exp(2*v)+math.exp(u*v)+u**2-2*u*v+2*v**2-3*u-2*v
print u,v,E
