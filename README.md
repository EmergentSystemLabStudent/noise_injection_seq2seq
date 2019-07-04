# noise_injection_seq2seq


# Overview



# contents


# Experiments
## Experiment 1
### Experimental procedure
 - 1. Prepare GPSRDATA
 - 2. Make "original" Dataset
 
     `./MakeoriginalDataset.sh`
     
     - `./OriginalDataset/test.csv`
     - `./OriginalDataset/dev.csv`
     - `./OriginalDataset/train.csv`
 - 3. Make "edited" Dataset (Ineject Noise)
 
     `./MakeSDM.sh`
     - `./Dataset/train/rho=<noise_level>_edited_phoneme.in`
     - `./Dataset/train/original_sentence.in`
     - `./Dataset/train/phoneme.in`
     - `./Dataset/train/label.out`
     - `./Dataset/dev/rho=<noise_level>_edited_phoneme.in`
     - `./Dataset/dev/original_sentence.in`
     - `./Dataset/dev/phoneme.in`
     - `./Dataset/dev/label.out`

 - 4. Prepare Utterance Data
   - 1. Speech Recognition
 
     `./SpeechRecognition.sh`
 - 5. Learning
 
 `python -m nmt.nmt --src=in --tgt=out\
--vocab_prefix=/path/to/Dataset/Vocab\
--train_prefix=/path/to/Dataset/traindata\
--dev_prefix=/path/to/Dataset/devdata\
--test_prefix=/path/to/Dataset/testdata\
--out_dir=/path/to/Noisy_model\
--num_train_steps=12000 --steps_per_stats=100 --num_layers=1 --num_units=128 --dropout=0.2 --metrics=bleu\
--attention_architecture=standard --attention=luong`

 - 6. Inference
### condition
- 隠れ層 : 1層,128次元
- ドロップアウト確率 : 0.2
    
## Experiment 2
### Experimental procedure
### condition



# Main Contributors
 - Yuki Tada (ex-student of Ritsumeikan University)
# maintainor
 - Hiroki Tanaka (assistant researcher of Ritsumeikan University)
