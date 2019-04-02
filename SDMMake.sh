
echo "SDM.py"
python SDM.py testdata.csv || echo "SDM.py testdata.csv failed"
python SDM.py traindata.csv || echo "SDM.py traindata.csv failed"
python SDM.py devdata.csv || echo "SDM.py testdata.csv failed"

echo "start vocabMake"
echo "vocabMake.py"
python vocabMake.py traindata.csv Input
python vocabMake.py traindata.csv phonemelabel
python vocabMake.py traindata.csv Noisylabel
