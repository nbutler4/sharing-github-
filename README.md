### Lab 4: Raster Analysis in Python

#### Total Points: 10

In this lab you will learn how to conduct a basic raster analysis in Python.  We will again use Binder and GitHub to open your Jupyter notebooks in an executable environment online. You can use either the GEOG VMs or your own computer to complete this lab.

Start by downloading this GitHub repository as a .zip file.  Unzip it onto your desktop, and then log in to your GitHub account and upload the files to your repository. Open https://ovh.mybinder.org/ as a new tab in your web browser, copy and paste the URL of your GitHub repository, and click launch.

After Binder has created your Jupyter notebook, open and run through the *Lab4_example* notebook – this will help you get familiar with raster analysis using the *rasterio* package.


#### Your Assignment

Your assignment is to conduct a basic analysis of two 3 band (RGB) Sentinel-2 scenes. Start by using Binder to create a new Jupyter Notebook named *yourlastname_Lab4*, then add your name, the date, and “GEOG 682 Lab 4” as Markup.

Now import the *matplotlib* and *rasterio* packages and load *image1.tif* and *image2.tif*. Your task is to create a complete Jupyter notebook that meets the following requirements:

- Plot(s) that show both of the Sentinel-2 scenes using the *terrain* colormap. 

- Code that confirms that both Sentinel-2 scenes have the same coordinate reference system. Use a Markup cell to show the name of this CRS. 

- Code that creates a plot showing all of the bands in *image1* individually including an appropriate title and colormap for each. 

- Code that creates a mosaic image from *image1* and *image2* and plots it using the *terrain* colormap.



When you have completed this notebook, upload it to your GitHub repository. Then re-launch Binder, copy the URL to share your Binder with others, and submit it to Canvas.  Good luck!
