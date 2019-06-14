
echo "SDM.py"
#python SDM.py testdata.csv || echo "SDM.py testdata.csv failed"
python SDM.py ./Dataset/ ./OriginalDataset/ traindata.csv || echo "SDM.py traindata.csv failed"
#python SDM.py devdata.csv || echo "SDM.py testdata.csv failed"

