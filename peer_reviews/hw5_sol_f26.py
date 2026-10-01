#! /usr/bin/env python3

# Initial version AST5765/4762 HW5 Solutions by Joseph Harrington <jh@physics.ucf.edu>
# Adapted by TK Fall 2024

# NOTE: This assignment uses Monte Carlo methods to generate datasets.
# This means that you may get different numbers from those presented
# here.  In the elimination questions, you may eliminate all 4 bad
# points right away, or have one that is within the data's range and
# is never gotten rid of.  Try running it more than once to get a
# sense for how it behaves.

import numpy as np
import matplotlib.pyplot as plt
import numpy.random

plt.ion()

print("Solutions")
print("AST 5765")
print("HW 6")

# === This part is part of the practicum ===

print("=== Practicum part 1 ===")

N     = 10000
#sigp = np.sqrt(N)   # appropriate for Gaussian approximation of Poisson
#cx   =         N    # appropriate for Gaussian approximation of Poisson
Nump  = 396
psamp = np.random.poisson(N, Nump)

ulo   = 0.
uhi   = 1e6
Numu  = 4
usamp = np.random.uniform(ulo, uhi, Numu)

samp = np.concatenate((psamp, usamp))

print("start mean: "+ str(samp.mean()))
# 15066.9163158

smed = np.median(samp.flat)
print("start median: "+ str(smed))
# 9999.0, which is closer to N = 10000.

print("=== Part 2 ===")

sstd = samp.std()
print("Second std dev: "+ str(sstd))
# 60304.627165

rejsig1 = 5.                    # Reject greater than this many sigma.
subsamp = samp[ np.abs((samp-smed)/sstd) < rejsig1 ]

print("subsample    mean: "+ str(subsamp.mean()))
# 10167.2211524

print("subsample  median: "+ str(np.median(subsamp)))
# 9999.0

print("subsample std dev: "+ str(subsamp.std()))
# 3378.8274823

# Three points (in this run) have been removed.  The median is still
# accurate, the mean is more accurate than before, but the standard
# deviation is still skewed.

print("=== Notice that we actually did this in class, so they should have this right (I hope) ===")

ssstd = subsamp.std()
print("subsample std dev: "+ str(ssstd))
# 3378.8274823

rejsig2 = 5.                    # Reject greater than this many sigma.
subsubsamp = subsamp[ np.abs((subsamp-smed)/ssstd) < rejsig2 ]

print("subsubsample    mean: "+ str(subsubsamp.mean()))
# 9997.5

print("subsubsample  median: "+ str(np.median(subsubsamp)))
# 9998.5

print("subsubsample std dev: "+ str(subsubsamp.std()))
# 98.0439887876

# Now the mean is as accurate than the median, and both are very close
# to the correct answer.  The standard deviation is ~98, close to the
# nominal value of np.sqrt(10000.).

# print(np.sqrt(10000.))
# 100.0

# This method misses bad pixels that happen to fall in the range of
# good data, even if they appear to stand out.

# === Problem 3 ===

print("=== Problem 3 ===")

# --------------------------------------------------Functions----------------------------------------------------------
def sigrej(data, rejlim, mask=None):
  """Function that performs sigma clipping.

  Parameters
  ----------
  data : array_like
    The data set that you want to run the sigma clipping on.
  rejlim : tuple
    The sigma limits you want to use. The tuple should contain N values
    depending on the number of iterations N you want to do.
  mask : array_like
    Optional boolean array mask to pass a mask for the function to use.

  Returns
  -------
  mask : array_like
    The modified boolean mask to use on your data.

  Examples
  --------
  >>> ttar = np.array([ 984. ,  968. ,  995. , 1049. ,
                       1024. , 1034. ,  965. ,  987. ,
                        947. , 1073. , 1034. ,  918. ,
                        987. , 1006. , 1056. ,  965. ,
                       1019. ,  978. , 1011. ,  979. ,
                        969. ,  937. ,  971. , 1022. ,
                        958. , 1042. ,
                     447431.23453748 , 811528.27457857 ,
                     268631.77214013 , 606309.85792563])
  >>> maskout = sigrej(ttar, (5.,5.,1.), [True for i in range(len(ttar))] )

  Returns:
  >>> array([ True,  True,  True,  True,  True,  True,  True,  True,  True,
    True,  True,  True,  True,  True,  True,  True,  True,  True,
    True,  True,  True,  True,  True,  True,  True,  True, False,
     False, False, False])
  and filtered data
  >>>  print(ttar[maskout])
  >>>  array([ 984.,  968.,  995., 1049., 1024., 1034.,  965.,  987.,  947.,
    1073., 1034.,  918.,  987., 1006., 1056.,  965., 1019.,  978.,
    1011.,  979.,  969.,  937.,  971., 1022.,  958., 1042.])
  """
  if mask is not None:
    # Tests
    if np.shape(mask) != np.shape(data):
      raise Exception('The mask is not the same shape as the data array!')
      return -1
    
    if type(mask[0]) != bool:
      raise Exception('The mask is not a boolean array!')
      return -1
    
    # Then update mask
    
    # Fix data to use the first mask, while keeping the data format:
    data = np.where(mask, data, False)
    
    # Loop over tuple params and clean data again
    for n in range( len(rejlim)):
      
      mask = np.where(np.abs(  ( data - np.median(data) )
                             / data.std() ) < rejlim[n], True, False)
      
      data = np.where(mask, data, False)
      
      if n == 0:
        masktemp = mask
      else:
        mask  = mask * masktemp
        mask2 = mask
  
  else:
    # Loop over tuple params and clean data
    for n in range( len(rejlim)):
      mask = np.where(np.abs(  ( data - np.median(data) )
                             / data.std() ) < rejlim[n], True, False)
      
      data = np.where(mask, data, False)
      
      if n ==0:
        masktemp = mask
      else:
        mask  = mask * masktemp
        mask2 = mask
  
  return mask

rejlim = (5., 5.)
print("Prob 3 mean: "+str(np.mean(samp[sigrej(samp, rejlim)])))

# 9997.5

# The means are the same.

