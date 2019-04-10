Stochastic deformation models(SDM)
====

Overview

# Usage
## 1. Prepare GPSRDATA
- cat1Sentences.en.xlsx
- items.txt
- locations.txt
- rooms.txt

## 2. Make original dataset
`./MakeOriginalDataset.sh`
 - Input
   - GPSRDATA
 - Output
   - OriginalDataset
     - devdata.csv
     - testdata.csv
     - traindata.csv
## 3. Inject noise
`./SDMMake.sh`
 - Input
   - OriginalDataset
 - Output
   - Dataset
