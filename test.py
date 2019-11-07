from random import seed

from exhaustive import exhaustive
from utils import create_points, scatter_plot
from TP1 import jarviss
from TP1 import floyd
from TP1 import hull_floyd
from TP1 import graham
import time

def main():
    """
    A sample main program to test our algorithms.

    @return: None
    """
    to=time.time()
    # initialize the random generator seed to always use the same set of points
    seed(0)
    # creates some points
    pts = create_points(1800)
    show = True  # to display a frame
    save = False  # to save into .png files in "figs" directory
    scatter_plot(pts, [[]], title="convex hull : initial set", show=show, save=save)
    print("Points:", pts)
    # compute the hull
    #hull = exhaustive(pts, show=show, save=save)
    print("graham",graham(pts))
    hull=graham(pts)
    print("Hull:", hull)
    scatter_plot(pts, [hull], title="convex hull : final result", show=True, save=save)
    print("Temps d'éxecution: %s secondes" %(time.time()-to))

if __name__ == "__main__":
    main()
