#!/bin/sh
cd GPSRDATA
python GPSRsentence_generator2015enMakelabeldata.py || exit
echo "[sucess]"
touch ../OriginalDataset/traindata.csv
touch ../OriginalDataset/testdata.csv
touch ../OriginalDataset/devdata.csv
echo "data,labeldata" > ../OriginalDataset/traindata.csv
echo "data,labeldata" > ../OriginalDataset/testdata.csv
echo "data,labeldata" > ../OriginalDataset/devdata.csv
sed -e '10000,$d' GPSRSentence.csv >> ../OriginalDataset/traindata.csv
sed -n '10001,12001p' GPSRSentence.csv >> ../OriginalDataset/testdata.csv
sed -n '12002,14002p' GPSRSentence.csv >> ../OriginalDataset/devdata.csv
cd ../OriginalDataset
