from setuptools import setup, find_packages
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))


with open(path.join(here, 'DESCRIPTION.rst'), encoding='utf-8') as f:
    long_description = f.read()

setup( 
21     name='pygp', 
22 
26     version='1.2.0a1', 
27 
 
28     description='A genetic programming library for symbolic regression\
                   applications', 
29     long_description=long_description, 
30 
 
31     # The project's main homepage. 
32     url='https://github.com/StarshipEngineer/pyGP', 
33 
 
34     # Author details 
35     author='Dan Shuman', 
36     author_email='dan.13.shuman@gmail.com', 
37 
 
38     # Choose your license 
39     license='MIT', 
40 
 
41     # See https://pypi.python.org/pypi?%3Aaction=list_classifiers 
42     classifiers=[ 
43         # How mature is this project? Common values are 
44         #   3 - Alpha 
45         #   4 - Beta 
46         #   5 - Production/Stable 
47         'Development Status :: 3 - Alpha', 
48 
 
49         # Indicate who your project is intended for 
50         'Intended Audience :: Developers', 
51         'Topic :: Software Development :: Build Tools', 
52 
 
53         # Pick your license as you wish (should match "license" above) 
54         'License :: OSI Approved :: MIT License', 
55 
61         'Programming Language :: Python :: 3', 
62         'Programming Language :: Python :: 3.2', 
63         'Programming Language :: Python :: 3.3', 
64         'Programming Language :: Python :: 3.4', 
65     ], 
66 
 
67     # What does your project relate to? 
68     keywords='symbolic regression', 
69 
 
70     # You can just specify the packages manually here if your project is 
71     # simple. Or you can use find_packages(). 
72     packages=find_packages(exclude=[]), 
73 
 
74     # List run-time dependencies here.  These will be installed by pip when 
75     # your project is installed. For an analysis of "install_requires" vs pip's 
76     # requirements files see: 
77     # https://packaging.python.org/en/latest/requirements.html 
78     install_requires=['random', 'math', 'copy', 'decimal'], 
79 
 
80     # List additional groups of dependencies here (e.g. development 
81     # dependencies). You can install these using the following syntax, 
82     # for example: 
83     # $ pip install -e .[dev,test] 
84     extras_require={ 
85         'dev': ['check-manifest'], 
86         'test': ['coverage'], 
87     }, 
88 
 
89     # If there are data files included in your packages that need to be 
90     # installed, specify them here.  If using Python 2.6 or less, then these 
91     # have to be included in MANIFEST.in as well. 
92     package_data={ 
93         'sample': ['package_data.dat'], 
94     }, 
95 
 
96     # Although 'package_data' is the preferred approach, in some case you may 
97     # need to place data files outside of your packages. See: 
98     # http://docs.python.org/3.4/distutils/setupscript.html#installing-additional-files # noqa 
99     # In this case, 'data_file' will be installed into '<sys.prefix>/my_data' 
100     data_files=[('my_data', ['data/data_file'])], 
101 
 
102     # To provide executable scripts, use entry points in preference to the 
103     # "scripts" keyword. Entry points provide cross-platform support and allow 
104     # pip to create the appropriate form of executable for the target platform. 
105     entry_points={ 
106         'console_scripts': [ 
107             'sample=sample:main', 
108         ], 
109     }, 
110 ) 
