# On Approximation of the General Poset Cover Problem

This repository contains all the codes used in and results generated from the empirical assessments
of the two approximation algorithms.

# Usage

To generate linear order inputs,
```bash
python linearorders.py <keyword> <vertex count>
```

To generate optimal solutions,
```bash
python optimalsolutions.py <vertex count>
```

To generate approximations,
```bash
python tests.py <algorithm> <vertex count> <type>
```

To compile results into .csv files,
```bash
python analysis.py <vertex count> <type>
```

*`vertex count` should be valued 3 or greater
*`type` is an optional argument

| keyword | description |
| ------- | ----------- |
| `all` | generates all linear order sets with `vertex count` vertices |
| `trees` | generates all linear order sets of trees with `vertex count` vertices |
| `hammocks ` | generates all linear order sets of hammocks with `vertex count` vertices |

| algorithm | description |
| --------- | ----------- |
| `algo1` | generates approximations of Algorithm 1 |
| `algo2` | generates approximations of Algorithm 2 |

| type | description |
| ---- | ----------- |
| `trees` | uses files concerning trees |
| `hammocks` | uses files concerning hammocks |