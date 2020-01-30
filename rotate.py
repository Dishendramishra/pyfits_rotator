#%%
from astropy.io import fits
import numpy as np 
import os 

files = [f for f in os.listdir('./') if f.endswith(".fits") or f.endswith(".fit")]
os.mkdir("rotated")

for file in files:
    f = fits.open(file)
    f[0].data = np.rot90(f[0].data,2)
    f.writeto("./rotated/"+file)

# %%
