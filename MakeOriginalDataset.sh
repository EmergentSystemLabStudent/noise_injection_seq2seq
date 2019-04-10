#!/bin/sh
cd GPSRDATA
rm GPSRSentence.csv
python GPSRsentence_generator2015enMakelabeldata.py || exit
echo "python実行できました."
touch ../OriginalDataset/traindata.csv
touch ../OriginalDataset/testdata.csv
touch ../OriginalDataset/devdata.csv
sed -e '10000,$d' GPSRSentence.csv > ../OriginalDataset/traindata.csv
sed -n '10001,12001p' GPSRSentence.csv > ../OriginalDataset/testdata.csv
sed -n '12002,14002p' GPSRSentence.csv > ../OriginalDataset/devdata.csv
cd ../OriginalDataset
gsed -e '1idata,labeldata' -i testdata.csv
gsed -e '1idata,labeldata' -i devdata.csv
