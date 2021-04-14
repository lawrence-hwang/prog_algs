# Prognostics Algorithm Python Package

The Prognostic Algorithm Package is a python framework for model-based prognostics (computation of remaining useful life) of engineering systems, and provides a set of algorithms for state estimation and prediction, including uncertainty propagation. The algorithms take as inputs prognostic models (from NASA's Prognostics Model Package), and perform estimation and prediction functions. The library allows the rapid development of prognostics solutions for given models of components and systems. Different algorithms can be easily swapped to do comparative studies and evaluations of different algorithms to select the best for the application at hand.

## Installation
1. Use `pip install -r requirements.txt` to install dependencies 
2. Ensure `prog_models` package is in path. This could be done by moving the `prog_models` directory into the path, or by adding the path to the `prog_models` package 

## Directory Structure 

`prog_algs/` - The prognostics algorithm python package
&nbsp;&nbsp;&nbsp;&nbsp;  |- `predictors/` - Algorithms for performing the prediction step of model-based prognostics
&nbsp;&nbsp;&nbsp;&nbsp;  |- `samplers/` - Standard tools for performing state sampling
&nbsp;&nbsp;&nbsp;&nbsp;  |- `state_estimators/` - Algorithms for performing the state estimation step of model-based prognostics
`benchmarking_example` - An example using metrics for benchmarking
`example.py` - An example python script using prog_algs 
`README.md` - The readme (this file)
`requirements.txt` - python library dependiencies required to be met to use this package. Install using `pip install -r requirements.txt`

## Citing this repository
Use the following to cite this repository:

```
@misc{2020_nasa_prog_model,
    author    = {Christopher Teubert and Chetan Kulkarni},
    title     = {Prognostics Algorithm Python Package},
    month     = Oct,
    year      = 2020,
    version   = {0.0.1},
    url       = {TBD}
    }
```

The corresponding reference should look like this:

C. Teubert, and C. Kulkarni, Prognostics Algorithm Python Package, v0.0.1, Oct. 2020. URL TBD.

## Notices

Copyright © 2021 United States Government as represented by the Administrator of the National Aeronautics and Space Administration.  All Rights Reserved.

## Disclaimers

No Warranty: THE SUBJECT SOFTWARE IS PROVIDED "AS IS" WITHOUT ANY WARRANTY OF ANY KIND, EITHER EXPRESSED, IMPLIED, OR STATUTORY, INCLUDING, BUT NOT LIMITED TO, ANY WARRANTY THAT THE SUBJECT SOFTWARE WILL CONFORM TO SPECIFICATIONS, ANY IMPLIED WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE, OR FREEDOM FROM INFRINGEMENT, ANY WARRANTY THAT THE SUBJECT SOFTWARE WILL BE ERROR FREE, OR ANY WARRANTY THAT DOCUMENTATION, IF PROVIDED, WILL CONFORM TO THE SUBJECT SOFTWARE. THIS AGREEMENT DOES NOT, IN ANY MANNER, CONSTITUTE AN ENDORSEMENT BY GOVERNMENT AGENCY OR ANY PRIOR RECIPIENT OF ANY RESULTS, RESULTING DESIGNS, HARDWARE, SOFTWARE PRODUCTS OR ANY OTHER APPLICATIONS RESULTING FROM USE OF THE SUBJECT SOFTWARE.  FURTHER, GOVERNMENT AGENCY DISCLAIMS ALL WARRANTIES AND LIABILITIES REGARDING THIRD-PARTY SOFTWARE, IF PRESENT IN THE ORIGINAL SOFTWARE, AND DISTRIBUTES IT "AS IS."

Waiver and Indemnity:  RECIPIENT AGREES TO WAIVE ANY AND ALL CLAIMS AGAINST THE UNITED STATES GOVERNMENT, ITS CONTRACTORS AND SUBCONTRACTORS, AS WELL AS ANY PRIOR RECIPIENT.  IF RECIPIENT'S USE OF THE SUBJECT SOFTWARE RESULTS IN ANY LIABILITIES, DEMANDS, DAMAGES, EXPENSES OR LOSSES ARISING FROM SUCH USE, INCLUDING ANY DAMAGES FROM PRODUCTS BASED ON, OR RESULTING FROM, RECIPIENT'S USE OF THE SUBJECT SOFTWARE, RECIPIENT SHALL INDEMNIFY AND HOLD HARMLESS THE UNITED STATES GOVERNMENT, ITS CONTRACTORS AND SUBCONTRACTORS, AS WELL AS ANY PRIOR RECIPIENT, TO THE EXTENT PERMITTED BY LAW.  RECIPIENT'S SOLE REMEDY FOR ANY SUCH MATTER SHALL BE THE IMMEDIATE, UNILATERAL TERMINATION OF THIS AGREEMENT.