#!/bin/sh

if [ $1 = "GPSR" ]; then
echo "GPSR"
rm GPSRSentenceJP.csv
python GPSRsentence_generator2015enMakelabeldata.py || exit
echo "python実行できました."
#ここでもう同じ担ってる

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

cd  ..

echo "SDM_experiment_2.py"
python SDM_experiment_2.py testdata.csv || echo "SDM_experiment_2.py testdata.csv 失敗しました"
python SDM_experiment_2.py traindata.csv || echo "SDM_experiment_2.py traindata.csv 失敗しました"
python SDM_experiment_2.py devdata.csv || echo "SDM_experiment_2.py testdata.csv 失敗しました"


echo "SDM.py"
python SDM.py testdata.csv || echo "SDM.py testdata.csv 失敗しました"
python SDM.py traindata.csv || echo "SDM.py traindata.csv 失敗しました"
python SDM.py devdata.csv || echo "SDM.py testdata.csv 失敗しました"


echo "vocabMakeを始めます"
echo "vocabMake.py"
python vocabMake.py PI_0.05PS_0.9PD_0.05traindata.csv Input
python vocabMake.py PI_0.05PS_0.9PD_0.05traindata.csv phonemelabel
python vocabMake.py PI_0.05PS_0.9PD_0.05traindata.csv Noisylabel


cd ..

tar -zcvf Dataset.tar.gz Dataset

#"Input,phonemelabel,Noisylabel,Labeldata\n"

#echo "データを作成しました"
#rm /Users/pro11/Desktop/yota/Master_thesis/source/seq2seqcharacter/traindata.csv
#rm /Users/pro11/Desktop/yota/Master_thesis/source/seq2seqcharacter/testdata.csv
#rm /Users/pro11/Desktop/yota/Master_thesis/source/seq2seqcharacter/devdata.csv




#tar -zcvf xxxx.tar.gz directory
#tar -zxvf xxxx.tar.gz
#ibissftp
#put
