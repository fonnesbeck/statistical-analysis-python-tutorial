# Statistical Data Analysis in Python

Introductory Tutorial, SciPy 2013, 25 June 2013

***Christopher Fonnesbeck - Vanderbilt University School of Medicine***

Chris Fonnesbeck is an Assistant Professor in the Department of Biostatistics at the Vanderbilt University School of Medicine. He specializes in computational statistics, Bayesian methods, meta-analysis, and applied decision analysis. He originally hails from Vancouver, BC and received his Ph.D. from the University of Georgia.

## Description

This tutorial will introduce the use of Python for statistical data analysis, using data stored as Pandas DataFrame objects. Much of the work involved in analyzing data resides in importing, cleaning and transforming data in preparation for analysis. Therefore, the first half of the course is comprised of a 2-part overview of basic and intermediate Pandas usage that will show how to effectively manipulate datasets in memory. This includes tasks like indexing, alignment, join/merge methods, date/time types, and handling of missing data. Next, we will cover plotting and visualization using Pandas and Matplotlib, focusing on creating effective visual representations of your data, while avoiding common pitfalls. Finally, participants will be introduced to methods for statistical data modeling using some of the advanced functions in Numpy, Scipy and Pandas. This will include fitting your data to probability distributions, estimating relationships among variables using linear and non-linear models, and a brief introduction to bootstrapping methods. Each section of the tutorial will involve hands-on manipulation and analysis of sample datasets, to be provided to attendees in advance.

The target audience for the tutorial includes all new Python users, though we recommend that users also attend the NumPy and IPython session in the introductory track.

### Student Instructions

For students familiar with Git, you may simply clone this repository to obtain all the materials (iPython notebooks and data) for the tutorial. Alternatively, you may [download a zip file containing the materials](https://github.com/fonnesbeck/statistical-analysis-python-tutorial/archive/master.zip). A third option is to simply view static notebooks by clicking on the titles of each section below.

## Outline

### [Introduction to Pandas][1]

* Importing data
* Series and DataFrame objects
* Indexing, data selection and subsetting
* Hierarchical indexing
* Reading and writing files
* Sorting and ranking
* Missing data
* Data summarization

### [Data Wrangling with Pandas][2]

* Date/time types
* Merging and joining DataFrame objects
* Concatenation
* Reshaping DataFrame objects
* Pivoting
* Data transformation
* Permutation and sampling
* Data aggregation and GroupBy operations

### [Plotting and Visualization][3]

* Plotting in Pandas vs Matplotlib
* Bar plots
* Histograms
* Box plots
* Grouped plots
* Scatterplots
* Trellis plots

### [Statistical Data Modeling][4]

* Statistical modeling
* Fitting data to probability distributions
* Fitting regression models
* Model selection
* Bootstrapping

## Required Packages

* Python 2.7 or higher (including Python 3)
* pandas >= 0.11.1 and its dependencies
* NumPy >= 1.6.1
* matplotlib >= 1.0.0
* pytz
* IPython >= 0.12
* pyzmq
* tornado

**Optional**: statsmodels, xlrd and openpyxl

For students running the latest version of Mac OS X (10.8), the easiest way to obtain all the packages is to install the [Scipy Superpack](http://bit.ly/scipy_superpack) which works with Python 2.7.2 that ships with OS X.

Otherwise, another easy way to install all the necessary packages is to use Continuum Analytics' [Anaconda](http://docs.continuum.io/anaconda/install.html).


## Statistical Reading List

[The Ecological Detective: Confronting Models with Data](http://www.amazon.com/Ecological-Detective-Confronting-Models-Data/dp/0691034974/ref=sr_1_1?s=books&ie=UTF8&qid=1372250186&sr=1-1&keywords=ecological+detective), Ray Hilborn and Marc Mangel

Though targeted to ecologists, Mangel and Hilborn identify key methods that scientists can use to build useful and credible models for their data. They don't shy away from the math, but the book is very readable and example-laden.

[Data Analysis Using Regression and Multilevel/Hierarchical Models](http://www.amazon.com/Analysis-Regression-Multilevel-Hierarchical-Models/dp/052168689X/ref=sr_1_1?s=books&ie=UTF8&qid=1372250274&sr=1-1&keywords=gelman), Andrew Gelman and Jennifer Hill

The go-to reference for applied hierarchical modeling.

[The Elements of Statistical Learning](http://www-stat.stanford.edu/~tibs/ElemStatLearn/), Hastie, Tibshirani and Friedman

A comprehensive machine learning guide for statisticians.

[A First Course in Bayesian Statistical Methods](http://www.amazon.com/Bayesian-Statistical-Methods-Springer-Statistics/dp/1441928286/ref=sr_1_24?ie=UTF8&qid=1372250835&sr=8-24&keywords=bayesian), Peter Hoff

An excellent, approachable book to get started with Bayesian methods.

[Regression Modeling Strategies](http://www.amazon.com/Regression-Modeling-Strategies-Applications-Statistics/dp/1441929185/ref=sr_1_1?s=books&ie=UTF8&qid=1372250898&sr=1-1&keywords=harrell+regression), Frank Harrell

Frank Harrell's bag of tricks for regression modeling. I pull this off the shelf every week.

[1]: http://nbviewer.ipython.org/urls/gist.github.com/fonnesbeck/5850375/raw/c18cfcd9580d382cb6d14e4708aab33a0916ff3e/1.+Introduction+to+Pandas.ipynb   "Introduction to Pandas"
[2]: http://nbviewer.ipython.org/urls/gist.github.com/fonnesbeck/5850413/raw/3a9406c73365480bc58d5e75bc80f7962243ba17/2.+Data+Wrangling+with+Pandas.ipynb "Data wrangling with Pandas"
[3]: http://nbviewer.ipython.org/urls/gist.github.com/fonnesbeck/5850463/raw/a29d9ffb863bfab09ff6c1fc853e1d5bf69fe3e4/3.+Plotting+and+Visualization.ipynb "Plotting and visualization"
[4]: http://nbviewer.ipython.org/urls/gist.github.com/fonnesbeck/5850483/raw/5e049b2fdd1c83ae386aa3205d3fc50a1a05e5b0/4.+Statistical+Data+Modeling.ipynb "Statistical data modeling"

---

<a rel="license" href="http://creativecommons.org/licenses/by/4.0/"><img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by/4.0/88x31.png" /></a><br /><span xmlns:dct="http://purl.org/dc/terms/" property="dct:title">Statistical Data Analysis in Python</span> by <a xmlns:cc="http://creativecommons.org/ns#" href="https://github.com/fonnesbeck/statistical-analysis-python-tutorial" property="cc:attributionName" rel="cc:attributionURL">Christopher Fonnesbeck</a> is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by/4.0/">Creative Commons Attribution 4.0 International License</a>.
