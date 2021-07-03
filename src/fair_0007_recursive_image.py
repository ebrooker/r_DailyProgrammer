'''
Ezra S. Brooker
Date Created: 2021-07-03

https://www.reddit.com/r/dailyprogrammer/comments/pr265/2152012_challenge_7_intermediate/

Write a program that draws a recursive image.

For example, a Sierpinski triangle, a Barnsley fern, or a Mandelbrot set 
fractal would be good drawings.

Any recursive image will do, but try to make them look fun or interesting.

Bonus points for adding a color scheme!

Please post a link to a sample image produced by your program, and above 
all, be creative.

'''

import sys
if sys.version[0] != '3':
    raise Exception("Python 2 is no longer supported, please use Python 3")

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm

from random import sample

class EquiTriangle:

    def __init__(self, leg_size=1., vert_coords=(0.,0.), vert='left'):

        self.leg_size   = leg_size

        if vert.lower() == 'left':
            self.vert_left  = vert_coords
            self.vert_right = ( vert_coords[0] +     self.leg_size, vert_coords[1]                                   )
            self.vert_top   = ( vert_coords[0] + 0.5*self.leg_size, vert_coords[1] + (3.**(0.5)) * 0.5*self.leg_size )

        elif vert.lower() == 'right':
            self.vert_right = vert_coords
            self.vert_left  = ( vert_coords[0] -     self.leg_size, vert_coords[1]                                   )
            self.vert_top   = ( vert_coords[0] - 0.5*self.leg_size, vert_coords[1] + (3.**(0.5)) * 0.5*self.leg_size )

        elif vert.lower() == 'top':
            self.vert_top   = vert_coords
            self.vert_right = ( vert_coords[0] + 0.5*self.leg_size, vert_coords[1] - (3.**(0.5)) * 0.5*self.leg_size )
            self.vert_left  = ( vert_coords[0] - 0.5*self.leg_size, vert_coords[1] - (3.**(0.5)) * 0.5*self.leg_size )

        self.xcoords    = [self.vert_left[0], self.vert_top[0], self.vert_right[0], self.vert_left[0] ]
        self.ycoords    = [self.vert_left[1], self.vert_top[1], self.vert_right[1], self.vert_left[1] ]


class SierpinksiTriangle:

    def __init__(self, main_triangle=EquiTriangle(), max_levels=3):

        self.max_levels = max_levels
        self.triangles = { i : [] for i in range(self.max_levels+1) }
        self.triangles[0].append(main_triangle)

    def build_set(self,):
        [[self.__build(tri,level) for tri in parent] for level, parent in self.triangles.items()]

    def __build(self,tri,level):
        if level == self.max_levels: return
        self.triangles[level+1].append(EquiTriangle(tri.leg_size*0.5, tri.vert_left,  vert='left'))
        self.triangles[level+1].append(EquiTriangle(tri.leg_size*0.5, tri.vert_right, vert='right'))
        self.triangles[level+1].append(EquiTriangle(tri.leg_size*0.5, tri.vert_top,   vert='top'))

    def plot_set(self):

        dlen = sum(len(v) for v in self.triangles.values())
        colors = cm.inferno_r(np.linspace(0,1,dlen))
        # colors = colors[1:-1]
        colors = colors[::-1]

        fig = plt.figure()
        fig.patch.set_facecolor('k')
        j = 0
        for k,v in self.triangles.items():

            # colors = cm.inferno_r(np.linspace(0,1,len(v)+3))
            # colors = colors[1:-1]
            # colors = colors[::-1]

            for i,tri in enumerate(v):
                plt.fill(tri.xcoords, tri.ycoords, color=colors[j])
                j+=1

        plt.axis("off")
        # plt.savefig("../images/fair_0007_sierpinski_triangle.pdf", dpi=1096)
        plt.show()


if __name__ == '__main__':

    sie = SierpinksiTriangle(max_levels=7)
    sie.build_set()
    sie.plot_set()