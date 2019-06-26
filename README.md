# noise_injection_seq2seq


# Overview



# contents


# Experiments
## Experiment 1
### Experimental procedure
 - 1. Prepare GPSRDATA
 - 2. Make "original" Dataset
 
     `./MakeoriginalDataset.sh`
 - 3. Make "edited" Dataset (Ineject Noise)
 
     `./MakeSDM.sh`
 - 4. Prepare Utterance Data
   - 1. Speech Recognition
 
     `./SpeechRecognition.sh`
 - 5. Learning
 - 6. Inference
### condition
- 隠れ層 : 1層,128次元
- ドロップアウト確率 : 0.2
    
## Experiment 2
### Experimental procedure
### condition


`python -m nmt.nmt --src=in --tgt=out\
--vocab_prefix=/path/to/Dataset/Vocab\
--train_prefix=/path/to/Dataset/traindata\
--dev_prefix=/path/to/Dataset/devdata\
--test_prefix=/path/to/Dataset/testdata\
--out_dir=/path/to/Noisy_model\
--num_train_steps=12000 --steps_per_stats=100 --num_layers=1 --num_units=128 --dropout=0.2 --metrics=bleu\
--attention_architecture=standard --attention=luong`

`python -m nmt.nmt --src=in --tgt=out\
--vocab_prefix=/home/emlab/Desktop/syuuron/phonemeWordSeq2Seq/Dataset/Vocab\
--train_prefix=/home/emlab/Desktop/syuuron/phonemeWordSeq2Seq/Dataset/traindata\
--dev_prefix=/home/emlab/Desktop/syuuron/phonemeWordSeq2Seq/Dataset/devdata\
--test_prefix=/home/emlab/Desktop/syuuron/phonemeWordSeq2Seq/Dataset/testdata\
--out_dir=/home/emlab/Desktop/syuuron/phonemeWordSeq2Seq/Wordphoneme_model\
--num_train_steps=12000 --steps_per_stats=100 --num_layers=1 --num_units=128 --dropout=0.2 --metrics=bleu\
--phenome_vocab_prefix=/home/emlab/Desktop/syuuron/phonemeWordSeq2Seq/Dataset/VocabNoisylabel
--phenome_train_prefix=/home/emlab/Desktop/syuuron/phonemeWordSeq2Seq/Noisytraindata\
--phenome_dev_prefix=/home/emlab/Desktop/syuuron/phonemeWordSeq2Seq/Dataset/Noisydevdata\
--phenome_test_prefix=/home/emlab/Desktop/syuuron/phonemeWordSeq2Seq/Dataset/Noisytestdata\
--attention_architecture=MultiInput`

`python -m nmt.nmt --src=in --tgt=out --vocab_prefix=/home/emlab/Desktop/syuuron/phonemeWordSeq2Seq/Dataset/Vocab --train_prefix=/home/emlab/Desktop/syuuron/phonemeWordSeq2Seq/Dataset/traindata --dev_prefix=/home/emlab/Desktop/syuuron/phonemeWordSeq2Seq/Dataset/devdata --test_prefix=/home/emlab/Desktop/syuuron/phonemeWordSeq2Seq/Dataset/testdata --out_dir=/home/emlab/Desktop/syuuron/phonemeWordSeq2Seq/Wordphoneme_model --num_train_steps=12000 --steps_per_stats=100 --num_layers=1 --num_units=128 --dropout=0.2 --metrics=bleu --phenome_vocab_prefix=/home/emlab/Desktop/syuuron/phonemeWordSeq2Seq/Dataset/VocabNoisylabel --phenome_train_prefix=/home/emlab/Desktop/syuuron/phonemeWordSeq2Seq/Noisytraindata --phenome_dev_prefix=/home/emlab/Desktop/syuuron/phonemeWordSeq2Seq/Dataset/Noisydevdata --phenome_test_prefix=/home/emlab/Desktop/syuuron/phonemeWordSeq2Seq/Dataset/Noisytestdata --attention_architecture=MultiInput`

`python -m nmt.nmt\
    --src=in --tgt=en \
    --vocab_prefix=/tmp/nmt_data/vocab  \
    --train_prefix=/tmp/nmt_data/train \
    --dev_prefix=/tmp/nmt_data/tst2012  \
    --test_prefix=/tmp/nmt_data/tst2013 \
    --out_dir=/home/emlab/Desktop/syuuron/phonemeWordSeq2Seq/Wordphoneme_model \
    --num_train_steps=12000 \
    --steps_per_stats=100 \
    --num_layers=1 \
    --num_units=128 \
    --dropout=0.2 \
    --metrics=bleu --phenome_vocab_prefix=/home/emlab/Desktop/syuuron/phonemeWordSeq2Seq/Dataset/Vocab \
    --phenome_train_prefix=/home/emlab/Desktop/syuuron/phonemeWordSeq2Seq/Dataset/traindata \
    --phenome_dev_prefix=/home/emlab/Desktop/syuuron/phonemeWordSeq2Seq/Dataset/devdata \
    --phenome_test_prefix=/home/emlab/Desktop/syuuron/phonemeWordSeq2Seq/Dataset/testdata \
    --attention_architecture=MultiInput`


