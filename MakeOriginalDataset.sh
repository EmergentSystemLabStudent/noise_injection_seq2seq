#!/bin/sh
cd GPSRDATA
if [ $1 = "GPSR" ]; then
echo "GPSR"
rm GPSRSentence.csv
python GPSRsentence_generator2015enMakelabeldata.py || exit
echo "python実行できました."
touch ../OriginDataset/traindata.csv
touch ../OriginDataset/testdata.csv
touch ../OriginDataset/devdata.csv
sed -e '10000,$d' GPSRSentence.csv > ../OriginDataset/traindata.csv
sed -n '10001,12001p' GPSRSentence.csv > ../OriginDataset/testdata.csv
sed -n '12002,14002p' GPSRSentence.csv > ../OriginDataset/devdata.csv
cd ../OriginDataset
gsed -e '1idata,labeldata' -i testdata.csv
gsed -e '1idata,labeldata' -i devdata.csv
else
  echo "GPSRSentenceを実行しません."
fi
