#!/bin/zsh
#学習時スクリプト

hoge=("Noisy")

noisedata=("PI_0.0PS_0.0PD_0.0PS_S1.0" "PI_0.1PS_0.1PD_0.1PS_S0.7" "PI_0.2PS_0.2PD_0.2PS_S0.4" "PI_0.3PS_0.3PD_0.3PS_S0.1")


i=1
while ((i < 10))
do
  cd Dataset
  echo $i
  i=$(( i + 1 )) 
  for noise in ${noisedata[@]}
  do
    for var in ${hoge[@]}
    do
      echo "Data"$var >> log.txt 
      echo `./datasetMake.sh $var $noise`
      cd ..
      python -m nmt.nmt --src=in --tgt=out --vocab_prefix=/home/emlab/Desktop/syuuron/nmt/Dataset/Vocab --train_prefix=/home/emlab/Desktop/syuuron/nmt/Dataset/traindata --dev_prefix=/home/emlab/Desktop/syuuron/nmt/Dataset/devdata --test_prefix=/home/emlab/Desktop/syuuron/recodescript/WANGDATA/google_phonemeresultdata --out_dir=/home/emlab/Desktop/syuuron/nmt/Noattention_${noise}_${var}_model --num_train_steps=12000 --steps_per_stats=100 --num_layers=1 --num_units=128 --dropout=0.2 --metrics=bleu --attention_architecture=standard 
      echo Noattention_${noise}_${var}_model >> log.txt
      echo attention_${noise}_${var}_model >> log.txt
      cd Dataset
    done
  done
  cd /home/emlab/Desktop/syuuron/nmt
  test=`date '+%F_%H'`
  echo $test
  mkdir $test
  mv *attention* $test
done


