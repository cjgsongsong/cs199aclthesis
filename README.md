# *On Approximation of the General Poset Cover Problem*

This repository contains all the codes used in the empirical assessments
of the two approximation algorithms studied by Kaizz Angeles and CJ Songsong for their undergraduate
thesis under the advisory of Ivy Ordanel. Results generated are accessible via [https://bit.ly/OnApprox-Files](https://bit.ly/OnApprox-Files). Manuscript is available on [https:/bit.ly/OnApprox-Manuscript](https://bit.ly/OnApprox-Manuscript).

## Installation

Before running `analysis.ipynb`, install the necessary packages.
```bash
pip install jupyter notebook
pip install matplotlib
pip install numpy
pip install pandas
pip install scipy
pip install seaborn
```

## Usage

To generate linear order inputs,
```bash
python linearorders.py <keyword> <vertex count*>
```

To generate optimal solutions,
```bash
python optimalsolutions.py <vertex count*> <type**>
```

To generate approximations,
```bash
python tests.py <algorithm> <vertex count*> <type**>
```

To compile results into .csv files,
```bash
python analysis.py <vertex count*> <type**>
```

*`vertex count` should be valued 3 or greater  
**`type` is an optional argument  

| keyword | description |
| ------- | ----------- |
| `all` | generates all linear order sets with `vertex count` vertices |
| `trees` | generates all linear order sets of trees with `vertex count` vertices |

| algorithm | description |
| --------- | ----------- |
| `algo1` | generates approximations of Algorithm 1 |
| `algo2` | generates approximations of Algorithm 2 |
| `algo2i` | generates approximations of improved Algorithm 2 |

| type | description |
| ---- | ----------- |
| `trees` | uses files concerning trees |
