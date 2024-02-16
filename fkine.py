import roboticstoolbox as rtb
import numpy as np

import arm_parameters

Arm = arm_parameters.ARM().ets()
solver = rtb.IK_NR(pinv=True)