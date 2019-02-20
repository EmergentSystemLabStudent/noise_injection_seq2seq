
echo "SDM.py"
python SDM.py testdata.csv || echo "SDM.py testdata.csv 失敗しました"
python SDM.py traindata.csv || echo "SDM.py traindata.csv 失敗しました"
python SDM.py devdata.csv || echo "SDM.py testdata.csv 失敗しました"

echo "vocabMakeを始めます"
echo "vocabMake.py"
python vocabMake.py traindata.csv Input
python vocabMake.py traindata.csv phonemelabel
python vocabMake.py traindata.csv Noisylabel




#"Input,phonemelabel,Noisylabel,Labeldata\n"
#echo "データを作成しました"
#rm /Users/pro11/Desktop/yota/Master_thesis/source/seq2seqcharacter/traindata.csv
#rm /Users/pro11/Desktop/yota/Master_thesis/source/seq2seqcharacter/testdata.csv
#rm /Users/pro11/Desktop/yota/Master_thesis/source/seq2seqcharacter/devdata.csv


#echo "データを消去しました"
#cp /Users/pro11/Desktop/yota/Master_thesis/source/NoiseMakeData/Resulttestdata/testdata.csv /Users/pro11/Desktop/yota/Master_thesis/source/seq2seqcharacter/
#cp /Users/pro11/Desktop/yota/Master_thesis/source/NoiseMakeData/Resulttraindata/traindata.csv /Users/pro11/Desktop/yota/Master_thesis/source/seq2seqcharacter/
#echo "データを移動しました"

#tar -zcvf xxxx.tar.gz directory
#tar -zxvf xxxx.tar.gz
