Stochastic deformation models(SDM)
====

# Overview
GPSRDATA->OriginalDataset---(SDM)--> EditedDataset

                          └─-------> Vocab
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
     - `PI=prob_PS=prob_PD=prob_Input_<dev/test/train>_data.in`

