if [ $# -ne 2 ]; then
  echo "実行するには2個の引数が必要です。" 
  exit 1
fi

cp -f VocabNoisylabel.in Vocabphonemelabel.in

rm devdata.in devdata.out  testdata.in  testdata.out traindata.in  traindata.out Vocab.in  
cp $2$1devdata.in devdata.in
echo $2$1 
cp $2$1traindata.in traindata.in

cp Noisytestdata.in testdata.in

cp labeldevdata.out devdata.out

cp labeltraindata.out traindata.out

cp labeltestdata.out testdata.out

cp Vocab$1.in   Vocab.in || cp Vocab$1label.in Vocab.in

echo $2$1

