#!/bin/zsh
cp /nmt/Noattention_${noise}_${var}_model/output_test\
   /nmt/DataResult/Noattention_${var}_model_${data}_sphinx_infer
rm ~/Desktop/syuuron/nmt/Noattention_${noise}_${var}_model/hparams
  
python -m nmt.nmt --src=in --tgt=out\
      --vocab_prefix=/Dataset/Vocab\
      --train_prefix=/Dataset/traindata\
      --dev_prefix=/Dataset/devdata\
      --test_prefix=google_phonemeresultdata\
      --out_dir=/Noattention_${noise}_${var}_model\
      --num_train_steps=12000 --steps_per_stats=100\
      --num_layers=1 --num_units=128 --dropout=0.2 --metrics=bleu --attention_architecture=standard 

cp ~/Desktop/syuuron/nmt/Noattention_${noise}_${var}_model/output_test\
   ~/Desktop/syuuron/nmt/DataResult/Noattention_${var}_model_${data}_google_infer

cp ~/Desktop/syuuron/nmt/attention_${noise}_${var}_model/output_test\
   ~/Desktop/syuuron/nmt/DataResult/attention_${var}_model_${data}_sphinx_infer
cp ~/Desktop/syuuron/nmt/attention_${noise}_${var}_model/output_test\
   ~/Desktop/syuuron/nmt/DataResult/attention_${noise}_${var}_model_${data}_google_infer

rm ~/Desktop/syuuron/nmt/attention_${noise}_${var}_model/hparams   

  


python Resultsummary.py $data

