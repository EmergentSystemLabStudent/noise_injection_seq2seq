#!/bin/sh

if [ $1 = "GPSR" ]; then
echo "GPSR"
rm GPSRSentenceJP.csv
python GPSRsentence_generator2015enMakelabeldata.py || exit
echo "python実行できました."

sed -e '10000,$d' GPSRSentenceJP.csv > traindata.csv
sed -n '10001,12001p' GPSRSentenceJP.csv > testdata.csv
sed -n '12002,14002p' GPSRSentenceJP.csv > devdata.csv
cp  testdata.csv ../OriginDataset
cp  traindata.csv ../OriginDataset
cp  devdata.csv ../OriginDataset
cd ../OriginDataset
gsed -e '1idata,labeldata' -i testdata.csv
gsed -e '1idata,labeldata' -i devdata.csv
else
  echo "GPSRSentenceJPを実行しません."
fi

