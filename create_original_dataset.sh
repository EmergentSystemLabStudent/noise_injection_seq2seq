#!/bin/sh
cd GPSRDATA
python GPSRsentence_generator2015enMakelabeldata.py || exit
echo "[sucess]"
cd ..
mkdir -p original_dataset
touch original_dataset/train.csv
touch original_dataset/test.csv
touch original_dataset/dev.csv
echo "data,labeldata" > original_dataset/train.csv
echo "data,labeldata" > original_dataset/test.csv
echo "data,labeldata" > original_dataset/dev.csv
sed -e '10000,$d' GPSRDATA/tempGPSRSentence.csv >> original_dataset/train.csv
sed -n '10001,12001p' GPSRDATA/tempGPSRSentence.csv >> original_dataset/test.csv
sed -n '12002,14002p' GPSRDATA/tempGPSRSentence.csv >> original_dataset/dev.csv
