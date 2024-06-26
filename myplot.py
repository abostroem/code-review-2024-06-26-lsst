import numpy as np
import matplotlib
import os
from matplotlib import pyplot
from astropy.io import fits
import glob

data = np.ones([1024, 1024])
data[500:600, 200:300] = 0
col1 = data[20, :]
col2 = data[200, :]
col3 = data[800, :]

g1= pyplot.figure()
pyplot.plot(np.arange(1024), col1)
mean = np.mean(col1)
pyplot.axhline(mean)
pyplot.legend(['Column 20', 'Mean'])
pyplot.title('Plot of Column 20 Values and Mean')
pyplot.xlabel('Pixels')
pyplot.ylabel('Intensity')

g2=pyplot.figure()
pyplot.plot(np.arange(1024), col2)
pyplot.axhline(np.mean(col2))
pyplot.legend(['Column 200', 'Mean'])
pyplot.title('Plot of Column 200 Values and Mean')
pyplot.xlabel('Pixels')
pyplot.ylabel('Intensity')

g3=pyplot.figure()
pyplot.plot(np.arange(1024), col3)
mean = np.mean(col3)
pyplot.axhline(mean)
pyplot.legend(['Column 800', 'Mean'])
pyplot.title('Plot of Column 800 Values and Mean')
pyplot.xlabel('Pixels')
