# Main testing class for T6xyz Algos
from manim import *

from BST import *


class makeBST(MovingCameraScene):

    def construct(self):
        # dot1 = LabeledDot(Tex("2", color="black"), radius=.5)
        # dot2 = LabeledDot(Tex("4", color="black"), radius=.5)
        # dot3 = LabeledDot(Tex("6", color="black"), radius=.5)
        # self.play(dot2.animate.shift(2 *RIGHT))
        # self.play(dot3.animate.shift(4 *RIGHT))
        # arrow1 = Arrow(buff = -1, start=dot1, end=dot2)
        # arrow2 = Arrow(buff = -1, start=dot2, end=dot3)
        # self.add(dot1)
        # self.add(arrow1)
        # self.add(dot2)
        # self.add(arrow2)
        # self.add(dot3)
        
    
        # self.wait()


        myBST = BST(self)

        myBST.add(4)

        myBST.add(6)

        myBST.add(8)

        myBST.add(5)

        myBST.add(0)

        myBST.add(-3)

        myBST.add(2)

        myBST.add(1)

        myBST.add(7)

        myBST.add(9)
        myBST.add(-4)
        myBST.add(-1)
        myBST.add(3)
        myBST.add(-10)

        self.wait()

        

        




