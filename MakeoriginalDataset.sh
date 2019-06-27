#!/bin/sh
cd GPSRDATA
python GPSRsentence_generator2015enMakelabeldata.py || exit
echo "[sucess]"
touch ../OriginalDataset/train.csv
touch ../OriginalDataset/test.csv
touch ../OriginalDataset/dev.csv
echo "data,labeldata" > ../OriginalDataset/train.csv
echo "data,labeldata" > ../OriginalDataset/test.csv
echo "data,labeldata" > ../OriginalDataset/dev.csv
sed -e '10000,$d' tempGPSRSentence.csv >> ../OriginalDataset/train.csv
sed -n '10001,12001p' tempGPSRSentence.csv >> ../OriginalDataset/test.csv
sed -n '12002,14002p' tempGPSRSentence.csv >> ../OriginalDataset/dev.csv
