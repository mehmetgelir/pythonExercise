import sys
import os
ff = "{} {}"
try:
    print(sys.executable)
    print(ff.format("Python", sys.version))
    import matplotlib
    print(ff.format("matplotlib", matplotlib.__version__))
    import numpy
    print(ff.format("numpy", numpy.__version__))
    import scipy
    print(ff.format("scipy", scipy.__version__))
except:
    pass