import pyfits
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
#pra ver o header
hdulist = pyfits.open('2.fits')

#para ver o cabecalho e a dimensao o aquivos filho 
hdulist.info()
print hdulist[0].header