`python -m nmt.nmt --src=in --tgt=out --vocab_prefix=/home/emlab/Desktop/syuuron/phonemeWordSeq2Seq/Dataset/Vocab --train_prefix=/home/emlab/Desktop/syuuron/phonemeWordSeq2Seq/Dataset/traindata --dev_prefix=/home/emlab/Desktop/syuuron/phonemeWordSeq2Seq/Dataset/devdata --test_prefix=/home/emlab/Desktop/syuuron/phonemeWordSeq2Seq/Dataset/testdata --out_dir=/home/emlab/Desktop/syuuron/phonemeWordSeq2Seq/Wordphoneme_model --num_train_steps=12000 --steps_per_stats=100 --num_layers=1 --num_units=128 --dropout=0.2 --metrics=bleu --phenome_vocab_prefix=/home/emlab/Desktop/syuuron/phonemeWordSeq2Seq/Dataset/VocabNoisylabel --phenome_train_prefix=/home/emlab/Desktop/syuuron/phonemeWordSeq2Seq/Dataset/Noisytraindata --phenome_dev_prefix=/home/emlab/Desktop/syuuron/phonemeWordSeq2Seq/Dataset/Noisydevdata --phenome_test_prefix=/home/emlab/Desktop/syuuron/phonemeWordSeq2Seq/Dataset/Noisytestdata --attention_architecture=MultiInput`

`python -m nmt.nmt --src=in --tgt=out --vocab_prefix=/home/emlab/Desktop/syuuron/phonemeWordSeq2Seq/Dataset/VocabNoisylabel --train_prefix=/home/emlab/Desktop/syuuron/phonemeWordSeq2Seq/Dataset/Noisytraindata --dev_prefix=/home/emlab/Desktop/syuuron/phonemeWordSeq2Seq/Dataset/Noisydevdata --test_prefix=/home/emlab/Desktop/syuuron/phonemeWordSeq2Seq/Dataset/Noisytestdata --out_dir=/home/emlab/Desktop/syuuron/phonemeWordSeq2Seq/Wordphoneme_model --num_train_steps=12000 --steps_per_stats=100 --num_layers=1 --num_units=128 --dropout=0.2 --metrics=bleu --phenome_vocab_prefix=/home/emlab/Desktop/syuuron/phonemeWordSeq2Seq/Dataset/Vocab --phenome_train_prefix=/home/emlab/Desktop/syuuron/phonemeWordSeq2Seq/Dataset/traindata --phenome_dev_prefix=/home/emlab/Desktop/syuuron/phonemeWordSeq2Seq/Dataset/devdata --phenome_test_prefix=/home/emlab/Desktop/syuuron/phonemeWordSeq2Seq/Dataset/testdata --attention_architecture=MultiInput`




- nmt GG
`python -m nmt.nmt \
   --out_dir=/home/emlab/Desktop/syuuron/nmt/ \
 　--vocab_prefix=/tmp/nmt_data/vocab \
   --inference_input_file=/tmp/my_infer_file.vi \
   --inference_output_file=/tmp/nmt_model/output_inferData \
   --metrics=bleu \
   --attention_architecture=MultiInput`

 
`python -m nmt.nmt \
--src=in --tgt=out \
--vocab_prefix=/home/emlab/Desktop/syuuron/phonemeWordSeq2Seq/Dataset/VocabNoisylabel \
--train_prefix=/home/emlab/Desktop/syuuron/phonemeWordSeq2Seq/Dataset/Noisytraindata \
--dev_prefix=/home/emlab/Desktop/syuuron/phonemeWordSeq2Seq/Dataset/Noisydevdata \
--test_prefix=/home/emlab/Desktop/syuuron/phonemeWordSeq2Seq/Dataset/Noisytestdata \
--out_dir=/home/emlab/Desktop/syuuron/phonemeWordSeq2Seq/Wordphoneme_model \
--num_train_steps=12000 \
--steps_per_stats=100 \
--num_layers=1 \
--num_units=128 \
--dropout=0.2 \
--metrics=bleu \
--phenome_vocab_prefix=/home/emlab/Desktop/syuuron/phonemeWordSeq2Seq/Dataset/Vocab \
--phenome_train_prefix=/home/emlab/Desktop/syuuron/phonemeWordSeq2Seq/Dataset/traindata \
--phenome_dev_prefix=/home/emlab/Desktop/syuuron/phonemeWordSeq2Seq/Dataset/devdata \
--phenome_test_prefix=/home/emlab/Desktop/syuuron/phonemeWordSeq2Seq/Dataset/testdata \
--attention_architecture=MultiInput`

`python -m nmt.nmt \
--src=in \
--tgt=out \
--vocab_prefix=/home/emlab/Desktop/syuuron/nmt/Dataset/Vocab \
--train_prefix=/home/emlab/Desktop/syuuron/nmt/Dataset/traindata \
--dev_prefix=/home/emlab/Desktop/syuuron/nmt/Dataset/devdata \
--test_prefix=/home/emlab/Desktop/syuuron/recodescript/${data}/google_phonemeresultdata \
--out_dir=/home/emlab/Desktop/syuuron/nmt/attention_${var}_model \
--num_train_steps=12000 \
--steps_per_stats=100 \
--num_layers=1 \
--num_units=128 \
--dropout=0.2 \
--metrics=bleu \
--attention_architecture=standard \
--attention=luong`
    
# Main Contributors
 - Yuki Tada (ex-student of Ritsumeikan University)
# maintainor
 - Hiroki Tanaka (assistant researcher of Ritsumeikan University)
