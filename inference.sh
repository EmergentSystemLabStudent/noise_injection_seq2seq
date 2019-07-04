#!/bin/zsh
  
python -m nmt.nmt --src=in --tgt=out\
      --vocab_prefix=/Dataset/Vocab\
      --train_prefix=/Dataset/traindata\
      --dev_prefix=/Dataset/devdata\
      --test_prefix=google_phonemeresultdata\
      --out_dir=/Noattention_${noise}_${var}_model\
      --num_train_steps=12000 --steps_per_stats=100\
      --num_layers=1 --num_units=128 --dropout=0.2 --metrics=bleu --attention_architecture=standard 

python Resultsummary.py $data

