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

from random import sample, random, choice
from time import perf_counter

from IPython import embed

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

        self.xcoords = np.array([self.vert_left[0], self.vert_top[0], self.vert_right[0], self.vert_left[0] ])
        self.ycoords = np.array([self.vert_left[1], self.vert_top[1], self.vert_right[1], self.vert_left[1] ])


class Sierpinksi:

    def __init__(self, main_triangle=EquiTriangle(), max_levels=3):
        self.max_levels = max_levels
        self.triangles = { i : [] for i in range(self.max_levels+1) }
        self.triangles[0].append(main_triangle)

    def __build_set(self,):
        [[self.__build(tri,level) for tri in parent] for level, parent in self.triangles.items()]

    def __build(self,tri,level):
        if level == self.max_levels: return
        self.triangles[level+1].append(EquiTriangle(tri.leg_size*0.5, tri.vert_left,  vert='left'))
        self.triangles[level+1].append(EquiTriangle(tri.leg_size*0.5, tri.vert_right, vert='right'))
        self.triangles[level+1].append(EquiTriangle(tri.leg_size*0.5, tri.vert_top,   vert='top'))

    def draw(self, fig=None):
        self.__build_set()
        dlen = sum(len(v) for v in self.triangles.values())
        colors = cm.inferno_r(np.linspace(0,1,dlen))
        colors = colors[::-1]

        if fig is None:
            fig = plt.figure()
            fig.patch.set_facecolor('k')

        j = 0
        for k,v in self.triangles.items():
            for i,tri in enumerate(v):
                plt.fill(tri.xcoords, tri.ycoords, color=colors[j], alpha=0.2)
                j+=1
        plt.axis("off")
        return plt


class Barnsley:

    # Barnsley coefficients

    # mats = {
    #     'f0': np.array([ [  0.00,  0.00 ], [  0.00, 0.16 ] ]),
    #     'f1': np.array([ [  0.85,  0.04 ], [ -0.04, 0.85 ] ]),
    #     'f2': np.array([ [  0.20, -0.26 ], [  0.23, 0.22 ] ]),
    #     'f3': np.array([ [ -0.15,  0.28 ], [  0.26, 0.24 ] ])
    # }

    # vecs = {
    #     'f0' : np.array([ 0.00, 0.00 ]),
    #     'f1' : np.array([ 0.00, 1.60 ]),
    #     'f2' : np.array([ 0.00, 1.60 ]),
    #     'f3' : np.array([ 0.00, 0.44 ]),
    # }

    # prob = [0.01,0.85,0.07,0.07]

    mats = {
        'f0': np.array([ [  0.00,  0.00 ], [  0.00, 0.16 ] ]),
        'f1': np.array([ [  0.69,  0.04 ], [ -0.04, 0.85 ] ]),
        'f2': np.array([ [  0.20, -0.26 ], [  0.23, 0.22 ] ]),
        'f3': np.array([ [ -0.15,  0.28 ], [  0.26, 0.24 ] ])
    }

    vecs = {
        'f0' : np.array([ 0.00, 0.00 ]),
        'f1' : np.array([ 0.00, 1.60 ]),
        'f2' : np.array([ 0.00, 1.60 ]),
        'f3' : np.array([ 0.00, 0.44 ]),
    }

    prob = [0.01,0.85,0.07,0.07]


    # mats = {
    #     'f0' : np.array( [ [  0.000,  0.000 ], [  0.000, 0.250 ] ] ),
    #     'f1' : np.array( [ [  0.950,  0.005 ], [ -0.005, 0.930 ] ] ),
    #     'f2' : np.array( [ [  0.035, -0.200 ], [  0.160, 0.040 ] ] ),
    #     'f3' : np.array( [ [ -0.040,  0.200 ], [  0.160, 0.040 ] ] )
    # }  

    # vecs = {
    #     'f0' : np.array( [  0.000, -0.400 ] ),
    #     'f1' : np.array( [ -0.002,  0.500 ] ),
    #     'f2' : np.array( [ -0.090,  0.020 ] ),
    #     'f3' : np.array( [  0.083,  0.120 ] )
    # }

    # probs = [ 0.02, 0.84, 0.07, 0.07 ]

    def __init__(self, origin=[0.,0.], scale=1.0, points=1000, affine_matrix=None, affine_vector=None, probabilities=None):
        self.origin = origin
        self.points = points
        self.scale  = scale
        if affine_matrix is not None: self.mats = affine_matrix
        if affine_vector is not None: self.vecs = affine_vector
        if probabilities is not None: self.prob = probabilities


    def draw(self,points=None, fig=None):
        
        if points is not None:
            self.points = points

        self.x = np.zeros((self.points))
        self.y = np.zeros((self.points))
        self.x[0], self.y[0] = self.origin

        [self.__next_point(i) for i in range(1,self.points)]

        self.z = np.sqrt( (self.x-self.origin[0])**2 + (self.y-self.origin[1])**2 )

        if fig is None:
            fig = plt.figure()
            fig.patch.set_facecolor('k')
        plt.scatter(self.x*self.scale, self.y*self.scale, marker='o', s=0.01, c=self.z, cmap=cm.Greens_r)
        plt.axis('off')
        return plt

    def __next_point(self,i):


        r = random()

        if r < self.prob[0]:
            self.x[i] = self.mats['f0'][0,0]*self.x[i-1] + \
                        self.mats['f0'][0,1]*self.y[i-1] + \
                        self.vecs['f0'][0]

            self.y[i] = self.mats['f0'][1,0]*self.x[i-1] + \
                        self.mats['f0'][1,1]*self.y[i-1] + \
                        self.vecs['f0'][1]
        
        elif r < sum(self.prob[0:2]):
            self.x[i] = self.mats['f1'][0,0]*self.x[i-1] + \
                        self.mats['f1'][0,1]*self.y[i-1] + \
                        self.vecs['f1'][0]

            self.y[i] = self.mats['f1'][1,0]*self.x[i-1] + \
                        self.mats['f1'][1,1]*self.y[i-1] + \
                        self.vecs['f1'][1]
        
        elif r < sum(self.prob[0:3]):
            self.x[i] = self.mats['f2'][0,0]*self.x[i-1] + \
                        self.mats['f2'][0,1]*self.y[i-1] + \
                        self.vecs['f2'][0]

            self.y[i] = self.mats['f2'][1,0]*self.x[i-1] + \
                        self.mats['f2'][1,1]*self.y[i-1] + \
                        self.vecs['f2'][1]

        else:
            self.x[i] = self.mats['f3'][0,0]*self.x[i-1] + \
                        self.mats['f3'][0,1]*self.y[i-1] + \
                        self.vecs['f3'][0]

            self.y[i] = self.mats['f3'][1,0]*self.x[i-1] + \
                        self.mats['f3'][1,1]*self.y[i-1] + \
                        self.vecs['f3'][1]



if __name__ == '__main__':

    fig = plt.figure()
    fig.patch.set_facecolor('k')    

    tri = EquiTriangle(vert_coords=(-0.5,0.0))
    sie = Sierpinksi(main_triangle=tri, max_levels=7)
    fig = sie.draw(fig=fig)
    

    bar = Barnsley(points=20000, scale=0.04)
    fig = bar.draw(fig=fig)

    fig.show()
    # fig.savefig("../images/fair_0007_recursives.pdf", dpi=1096)

