
echo "SDM.py"

python SDM.py ./Dataset/ ./OriginalDataset/ traindata.csv 0.0
python SDM.py ./Dataset/ ./OriginalDataset/ traindata.csv 0.05
python SDM.py ./Dataset/ ./OriginalDataset/ traindata.csv 0.1
python SDM.py ./Dataset/ ./OriginalDataset/ traindata.csv 0.15
python SDM.py ./Dataset/ ./OriginalDataset/ traindata.csv 0.2
python SDM.py ./Dataset/ ./OriginalDataset/ traindata.csv 0.25
python SDM.py ./Dataset/ ./OriginalDataset/ traindata.csv 0.3

python SDM.py ./Dataset/ ./OriginalDataset/ devdata.csv 0.0
python SDM.py ./Dataset/ ./OriginalDataset/ devdata.csv 0.05
python SDM.py ./Dataset/ ./OriginalDataset/ devdata.csv 0.1
python SDM.py ./Dataset/ ./OriginalDataset/ devdata.csv 0.15
python SDM.py ./Dataset/ ./OriginalDataset/ devdata.csv 0.2
python SDM.py ./Dataset/ ./OriginalDataset/ devdata.csv 0.25
python SDM.py ./Dataset/ ./OriginalDataset/ devdata.csv 0.3

python SDM.py ./Dataset/ ./OriginalDataset/ testdata.csv 0.0
python SDM.py ./Dataset/ ./OriginalDataset/ testdata.csv 0.05
python SDM.py ./Dataset/ ./OriginalDataset/ testdata.csv 0.1
python SDM.py ./Dataset/ ./OriginalDataset/ testdata.csv 0.15
python SDM.py ./Dataset/ ./OriginalDataset/ testdata.csv 0.2
python SDM.py ./Dataset/ ./OriginalDataset/ testdata.csv 0.25
python SDM.py ./Dataset/ ./OriginalDataset/ testdata.csv 0.3


