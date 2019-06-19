#!/bin/zsh
hoge=()
datas=()
noisedata=()
cd Dataset
for data in ${datas[@]}
do
  for var in ${hoge[@]}
  do
    for noise in ${noisedata[@]}
    do
      cp ~/Desktop/syuuron/nmt/Noattention_${noise}_${var}_model/output_test ~/Desktop/syuuron/nmt/DataResult/Noattention_${var}_model_${data}_sphinx_infer

      rm ~/Desktop/syuuron/nmt/Noattention_${noise}_${var}_model/hparams
  
      python -m nmt.nmt --src=in --tgt=out\
      --vocab_prefix=/home/emlab/Desktop/syuuron/nmt/Dataset/Vocab\
      --train_prefix=/home/emlab/Desktop/syuuron/nmt/Dataset/traindata\
      --dev_prefix=/home/emlab/Desktop/syuuron/nmt/Dataset/devdata\
      --test_prefix=/home/emlab/Desktop/syuuron/recodescript/${data}/google_phonemeresultdata\
      --out_dir=/home/emlab/Desktop/syuuron/nmt/Noattention_${noise}_${var}_model\
      --num_train_steps=12000 --steps_per_stats=100\
      --num_layers=1 --num_units=128 --dropout=0.2 --metrics=bleu --attention_architecture=standard 

      cp ~/Desktop/syuuron/nmt/Noattention_${noise}_${var}_model/output_test ~/Desktop/syuuron/nmt/DataResult/Noattention_${var}_model_${data}_google_infer

      echo Noattention_${noise}_${var}_model >> log.txt
      rm ~/Desktop/syuuron/nmt/attention_${noise}_${var}_model/hparams   
      rm ~/Desktop/syuuron/nmt/attention_${noise}_${var}_model/hparams
  
      cp ~/Desktop/syuuron/nmt/attention_${noise}_${var}_model/output_test ~/Desktop/syuuron/nmt/DataResult/attention_${var}_model_${data}_sphinx_infer
      cp ~/Desktop/syuuron/nmt/attention_${noise}_${var}_model/output_test ~/Desktop/syuuron/nmt/DataResult/attention_${noise}_${var}_model_${data}_google_infer
      echo attention_${var}_model >> log.txt
      cd Dataset
    done
  done
  cd /home/emlab/Desktop/syuuron/nmt
  python Resultsummary.py $data
  cd Dataset
done
