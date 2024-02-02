import numpy as np
from VoxcraftVXA import VXA
from VoxcraftVXD import VXD
import os

body = np.asarray([[[1,1],
                    [1,1]],
                    [[1,1],
                    [1,1]]]) # set data

vxa = VXA(Data=body, EnableExpansion=1, TempEnabled=1, VaryTempEnabled=1, TempPeriod=0.1, TempBase=25, TempAmplitude=20)
mat1 = vxa.add_material(RGBA=(0,255,0), E=1e9, RHO=1e3) # passive
mat2 = vxa.add_material(RGBA=(255,0,0), E=1e7, RHO=1e6, CTE=0.01) # active
vxa.write("base.vxa")

os.system("voxcraft-viz data/base.vxa")


