import numpy as np
from roboticstoolbox import DHRobot, RevoluteMDH


class ARM(DHRobot):

    def __init__(self):

        deg = np.pi/180
        mm = 1e-3
        L = [
            RevoluteMDH(
                #value of length
                a=36,
                d=0.0,
                alpha=0.0,
                qlim=np.array([-np.pi/2,np.pi/2]),
                #mass of first portion of the arm
                m=2,
                I=[
                    7.03370e-01,
                    7.06610e-01,
                    9.11700e-03,
                    -1.39000e-04,
                    1.91690e-02,
                    6.77200e-03,
                ],
                G=1
            ),
            RevoluteMDH(
                #value of length part 2
                a=5,
                d=1,
                alpha=-np.pi/2,
                qlim=np.array([-np.pi/2,np.pi/2]),
                #mass of part 2
                m=2,
                I=[
                    7.03370e-01,
                    7.06610e-01,
                    9.11700e-03,
                    -1.39000e-04,
                    1.91690e-02,
                    6.77200e-03,
                ],
                G=1,
            ),
            RevoluteMDH(
                #value of length of part 3
                a=25,
                d=0.0,
                alpha=np.pi/2,
                qlim=np.array([-np.pi/2,np.pi/2]),
                #mass of part 3
                m=2,
                I=[
                    7.03370e-01,
                    7.06610e-01,
                    9.11700e-03,
                    -1.39000e-04,
                    1.91690e-02,
                    6.77200e-03,
                ],
                G=1,
            ),
            RevoluteMDH(
                #value of length of part 4
                a=18,
                d=0.0,
                alpha=0.0,
                qlim=np.array([-np.pi/2,np.pi/2]),
                #mass of part 4
                m=2,
                I=[
                    7.03370e-01,
                    7.06610e-01,
                    9.11700e-03,
                    -1.39000e-04,
                    1.91690e-02,
                    6.77200e-03,
                ],
                G=1,
            )
        ]

        #tool = transl(0,0,tool_offset) @ trotz(-np.pi/4)
        super().__init__(
            L,
            name="Panda",
            manufacturer="Franka Emika",
            meshdir="meshes/FRANKA-EMIKA/Panda",
            # tool=tool,
        )

        self.qr = np.array([0, -0.3, 0, -2.2])
        self.qz = np.zeros(4)

        self.addconfiguration("qr", self.qr)
        self.addconfiguration("qz", self.qz)

if __name__ == "__main__":  # pragma nocover

    arm = ARM()
    print(arm)