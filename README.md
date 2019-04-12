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
     - PI_*PS_*PD_*Input<dev/test/train>data.in
     - PI_*PS_*PD_*phoneme<dev/test/train>data.in
     - PI_*PS_*PD_*Noisy<dev/test/train>data.in
     - PI_*PS_*PD_*label<dev/test/train>data.out
     - PI_*PS_*PD_* <dev/test/train>data.csv
