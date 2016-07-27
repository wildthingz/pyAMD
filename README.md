# pyAMD
This code is used to determine the optimal segmentation size for visulazing segregation. In order to test this code a series of carefully designed microstructure-like images were generated using `gradientGen.py`. (fig1). 
<p align="center"><img src=doc/images/img1.png width="800"></p>
<p align="center"><i>fig1.</i> Sample microstructure-like images, with 1D linearly decreasing-increasing (left) and 2D linearly increasing-decreasing (right) structures having area fraction between 0.05 and 0.15.</p>
## `gradientGen` method
in order to generate these images, a series of random binary matrices with fixed densities were attached together, resulting in a final 1000x1000 matrix. It should be noted that the shape of the resultant square matrix can be changed within the code.
## `AMD` method
The accuracy of generated segregation map is strongly dependent upon the number of segments. For small number of segments, the generated contour map would not be able to fully represent the concentration. On the contrary, a large number of segmentation will ultimately represent the microstructure itself, as the size of one segment will eventually equate the size of a pixel. Therefore, a method is developed to find an optimum number of segmentation to represent the concentration map as accurately as possible. The method itself has a simple algorithm. In a meshed image, for each element, AMD calculates the difference of the area fraction of an element with its nearby elements using a specified kernel then choosing the maximum value. Iterating this process for the whole image, each element will have a value associated to them. These values are actually representing how sharp the area fraction is changing with respect to the neighbouring cells.

## Results
Fig.2 shows the AMD curves for the two test images. The AMD was applied to find a value between ~1% to ~10% of the image width, which are the recomended values. 
<p align="center"><img src=doc/images/img2.png width="800"></p>
<p align="center"><i>fig2.</i> AMD curves for the test images, 1D-DI (left) and 2d-ID (right).</p>

Fig 3. shows the comparison of the actual gradient the calculated gradient using optmizied segmentation size.. 
<p align="center"><img src=doc/images/img3.png width="800"></p>
<p align="center"><i>fig3.</i> Final contour map.</p>

Fig4. illustrates the final contour maps.
<p align="center"><img src=doc/images/img4.png width="800"></p>
<p align="center"><i>fig4.</i> Final contour maps for 1D-DI (left) and 2d-ID (right) .</p>
# Requiurements
- Python 2.7
- Tecplot
- `MakeContour` module

# Installation

Installing pyAMD is easily done using pip. Assuming it is installed, just run the following from the command-line:

```
pip install pyAMD
```

This command will download the latest version of pyAMD from the Python Package Index and install it to your system.

Alternatively, you can install from the distribution using the setup.py script. The source is stored in the GitHub repo, which can be browsed at:

https://github.com/wildthingz/pyAMD

Simply download and unpack, then navigate to the download directory and run the following from the command-line:

```
python setup.py install
```

# Tested versions
These scripts have been tested using:
- Tecplot 360 EX 2015 R2
- Python 2.7.11 Anaconda 2.3.0
    
