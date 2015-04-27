{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Introduction to Pandas\n",
    "\n",
    "**pandas** is a Python package providing fast, flexible, and expressive data structures designed to work with *relational* or *labeled* data both. It is a fundamental high-level building block for doing practical, real world data analysis in Python. \n",
    "\n",
    "pandas is well suited for:\n",
    "\n",
    "- Tabular data with heterogeneously-typed columns, as in an SQL table or Excel spreadsheet\n",
    "- Ordered and unordered (not necessarily fixed-frequency) time series data.\n",
    "- Arbitrary matrix data (homogeneously typed or heterogeneous) with row and column labels\n",
    "- Any other form of observational / statistical data sets. The data actually need not be labeled at all to be placed into a pandas data structure\n",
    "\n",
    "\n",
    "Key features:\n",
    "    \n",
    "- Easy handling of **missing data**\n",
    "- **Size mutability**: columns can be inserted and deleted from DataFrame and higher dimensional objects\n",
    "- Automatic and explicit **data alignment**: objects can be explicitly aligned to a set of labels, or the data can be aligned automatically\n",
    "- Powerful, flexible **group by functionality** to perform split-apply-combine operations on data sets\n",
    "- Intelligent label-based **slicing, fancy indexing, and subsetting** of large data sets\n",
    "- Intuitive **merging and joining** data sets\n",
    "- Flexible **reshaping and pivoting** of data sets\n",
    "- **Hierarchical labeling** of axes\n",
    "- Robust **IO tools** for loading data from flat files, Excel files, databases, and HDF5\n",
    "- **Time series functionality**: date range generation and frequency conversion, moving window statistics, moving window linear regressions, date shifting and lagging, etc."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "data": {
      "text/html": [
       "<iframe src=http://pandas.pydata.org width=800 height=350></iframe>"
      ],
      "text/plain": [
       "<IPython.core.display.HTML object>"
      ]
     },
     "execution_count": 1,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "from IPython.core.display import HTML\n",
    "HTML(\"<iframe src=http://pandas.pydata.org width=800 height=350></iframe>\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {
    "collapsed": false
   },
   "outputs": [],
   "source": [
    "%matplotlib inline\n",
    "import pandas as pd\n",
    "import numpy as np\n",
    "\n",
    "# Set some Pandas options\n",
    "pd.set_option('html', False)\n",
    "pd.set_option('max_columns', 30)\n",
    "pd.set_option('max_rows', 20)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Pandas Data Structures"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Series\n",
    "\n",
    "A **Series** is a single vector of data (like a NumPy array) with an *index* that labels each element in the vector."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "0     632\n",
       "1    1638\n",
       "2     569\n",
       "3     115\n",
       "dtype: int64"
      ]
     },
     "execution_count": 3,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "counts = pd.Series([632, 1638, 569, 115])\n",
    "counts"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "If an index is not specified, a default sequence of integers is assigned as the index. A NumPy array comprises the values of the `Series`, while the index is a pandas `Index` object."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([ 632, 1638,  569,  115])"
      ]
     },
     "execution_count": 4,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "counts.values"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Int64Index([0, 1, 2, 3], dtype='int64')"
      ]
     },
     "execution_count": 5,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "counts.index"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "We can assign meaningful labels to the index, if they are available:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Firmicutes         632\n",
       "Proteobacteria    1638\n",
       "Actinobacteria     569\n",
       "Bacteroidetes      115\n",
       "dtype: int64"
      ]
     },
     "execution_count": 6,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "bacteria = pd.Series([632, 1638, 569, 115], \n",
    "    index=['Firmicutes', 'Proteobacteria', 'Actinobacteria', 'Bacteroidetes'])\n",
    "\n",
    "bacteria"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "These labels can be used to refer to the values in the `Series`."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "569"
      ]
     },
     "execution_count": 7,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "bacteria['Actinobacteria']"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Proteobacteria    1638\n",
       "Actinobacteria     569\n",
       "dtype: int64"
      ]
     },
     "execution_count": 8,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "bacteria[[name.endswith('bacteria') for name in bacteria.index]]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[False, True, True, False]"
      ]
     },
     "execution_count": 9,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "[name.endswith('bacteria') for name in bacteria.index]"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Notice that the indexing operation preserved the association between the values and the corresponding indices.\n",
    "\n",
    "We can still use positional indexing if we wish."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "632"
      ]
     },
     "execution_count": 10,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "bacteria[0]"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "We can give both the array of values and the index meaningful labels themselves:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "phylum\n",
       "Firmicutes         632\n",
       "Proteobacteria    1638\n",
       "Actinobacteria     569\n",
       "Bacteroidetes      115\n",
       "Name: counts, dtype: int64"
      ]
     },
     "execution_count": 11,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "bacteria.name = 'counts'\n",
    "bacteria.index.name = 'phylum'\n",
    "bacteria"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "NumPy's math functions and other operations can be applied to Series without losing the data structure."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "phylum\n",
       "Firmicutes        6.448889\n",
       "Proteobacteria    7.401231\n",
       "Actinobacteria    6.343880\n",
       "Bacteroidetes     4.744932\n",
       "Name: counts, dtype: float64"
      ]
     },
     "execution_count": 12,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "np.log(bacteria)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "We can also filter according to the values in the `Series`:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "phylum\n",
       "Proteobacteria    1638\n",
       "Name: counts, dtype: int64"
      ]
     },
     "execution_count": 13,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "bacteria[bacteria>1000]"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "A `Series` can be thought of as an ordered key-value store. In fact, we can create one from a `dict`:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Actinobacteria     569\n",
       "Bacteroidetes      115\n",
       "Firmicutes         632\n",
       "Proteobacteria    1638\n",
       "dtype: int64"
      ]
     },
     "execution_count": 14,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "bacteria_dict = {'Firmicutes': 632, 'Proteobacteria': 1638, 'Actinobacteria': 569, 'Bacteroidetes': 115}\n",
    "pd.Series(bacteria_dict)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Notice that the `Series` is created in key-sorted order.\n",
    "\n",
    "If we pass a custom index to `Series`, it will select the corresponding values from the dict, and treat indices without corrsponding values as missing. Pandas uses the `NaN` (not a number) type for missing values."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Cyanobacteria      NaN\n",
       "Firmicutes         632\n",
       "Proteobacteria    1638\n",
       "Actinobacteria     569\n",
       "dtype: float64"
      ]
     },
     "execution_count": 15,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "bacteria2 = pd.Series(bacteria_dict, index=['Cyanobacteria','Firmicutes','Proteobacteria','Actinobacteria'])\n",
    "bacteria2"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Cyanobacteria      True\n",
       "Firmicutes        False\n",
       "Proteobacteria    False\n",
       "Actinobacteria    False\n",
       "dtype: bool"
      ]
     },
     "execution_count": 16,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "bacteria2.isnull()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Critically, the labels are used to **align data** when used in operations with other Series objects:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Actinobacteria    1138\n",
       "Bacteroidetes      NaN\n",
       "Cyanobacteria      NaN\n",
       "Firmicutes        1264\n",
       "Proteobacteria    3276\n",
       "dtype: float64"
      ]
     },
     "execution_count": 17,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "bacteria + bacteria2"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Contrast this with NumPy arrays, where arrays of the same length will combine values element-wise; adding Series combined values with the same label in the resulting series. Notice also that the missing values were propogated by addition."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### DataFrame\n",
    "\n",
    "Inevitably, we want to be able to store, view and manipulate data that is *multivariate*, where for every index there are multiple fields or columns of data, often of varying data type.\n",
    "\n",
    "A `DataFrame` is a tabular data structure, encapsulating multiple series like columns in a spreadsheet. Data are stored internally as a 2-dimensional object, but the `DataFrame` allows us to represent and manipulate higher-dimensional data."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "   patient          phylum  value\n",
       "0        1      Firmicutes    632\n",
       "1        1  Proteobacteria   1638\n",
       "2        1  Actinobacteria    569\n",
       "3        1   Bacteroidetes    115\n",
       "4        2      Firmicutes    433\n",
       "5        2  Proteobacteria   1130\n",
       "6        2  Actinobacteria    754\n",
       "7        2   Bacteroidetes    555"
      ]
     },
     "execution_count": 18,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "data = pd.DataFrame({'value':[632, 1638, 569, 115, 433, 1130, 754, 555],\n",
    "                     'patient':[1, 1, 1, 1, 2, 2, 2, 2],\n",
    "                     'phylum':['Firmicutes', 'Proteobacteria', 'Actinobacteria', \n",
    "    'Bacteroidetes', 'Firmicutes', 'Proteobacteria', 'Actinobacteria', 'Bacteroidetes']})\n",
    "data"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Notice the `DataFrame` is sorted by column name. We can change the order by indexing them in the order we desire:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "           phylum  value  patient\n",
       "0      Firmicutes    632        1\n",
       "1  Proteobacteria   1638        1\n",
       "2  Actinobacteria    569        1\n",
       "3   Bacteroidetes    115        1\n",
       "4      Firmicutes    433        2\n",
       "5  Proteobacteria   1130        2\n",
       "6  Actinobacteria    754        2\n",
       "7   Bacteroidetes    555        2"
      ]
     },
     "execution_count": 19,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "data[['phylum','value','patient']]"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "A `DataFrame` has a second index, representing the columns:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Index([u'patient', u'phylum', u'value'], dtype='object')"
      ]
     },
     "execution_count": 20,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "data.columns"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "If we wish to access columns, we can do so either by dict-like indexing or by attribute:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 21,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "0     632\n",
       "1    1638\n",
       "2     569\n",
       "3     115\n",
       "4     433\n",
       "5    1130\n",
       "6     754\n",
       "7     555\n",
       "Name: value, dtype: int64"
      ]
     },
     "execution_count": 21,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "data['value']"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 22,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "0     632\n",
       "1    1638\n",
       "2     569\n",
       "3     115\n",
       "4     433\n",
       "5    1130\n",
       "6     754\n",
       "7     555\n",
       "Name: value, dtype: int64"
      ]
     },
     "execution_count": 22,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "data.value"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 23,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "pandas.core.series.Series"
      ]
     },
     "execution_count": 23,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "type(data.value)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 24,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "pandas.core.frame.DataFrame"
      ]
     },
     "execution_count": 24,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "type(data[['value']])"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Notice this is different than with `Series`, where dict-like indexing retrieved a particular element (row). If we want access to a row in a `DataFrame`, we index its `ix` attribute.\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 25,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "patient                1\n",
       "phylum     Bacteroidetes\n",
       "value                115\n",
       "Name: 3, dtype: object"
      ]
     },
     "execution_count": 25,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "data.ix[3]"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Alternatively, we can create a `DataFrame` with a dict of dicts:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 26,
   "metadata": {
    "collapsed": false
   },
   "outputs": [],
   "source": [
    "data = pd.DataFrame({0: {'patient': 1, 'phylum': 'Firmicutes', 'value': 632},\n",
    "                    1: {'patient': 1, 'phylum': 'Proteobacteria', 'value': 1638},\n",
    "                    2: {'patient': 1, 'phylum': 'Actinobacteria', 'value': 569},\n",
    "                    3: {'patient': 1, 'phylum': 'Bacteroidetes', 'value': 115},\n",
    "                    4: {'patient': 2, 'phylum': 'Firmicutes', 'value': 433},\n",
    "                    5: {'patient': 2, 'phylum': 'Proteobacteria', 'value': 1130},\n",
    "                    6: {'patient': 2, 'phylum': 'Actinobacteria', 'value': 754},\n",
    "                    7: {'patient': 2, 'phylum': 'Bacteroidetes', 'value': 555}})"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 27,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "                  0               1               2              3  \\\n",
       "patient           1               1               1              1   \n",
       "phylum   Firmicutes  Proteobacteria  Actinobacteria  Bacteroidetes   \n",
       "value           632            1638             569            115   \n",
       "\n",
       "                  4               5               6              7  \n",
       "patient           2               2               2              2  \n",
       "phylum   Firmicutes  Proteobacteria  Actinobacteria  Bacteroidetes  \n",
       "value           433            1130             754            555  "
      ]
     },
     "execution_count": 27,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "data"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "We probably want this transposed:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 28,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "  patient          phylum value\n",
       "0       1      Firmicutes   632\n",
       "1       1  Proteobacteria  1638\n",
       "2       1  Actinobacteria   569\n",
       "3       1   Bacteroidetes   115\n",
       "4       2      Firmicutes   433\n",
       "5       2  Proteobacteria  1130\n",
       "6       2  Actinobacteria   754\n",
       "7       2   Bacteroidetes   555"
      ]
     },
     "execution_count": 28,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "data = data.T\n",
    "data"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Its important to note that the Series returned when a DataFrame is indexted is merely a **view** on the DataFrame, and not a copy of the data itself. So you must be cautious when manipulating this data:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 29,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "0     632\n",
       "1    1638\n",
       "2     569\n",
       "3     115\n",
       "4     433\n",
       "5    1130\n",
       "6     754\n",
       "7     555\n",
       "Name: value, dtype: object"
      ]
     },
     "execution_count": 29,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "vals = data.value\n",
    "vals"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 30,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "0     632\n",
       "1    1638\n",
       "2     569\n",
       "3     115\n",
       "4     433\n",
       "5       0\n",
       "6     754\n",
       "7     555\n",
       "Name: value, dtype: object"
      ]
     },
     "execution_count": 30,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "vals[5] = 0\n",
    "vals"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 31,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "  patient          phylum value\n",
       "0       1      Firmicutes   632\n",
       "1       1  Proteobacteria  1638\n",
       "2       1  Actinobacteria   569\n",
       "3       1   Bacteroidetes   115\n",
       "4       2      Firmicutes   433\n",
       "5       2  Proteobacteria     0\n",
       "6       2  Actinobacteria   754\n",
       "7       2   Bacteroidetes   555"
      ]
     },
     "execution_count": 31,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "data"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 32,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "  patient          phylum value\n",
       "0       1      Firmicutes   632\n",
       "1       1  Proteobacteria  1638\n",
       "2       1  Actinobacteria   569\n",
       "3       1   Bacteroidetes   115\n",
       "4       2      Firmicutes   433\n",
       "5       2  Proteobacteria     0\n",
       "6       2  Actinobacteria   754\n",
       "7       2   Bacteroidetes   555"
      ]
     },
     "execution_count": 32,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "vals = data.value.copy()\n",
    "vals[5] = 1000\n",
    "data"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "We can create or modify columns by assignment:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 33,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "  patient          phylum value\n",
       "0       1      Firmicutes   632\n",
       "1       1  Proteobacteria  1638\n",
       "2       1  Actinobacteria   569\n",
       "3       1   Bacteroidetes    14\n",
       "4       2      Firmicutes   433\n",
       "5       2  Proteobacteria     0\n",
       "6       2  Actinobacteria   754\n",
       "7       2   Bacteroidetes   555"
      ]
     },
     "execution_count": 33,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "data.value[3] = 14\n",
    "data"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 34,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "  patient          phylum value  year\n",
       "0       1      Firmicutes   632  2013\n",
       "1       1  Proteobacteria  1638  2013\n",
       "2       1  Actinobacteria   569  2013\n",
       "3       1   Bacteroidetes    14  2013\n",
       "4       2      Firmicutes   433  2013\n",
       "5       2  Proteobacteria     0  2013\n",
       "6       2  Actinobacteria   754  2013\n",
       "7       2   Bacteroidetes   555  2013"
      ]
     },
     "execution_count": 34,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "data['year'] = 2013\n",
    "data"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "But note, we cannot use the attribute indexing method to add a new column:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 35,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "  patient          phylum value  year\n",
       "0       1      Firmicutes   632  2013\n",
       "1       1  Proteobacteria  1638  2013\n",
       "2       1  Actinobacteria   569  2013\n",
       "3       1   Bacteroidetes    14  2013\n",
       "4       2      Firmicutes   433  2013\n",
       "5       2  Proteobacteria     0  2013\n",
       "6       2  Actinobacteria   754  2013\n",
       "7       2   Bacteroidetes   555  2013"
      ]
     },
     "execution_count": 35,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "data.treatment = 1\n",
    "data"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 36,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "1"
      ]
     },
     "execution_count": 36,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "data.treatment"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Specifying a `Series` as a new columns cause its values to be added according to the `DataFrame`'s index:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 37,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "0    0\n",
       "1    0\n",
       "2    0\n",
       "3    0\n",
       "4    1\n",
       "5    1\n",
       "dtype: int64"
      ]
     },
     "execution_count": 37,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "treatment = pd.Series([0]*4 + [1]*2)\n",
    "treatment"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 38,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "  patient          phylum value  year  treatment\n",
       "0       1      Firmicutes   632  2013          0\n",
       "1       1  Proteobacteria  1638  2013          0\n",
       "2       1  Actinobacteria   569  2013          0\n",
       "3       1   Bacteroidetes    14  2013          0\n",
       "4       2      Firmicutes   433  2013          1\n",
       "5       2  Proteobacteria     0  2013          1\n",
       "6       2  Actinobacteria   754  2013        NaN\n",
       "7       2   Bacteroidetes   555  2013        NaN"
      ]
     },
     "execution_count": 38,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "data['treatment'] = treatment\n",
    "data"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Other Python data structures (ones without an index) need to be the same length as the `DataFrame`:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 39,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "ename": "ValueError",
     "evalue": "Length of values does not match length of index",
     "output_type": "error",
     "traceback": [
      "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m\n\u001b[0;31mValueError\u001b[0m                                Traceback (most recent call last)",
      "\u001b[0;32m<ipython-input-39-360d03fdde9a>\u001b[0m in \u001b[0;36m<module>\u001b[0;34m()\u001b[0m\n\u001b[1;32m      1\u001b[0m \u001b[0mmonth\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0;34m[\u001b[0m\u001b[0;34m'Jan'\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0;34m'Feb'\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0;34m'Mar'\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0;34m'Apr'\u001b[0m\u001b[0;34m]\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m----> 2\u001b[0;31m \u001b[0mdata\u001b[0m\u001b[0;34m[\u001b[0m\u001b[0;34m'month'\u001b[0m\u001b[0;34m]\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mmonth\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m",
      "\u001b[0;32m/usr/local/lib/python2.7/site-packages/pandas/core/frame.pyc\u001b[0m in \u001b[0;36m__setitem__\u001b[0;34m(self, key, value)\u001b[0m\n\u001b[1;32m   1899\u001b[0m         \u001b[0;32melse\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m   1900\u001b[0m             \u001b[0;31m# set column\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m-> 1901\u001b[0;31m             \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0m_set_item\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mkey\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mvalue\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m   1902\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m   1903\u001b[0m     \u001b[0;32mdef\u001b[0m \u001b[0m_setitem_slice\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mself\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mkey\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mvalue\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
      "\u001b[0;32m/usr/local/lib/python2.7/site-packages/pandas/core/frame.pyc\u001b[0m in \u001b[0;36m_set_item\u001b[0;34m(self, key, value)\u001b[0m\n\u001b[1;32m   1981\u001b[0m         \u001b[0mis_existing\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mkey\u001b[0m \u001b[0;32min\u001b[0m \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mcolumns\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m   1982\u001b[0m         \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0m_ensure_valid_index\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mvalue\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m-> 1983\u001b[0;31m         \u001b[0mvalue\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0m_sanitize_column\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mkey\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mvalue\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m   1984\u001b[0m         \u001b[0mNDFrame\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0m_set_item\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mself\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mkey\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mvalue\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m   1985\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n",
      "\u001b[0;32m/usr/local/lib/python2.7/site-packages/pandas/core/frame.pyc\u001b[0m in \u001b[0;36m_sanitize_column\u001b[0;34m(self, key, value)\u001b[0m\n\u001b[1;32m   2031\u001b[0m         \u001b[0;32melif\u001b[0m \u001b[0misinstance\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mvalue\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mIndex\u001b[0m\u001b[0;34m)\u001b[0m \u001b[0;32mor\u001b[0m \u001b[0m_is_sequence\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mvalue\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m   2032\u001b[0m             \u001b[0;32mif\u001b[0m \u001b[0mlen\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mvalue\u001b[0m\u001b[0;34m)\u001b[0m \u001b[0;34m!=\u001b[0m \u001b[0mlen\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mindex\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m-> 2033\u001b[0;31m                 raise ValueError('Length of values does not match length of '\n\u001b[0m\u001b[1;32m   2034\u001b[0m                                  'index')\n\u001b[1;32m   2035\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n",
      "\u001b[0;31mValueError\u001b[0m: Length of values does not match length of index"
     ]
    }
   ],
   "source": [
    "month = ['Jan', 'Feb', 'Mar', 'Apr']\n",
    "data['month'] = month"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 40,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "  patient          phylum value  year  treatment month\n",
       "0       1      Firmicutes   632  2013          0   Jan\n",
       "1       1  Proteobacteria  1638  2013          0   Jan\n",
       "2       1  Actinobacteria   569  2013          0   Jan\n",
       "3       1   Bacteroidetes    14  2013          0   Jan\n",
       "4       2      Firmicutes   433  2013          1   Jan\n",
       "5       2  Proteobacteria     0  2013          1   Jan\n",
       "6       2  Actinobacteria   754  2013        NaN   Jan\n",
       "7       2   Bacteroidetes   555  2013        NaN   Jan"
      ]
     },
     "execution_count": 40,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "data['month'] = ['Jan']*len(data)\n",
    "data"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "We can use `del` to remove columns, in the same way `dict` entries can be removed:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 41,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "  patient          phylum value  year  treatment\n",
       "0       1      Firmicutes   632  2013          0\n",
       "1       1  Proteobacteria  1638  2013          0\n",
       "2       1  Actinobacteria   569  2013          0\n",
       "3       1   Bacteroidetes    14  2013          0\n",
       "4       2      Firmicutes   433  2013          1\n",
       "5       2  Proteobacteria     0  2013          1\n",
       "6       2  Actinobacteria   754  2013        NaN\n",
       "7       2   Bacteroidetes   555  2013        NaN"
      ]
     },
     "execution_count": 41,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "del data['month']\n",
    "data"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "We can extract the underlying data as a simple `ndarray` by accessing the `values` attribute:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 42,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([[1, 'Firmicutes', 632, 2013, 0.0],\n",
       "       [1, 'Proteobacteria', 1638, 2013, 0.0],\n",
       "       [1, 'Actinobacteria', 569, 2013, 0.0],\n",
       "       [1, 'Bacteroidetes', 14, 2013, 0.0],\n",
       "       [2, 'Firmicutes', 433, 2013, 1.0],\n",
       "       [2, 'Proteobacteria', 0, 2013, 1.0],\n",
       "       [2, 'Actinobacteria', 754, 2013, nan],\n",
       "       [2, 'Bacteroidetes', 555, 2013, nan]], dtype=object)"
      ]
     },
     "execution_count": 42,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "data.values"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Notice that because of the mix of string and integer (and `NaN`) values, the dtype of the array is `object`. The dtype will automatically be chosen to be as general as needed to accomodate all the columns."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 43,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([[ 0.4,  1. ],\n",
       "       [-1. ,  2. ],\n",
       "       [ 4.5,  3. ]])"
      ]
     },
     "execution_count": 43,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df = pd.DataFrame({'foo': [1,2,3], 'bar':[0.4, -1.0, 4.5]})\n",
    "df.values"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Pandas uses a custom data structure to represent the indices of Series and DataFrames."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 44,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Int64Index([0, 1, 2, 3, 4, 5, 6, 7], dtype='int64')"
      ]
     },
     "execution_count": 44,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "data.index"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Index objects are immutable:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 45,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "ename": "TypeError",
     "evalue": "'<class 'pandas.core.index.Int64Index'>' does not support mutable operations.",
     "output_type": "error",
     "traceback": [
      "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m\n\u001b[0;31mTypeError\u001b[0m                                 Traceback (most recent call last)",
      "\u001b[0;32m<ipython-input-45-42a852cc9eac>\u001b[0m in \u001b[0;36m<module>\u001b[0;34m()\u001b[0m\n\u001b[0;32m----> 1\u001b[0;31m \u001b[0mdata\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mindex\u001b[0m\u001b[0;34m[\u001b[0m\u001b[0;36m0\u001b[0m\u001b[0;34m]\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0;36m15\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m",
      "\u001b[0;32m/usr/local/lib/python2.7/site-packages/pandas/core/base.pyc\u001b[0m in \u001b[0;36m_disabled\u001b[0;34m(self, *args, **kwargs)\u001b[0m\n\u001b[1;32m    177\u001b[0m         \u001b[0;34m\"\"\"This method will not function because object is immutable.\"\"\"\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    178\u001b[0m         raise TypeError(\"'%s' does not support mutable operations.\" %\n\u001b[0;32m--> 179\u001b[0;31m                         self.__class__)\n\u001b[0m\u001b[1;32m    180\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    181\u001b[0m     \u001b[0m__setitem__\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0m__setslice__\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0m__delitem__\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0m__delslice__\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0m_disabled\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
      "\u001b[0;31mTypeError\u001b[0m: '<class 'pandas.core.index.Int64Index'>' does not support mutable operations."
     ]
    }
   ],
   "source": [
    "data.index[0] = 15"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "This is so that Index objects can be shared between data structures without fear that they will be changed."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 46,
   "metadata": {
    "collapsed": false
   },
   "outputs": [],
   "source": [
    "bacteria2.index = bacteria.index"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 47,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "phylum\n",
       "Firmicutes         NaN\n",
       "Proteobacteria     632\n",
       "Actinobacteria    1638\n",
       "Bacteroidetes      569\n",
       "dtype: float64"
      ]
     },
     "execution_count": 47,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "bacteria2"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Importing data"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "A key, but often under-appreciated, step in data analysis is importing the data that we wish to analyze. Though it is easy to load basic data structures into Python using built-in tools or those provided by packages like NumPy, it is non-trivial to import structured data well, and to easily convert this input into a robust data structure:\n",
    "\n",
    "    genes = np.loadtxt(\"genes.csv\", delimiter=\",\", dtype=[('gene', '|S10'), ('value', '<f4')])\n",
    "\n",
    "Pandas provides a convenient set of functions for importing tabular data in a number of formats directly into a `DataFrame` object. These functions include a slew of options to perform type inference, indexing, parsing, iterating and cleaning automatically as data are imported."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Let's start with some more bacteria data, stored in csv format."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 48,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Taxon,Patient,Tissue,Stool\r\n",
      "Firmicutes,1,632,305\r\n",
      "Firmicutes,2,136,4182\r\n",
      "Firmicutes,3,1174,703\r\n",
      "Firmicutes,4,408,3946\r\n",
      "Firmicutes,5,831,8605\r\n",
      "Firmicutes,6,693,50\r\n",
      "Firmicutes,7,718,717\r\n",
      "Firmicutes,8,173,33\r\n",
      "Firmicutes,9,228,80\r\n",
      "Firmicutes,10,162,3196\r\n",
      "Firmicutes,11,372,32\r\n",
      "Firmicutes,12,4255,4361\r\n",
      "Firmicutes,13,107,1667\r\n",
      "Firmicutes,14,96,223\r\n",
      "Firmicutes,15,281,2377\r\n",
      "Proteobacteria,1,1638,3886\r\n",
      "Proteobacteria,2,2469,1821\r\n",
      "Proteobacteria,3,839,661\r\n",
      "Proteobacteria,4,4414,18\r\n",
      "Proteobacteria,5,12044,83\r\n",
      "Proteobacteria,6,2310,12\r\n",
      "Proteobacteria,7,3053,547\r\n",
      "Proteobacteria,8,395,2174\r\n",
      "Proteobacteria,9,2651,767\r\n",
      "Proteobacteria,10,1195,76\r\n",
      "Proteobacteria,11,6857,795\r\n",
      "Proteobacteria,12,483,666\r\n",
      "Proteobacteria,13,2950,3994\r\n",
      "Proteobacteria,14,1541,816\r\n",
      "Proteobacteria,15,1307,53\r\n",
      "Actinobacteria,1,569,648\r\n",
      "Actinobacteria,2,1590,4\r\n",
      "Actinobacteria,3,25,2\r\n",
      "Actinobacteria,4,259,300\r\n",
      "Actinobacteria,5,568,7\r\n",
      "Actinobacteria,6,1102,9\r\n",
      "Actinobacteria,7,678,377\r\n",
      "Actinobacteria,8,260,58\r\n",
      "Actinobacteria,9,424,233\r\n",
      "Actinobacteria,10,548,21\r\n",
      "Actinobacteria,11,201,83\r\n",
      "Actinobacteria,12,42,75\r\n",
      "Actinobacteria,13,109,59\r\n",
      "Actinobacteria,14,51,183\r\n",
      "Actinobacteria,15,310,204\r\n",
      "Bacteroidetes,1,115,380\r\n",
      "Bacteroidetes,2,67,0\r\n",
      "Bacteroidetes,3,0,0\r\n",
      "Bacteroidetes,4,85,5\r\n",
      "Bacteroidetes,5,143,7\r\n",
      "Bacteroidetes,6,678,2\r\n",
      "Bacteroidetes,7,4829,209\r\n",
      "Bacteroidetes,8,74,651\r\n",
      "Bacteroidetes,9,169,254\r\n",
      "Bacteroidetes,10,106,10\r\n",
      "Bacteroidetes,11,73,381\r\n",
      "Bacteroidetes,12,30,359\r\n",
      "Bacteroidetes,13,51,51\r\n",
      "Bacteroidetes,14,2473,2314\r\n",
      "Bacteroidetes,15,102,33\r\n",
      "Other,1,114,277\r\n",
      "Other,2,195,18\r\n",
      "Other,3,42,2\r\n",
      "Other,4,316,43\r\n",
      "Other,5,202,40\r\n",
      "Other,6,116,0\r\n",
      "Other,7,527,12\r\n",
      "Other,8,357,11\r\n",
      "Other,9,106,11\r\n",
      "Other,10,67,14\r\n",
      "Other,11,203,6\r\n",
      "Other,12,392,6\r\n",
      "Other,13,28,25\r\n",
      "Other,14,12,22\r\n",
      "Other,15,305,32"
     ]
    }
   ],
   "source": [
    "!cat data/microbiome.csv"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "This table can be read into a DataFrame using `read_csv`:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 49,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "         Taxon  Patient  Tissue  Stool\n",
       "0   Firmicutes        1     632    305\n",
       "1   Firmicutes        2     136   4182\n",
       "2   Firmicutes        3    1174    703\n",
       "3   Firmicutes        4     408   3946\n",
       "4   Firmicutes        5     831   8605\n",
       "5   Firmicutes        6     693     50\n",
       "6   Firmicutes        7     718    717\n",
       "7   Firmicutes        8     173     33\n",
       "8   Firmicutes        9     228     80\n",
       "9   Firmicutes       10     162   3196\n",
       "..         ...      ...     ...    ...\n",
       "65       Other        6     116      0\n",
       "66       Other        7     527     12\n",
       "67       Other        8     357     11\n",
       "68       Other        9     106     11\n",
       "69       Other       10      67     14\n",
       "70       Other       11     203      6\n",
       "71       Other       12     392      6\n",
       "72       Other       13      28     25\n",
       "73       Other       14      12     22\n",
       "74       Other       15     305     32\n",
       "\n",
       "[75 rows x 4 columns]"
      ]
     },
     "execution_count": 49,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "mb = pd.read_csv(\"data/microbiome.csv\")\n",
    "mb"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Notice that `read_csv` automatically considered the first row in the file to be a header row.\n",
    "\n",
    "We can override default behavior by customizing some the arguments, like `header`, `names` or `index_col`."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 50,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "            0        1       2      3\n",
       "0       Taxon  Patient  Tissue  Stool\n",
       "1  Firmicutes        1     632    305\n",
       "2  Firmicutes        2     136   4182\n",
       "3  Firmicutes        3    1174    703\n",
       "4  Firmicutes        4     408   3946"
      ]
     },
     "execution_count": 50,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "pd.read_csv(\"data/microbiome.csv\", header=None).head()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "`read_csv` is just a convenience function for `read_table`, since csv is such a common format:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 51,
   "metadata": {
    "collapsed": false
   },
   "outputs": [],
   "source": [
    "mb = pd.read_table(\"data/microbiome.csv\", sep=',')"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "The `sep` argument can be customized as needed to accomodate arbitrary separators. For example, we can use a regular expression to define a variable amount of whitespace, which is unfortunately very common in some data formats: \n",
    "    \n",
    "    sep='\\s+'"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "For a more useful index, we can specify the first two columns, which together provide a unique index to the data."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 52,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "                    Tissue  Stool\n",
       "Taxon      Patient               \n",
       "Firmicutes 1           632    305\n",
       "           2           136   4182\n",
       "           3          1174    703\n",
       "           4           408   3946\n",
       "           5           831   8605"
      ]
     },
     "execution_count": 52,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "mb = pd.read_csv(\"data/microbiome.csv\", index_col=['Taxon','Patient'])\n",
    "mb.head()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "This is called a *hierarchical* index, which we will revisit later in the tutorial."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "If we have sections of data that we do not wish to import (for example, known bad data), we can populate the `skiprows` argument:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 53,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "        Taxon  Patient  Tissue  Stool\n",
       "0  Firmicutes        1     632    305\n",
       "1  Firmicutes        2     136   4182\n",
       "2  Firmicutes        5     831   8605\n",
       "3  Firmicutes        7     718    717\n",
       "4  Firmicutes        8     173     33"
      ]
     },
     "execution_count": 53,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "pd.read_csv(\"data/microbiome.csv\", skiprows=[3,4,6]).head()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Conversely, if we only want to import a small number of rows from, say, a very large data file we can use `nrows`:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 54,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "        Taxon  Patient  Tissue  Stool\n",
       "0  Firmicutes        1     632    305\n",
       "1  Firmicutes        2     136   4182\n",
       "2  Firmicutes        3    1174    703\n",
       "3  Firmicutes        4     408   3946"
      ]
     },
     "execution_count": 54,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "pd.read_csv(\"data/microbiome.csv\", nrows=4)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Alternately, if we want to process our data in reasonable chunks, the `chunksize` argument will return an iterable object that can be employed in a data processing loop. For example, our microbiome data are organized by bacterial phylum, with 15 patients represented in each:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 55,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "{'Actinobacteria': 449.06666666666666,\n",
       " 'Bacteroidetes': 599.66666666666663,\n",
       " 'Firmicutes': 684.39999999999998,\n",
       " 'Other': 198.80000000000001,\n",
       " 'Proteobacteria': 2943.0666666666666}"
      ]
     },
     "execution_count": 55,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "data_chunks = pd.read_csv(\"data/microbiome.csv\", chunksize=15)\n",
    "\n",
    "mean_tissue = {chunk.Taxon[0]:chunk.Tissue.mean() for chunk in data_chunks}\n",
    "    \n",
    "mean_tissue"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Most real-world data is incomplete, with values missing due to incomplete observation, data entry or transcription error, or other reasons. Pandas will automatically recognize and parse common missing data indicators, including `NA` and `NULL`."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 56,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Taxon,Patient,Tissue,Stool\r\n",
      "Firmicutes,1,632,305\r\n",
      "Firmicutes,2,136,4182\r\n",
      "Firmicutes,3,,703\r\n",
      "Firmicutes,4,408,3946\r\n",
      "Firmicutes,5,831,8605\r\n",
      "Firmicutes,6,693,50\r\n",
      "Firmicutes,7,718,717\r\n",
      "Firmicutes,8,173,33\r\n",
      "Firmicutes,9,228,NA\r\n",
      "Firmicutes,10,162,3196\r\n",
      "Firmicutes,11,372,-99999\r\n",
      "Firmicutes,12,4255,4361\r\n",
      "Firmicutes,13,107,1667\r\n",
      "Firmicutes,14,?,223\r\n",
      "Firmicutes,15,281,2377\r\n",
      "Proteobacteria,1,1638,3886\r\n",
      "Proteobacteria,2,2469,1821\r\n",
      "Proteobacteria,3,839,661\r\n",
      "Proteobacteria,4,4414,18\r\n",
      "Proteobacteria,5,12044,83\r\n",
      "Proteobacteria,6,2310,12\r\n",
      "Proteobacteria,7,3053,547\r\n",
      "Proteobacteria,8,395,2174\r\n",
      "Proteobacteria,9,2651,767\r\n",
      "Proteobacteria,10,1195,76\r\n",
      "Proteobacteria,11,6857,795\r\n",
      "Proteobacteria,12,483,666\r\n",
      "Proteobacteria,13,2950,3994\r\n",
      "Proteobacteria,14,1541,816\r\n",
      "Proteobacteria,15,1307,53\r\n",
      "Actinobacteria,1,569,648\r\n",
      "Actinobacteria,2,1590,4\r\n",
      "Actinobacteria,3,25,2\r\n",
      "Actinobacteria,4,259,300\r\n",
      "Actinobacteria,5,568,7\r\n",
      "Actinobacteria,6,1102,9\r\n",
      "Actinobacteria,7,678,377\r\n",
      "Actinobacteria,8,260,58\r\n",
      "Actinobacteria,9,424,233\r\n",
      "Actinobacteria,10,548,21\r\n",
      "Actinobacteria,11,201,83\r\n",
      "Actinobacteria,12,42,75\r\n",
      "Actinobacteria,13,109,59\r\n",
      "Actinobacteria,14,51,183\r\n",
      "Actinobacteria,15,310,204\r\n",
      "Bacteroidetes,1,115,380\r\n",
      "Bacteroidetes,2,67,0\r\n",
      "Bacteroidetes,3,0,0\r\n",
      "Bacteroidetes,4,85,5\r\n",
      "Bacteroidetes,5,143,7\r\n",
      "Bacteroidetes,6,678,2\r\n",
      "Bacteroidetes,7,4829,209\r\n",
      "Bacteroidetes,8,74,651\r\n",
      "Bacteroidetes,9,169,254\r\n",
      "Bacteroidetes,10,106,10\r\n",
      "Bacteroidetes,11,73,381\r\n",
      "Bacteroidetes,12,30,359\r\n",
      "Bacteroidetes,13,51,51\r\n",
      "Bacteroidetes,14,2473,2314\r\n",
      "Bacteroidetes,15,102,33\r\n",
      "Other,1,114,277\r\n",
      "Other,2,195,18\r\n",
      "Other,3,42,2\r\n",
      "Other,4,316,43\r\n",
      "Other,5,202,40\r\n",
      "Other,6,116,0\r\n",
      "Other,7,527,12\r\n",
      "Other,8,357,11\r\n",
      "Other,9,106,11\r\n",
      "Other,10,67,14\r\n",
      "Other,11,203,6\r\n",
      "Other,12,392,6\r\n",
      "Other,13,28,25\r\n",
      "Other,14,12,22\r\n",
      "Other,15,305,32"
     ]
    }
   ],
   "source": [
    "!cat data/microbiome_missing.csv"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 57,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "             Taxon  Patient Tissue  Stool\n",
       "0       Firmicutes        1    632    305\n",
       "1       Firmicutes        2    136   4182\n",
       "2       Firmicutes        3    NaN    703\n",
       "3       Firmicutes        4    408   3946\n",
       "4       Firmicutes        5    831   8605\n",
       "5       Firmicutes        6    693     50\n",
       "6       Firmicutes        7    718    717\n",
       "7       Firmicutes        8    173     33\n",
       "8       Firmicutes        9    228    NaN\n",
       "9       Firmicutes       10    162   3196\n",
       "10      Firmicutes       11    372 -99999\n",
       "11      Firmicutes       12   4255   4361\n",
       "12      Firmicutes       13    107   1667\n",
       "13      Firmicutes       14      ?    223\n",
       "14      Firmicutes       15    281   2377\n",
       "15  Proteobacteria        1   1638   3886\n",
       "16  Proteobacteria        2   2469   1821\n",
       "17  Proteobacteria        3    839    661\n",
       "18  Proteobacteria        4   4414     18\n",
       "19  Proteobacteria        5  12044     83"
      ]
     },
     "execution_count": 57,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "pd.read_csv(\"data/microbiome_missing.csv\").head(20)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Above, Pandas recognized `NA` and an empty field as missing data."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 58,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "    Taxon Patient Tissue  Stool\n",
       "0   False   False  False  False\n",
       "1   False   False  False  False\n",
       "2   False   False   True  False\n",
       "3   False   False  False  False\n",
       "4   False   False  False  False\n",
       "5   False   False  False  False\n",
       "6   False   False  False  False\n",
       "7   False   False  False  False\n",
       "8   False   False  False   True\n",
       "9   False   False  False  False\n",
       "10  False   False  False  False\n",
       "11  False   False  False  False\n",
       "12  False   False  False  False\n",
       "13  False   False  False  False\n",
       "14  False   False  False  False\n",
       "15  False   False  False  False\n",
       "16  False   False  False  False\n",
       "17  False   False  False  False\n",
       "18  False   False  False  False\n",
       "19  False   False  False  False"
      ]
     },
     "execution_count": 58,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "pd.isnull(pd.read_csv(\"data/microbiome_missing.csv\")).head(20)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Unfortunately, there will sometimes be inconsistency with the conventions for missing data. In this example, there is a question mark \"?\" and a large negative number where there should have been a positive integer. We can specify additional symbols with the `na_values` argument:\n",
    "   "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 59,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "             Taxon  Patient  Tissue  Stool\n",
       "0       Firmicutes        1     632    305\n",
       "1       Firmicutes        2     136   4182\n",
       "2       Firmicutes        3     NaN    703\n",
       "3       Firmicutes        4     408   3946\n",
       "4       Firmicutes        5     831   8605\n",
       "5       Firmicutes        6     693     50\n",
       "6       Firmicutes        7     718    717\n",
       "7       Firmicutes        8     173     33\n",
       "8       Firmicutes        9     228    NaN\n",
       "9       Firmicutes       10     162   3196\n",
       "10      Firmicutes       11     372    NaN\n",
       "11      Firmicutes       12    4255   4361\n",
       "12      Firmicutes       13     107   1667\n",
       "13      Firmicutes       14     NaN    223\n",
       "14      Firmicutes       15     281   2377\n",
       "15  Proteobacteria        1    1638   3886\n",
       "16  Proteobacteria        2    2469   1821\n",
       "17  Proteobacteria        3     839    661\n",
       "18  Proteobacteria        4    4414     18\n",
       "19  Proteobacteria        5   12044     83"
      ]
     },
     "execution_count": 59,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "pd.read_csv(\"data/microbiome_missing.csv\", na_values=['?', -99999]).head(20)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "These can be specified on a column-wise basis using an appropriate dict as the argument for `na_values`."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Microsoft Excel\n",
    "\n",
    "Since so much financial and scientific data ends up in Excel spreadsheets (regrettably), Pandas' ability to directly import Excel spreadsheets is valuable. This support is contingent on having one or two dependencies (depending on what version of Excel file is being imported) installed: `xlrd` and `openpyxl` (these may be installed with either `pip` or `easy_install`).\n",
    "\n",
    "Importing Excel data to Pandas is a two-step process. First, we create an `ExcelFile` object using the path of the file:                                             "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 60,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<pandas.io.excel.ExcelFile at 0x10f8426d0>"
      ]
     },
     "execution_count": 60,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "mb_file = pd.ExcelFile('data/microbiome/MID1.xls')\n",
    "mb_file"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Then, since modern spreadsheets consist of one or more \"sheets\", we parse the sheet with the data of interest:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 61,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "                                               Taxon  Count\n",
       "0  Archaea \"Crenarchaeota\" Thermoprotei Desulfuro...      7\n",
       "1  Archaea \"Crenarchaeota\" Thermoprotei Desulfuro...      2\n",
       "2  Archaea \"Crenarchaeota\" Thermoprotei Sulfoloba...      3\n",
       "3  Archaea \"Crenarchaeota\" Thermoprotei Thermopro...      3\n",
       "4  Archaea \"Euryarchaeota\" \"Methanomicrobia\" Meth...      7"
      ]
     },
     "execution_count": 61,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "mb1 = mb_file.parse(\"Sheet 1\", header=None)\n",
    "mb1.columns = [\"Taxon\", \"Count\"]\n",
    "mb1.head()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "There is now a `read_excel` conveneince function in Pandas that combines these steps into a single call:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 62,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "                                                   0   1\n",
       "0  Archaea \"Crenarchaeota\" Thermoprotei Acidiloba...   2\n",
       "1  Archaea \"Crenarchaeota\" Thermoprotei Acidiloba...  14\n",
       "2  Archaea \"Crenarchaeota\" Thermoprotei Desulfuro...  23\n",
       "3  Archaea \"Crenarchaeota\" Thermoprotei Desulfuro...   1\n",
       "4  Archaea \"Crenarchaeota\" Thermoprotei Desulfuro...   2"
      ]
     },
     "execution_count": 62,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "mb2 = pd.read_excel('data/microbiome/MID2.xls', sheetname='Sheet 1', header=None)\n",
    "mb2.head()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "There are several other data formats that can be imported into Python and converted into DataFrames, with the help of buitl-in or third-party libraries. These include JSON, XML, HDF5, relational and non-relational databases, and various web APIs. These are beyond the scope of this tutorial, but are covered in [Python for Data Analysis](http://shop.oreilly.com/product/0636920023784.do)."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Pandas Fundamentals"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "This section introduces the new user to the key functionality of Pandas that is required to use the software effectively.\n",
    "\n",
    "For some variety, we will leave our digestive tract bacteria behind and employ some baseball data."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 63,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "          player  year  stint team  lg   g  ab  r   h  X2b  X3b  hr  rbi  sb  \\\n",
       "id                                                                             \n",
       "88641  womacto01  2006      2  CHN  NL  19  50  6  14    1    0   1    2   1   \n",
       "88643  schilcu01  2006      1  BOS  AL  31   2  0   1    0    0   0    0   0   \n",
       "88645  myersmi01  2006      1  NYA  AL  62   0  0   0    0    0   0    0   0   \n",
       "88649  helliri01  2006      1  MIL  NL  20   3  0   0    0    0   0    0   0   \n",
       "88650  johnsra05  2006      1  NYA  AL  33   6  0   1    0    0   0    0   0   \n",
       "\n",
       "       cs  bb  so  ibb  hbp  sh  sf  gidp  \n",
       "id                                         \n",
       "88641   1   4   4    0    0   3   0     0  \n",
       "88643   0   0   1    0    0   0   0     0  \n",
       "88645   0   0   0    0    0   0   0     0  \n",
       "88649   0   0   2    0    0   0   0     0  \n",
       "88650   0   0   4    0    0   0   0     0  "
      ]
     },
     "execution_count": 63,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "baseball = pd.read_csv(\"data/baseball.csv\", index_col='id')\n",
    "baseball.head()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Notice that we specified the `id` column as the index, since it appears to be a unique identifier. We could try to create a unique index ourselves by combining `player` and `year`:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 64,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "                  player  year  stint team  lg   g  ab  r   h  X2b  X3b  hr  \\\n",
       "womacto012006  womacto01  2006      2  CHN  NL  19  50  6  14    1    0   1   \n",
       "schilcu012006  schilcu01  2006      1  BOS  AL  31   2  0   1    0    0   0   \n",
       "myersmi012006  myersmi01  2006      1  NYA  AL  62   0  0   0    0    0   0   \n",
       "helliri012006  helliri01  2006      1  MIL  NL  20   3  0   0    0    0   0   \n",
       "johnsra052006  johnsra05  2006      1  NYA  AL  33   6  0   1    0    0   0   \n",
       "\n",
       "               rbi  sb  cs  bb  so  ibb  hbp  sh  sf  gidp  \n",
       "womacto012006    2   1   1   4   4    0    0   3   0     0  \n",
       "schilcu012006    0   0   0   0   1    0    0   0   0     0  \n",
       "myersmi012006    0   0   0   0   0    0    0   0   0     0  \n",
       "helliri012006    0   0   0   0   2    0    0   0   0     0  \n",
       "johnsra052006    0   0   0   0   4    0    0   0   0     0  "
      ]
     },
     "execution_count": 64,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "player_id = baseball.player + baseball.year.astype(str)\n",
    "baseball_newind = baseball.copy()\n",
    "baseball_newind.index = player_id\n",
    "baseball_newind.head()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "This looks okay, but let's check:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 65,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "False"
      ]
     },
     "execution_count": 65,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "baseball_newind.index.is_unique"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "So, indices need not be unique. Our choice is not unique because some players change teams within years."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 66,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "wickmbo012007    2\n",
       "gomezch022007    2\n",
       "sweenma012007    2\n",
       "claytro012007    2\n",
       "hernaro012007    2\n",
       "loftoke012007    2\n",
       "trachst012007    2\n",
       "wellsda012007    2\n",
       "...\n",
       "myersmi012007    1\n",
       "alomasa022007    1\n",
       "edmonji012007    1\n",
       "sheffga012007    1\n",
       "whiteri012007    1\n",
       "cormirh012007    1\n",
       "floydcl012007    1\n",
       "embreal012007    1\n",
       "Length: 88, dtype: int64"
      ]
     },
     "execution_count": 66,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "pd.Series(baseball_newind.index).value_counts()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "The most important consequence of a non-unique index is that indexing by label will return multiple values for some labels:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 67,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "                  player  year  stint team  lg   g  ab  r  h  X2b  X3b  hr  \\\n",
       "wickmbo012007  wickmbo01  2007      2  ARI  NL   8   0  0  0    0    0   0   \n",
       "wickmbo012007  wickmbo01  2007      1  ATL  NL  47   0  0  0    0    0   0   \n",
       "\n",
       "               rbi  sb  cs  bb  so  ibb  hbp  sh  sf  gidp  \n",
       "wickmbo012007    0   0   0   0   0    0    0   0   0     0  \n",
       "wickmbo012007    0   0   0   0   0    0    0   0   0     0  "
      ]
     },
     "execution_count": 67,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "baseball_newind.ix['wickmbo012007']"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "We will learn more about indexing below."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "We can create a truly unique index by combining `player`, `team` and `year`:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 68,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "                     player  year  stint team  lg   g  ab  r   h  X2b  X3b  \\\n",
       "womacto01CHN2006  womacto01  2006      2  CHN  NL  19  50  6  14    1    0   \n",
       "schilcu01BOS2006  schilcu01  2006      1  BOS  AL  31   2  0   1    0    0   \n",
       "myersmi01NYA2006  myersmi01  2006      1  NYA  AL  62   0  0   0    0    0   \n",
       "helliri01MIL2006  helliri01  2006      1  MIL  NL  20   3  0   0    0    0   \n",
       "johnsra05NYA2006  johnsra05  2006      1  NYA  AL  33   6  0   1    0    0   \n",
       "\n",
       "                  hr  rbi  sb  cs  bb  so  ibb  hbp  sh  sf  gidp  \n",
       "womacto01CHN2006   1    2   1   1   4   4    0    0   3   0     0  \n",
       "schilcu01BOS2006   0    0   0   0   0   1    0    0   0   0     0  \n",
       "myersmi01NYA2006   0    0   0   0   0   0    0    0   0   0     0  \n",
       "helliri01MIL2006   0    0   0   0   0   2    0    0   0   0     0  \n",
       "johnsra05NYA2006   0    0   0   0   0   4    0    0   0   0     0  "
      ]
     },
     "execution_count": 68,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "player_unique = baseball.player + baseball.team + baseball.year.astype(str)\n",
    "baseball_newind = baseball.copy()\n",
    "baseball_newind.index = player_unique\n",
    "baseball_newind.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 69,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "True"
      ]
     },
     "execution_count": 69,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "baseball_newind.index.is_unique"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "We can create meaningful indices more easily using a hierarchical index; for now, we will stick with the numeric `id` field as our index."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Manipulating indices\n",
    "\n",
    "**Reindexing** allows users to manipulate the data labels in a DataFrame. It forces a DataFrame to conform to the new index, and optionally, fill in missing data if requested.\n",
    "\n",
    "A simple use of `reindex` is to alter the order of the rows:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 70,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "          player  year  stint team  lg    g   ab   r    h  X2b  X3b  hr  rbi  \\\n",
       "id                                                                             \n",
       "89534  alomasa02  2007      1  NYN  NL    8   22   1    3    1    0   0    0   \n",
       "89533   aloumo01  2007      1  NYN  NL   87  328  51  112   19    1  13   49   \n",
       "89530  ausmubr01  2007      1  HOU  NL  117  349  38   82   16    3   3   25   \n",
       "89526  benitar01  2007      1  SFN  NL   19    0   0    0    0    0   0    0   \n",
       "89525  benitar01  2007      2  FLO  NL   34    0   0    0    0    0   0    0   \n",
       "\n",
       "       sb  cs  bb  so  ibb  hbp  sh  sf  gidp  \n",
       "id                                             \n",
       "89534   0   0   0   3    0    0   0   0     0  \n",
       "89533   3   0  27  30    5    2   0   3    13  \n",
       "89530   6   1  37  74    3    6   4   1    11  \n",
       "89526   0   0   0   0    0    0   0   0     0  \n",
       "89525   0   0   0   0    0    0   0   0     0  "
      ]
     },
     "execution_count": 70,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "baseball.reindex(baseball.index[::-1]).head()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Notice that the `id` index is not sequential. Say we wanted to populate the table with every `id` value. We could specify and index that is a sequence from the first to the last `id` numbers in the database, and Pandas would fill in the missing data with `NaN` values:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 71,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "          player  year  stint team   lg   g  ab   r   h  X2b  X3b  hr  rbi  \\\n",
       "88641  womacto01  2006      2  CHN   NL  19  50   6  14    1    0   1    2   \n",
       "88642        NaN   NaN    NaN  NaN  NaN NaN NaN NaN NaN  NaN  NaN NaN  NaN   \n",
       "88643  schilcu01  2006      1  BOS   AL  31   2   0   1    0    0   0    0   \n",
       "88644        NaN   NaN    NaN  NaN  NaN NaN NaN NaN NaN  NaN  NaN NaN  NaN   \n",
       "88645  myersmi01  2006      1  NYA   AL  62   0   0   0    0    0   0    0   \n",
       "\n",
       "       sb  cs  bb  so  ibb  hbp  sh  sf  gidp  \n",
       "88641   1   1   4   4    0    0   3   0     0  \n",
       "88642 NaN NaN NaN NaN  NaN  NaN NaN NaN   NaN  \n",
       "88643   0   0   0   1    0    0   0   0     0  \n",
       "88644 NaN NaN NaN NaN  NaN  NaN NaN NaN   NaN  \n",
       "88645   0   0   0   0    0    0   0   0     0  "
      ]
     },
     "execution_count": 71,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "id_range = range(baseball.index.values.min(), baseball.index.values.max())\n",
    "baseball.reindex(id_range).head()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Missing values can be filled as desired, either with selected values, or by rule:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 72,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "          player  year\n",
       "88641  womacto01  2006\n",
       "88642  womacto01  2006\n",
       "88643  schilcu01  2006\n",
       "88644  schilcu01  2006\n",
       "88645  myersmi01  2006"
      ]
     },
     "execution_count": 72,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "baseball.reindex(id_range, method='ffill', columns=['player','year']).head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 73,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "          player\n",
       "88641  womacto01\n",
       "88642  mr.nobody\n",
       "88643  schilcu01\n",
       "88644  mr.nobody\n",
       "88645  myersmi01"
      ]
     },
     "execution_count": 73,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "baseball.reindex(id_range, fill_value='mr.nobody', columns=['player']).head()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Keep in mind that `reindex` does not work if we pass a non-unique index series."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "We can remove rows or columns via the `drop` method:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 74,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "(100, 22)"
      ]
     },
     "execution_count": 74,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "baseball.shape"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 75,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "          player  year  stint team  lg    g   ab   r    h  X2b  X3b  hr  rbi  \\\n",
       "id                                                                             \n",
       "88641  womacto01  2006      2  CHN  NL   19   50   6   14    1    0   1    2   \n",
       "88643  schilcu01  2006      1  BOS  AL   31    2   0    1    0    0   0    0   \n",
       "88645  myersmi01  2006      1  NYA  AL   62    0   0    0    0    0   0    0   \n",
       "88649  helliri01  2006      1  MIL  NL   20    3   0    0    0    0   0    0   \n",
       "88650  johnsra05  2006      1  NYA  AL   33    6   0    1    0    0   0    0   \n",
       "88652  finlest01  2006      1  SFN  NL  139  426  66  105   21   12   6   40   \n",
       "88653  gonzalu01  2006      1  ARI  NL  153  586  93  159   52    2  15   73   \n",
       "88662   seleaa01  2006      1  LAN  NL   28   26   2    5    1    0   0    0   \n",
       "89177  francju01  2007      2  ATL  NL   15   40   1   10    3    0   0    8   \n",
       "89178  francju01  2007      1  NYN  NL   40   50   7   10    0    0   1    8   \n",
       "...          ...   ...    ...  ...  ..  ...  ...  ..  ...  ...  ...  ..  ...   \n",
       "89497  clemero02  2007      1  NYA  AL    2    2   0    1    0    0   0    0   \n",
       "89498  claytro01  2007      2  BOS  AL    8    6   1    0    0    0   0    0   \n",
       "89499  claytro01  2007      1  TOR  AL   69  189  23   48   14    0   1   12   \n",
       "89501  cirilje01  2007      2  ARI  NL   28   40   6    8    4    0   0    6   \n",
       "89502  cirilje01  2007      1  MIN  AL   50  153  18   40    9    2   2   21   \n",
       "89521  bondsba01  2007      1  SFN  NL  126  340  75   94   14    0  28   66   \n",
       "89523  biggicr01  2007      1  HOU  NL  141  517  68  130   31    3  10   50   \n",
       "89530  ausmubr01  2007      1  HOU  NL  117  349  38   82   16    3   3   25   \n",
       "89533   aloumo01  2007      1  NYN  NL   87  328  51  112   19    1  13   49   \n",
       "89534  alomasa02  2007      1  NYN  NL    8   22   1    3    1    0   0    0   \n",
       "\n",
       "       sb  cs   bb   so  ibb  hbp  sh  sf  gidp  \n",
       "id                                               \n",
       "88641   1   1    4    4    0    0   3   0     0  \n",
       "88643   0   0    0    1    0    0   0   0     0  \n",
       "88645   0   0    0    0    0    0   0   0     0  \n",
       "88649   0   0    0    2    0    0   0   0     0  \n",
       "88650   0   0    0    4    0    0   0   0     0  \n",
       "88652   7   0   46   55    2    2   3   4     6  \n",
       "88653   0   1   69   58   10    7   0   6    14  \n",
       "88662   0   0    1    7    0    0   6   0     1  \n",
       "89177   0   0    4   10    1    0   0   1     1  \n",
       "89178   2   1   10   13    0    0   0   1     1  \n",
       "...    ..  ..  ...  ...  ...  ...  ..  ..   ...  \n",
       "89497   0   0    0    0    0    0   0   0     0  \n",
       "89498   0   0    0    3    0    0   0   0     2  \n",
       "89499   2   1   14   50    0    1   3   3     8  \n",
       "89501   0   0    4    6    0    0   0   0     1  \n",
       "89502   2   0   15   13    0    1   3   2     9  \n",
       "89521   5   0  132   54   43    3   0   2    13  \n",
       "89523   4   3   23  112    0    3   7   5     5  \n",
       "89530   6   1   37   74    3    6   4   1    11  \n",
       "89533   3   0   27   30    5    2   0   3    13  \n",
       "89534   0   0    0    3    0    0   0   0     0  \n",
       "\n",
       "[98 rows x 22 columns]"
      ]
     },
     "execution_count": 75,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "baseball.drop([89525, 89526])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 76,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "          player  year  stint team  lg    g   ab   r    h  X2b  X3b  hr  rbi  \\\n",
       "id                                                                             \n",
       "88641  womacto01  2006      2  CHN  NL   19   50   6   14    1    0   1    2   \n",
       "88643  schilcu01  2006      1  BOS  AL   31    2   0    1    0    0   0    0   \n",
       "88645  myersmi01  2006      1  NYA  AL   62    0   0    0    0    0   0    0   \n",
       "88649  helliri01  2006      1  MIL  NL   20    3   0    0    0    0   0    0   \n",
       "88650  johnsra05  2006      1  NYA  AL   33    6   0    1    0    0   0    0   \n",
       "88652  finlest01  2006      1  SFN  NL  139  426  66  105   21   12   6   40   \n",
       "88653  gonzalu01  2006      1  ARI  NL  153  586  93  159   52    2  15   73   \n",
       "88662   seleaa01  2006      1  LAN  NL   28   26   2    5    1    0   0    0   \n",
       "89177  francju01  2007      2  ATL  NL   15   40   1   10    3    0   0    8   \n",
       "89178  francju01  2007      1  NYN  NL   40   50   7   10    0    0   1    8   \n",
       "...          ...   ...    ...  ...  ..  ...  ...  ..  ...  ...  ...  ..  ...   \n",
       "89499  claytro01  2007      1  TOR  AL   69  189  23   48   14    0   1   12   \n",
       "89501  cirilje01  2007      2  ARI  NL   28   40   6    8    4    0   0    6   \n",
       "89502  cirilje01  2007      1  MIN  AL   50  153  18   40    9    2   2   21   \n",
       "89521  bondsba01  2007      1  SFN  NL  126  340  75   94   14    0  28   66   \n",
       "89523  biggicr01  2007      1  HOU  NL  141  517  68  130   31    3  10   50   \n",
       "89525  benitar01  2007      2  FLO  NL   34    0   0    0    0    0   0    0   \n",
       "89526  benitar01  2007      1  SFN  NL   19    0   0    0    0    0   0    0   \n",
       "89530  ausmubr01  2007      1  HOU  NL  117  349  38   82   16    3   3   25   \n",
       "89533   aloumo01  2007      1  NYN  NL   87  328  51  112   19    1  13   49   \n",
       "89534  alomasa02  2007      1  NYN  NL    8   22   1    3    1    0   0    0   \n",
       "\n",
       "       sb  cs   bb   so  sh  sf  gidp  \n",
       "id                                     \n",
       "88641   1   1    4    4   3   0     0  \n",
       "88643   0   0    0    1   0   0     0  \n",
       "88645   0   0    0    0   0   0     0  \n",
       "88649   0   0    0    2   0   0     0  \n",
       "88650   0   0    0    4   0   0     0  \n",
       "88652   7   0   46   55   3   4     6  \n",
       "88653   0   1   69   58   0   6    14  \n",
       "88662   0   0    1    7   6   0     1  \n",
       "89177   0   0    4   10   0   1     1  \n",
       "89178   2   1   10   13   0   1     1  \n",
       "...    ..  ..  ...  ...  ..  ..   ...  \n",
       "89499   2   1   14   50   3   3     8  \n",
       "89501   0   0    4    6   0   0     1  \n",
       "89502   2   0   15   13   3   2     9  \n",
       "89521   5   0  132   54   0   2    13  \n",
       "89523   4   3   23  112   7   5     5  \n",
       "89525   0   0    0    0   0   0     0  \n",
       "89526   0   0    0    0   0   0     0  \n",
       "89530   6   1   37   74   4   1    11  \n",
       "89533   3   0   27   30   0   3    13  \n",
       "89534   0   0    0    3   0   0     0  \n",
       "\n",
       "[100 rows x 20 columns]"
      ]
     },
     "execution_count": 76,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "baseball.drop(['ibb','hbp'], axis=1)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Indexing and Selection\n",
    "\n",
    "Indexing works analogously to indexing in NumPy arrays, except we can use the labels in the `Index` object to extract values in addition to arrays of integers."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 77,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "womacto01CHN2006     14\n",
       "schilcu01BOS2006      1\n",
       "myersmi01NYA2006      0\n",
       "helliri01MIL2006      0\n",
       "johnsra05NYA2006      1\n",
       "finlest01SFN2006    105\n",
       "gonzalu01ARI2006    159\n",
       "seleaa01LAN2006       5\n",
       "...\n",
       "cirilje01MIN2007     40\n",
       "bondsba01SFN2007     94\n",
       "biggicr01HOU2007    130\n",
       "benitar01FLO2007      0\n",
       "benitar01SFN2007      0\n",
       "ausmubr01HOU2007     82\n",
       "aloumo01NYN2007     112\n",
       "alomasa02NYN2007      3\n",
       "Name: h, Length: 100, dtype: int64"
      ]
     },
     "execution_count": 77,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Sample Series object\n",
    "hits = baseball_newind.h\n",
    "hits"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 78,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "womacto01CHN2006    14\n",
       "schilcu01BOS2006     1\n",
       "myersmi01NYA2006     0\n",
       "Name: h, dtype: int64"
      ]
     },
     "execution_count": 78,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Numpy-style indexing\n",
    "hits[:3]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 79,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "womacto01CHN2006    14\n",
       "schilcu01BOS2006     1\n",
       "Name: h, dtype: int64"
      ]
     },
     "execution_count": 79,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Indexing by label\n",
    "hits[['womacto01CHN2006','schilcu01BOS2006']]"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "We can also slice with data labels, since they have an intrinsic order within the Index:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 80,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "womacto01CHN2006     14\n",
       "schilcu01BOS2006      1\n",
       "myersmi01NYA2006      0\n",
       "helliri01MIL2006      0\n",
       "johnsra05NYA2006      1\n",
       "finlest01SFN2006    105\n",
       "gonzalu01ARI2006    159\n",
       "Name: h, dtype: int64"
      ]
     },
     "execution_count": 80,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "hits['womacto01CHN2006':'gonzalu01ARI2006']"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 81,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "womacto01CHN2006    5\n",
       "schilcu01BOS2006    5\n",
       "myersmi01NYA2006    5\n",
       "helliri01MIL2006    5\n",
       "johnsra05NYA2006    5\n",
       "finlest01SFN2006    5\n",
       "gonzalu01ARI2006    5\n",
       "seleaa01LAN2006     5\n",
       "...\n",
       "cirilje01MIN2007     40\n",
       "bondsba01SFN2007     94\n",
       "biggicr01HOU2007    130\n",
       "benitar01FLO2007      0\n",
       "benitar01SFN2007      0\n",
       "ausmubr01HOU2007     82\n",
       "aloumo01NYN2007     112\n",
       "alomasa02NYN2007      3\n",
       "Name: h, Length: 100, dtype: int64"
      ]
     },
     "execution_count": 81,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "hits['womacto01CHN2006':'gonzalu01ARI2006'] = 5\n",
    "hits"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "In a `DataFrame` we can slice along either or both axes:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 82,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "                    h   ab\n",
       "womacto01CHN2006    5   50\n",
       "schilcu01BOS2006    5    2\n",
       "myersmi01NYA2006    5    0\n",
       "helliri01MIL2006    5    3\n",
       "johnsra05NYA2006    5    6\n",
       "finlest01SFN2006    5  426\n",
       "gonzalu01ARI2006    5  586\n",
       "seleaa01LAN2006     5   26\n",
       "francju01ATL2007   10   40\n",
       "francju01NYN2007   10   50\n",
       "...               ...  ...\n",
       "claytro01TOR2007   48  189\n",
       "cirilje01ARI2007    8   40\n",
       "cirilje01MIN2007   40  153\n",
       "bondsba01SFN2007   94  340\n",
       "biggicr01HOU2007  130  517\n",
       "benitar01FLO2007    0    0\n",
       "benitar01SFN2007    0    0\n",
       "ausmubr01HOU2007   82  349\n",
       "aloumo01NYN2007   112  328\n",
       "alomasa02NYN2007    3   22\n",
       "\n",
       "[100 rows x 2 columns]"
      ]
     },
     "execution_count": 82,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "baseball_newind[['h','ab']]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 83,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "                     player  year  stint team  lg    g   ab   r    h  X2b  \\\n",
       "gonzalu01ARI2006  gonzalu01  2006      1  ARI  NL  153  586  93    5   52   \n",
       "vizquom01SFN2007  vizquom01  2007      1  SFN  NL  145  513  54  126   18   \n",
       "thomafr04TOR2007  thomafr04  2007      1  TOR  AL  155  531  63  147   30   \n",
       "rodriiv01DET2007  rodriiv01  2007      1  DET  AL  129  502  50  141   31   \n",
       "griffke02CIN2007  griffke02  2007      1  CIN  NL  144  528  78  146   24   \n",
       "delgaca01NYN2007  delgaca01  2007      1  NYN  NL  139  538  71  139   30   \n",
       "biggicr01HOU2007  biggicr01  2007      1  HOU  NL  141  517  68  130   31   \n",
       "\n",
       "                  X3b  hr  rbi  sb  cs  bb   so  ibb  hbp  sh  sf  gidp  \n",
       "gonzalu01ARI2006    2  15   73   0   1  69   58   10    7   0   6    14  \n",
       "vizquom01SFN2007    3   4   51  14   6  44   48    6    1  14   3    14  \n",
       "thomafr04TOR2007    0  26   95   0   0  81   94    3    7   0   5    14  \n",
       "rodriiv01DET2007    3  11   63   2   2   9   96    1    1   1   2    16  \n",
       "griffke02CIN2007    1  30   93   6   1  85   99   14    1   0   9    14  \n",
       "delgaca01NYN2007    0  24   87   4   0  52  118    8   11   0   6    12  \n",
       "biggicr01HOU2007    3  10   50   4   3  23  112    0    3   7   5     5  "
      ]
     },
     "execution_count": 83,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "baseball_newind[baseball_newind.ab>500]"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "The indexing field `ix` allows us to select subsets of rows and columns in an intuitive way:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 84,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "h       5\n",
       "X2b    52\n",
       "X3b     2\n",
       "hr     15\n",
       "Name: gonzalu01ARI2006, dtype: object"
      ]
     },
     "execution_count": 84,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "baseball_newind.ix['gonzalu01ARI2006', ['h','X2b', 'X3b', 'hr']]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 85,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "                    g   ab   r\n",
       "gonzalu01ARI2006  153  586  93\n",
       "finlest01SFN2006  139  426  66"
      ]
     },
     "execution_count": 85,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "baseball_newind.ix[['gonzalu01ARI2006','finlest01SFN2006'], 5:8]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 86,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "womacto01CHN2006    1\n",
       "schilcu01BOS2006    0\n",
       "myersmi01NYA2006    0\n",
       "Name: hr, dtype: int64"
      ]
     },
     "execution_count": 86,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "baseball_newind.ix[:'myersmi01NYA2006', 'hr']"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Similarly, the cross-section method `xs` (not a field) extracts a single column or row *by label* and returns it as a `Series`:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 87,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "player    myersmi01\n",
       "year           2006\n",
       "stint             1\n",
       "team            NYA\n",
       "lg               AL\n",
       "g                62\n",
       "ab                0\n",
       "r                 0\n",
       "...\n",
       "cs      0\n",
       "bb      0\n",
       "so      0\n",
       "ibb     0\n",
       "hbp     0\n",
       "sh      0\n",
       "sf      0\n",
       "gidp    0\n",
       "Name: myersmi01NYA2006, Length: 22, dtype: object"
      ]
     },
     "execution_count": 87,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "baseball_newind.xs('myersmi01NYA2006')"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Operations\n",
    "\n",
    "`DataFrame` and `Series` objects allow for several operations to take place either on a single object, or between two or more objects.\n",
    "\n",
    "For example, we can perform arithmetic on the elements of two objects, such as combining baseball statistics across years:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 88,
   "metadata": {
    "collapsed": false
   },
   "outputs": [],
   "source": [
    "hr2006 = baseball[baseball.year==2006].xs('hr', axis=1)\n",
    "hr2006.index = baseball.player[baseball.year==2006]\n",
    "\n",
    "hr2007 = baseball[baseball.year==2007].xs('hr', axis=1)\n",
    "hr2007.index = baseball.player[baseball.year==2007]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 89,
   "metadata": {
    "collapsed": false
   },
   "outputs": [],
   "source": [
    "hr2006 = pd.Series(baseball.hr[baseball.year==2006].values, index=baseball.player[baseball.year==2006])\n",
    "hr2007 = pd.Series(baseball.hr[baseball.year==2007].values, index=baseball.player[baseball.year==2007])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 90,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "player\n",
       "alomasa02   NaN\n",
       "aloumo01    NaN\n",
       "ausmubr01   NaN\n",
       "benitar01   NaN\n",
       "benitar01   NaN\n",
       "biggicr01   NaN\n",
       "bondsba01   NaN\n",
       "cirilje01   NaN\n",
       "...\n",
       "whiteri01   NaN\n",
       "whitero02   NaN\n",
       "wickmbo01   NaN\n",
       "wickmbo01   NaN\n",
       "williwo02   NaN\n",
       "witasja01   NaN\n",
       "womacto01   NaN\n",
       "zaungr01    NaN\n",
       "Length: 94, dtype: float64"
      ]
     },
     "execution_count": 90,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "hr_total = hr2006 + hr2007\n",
    "hr_total"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Pandas' data alignment places `NaN` values for labels that do not overlap in the two Series. In fact, there are only 6 players that occur in both years."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 91,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "player\n",
       "finlest01     7\n",
       "gonzalu01    30\n",
       "johnsra05     0\n",
       "myersmi01     0\n",
       "schilcu01     0\n",
       "seleaa01      0\n",
       "dtype: float64"
      ]
     },
     "execution_count": 91,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "hr_total[hr_total.notnull()]"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "While we do want the operation to honor the data labels in this way, we probably do not want the missing values to be filled with `NaN`. We can use the `add` method to calculate player home run totals by using the `fill_value` argument to insert a zero for home runs where labels do not overlap:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 92,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "player\n",
       "alomasa02     0\n",
       "aloumo01     13\n",
       "ausmubr01     3\n",
       "benitar01     0\n",
       "benitar01     0\n",
       "biggicr01    10\n",
       "bondsba01    28\n",
       "cirilje01     0\n",
       "...\n",
       "whiteri01     0\n",
       "whitero02     4\n",
       "wickmbo01     0\n",
       "wickmbo01     0\n",
       "williwo02     1\n",
       "witasja01     0\n",
       "womacto01     1\n",
       "zaungr01     10\n",
       "Length: 94, dtype: float64"
      ]
     },
     "execution_count": 92,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "hr2007.add(hr2006, fill_value=0)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Operations can also be **broadcast** between rows or columns.\n",
    "\n",
    "For example, if we subtract the maximum number of home runs hit from the `hr` column, we get how many fewer than the maximum were hit by each player:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 93,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "id\n",
       "88641   -34\n",
       "88643   -35\n",
       "88645   -35\n",
       "88649   -35\n",
       "88650   -35\n",
       "88652   -29\n",
       "88653   -20\n",
       "88662   -35\n",
       "...\n",
       "89502   -33\n",
       "89521    -7\n",
       "89523   -25\n",
       "89525   -35\n",
       "89526   -35\n",
       "89530   -32\n",
       "89533   -22\n",
       "89534   -35\n",
       "Name: hr, Length: 100, dtype: int64"
      ]
     },
     "execution_count": 93,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "baseball.hr - baseball.hr.max()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Or, looking at things row-wise, we can see how a particular player compares with the rest of the group with respect to important statistics"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 94,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'bondsba01'"
      ]
     },
     "execution_count": 94,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "baseball.ix[89521][\"player\"]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 95,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "        h  X2b  X3b  hr\n",
       "id                     \n",
       "88641 -80  -13    0 -27\n",
       "88643 -93  -14    0 -28\n",
       "88645 -94  -14    0 -28\n",
       "88649 -94  -14    0 -28\n",
       "88650 -93  -14    0 -28\n",
       "88652  11    7   12 -22\n",
       "88653  65   38    2 -13\n",
       "88662 -89  -13    0 -28\n",
       "89177 -84  -11    0 -28\n",
       "89178 -84  -14    0 -27"
      ]
     },
     "execution_count": 95,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "stats = baseball[['h','X2b', 'X3b', 'hr']]\n",
    "diff = stats - stats.xs(89521)\n",
    "diff[:10]"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "We can also apply functions to each column or row of a `DataFrame`"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 96,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "h      8\n",
       "X2b    1\n",
       "X3b    0\n",
       "hr     0\n",
       "dtype: float64"
      ]
     },
     "execution_count": 96,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "stats.apply(np.median)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 97,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "h      159\n",
       "X2b     52\n",
       "X3b     12\n",
       "hr      35\n",
       "dtype: int64"
      ]
     },
     "execution_count": 97,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "stat_range = lambda x: x.max() - x.min()\n",
    "stats.apply(stat_range)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Lets use apply to calculate a meaningful baseball statistics, slugging percentage:\n",
    "\n",
    "$$SLG = \\frac{1B + (2 \\times 2B) + (3 \\times 3B) + (4 \\times HR)}{AB}$$\n",
    "\n",
    "And just for fun, we will format the resulting estimate."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 98,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "id\n",
       "88641    0.360\n",
       "88643    0.500\n",
       "88645    0.000\n",
       "88649    0.000\n",
       "88650    0.167\n",
       "88652    0.394\n",
       "88653    0.444\n",
       "88662    0.231\n",
       "...\n",
       "89502    0.386\n",
       "89521    0.565\n",
       "89523    0.381\n",
       "89525    0.000\n",
       "89526    0.000\n",
       "89530    0.324\n",
       "89533    0.524\n",
       "89534    0.182\n",
       "Length: 100, dtype: object"
      ]
     },
     "execution_count": 98,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "slg = lambda x: (x['h']-x['X2b']-x['X3b']-x['hr'] + 2*x['X2b'] + 3*x['X3b'] + 4*x['hr'])/(x['ab']+1e-6)\n",
    "baseball.apply(slg, axis=1).apply(lambda x: '%.3f' % x)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Sorting and Ranking\n",
    "\n",
    "Pandas objects include methods for re-ordering data."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 99,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "                     player  year  stint team  lg    g   ab   r    h  X2b  \\\n",
       "alomasa02NYN2007  alomasa02  2007      1  NYN  NL    8   22   1    3    1   \n",
       "aloumo01NYN2007    aloumo01  2007      1  NYN  NL   87  328  51  112   19   \n",
       "ausmubr01HOU2007  ausmubr01  2007      1  HOU  NL  117  349  38   82   16   \n",
       "benitar01FLO2007  benitar01  2007      2  FLO  NL   34    0   0    0    0   \n",
       "benitar01SFN2007  benitar01  2007      1  SFN  NL   19    0   0    0    0   \n",
       "\n",
       "                  X3b  hr  rbi  sb  cs  bb  so  ibb  hbp  sh  sf  gidp  \n",
       "alomasa02NYN2007    0   0    0   0   0   0   3    0    0   0   0     0  \n",
       "aloumo01NYN2007     1  13   49   3   0  27  30    5    2   0   3    13  \n",
       "ausmubr01HOU2007    3   3   25   6   1  37  74    3    6   4   1    11  \n",
       "benitar01FLO2007    0   0    0   0   0   0   0    0    0   0   0     0  \n",
       "benitar01SFN2007    0   0    0   0   0   0   0    0    0   0   0     0  "
      ]
     },
     "execution_count": 99,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "baseball_newind.sort_index().head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 100,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "                     player  year  stint team  lg    g   ab   r   h  X2b  X3b  \\\n",
       "zaungr01TOR2007    zaungr01  2007      1  TOR  AL  110  331  43  80   24    1   \n",
       "womacto01CHN2006  womacto01  2006      2  CHN  NL   19   50   6   5    1    0   \n",
       "witasja01TBA2007  witasja01  2007      1  TBA  AL    3    0   0   0    0    0   \n",
       "williwo02HOU2007  williwo02  2007      1  HOU  NL   33   59   3   6    0    0   \n",
       "wickmbo01ATL2007  wickmbo01  2007      1  ATL  NL   47    0   0   0    0    0   \n",
       "\n",
       "                  hr  rbi  sb  cs  bb  so  ibb  hbp  sh  sf  gidp  \n",
       "zaungr01TOR2007   10   52   0   0  51  55    8    2   1   6     9  \n",
       "womacto01CHN2006   1    2   1   1   4   4    0    0   3   0     0  \n",
       "witasja01TBA2007   0    0   0   0   0   0    0    0   0   0     0  \n",
       "williwo02HOU2007   1    2   0   0   0  25    0    0   5   0     1  \n",
       "wickmbo01ATL2007   0    0   0   0   0   0    0    0   0   0     0  "
      ]
     },
     "execution_count": 100,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "baseball_newind.sort_index(ascending=False).head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 101,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "                  X2b  X3b  ab  bb  cs   g  gidp  h  hbp  hr  ibb  lg  \\\n",
       "womacto01CHN2006    1    0  50   4   1  19     0  5    0   1    0  NL   \n",
       "schilcu01BOS2006    0    0   2   0   0  31     0  5    0   0    0  AL   \n",
       "myersmi01NYA2006    0    0   0   0   0  62     0  5    0   0    0  AL   \n",
       "helliri01MIL2006    0    0   3   0   0  20     0  5    0   0    0  NL   \n",
       "johnsra05NYA2006    0    0   6   0   0  33     0  5    0   0    0  AL   \n",
       "\n",
       "                     player  r  rbi  sb  sf  sh  so  stint team  year  \n",
       "womacto01CHN2006  womacto01  6    2   1   0   3   4      2  CHN  2006  \n",
       "schilcu01BOS2006  schilcu01  0    0   0   0   0   1      1  BOS  2006  \n",
       "myersmi01NYA2006  myersmi01  0    0   0   0   0   0      1  NYA  2006  \n",
       "helliri01MIL2006  helliri01  0    0   0   0   0   2      1  MIL  2006  \n",
       "johnsra05NYA2006  johnsra05  0    0   0   0   0   4      1  NYA  2006  "
      ]
     },
     "execution_count": 101,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "baseball_newind.sort_index(axis=1).head()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "We can also use `order` to sort a `Series` by value, rather than by label."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 102,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "id\n",
       "89360    35\n",
       "89462    30\n",
       "89521    28\n",
       "89361    26\n",
       "89378    25\n",
       "89489    24\n",
       "89371    21\n",
       "89374    21\n",
       "...\n",
       "89465    0\n",
       "89372    0\n",
       "89467    0\n",
       "89370    0\n",
       "89367    0\n",
       "89469    0\n",
       "89365    0\n",
       "89534    0\n",
       "Name: hr, Length: 100, dtype: int64"
      ]
     },
     "execution_count": 102,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "baseball.hr.order(ascending=False)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "For a `DataFrame`, we can sort according to the values of one or more columns using the `by` argument of `sort_index`:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 103,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "          player  sb  cs\n",
       "id                      \n",
       "89378  sheffga01  22   5\n",
       "89430  loftoke01  21   4\n",
       "89347  vizquom01  14   6\n",
       "89463  greensh01  11   1\n",
       "88652  finlest01   7   0\n",
       "89462  griffke02   6   1\n",
       "89530  ausmubr01   6   1\n",
       "89466  gonzalu01   6   2\n",
       "89521  bondsba01   5   0\n",
       "89438  kleskry01   5   1"
      ]
     },
     "execution_count": 103,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "baseball[['player','sb','cs']].sort_index(ascending=[False,True], by=['sb', 'cs']).head(10)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "**Ranking** does not re-arrange data, but instead returns an index that ranks each value relative to others in the Series."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 104,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "id\n",
       "88641    62.5\n",
       "88643    29.0\n",
       "88645    29.0\n",
       "88649    29.0\n",
       "88650    29.0\n",
       "88652    76.0\n",
       "88653    89.5\n",
       "88662    29.0\n",
       "...\n",
       "89502    69.0\n",
       "89521    98.0\n",
       "89523    83.5\n",
       "89525    29.0\n",
       "89526    29.0\n",
       "89530    71.5\n",
       "89533    88.0\n",
       "89534    29.0\n",
       "Name: hr, Length: 100, dtype: float64"
      ]
     },
     "execution_count": 104,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "baseball.hr.rank()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Ties are assigned the mean value of the tied ranks, which may result in decimal values."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 105,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "0    1.5\n",
       "1    1.5\n",
       "dtype: float64"
      ]
     },
     "execution_count": 105,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "pd.Series([100,100]).rank()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Alternatively, you can break ties via one of several methods, such as by the order in which they occur in the dataset:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 106,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "id\n",
       "88641    58\n",
       "88643     1\n",
       "88645     2\n",
       "88649     3\n",
       "88650     4\n",
       "88652    75\n",
       "88653    89\n",
       "88662     5\n",
       "...\n",
       "89502    70\n",
       "89521    98\n",
       "89523    85\n",
       "89525    55\n",
       "89526    56\n",
       "89530    72\n",
       "89533    88\n",
       "89534    57\n",
       "Name: hr, Length: 100, dtype: float64"
      ]
     },
     "execution_count": 106,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "baseball.hr.rank(method='first')"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Calling the `DataFrame`'s `rank` method results in the ranks of all columns:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 107,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "       player  year  stint  team    lg     g    ab     r     h   X2b   X3b  \\\n",
       "id                                                                           \n",
       "88641     2.0  96.5      7  82.0  31.5  70.0  47.5  40.5  39.0  50.5  63.5   \n",
       "88643    37.5  96.5     57  88.0  81.5  55.5  73.0  81.0  63.5  78.0  63.5   \n",
       "88645    47.5  96.5     57  40.5  81.5  36.0  91.0  81.0  84.5  78.0  63.5   \n",
       "88649    66.0  96.5     57  47.0  31.5  67.5  69.0  81.0  84.5  78.0  63.5   \n",
       "88650    61.5  96.5     57  40.5  81.5  51.0  64.5  81.0  63.5  78.0  63.5   \n",
       "\n",
       "         hr   rbi    sb    cs    bb  so  ibb   hbp    sh  sf  gidp  \n",
       "id                                                                  \n",
       "88641  38.5  51.0  24.5  17.5  44.5  59   66  65.5  16.0  70  76.5  \n",
       "88643  72.0  78.5  63.5  62.5  79.0  73   66  65.5  67.5  70  76.5  \n",
       "88645  72.0  78.5  63.5  62.5  79.0  89   66  65.5  67.5  70  76.5  \n",
       "88649  72.0  78.5  63.5  62.5  79.0  67   66  65.5  67.5  70  76.5  \n",
       "88650  72.0  78.5  63.5  62.5  79.0  59   66  65.5  67.5  70  76.5  "
      ]
     },
     "execution_count": 107,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "baseball.rank(ascending=False).head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 108,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "          r     h    hr\n",
       "id                     \n",
       "88641  40.5  39.0  38.5\n",
       "88643  81.0  63.5  72.0\n",
       "88645  81.0  84.5  72.0\n",
       "88649  81.0  84.5  72.0\n",
       "88650  81.0  63.5  72.0"
      ]
     },
     "execution_count": 108,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "baseball[['r','h','hr']].rank(ascending=False).head()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Exercise\n",
    "\n",
    "Calculate **on base percentage** for each player, and return the ordered series of estimates.\n",
    "\n",
    "$$OBP = \\frac{H + BB + HBP}{AB + BB + HBP + SF}$$"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 108,
   "metadata": {
    "collapsed": false
   },
   "outputs": [],
   "source": [
    "# Write your answer here"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Hierarchical indexing\n",
    "\n",
    "In the baseball example, I was forced to combine 3 fields to obtain a unique index that was not simply an integer value. A more elegant way to have done this would be to create a hierarchical index from the three fields."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 109,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "                     stint  lg    g   ab   r    h  X2b  X3b  hr  rbi  sb  cs  \\\n",
       "year team player                                                               \n",
       "2006 CHN  womacto01      2  NL   19   50   6   14    1    0   1    2   1   1   \n",
       "     BOS  schilcu01      1  AL   31    2   0    1    0    0   0    0   0   0   \n",
       "     NYA  myersmi01      1  AL   62    0   0    0    0    0   0    0   0   0   \n",
       "     MIL  helliri01      1  NL   20    3   0    0    0    0   0    0   0   0   \n",
       "     NYA  johnsra05      1  AL   33    6   0    1    0    0   0    0   0   0   \n",
       "     SFN  finlest01      1  NL  139  426  66  105   21   12   6   40   7   0   \n",
       "     ARI  gonzalu01      1  NL  153  586  93  159   52    2  15   73   0   1   \n",
       "     LAN  seleaa01       1  NL   28   26   2    5    1    0   0    0   0   0   \n",
       "2007 ATL  francju01      2  NL   15   40   1   10    3    0   0    8   0   0   \n",
       "     NYN  francju01      1  NL   40   50   7   10    0    0   1    8   2   1   \n",
       "\n",
       "                     bb  so  ibb  hbp  sh  sf  gidp  \n",
       "year team player                                     \n",
       "2006 CHN  womacto01   4   4    0    0   3   0     0  \n",
       "     BOS  schilcu01   0   1    0    0   0   0     0  \n",
       "     NYA  myersmi01   0   0    0    0   0   0     0  \n",
       "     MIL  helliri01   0   2    0    0   0   0     0  \n",
       "     NYA  johnsra05   0   4    0    0   0   0     0  \n",
       "     SFN  finlest01  46  55    2    2   3   4     6  \n",
       "     ARI  gonzalu01  69  58   10    7   0   6    14  \n",
       "     LAN  seleaa01    1   7    0    0   6   0     1  \n",
       "2007 ATL  francju01   4  10    1    0   0   1     1  \n",
       "     NYN  francju01  10  13    0    0   0   1     1  "
      ]
     },
     "execution_count": 109,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "baseball_h = baseball.set_index(['year', 'team', 'player'])\n",
    "baseball_h.head(10)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "This index is a `MultiIndex` object that consists of a sequence of tuples, the elements of which is some combination of the three columns used to create the index. Where there are multiple repeated values, Pandas does not print the repeats, making it easy to identify groups of values."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 110,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "MultiIndex(levels=[[2006, 2007], [u'ARI', u'ATL', u'BAL', u'BOS', u'CHA', u'CHN', u'CIN', u'CLE', u'COL', u'DET', u'FLO', u'HOU', u'KCA', u'LAA', u'LAN', u'MIL', u'MIN', u'NYA', u'NYN', u'OAK', u'PHI', u'SDN', u'SFN', u'SLN', u'TBA', u'TEX', u'TOR'], [u'alomasa02', u'aloumo01', u'ausmubr01', u'benitar01', u'biggicr01', u'bondsba01', u'cirilje01', u'claytro01', u'clemero02', u'coninje01', u'cormirh01', u'delgaca01', u'easleda01', u'edmonji01', u'embreal01', u'finlest01', u'floydcl01', u'francju01', u'glavito02', u'gomezch02', u'gonzalu01', u'gordoto01', u'graffto01', u'greensh01', u'griffke02', u'guarded01', u'helliri01', u'hernaro01', u'hoffmtr01', u'johnsra05', u'jonesto02', u'kentje01', u'kleskry01', u'loaizes01', u'loftoke01', u'mabryjo01', u'maddugr01', u'martipe02', u'mesajo01', u'moyerja01', u'mussimi01', u'myersmi01', u'oliveda02', u'parkch01', u'perezne01', u'piazzmi01', u'ramirma02', u'rodriiv01', u'rogerke01', u'sandere02', u'schilcu01', u'schmija01', u'seaneru01', u'seleaa01', u'sheffga01', u'smoltjo01', u'sosasa01', u'sprinru01', u'stairma01', u'stantmi02', u'stinnke01', u'suppaje01', u'sweenma01', u'tavarju01', u'thomafr04', u'thomeji01', u'timlimi01', u'trachst01', u'valenjo03', u'villoro01', u'vizquom01', u'wakefti01', u'walketo04', u'weathda01', u'wellsda01', u'whiteri01', u'whitero02', u'wickmbo01', u'williwo02', u'witasja01', u'womacto01', u'zaungr01']],\n",
       "           labels=[[0, 0, 0, 0, 0, 0, 0, 0, 1, 1], [5, 3, 17, 15, 17, 22, 0, 14, 1, 18], [80, 50, 41, 26, 29, 15, 20, 53, 17, 17]],\n",
       "           names=[u'year', u'team', u'player'])"
      ]
     },
     "execution_count": 110,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "baseball_h.index[:10]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 111,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "True"
      ]
     },
     "execution_count": 111,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "baseball_h.index.is_unique"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 112,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "stint     2\n",
       "lg       NL\n",
       "g        15\n",
       "ab       40\n",
       "r         1\n",
       "h        10\n",
       "X2b       3\n",
       "X3b       0\n",
       "hr        0\n",
       "rbi       8\n",
       "sb        0\n",
       "cs        0\n",
       "bb        4\n",
       "so       10\n",
       "ibb       1\n",
       "hbp       0\n",
       "sh        0\n",
       "sf        1\n",
       "gidp      1\n",
       "Name: (2007, ATL, francju01), dtype: object"
      ]
     },
     "execution_count": 112,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "baseball_h.ix[(2007, 'ATL', 'francju01')]"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Recall earlier we imported some microbiome data using two index columns. This created a 2-level hierarchical index:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 113,
   "metadata": {
    "collapsed": false
   },
   "outputs": [],
   "source": [
    "mb = pd.read_csv(\"data/microbiome.csv\", index_col=['Taxon','Patient'])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 114,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "                    Tissue  Stool\n",
       "Taxon      Patient               \n",
       "Firmicutes 1           632    305\n",
       "           2           136   4182\n",
       "           3          1174    703\n",
       "           4           408   3946\n",
       "           5           831   8605\n",
       "           6           693     50\n",
       "           7           718    717\n",
       "           8           173     33\n",
       "           9           228     80\n",
       "           10          162   3196"
      ]
     },
     "execution_count": 114,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "mb.head(10)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 115,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "MultiIndex(levels=[[u'Actinobacteria', u'Bacteroidetes', u'Firmicutes', u'Other', u'Proteobacteria'], [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]],\n",
       "           labels=[[2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]],\n",
       "           names=[u'Taxon', u'Patient'])"
      ]
     },
     "execution_count": 115,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "mb.index"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "With a hierachical index, we can select subsets of the data based on a *partial* index:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 116,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "         Tissue  Stool\n",
       "Patient               \n",
       "1          1638   3886\n",
       "2          2469   1821\n",
       "3           839    661\n",
       "4          4414     18\n",
       "5         12044     83\n",
       "6          2310     12\n",
       "7          3053    547\n",
       "8           395   2174\n",
       "9          2651    767\n",
       "10         1195     76\n",
       "11         6857    795\n",
       "12          483    666\n",
       "13         2950   3994\n",
       "14         1541    816\n",
       "15         1307     53"
      ]
     },
     "execution_count": 116,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "mb.ix['Proteobacteria']"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Hierarchical indices can be created on either or both axes. Here is a trivial example:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 117,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "      Ohio       Colorado\n",
       "     Green  Red     Green\n",
       "a 1      0    1         2\n",
       "  2      3    4         5\n",
       "b 1      6    7         8\n",
       "  2      9   10        11"
      ]
     },
     "execution_count": 117,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "frame = pd.DataFrame(np.arange(12).reshape(( 4, 3)), \n",
    "                  index =[['a', 'a', 'b', 'b'], [1, 2, 1, 2]], \n",
    "                  columns =[['Ohio', 'Ohio', 'Colorado'], ['Green', 'Red', 'Green']])\n",
    "\n",
    "frame"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "If you want to get fancy, both the row and column indices themselves can be given names:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 118,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "state       Ohio       Colorado\n",
       "color      Green  Red     Green\n",
       "key1 key2                      \n",
       "a    1         0    1         2\n",
       "     2         3    4         5\n",
       "b    1         6    7         8\n",
       "     2         9   10        11"
      ]
     },
     "execution_count": 118,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "frame.index.names = ['key1', 'key2']\n",
    "frame.columns.names = ['state', 'color']\n",
    "frame"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "With this, we can do all sorts of custom indexing:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 119,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "color  Green  Red\n",
       "key2             \n",
       "1          0    1\n",
       "2          3    4"
      ]
     },
     "execution_count": 119,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "frame.ix['a']['Ohio']"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 120,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "color\n",
       "Green    11\n",
       "Name: (b, 2), dtype: int64"
      ]
     },
     "execution_count": 120,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "frame.ix['b', 2]['Colorado']"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Additionally, the order of the set of indices in a hierarchical `MultiIndex` can be changed by swapping them pairwise:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 121,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "                    Tissue  Stool\n",
       "Patient Taxon                    \n",
       "1       Firmicutes     632    305\n",
       "2       Firmicutes     136   4182\n",
       "3       Firmicutes    1174    703\n",
       "4       Firmicutes     408   3946\n",
       "5       Firmicutes     831   8605"
      ]
     },
     "execution_count": 121,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "mb.swaplevel('Patient', 'Taxon').head()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Data can also be sorted by any index level, using `sortlevel`:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 122,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "                        Tissue  Stool\n",
       "Taxon          Patient               \n",
       "Proteobacteria 15         1307     53\n",
       "Other          15          305     32\n",
       "Firmicutes     15          281   2377\n",
       "Bacteroidetes  15          102     33\n",
       "Actinobacteria 15          310    204"
      ]
     },
     "execution_count": 122,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "mb.sortlevel('Patient', ascending=False).head()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Missing data\n",
    "\n",
    "The occurence of missing data is so prevalent that it pays to use tools like Pandas, which seamlessly integrates missing data handling so that it can be dealt with easily, and in the manner required by the analysis at hand.\n",
    "\n",
    "Missing data are represented in `Series` and `DataFrame` objects by the `NaN` floating point value. However, `None` is also treated as missing, since it is commonly used as such in other contexts (*e.g.* NumPy)."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 130,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "0       NaN\n",
       "1        -3\n",
       "2      None\n",
       "3    foobar\n",
       "dtype: object"
      ]
     },
     "execution_count": 130,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "foo = pd.Series([np.nan, -3, None, 'foobar'])\n",
    "foo"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 131,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "0     True\n",
       "1    False\n",
       "2     True\n",
       "3    False\n",
       "dtype: bool"
      ]
     },
     "execution_count": 131,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "foo.isnull()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Missing values may be dropped or indexed out:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 132,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "phylum\n",
       "Firmicutes         NaN\n",
       "Proteobacteria     632\n",
       "Actinobacteria    1638\n",
       "Bacteroidetes      569\n",
       "dtype: float64"
      ]
     },
     "execution_count": 132,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "bacteria2"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 133,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "phylum\n",
       "Proteobacteria     632\n",
       "Actinobacteria    1638\n",
       "Bacteroidetes      569\n",
       "dtype: float64"
      ]
     },
     "execution_count": 133,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "bacteria2.dropna()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 134,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "phylum\n",
       "Proteobacteria     632\n",
       "Actinobacteria    1638\n",
       "Bacteroidetes      569\n",
       "dtype: float64"
      ]
     },
     "execution_count": 134,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "bacteria2[bacteria2.notnull()]"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "By default, `dropna` drops entire rows in which one or more values are missing."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 135,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "  patient          phylum value  year  treatment\n",
       "0       1      Firmicutes   632  2013          0\n",
       "1       1  Proteobacteria  1638  2013          0\n",
       "2       1  Actinobacteria   569  2013          0\n",
       "3       1   Bacteroidetes    14  2013          0\n",
       "4       2      Firmicutes   433  2013          1\n",
       "5       2  Proteobacteria     0  2013          1\n",
       "6       2  Actinobacteria   754  2013        NaN\n",
       "7       2   Bacteroidetes   555  2013        NaN"
      ]
     },
     "execution_count": 135,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "data"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 136,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "  patient          phylum value  year  treatment\n",
       "0       1      Firmicutes   632  2013          0\n",
       "1       1  Proteobacteria  1638  2013          0\n",
       "2       1  Actinobacteria   569  2013          0\n",
       "3       1   Bacteroidetes    14  2013          0\n",
       "4       2      Firmicutes   433  2013          1\n",
       "5       2  Proteobacteria     0  2013          1"
      ]
     },
     "execution_count": 136,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "data.dropna()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "This can be overridden by passing the `how='all'` argument, which only drops a row when every field is a missing value."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 137,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "  patient          phylum value  year  treatment\n",
       "0       1      Firmicutes   632  2013          0\n",
       "1       1  Proteobacteria  1638  2013          0\n",
       "2       1  Actinobacteria   569  2013          0\n",
       "3       1   Bacteroidetes    14  2013          0\n",
       "4       2      Firmicutes   433  2013          1\n",
       "5       2  Proteobacteria     0  2013          1\n",
       "6       2  Actinobacteria   754  2013        NaN\n",
       "7       2   Bacteroidetes   555  2013        NaN"
      ]
     },
     "execution_count": 137,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "data.dropna(how='all')"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "This can be customized further by specifying how many values need to be present before a row is dropped via the `thresh` argument."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 140,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "  patient          phylum value  year  treatment\n",
       "0       1      Firmicutes   632  2013          0\n",
       "1       1  Proteobacteria  1638  2013          0\n",
       "2       1  Actinobacteria   569  2013          0\n",
       "3       1   Bacteroidetes    14  2013          0\n",
       "4       2      Firmicutes   433  2013          1\n",
       "5       2  Proteobacteria     0  2013          1\n",
       "6       2  Actinobacteria   754  2013        NaN\n",
       "7       2   Bacteroidetes   555   NaN        NaN"
      ]
     },
     "execution_count": 140,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "data.ix[7, 'year'] = np.nan\n",
    "data"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 141,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "  patient          phylum value  year  treatment\n",
       "0       1      Firmicutes   632  2013          0\n",
       "1       1  Proteobacteria  1638  2013          0\n",
       "2       1  Actinobacteria   569  2013          0\n",
       "3       1   Bacteroidetes    14  2013          0\n",
       "4       2      Firmicutes   433  2013          1\n",
       "5       2  Proteobacteria     0  2013          1\n",
       "6       2  Actinobacteria   754  2013        NaN"
      ]
     },
     "execution_count": 141,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "data.dropna(thresh=4)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "This is typically used in time series applications, where there are repeated measurements that are incomplete for some subjects."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "If we want to drop missing values column-wise instead of row-wise, we use `axis=1`."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 142,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "  patient          phylum value\n",
       "0       1      Firmicutes   632\n",
       "1       1  Proteobacteria  1638\n",
       "2       1  Actinobacteria   569\n",
       "3       1   Bacteroidetes    14\n",
       "4       2      Firmicutes   433\n",
       "5       2  Proteobacteria     0\n",
       "6       2  Actinobacteria   754\n",
       "7       2   Bacteroidetes   555"
      ]
     },
     "execution_count": 142,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "data.dropna(axis=1)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Rather than omitting missing data from an analysis, in some cases it may be suitable to fill the missing value in, either with a default value (such as zero) or a value that is either imputed or carried forward/backward from similar data points. We can do this programmatically in Pandas with the `fillna` argument."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 143,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "phylum\n",
       "Firmicutes           0\n",
       "Proteobacteria     632\n",
       "Actinobacteria    1638\n",
       "Bacteroidetes      569\n",
       "dtype: float64"
      ]
     },
     "execution_count": 143,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "bacteria2.fillna(0)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 144,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "  patient          phylum value  year  treatment\n",
       "0       1      Firmicutes   632  2013          0\n",
       "1       1  Proteobacteria  1638  2013          0\n",
       "2       1  Actinobacteria   569  2013          0\n",
       "3       1   Bacteroidetes    14  2013          0\n",
       "4       2      Firmicutes   433  2013          1\n",
       "5       2  Proteobacteria     0  2013          1\n",
       "6       2  Actinobacteria   754  2013          2\n",
       "7       2   Bacteroidetes   555  2013          2"
      ]
     },
     "execution_count": 144,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "data.fillna({'year': 2013, 'treatment':2})"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Notice that `fillna` by default returns a new object with the desired filling behavior, rather than changing the `Series` or  `DataFrame` in place (**in general, we like to do this, by the way!**)."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 145,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "  patient          phylum value  year  treatment\n",
       "0       1      Firmicutes   632  2013          0\n",
       "1       1  Proteobacteria  1638  2013          0\n",
       "2       1  Actinobacteria   569  2013          0\n",
       "3       1   Bacteroidetes    14  2013          0\n",
       "4       2      Firmicutes   433  2013          1\n",
       "5       2  Proteobacteria     0  2013          1\n",
       "6       2  Actinobacteria   754  2013        NaN\n",
       "7       2   Bacteroidetes   555   NaN        NaN"
      ]
     },
     "execution_count": 145,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "data"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "We can alter values in-place using `inplace=True`."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 146,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "  patient          phylum value  year  treatment\n",
       "0       1      Firmicutes   632  2013          0\n",
       "1       1  Proteobacteria  1638  2013          0\n",
       "2       1  Actinobacteria   569  2013          0\n",
       "3       1   Bacteroidetes    14  2013          0\n",
       "4       2      Firmicutes   433  2013          1\n",
       "5       2  Proteobacteria     0  2013          1\n",
       "6       2  Actinobacteria   754  2013        NaN\n",
       "7       2   Bacteroidetes   555  2013        NaN"
      ]
     },
     "execution_count": 146,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "_ = data.year.fillna(2013, inplace=True)\n",
    "data"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Missing values can also be interpolated, using any one of a variety of methods:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 147,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "phylum\n",
       "Firmicutes         632\n",
       "Proteobacteria     632\n",
       "Actinobacteria    1638\n",
       "Bacteroidetes      569\n",
       "dtype: float64"
      ]
     },
     "execution_count": 147,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "bacteria2.fillna(method='bfill')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 148,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "phylum\n",
       "Firmicutes         946.333333\n",
       "Proteobacteria     632.000000\n",
       "Actinobacteria    1638.000000\n",
       "Bacteroidetes      569.000000\n",
       "dtype: float64"
      ]
     },
     "execution_count": 148,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "bacteria2.fillna(bacteria2.mean())"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Data summarization\n",
    "\n",
    "We often wish to summarize data in `Series` or `DataFrame` objects, so that they can more easily be understood or compared with similar data. The NumPy package contains several functions that are useful here, but several summarization or reduction methods are built into Pandas data structures."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 149,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "player    womacto01schilcu01myersmi01helliri01johnsra05f...\n",
       "year                                                 200692\n",
       "stint                                                   113\n",
       "team      CHNBOSNYAMILNYASFNARILANATLNYNTORTBAHOUARIATLM...\n",
       "lg        NLALALNLALNLNLNLNLNLALALNLNLNLALNLNLNLNLALALNL...\n",
       "g                                                      5238\n",
       "ab                                                    13654\n",
       "r                                                      1869\n",
       "...\n",
       "cs        46\n",
       "bb      1549\n",
       "so      2408\n",
       "ibb      177\n",
       "hbp      112\n",
       "sh       138\n",
       "sf       120\n",
       "gidp     354\n",
       "Length: 22, dtype: object"
      ]
     },
     "execution_count": 149,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "baseball.sum()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Clearly, `sum` is more meaningful for some columns than others. For methods like `mean` for which application to string variables is not just meaningless, but impossible, these columns are automatically exculded:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 150,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "year     2006.92\n",
       "stint       1.13\n",
       "g          52.38\n",
       "ab        136.54\n",
       "r          18.69\n",
       "h          35.82\n",
       "X2b         7.39\n",
       "X3b         0.55\n",
       "hr          4.37\n",
       "rbi        18.47\n",
       "sb          1.38\n",
       "cs          0.46\n",
       "bb         15.49\n",
       "so         24.08\n",
       "ibb         1.77\n",
       "hbp         1.12\n",
       "sh          1.38\n",
       "sf          1.20\n",
       "gidp        3.54\n",
       "dtype: float64"
      ]
     },
     "execution_count": 150,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "baseball.mean()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "The important difference between NumPy's functions and Pandas' methods is that the latter have built-in support for handling missing data."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 151,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "phylum\n",
       "Firmicutes         NaN\n",
       "Proteobacteria     632\n",
       "Actinobacteria    1638\n",
       "Bacteroidetes      569\n",
       "dtype: float64"
      ]
     },
     "execution_count": 151,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "bacteria2"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 152,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "946.33333333333337"
      ]
     },
     "execution_count": 152,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "bacteria2.mean()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Sometimes we may not want to ignore missing values, and allow the `nan` to propagate."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 153,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "nan"
      ]
     },
     "execution_count": 153,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "bacteria2.mean(skipna=False)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Passing `axis=1` will summarize over rows instead of columns, which only makes sense in certain situations."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 154,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "id\n",
       "88653    69\n",
       "89439    57\n",
       "89361    56\n",
       "89462    55\n",
       "89396    54\n",
       "89489    54\n",
       "89360    54\n",
       "89371    50\n",
       "...\n",
       "89445    0\n",
       "89388    0\n",
       "89359    0\n",
       "89355    0\n",
       "89354    0\n",
       "89480    0\n",
       "89348    0\n",
       "89420    0\n",
       "Length: 100, dtype: int64"
      ]
     },
     "execution_count": 154,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "extra_bases = baseball[['X2b','X3b','hr']].sum(axis=1)\n",
    "extra_bases.order(ascending=False)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "A useful summarization that gives a quick snapshot of multiple statistics for a `Series` or `DataFrame` is `describe`:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 155,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "             year       stint           g          ab          r           h  \\\n",
       "count   100.00000  100.000000  100.000000  100.000000  100.00000  100.000000   \n",
       "mean   2006.92000    1.130000   52.380000  136.540000   18.69000   35.820000   \n",
       "std       0.27266    0.337998   48.031299  181.936853   27.77496   50.221807   \n",
       "min    2006.00000    1.000000    1.000000    0.000000    0.00000    0.000000   \n",
       "25%    2007.00000    1.000000    9.500000    2.000000    0.00000    0.000000   \n",
       "50%    2007.00000    1.000000   33.000000   40.500000    2.00000    8.000000   \n",
       "75%    2007.00000    1.000000   83.250000  243.750000   33.25000   62.750000   \n",
       "max    2007.00000    2.000000  155.000000  586.000000  107.00000  159.000000   \n",
       "\n",
       "              X2b         X3b          hr        rbi          sb          cs  \\\n",
       "count  100.000000  100.000000  100.000000  100.00000  100.000000  100.000000   \n",
       "mean     7.390000    0.550000    4.370000   18.47000    1.380000    0.460000   \n",
       "std     11.117277    1.445124    7.975537   28.34793    3.694878    1.067613   \n",
       "min      0.000000    0.000000    0.000000    0.00000    0.000000    0.000000   \n",
       "25%      0.000000    0.000000    0.000000    0.00000    0.000000    0.000000   \n",
       "50%      1.000000    0.000000    0.000000    2.00000    0.000000    0.000000   \n",
       "75%     11.750000    1.000000    6.000000   27.00000    1.000000    0.000000   \n",
       "max     52.000000   12.000000   35.000000   96.00000   22.000000    6.000000   \n",
       "\n",
       "               bb          so         ibb        hbp          sh          sf  \\\n",
       "count  100.000000  100.000000  100.000000  100.00000  100.000000  100.000000   \n",
       "mean    15.490000   24.080000    1.770000    1.12000    1.380000    1.200000   \n",
       "std     25.812649   32.804496    5.042957    2.23055    2.919042    2.035046   \n",
       "min      0.000000    0.000000    0.000000    0.00000    0.000000    0.000000   \n",
       "25%      0.000000    1.000000    0.000000    0.00000    0.000000    0.000000   \n",
       "50%      1.000000    7.000000    0.000000    0.00000    0.000000    0.000000   \n",
       "75%     19.250000   37.250000    1.250000    1.00000    1.000000    2.000000   \n",
       "max    132.000000  134.000000   43.000000   11.00000   14.000000    9.000000   \n",
       "\n",
       "             gidp  \n",
       "count  100.000000  \n",
       "mean     3.540000  \n",
       "std      5.201826  \n",
       "min      0.000000  \n",
       "25%      0.000000  \n",
       "50%      1.000000  \n",
       "75%      6.000000  \n",
       "max     21.000000  "
      ]
     },
     "execution_count": 155,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "baseball.describe()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "`describe` can detect non-numeric data and sometimes yield useful information about it."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 156,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "count           100\n",
       "unique           82\n",
       "top       coninje01\n",
       "freq              2\n",
       "dtype: object"
      ]
     },
     "execution_count": 156,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "baseball.player.describe()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "We can also calculate summary statistics *across* multiple columns, for example, correlation and covariance.\n",
    "\n",
    "$$cov(x,y) = \\sum_i (x_i - \\bar{x})(y_i - \\bar{y})$$"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 157,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "69.076464646464629"
      ]
     },
     "execution_count": 157,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "baseball.hr.cov(baseball.X2b)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "$$corr(x,y) = \\frac{cov(x,y)}{(n-1)s_x s_y} = \\frac{\\sum_i (x_i - \\bar{x})(y_i - \\bar{y})}{\\sqrt{\\sum_i (x_i - \\bar{x})^2 \\sum_i (y_i - \\bar{y})^2}}$$"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 158,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "0.77906151825397507"
      ]
     },
     "execution_count": 158,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "baseball.hr.corr(baseball.X2b)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 159,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "0.99421740362723787"
      ]
     },
     "execution_count": 159,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "baseball.ab.corr(baseball.h)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 160,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "           year     stint         g        ab         r         h       X2b  \\\n",
       "year   1.000000  0.004384 -0.050874 -0.001360 -0.023315  0.001151 -0.052917   \n",
       "stint  0.004384  1.000000 -0.257552 -0.216333 -0.209781 -0.206878 -0.196423   \n",
       "g     -0.050874 -0.257552  1.000000  0.935910  0.910262  0.929292  0.885847   \n",
       "ab    -0.001360 -0.216333  0.935910  1.000000  0.965609  0.994217  0.952249   \n",
       "r     -0.023315 -0.209781  0.910262  0.965609  1.000000  0.970560  0.923508   \n",
       "h      0.001151 -0.206878  0.929292  0.994217  0.970560  1.000000  0.957275   \n",
       "X2b   -0.052917 -0.196423  0.885847  0.952249  0.923508  0.957275  1.000000   \n",
       "X3b   -0.246099 -0.085821  0.518663  0.535986  0.500807  0.514245  0.493267   \n",
       "hr     0.060199 -0.209124  0.802014  0.843308  0.890060  0.855163  0.779062   \n",
       "rbi    0.042812 -0.205688  0.891563  0.947911  0.941483  0.952320  0.901751   \n",
       "sb     0.030480 -0.120837  0.492362  0.533536  0.596343  0.530018  0.413655   \n",
       "cs     0.058296 -0.055425  0.520923  0.577192  0.576454  0.571629  0.477487   \n",
       "bb     0.005626 -0.190301  0.828572  0.850803  0.915010  0.853384  0.780012   \n",
       "so     0.069610 -0.214121  0.866499  0.923926  0.879375  0.906966  0.862149   \n",
       "ibb    0.015868 -0.118580  0.514423  0.506398  0.588882  0.513009  0.453301   \n",
       "hbp   -0.000664 -0.195074  0.730161  0.767210  0.806523  0.767449  0.738226   \n",
       "sh    -0.012184 -0.091527  0.079361  0.094537 -0.001273  0.045533  0.005659   \n",
       "sf    -0.007282 -0.155662  0.767543  0.840361  0.839592  0.839737  0.819361   \n",
       "gidp   0.052131 -0.224173  0.863041  0.926632  0.894724  0.935525  0.906860   \n",
       "\n",
       "            X3b        hr       rbi        sb        cs        bb        so  \\\n",
       "year  -0.246099  0.060199  0.042812  0.030480  0.058296  0.005626  0.069610   \n",
       "stint -0.085821 -0.209124 -0.205688 -0.120837 -0.055425 -0.190301 -0.214121   \n",
       "g      0.518663  0.802014  0.891563  0.492362  0.520923  0.828572  0.866499   \n",
       "ab     0.535986  0.843308  0.947911  0.533536  0.577192  0.850803  0.923926   \n",
       "r      0.500807  0.890060  0.941483  0.596343  0.576454  0.915010  0.879375   \n",
       "h      0.514245  0.855163  0.952320  0.530018  0.571629  0.853384  0.906966   \n",
       "X2b    0.493267  0.779062  0.901751  0.413655  0.477487  0.780012  0.862149   \n",
       "X3b    1.000000  0.210028  0.369890  0.450421  0.384312  0.350682  0.408800   \n",
       "hr     0.210028  1.000000  0.948787  0.364346  0.345187  0.916774  0.865929   \n",
       "rbi    0.369890  0.948787  1.000000  0.394633  0.435011  0.893945  0.929410   \n",
       "sb     0.450421  0.364346  0.394633  1.000000  0.743921  0.491351  0.365841   \n",
       "cs     0.384312  0.345187  0.435011  0.743921  1.000000  0.425352  0.426658   \n",
       "bb     0.350682  0.916774  0.893945  0.491351  0.425352  1.000000  0.795751   \n",
       "so     0.408800  0.865929  0.929410  0.365841  0.426658  0.795751  1.000000   \n",
       "ibb    0.090993  0.673691  0.582982  0.209110  0.106152  0.792057  0.476613   \n",
       "hbp    0.217474  0.767411  0.780899  0.413570  0.337129  0.742118  0.742547   \n",
       "sh     0.187012 -0.145374 -0.054670  0.171910  0.293397 -0.044992  0.073624   \n",
       "sf     0.394987  0.782038  0.855260  0.412947  0.422146  0.760932  0.782314   \n",
       "gidp   0.411577  0.798350  0.906908  0.431198  0.456820  0.823631  0.846629   \n",
       "\n",
       "            ibb       hbp        sh        sf      gidp  \n",
       "year   0.015868 -0.000664 -0.012184 -0.007282  0.052131  \n",
       "stint -0.118580 -0.195074 -0.091527 -0.155662 -0.224173  \n",
       "g      0.514423  0.730161  0.079361  0.767543  0.863041  \n",
       "ab     0.506398  0.767210  0.094537  0.840361  0.926632  \n",
       "r      0.588882  0.806523 -0.001273  0.839592  0.894724  \n",
       "h      0.513009  0.767449  0.045533  0.839737  0.935525  \n",
       "X2b    0.453301  0.738226  0.005659  0.819361  0.906860  \n",
       "X3b    0.090993  0.217474  0.187012  0.394987  0.411577  \n",
       "hr     0.673691  0.767411 -0.145374  0.782038  0.798350  \n",
       "rbi    0.582982  0.780899 -0.054670  0.855260  0.906908  \n",
       "sb     0.209110  0.413570  0.171910  0.412947  0.431198  \n",
       "cs     0.106152  0.337129  0.293397  0.422146  0.456820  \n",
       "bb     0.792057  0.742118 -0.044992  0.760932  0.823631  \n",
       "so     0.476613  0.742547  0.073624  0.782314  0.846629  \n",
       "ibb    1.000000  0.431714 -0.075658  0.451377  0.572355  \n",
       "hbp    0.431714  1.000000 -0.104810  0.648882  0.700380  \n",
       "sh    -0.075658 -0.104810  1.000000 -0.002721  0.028924  \n",
       "sf     0.451377  0.648882 -0.002721  1.000000  0.785489  \n",
       "gidp   0.572355  0.700380  0.028924  0.785489  1.000000  "
      ]
     },
     "execution_count": 160,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "baseball.corr()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "If we have a `DataFrame` with a hierarchical index (or indices), summary statistics can be applied with respect to any of the index levels:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 161,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "                    Tissue  Stool\n",
       "Taxon      Patient               \n",
       "Firmicutes 1           632    305\n",
       "           2           136   4182\n",
       "           3          1174    703\n",
       "           4           408   3946\n",
       "           5           831   8605"
      ]
     },
     "execution_count": 161,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "mb.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 162,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "                Tissue  Stool\n",
       "Taxon                        \n",
       "Actinobacteria    6736   2263\n",
       "Bacteroidetes     8995   4656\n",
       "Firmicutes       10266  30477\n",
       "Other             2982    519\n",
       "Proteobacteria   44146  16369"
      ]
     },
     "execution_count": 162,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "mb.sum(level='Taxon')"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Writing Data to Files\n",
    "\n",
    "As well as being able to read several data input formats, Pandas can also export data to a variety of storage formats. We will bring your attention to just a couple of these."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 163,
   "metadata": {
    "collapsed": false
   },
   "outputs": [],
   "source": [
    "mb.to_csv(\"mb.csv\")"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "The `to_csv` method writes a `DataFrame` to a comma-separated values (csv) file. You can specify custom delimiters (via `sep` argument), how missing values are written (via `na_rep` argument), whether the index is writen (via `index` argument), whether the header is included (via `header` argument), among other options."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "An efficient way of storing data to disk is in binary format. Pandas supports this using Python’s built-in pickle serialization."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 164,
   "metadata": {
    "collapsed": false
   },
   "outputs": [],
   "source": [
    "baseball.to_pickle(\"baseball_pickle\")"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "The complement to `to_pickle` is the `read_pickle` function, which restores the pickle to a `DataFrame` or `Series`:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 165,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "          player  year  stint team  lg    g   ab   r    h  X2b  X3b  hr  rbi  \\\n",
       "id                                                                             \n",
       "88641  womacto01  2006      2  CHN  NL   19   50   6   14    1    0   1    2   \n",
       "88643  schilcu01  2006      1  BOS  AL   31    2   0    1    0    0   0    0   \n",
       "88645  myersmi01  2006      1  NYA  AL   62    0   0    0    0    0   0    0   \n",
       "88649  helliri01  2006      1  MIL  NL   20    3   0    0    0    0   0    0   \n",
       "88650  johnsra05  2006      1  NYA  AL   33    6   0    1    0    0   0    0   \n",
       "88652  finlest01  2006      1  SFN  NL  139  426  66  105   21   12   6   40   \n",
       "88653  gonzalu01  2006      1  ARI  NL  153  586  93  159   52    2  15   73   \n",
       "88662   seleaa01  2006      1  LAN  NL   28   26   2    5    1    0   0    0   \n",
       "89177  francju01  2007      2  ATL  NL   15   40   1   10    3    0   0    8   \n",
       "89178  francju01  2007      1  NYN  NL   40   50   7   10    0    0   1    8   \n",
       "...          ...   ...    ...  ...  ..  ...  ...  ..  ...  ...  ...  ..  ...   \n",
       "89499  claytro01  2007      1  TOR  AL   69  189  23   48   14    0   1   12   \n",
       "89501  cirilje01  2007      2  ARI  NL   28   40   6    8    4    0   0    6   \n",
       "89502  cirilje01  2007      1  MIN  AL   50  153  18   40    9    2   2   21   \n",
       "89521  bondsba01  2007      1  SFN  NL  126  340  75   94   14    0  28   66   \n",
       "89523  biggicr01  2007      1  HOU  NL  141  517  68  130   31    3  10   50   \n",
       "89525  benitar01  2007      2  FLO  NL   34    0   0    0    0    0   0    0   \n",
       "89526  benitar01  2007      1  SFN  NL   19    0   0    0    0    0   0    0   \n",
       "89530  ausmubr01  2007      1  HOU  NL  117  349  38   82   16    3   3   25   \n",
       "89533   aloumo01  2007      1  NYN  NL   87  328  51  112   19    1  13   49   \n",
       "89534  alomasa02  2007      1  NYN  NL    8   22   1    3    1    0   0    0   \n",
       "\n",
       "       sb  cs   bb   so  ibb  hbp  sh  sf  gidp  \n",
       "id                                               \n",
       "88641   1   1    4    4    0    0   3   0     0  \n",
       "88643   0   0    0    1    0    0   0   0     0  \n",
       "88645   0   0    0    0    0    0   0   0     0  \n",
       "88649   0   0    0    2    0    0   0   0     0  \n",
       "88650   0   0    0    4    0    0   0   0     0  \n",
       "88652   7   0   46   55    2    2   3   4     6  \n",
       "88653   0   1   69   58   10    7   0   6    14  \n",
       "88662   0   0    1    7    0    0   6   0     1  \n",
       "89177   0   0    4   10    1    0   0   1     1  \n",
       "89178   2   1   10   13    0    0   0   1     1  \n",
       "...    ..  ..  ...  ...  ...  ...  ..  ..   ...  \n",
       "89499   2   1   14   50    0    1   3   3     8  \n",
       "89501   0   0    4    6    0    0   0   0     1  \n",
       "89502   2   0   15   13    0    1   3   2     9  \n",
       "89521   5   0  132   54   43    3   0   2    13  \n",
       "89523   4   3   23  112    0    3   7   5     5  \n",
       "89525   0   0    0    0    0    0   0   0     0  \n",
       "89526   0   0    0    0    0    0   0   0     0  \n",
       "89530   6   1   37   74    3    6   4   1    11  \n",
       "89533   3   0   27   30    5    2   0   3    13  \n",
       "89534   0   0    0    3    0    0   0   0     0  \n",
       "\n",
       "[100 rows x 22 columns]"
      ]
     },
     "execution_count": 165,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "pd.read_pickle(\"baseball_pickle\")"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "As Wes warns in his book, it is recommended that binary storage of data via pickle only be used as a temporary storage format, in situations where speed is relevant. This is because there is no guarantee that the pickle format will not change with future versions of Python."
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.4.2"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 0
}
