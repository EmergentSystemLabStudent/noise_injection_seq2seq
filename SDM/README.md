Stochastic deformation models(SDM)
====

# Overview

# Script List
## Python
  - GPSRDATA/GPSRsentence_generator2015enMakelabeldata.py
  - SDM.py
  - vocabMake.py
  - SDM_experiment_2.py
## Shell
  - MakeOriginalDataset.sh
  - SDMMake.sh
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
     - PI=0.*_PS=0.*_PD=*_Input_<dev/test/train>_data.in
     - PI=0.*_PS_0.*_PD=*_phoneme_<dev/test/train>_data.in
     - PI=0.*_PS_0.*_PD=*_Noisy_<dev/test/train>_data.in
     - PI=0.*_PS_0.*_PD=*_label_<dev/test/train>_data.out
     - PI=0.*_PS_0.*_PD=*_<dev/test/train>_data.csv
