#!/bin/zsh
hoge=("Noisy")
datas=("WANGDATA","YOTA","LiuDATA","WANGDATA")
noisedata=("PI_0.0PS_0.0PD_0.0PS_S1.0" "PI_0.1PS_0.1PD_0.1PS_S0.7" "PI_0.2PS_0.2PD_0.2PS_S0.4" "PI_0.3PS_0.3PD_0.3PS_S0.1")
cd Dataset
for data in ${datas[@]}
do
for var in ${hoge[@]}
do
for noise in ${noisedata[@]}
do


  echo "わぁ"$var >> log.txt 
  echo `./datasetMake.sh $var $noise`
  cd ..
  rm ~/Desktop/syuuron/nmt/Noattention_${noise}_${var}_model/hparams

  #python -m nmt.nmt --src=in --tgt=out --vocab_prefix=/home/emlab/Desktop/syuuron/nmt/Dataset/Vocab --train_prefix=/home/emlab/Desktop/syuuron/nmt/Dataset/traindata --dev_prefix=/home/emlab/Desktop/syuuron/nmt/Dataset/devdata --test_prefix=/home/emlab/Desktop/syuuron/recodescript/${data}/sphinx_wordresultdata --out_dir=/home/emlab/Desktop/syuuron/nmt/Noattention_${noise}_${var}_model --num_train_steps=12000 --steps_per_stats=100 --num_layers=1 --num_units=128 --dropout=0.2 --metrics=bleu --attention_architecture=standard 


  cp ~/Desktop/syuuron/nmt/Noattention_${noise}_${var}_model/output_test ~/Desktop/syuuron/nmt/DataResult/Noattention_${var}_model_${data}_sphinx_infer

  rm ~/Desktop/syuuron/nmt/Noattention_${noise}_${var}_model/hparams
  
python -m nmt.nmt --src=in --tgt=out --vocab_prefix=/home/emlab/Desktop/syuuron/nmt/Dataset/Vocab --train_prefix=/home/emlab/Desktop/syuuron/nmt/Dataset/traindata --dev_prefix=/home/emlab/Desktop/syuuron/nmt/Dataset/devdata --test_prefix=/home/emlab/Desktop/syuuron/recodescript/${data}/google_phonemeresultdata --out_dir=/home/emlab/Desktop/syuuron/nmt/Noattention_${noise}_${var}_model --num_train_steps=12000 --steps_per_stats=100 --num_layers=1 --num_units=128 --dropout=0.2 --metrics=bleu --attention_architecture=standard 

  cp ~/Desktop/syuuron/nmt/Noattention_${noise}_${var}_model/output_test ~/Desktop/syuuron/nmt/DataResult/Noattention_${var}_model_${data}_google_infer

  echo Noattention_${noise}_${var}_model >> log.txt
  rm ~/Desktop/syuuron/nmt/attention_${noise}_${var}_model/hparams

  #python -m nmt.nmt --src=in --tgt=out --vocab_prefix=/home/emlab/Desktop/syuuron/nmt/Dataset/Vocab --train_prefix=/home/emlab/Desktop/syuuron/nmt/Dataset/traindata --dev_prefix=/home/emlab/Desktop/syuuron/nmt/Dataset/devdata --test_prefix=/home/emlab/Desktop/syuuron/recodescript/${data}/google_Wordresultdata --out_dir=/home/emlab/Desktop/syuuron/nmt/attention_${noise}_${var}_model --num_train_steps=12000 --steps_per_stats=100 --num_layers=1 --num_units=128 --dropout=0.2 --metrics=bleu --attention_architecture=standard --attention=luong

  rm ~/Desktop/syuuron/nmt/attention_${noise}_${var}_model/hparams
  
  cp ~/Desktop/syuuron/nmt/attention_${noise}_${var}_model/output_test ~/Desktop/syuuron/nmt/DataResult/attention_${var}_model_${data}_sphinx_infer

  #python -m nmt.nmt --src=in --tgt=out --vocab_prefix=/home/emlab/Desktop/syuuron/nmt/Dataset/Vocab --train_prefix=/home/emlab/Desktop/syuuron/nmt/Dataset/traindata --dev_prefix=/home/emlab/Desktop/syuuron/nmt/Dataset/devdata --test_prefix=/home/emlab/Desktop/syuuron/recodescript/${data}/google_phonemeresultdata --out_dir=/home/emlab/Desktop/syuuron/nmt/attention_${noise}_${var}_model --num_train_steps=12000 --steps_per_stats=100 --num_layers=1 --num_units=128 --dropout=0.2 --metrics=bleu --attention_architecture=standard --attention=luong

  cp ~/Desktop/syuuron/nmt/attention_${noise}_${var}_model/output_test ~/Desktop/syuuron/nmt/DataResult/attention_${noise}_${var}_model_${data}_google_infer
  echo attention_${var}_model >> log.txt
  cd Dataset
done
done
cd /home/emlab/Desktop/syuuron/nmt
python Resultsummary.py $data
cd Dataset
done

#cd /home/emlab/Desktop/syuuron/phonemeWordSeq2Seq
#python -m nmt.nmt --src=in --tgt=out --vocab_prefix=/home/emlab/Desktop/syuuron/phonemeWordSeq2Seq/Dataset/Vocab --train_prefix=/home/emlab/Desktop/syuuron/phonemeWordSeq2Seq/Dataset/traindata --dev_prefix=/home/emlab/Desktop/syuuron/phonemeWordSeq2Seq/Dataset/devdata --test_prefix=/home/emlab/Desktop/syuuron/phonemeWordSeq2Seq/Dataset/testdata --out_dir=/home/emlab/Desktop/syuuron/phonemeWordSeq2Seq/Wordphoneme_model --num_train_steps=12000 --steps_per_stats=100 --num_layers=1 --num_units=128 --dropout=0.2 --metrics=bleu --phenome_vocab_prefix=/home/emlab/Desktop/syuuron/phonemeWordSeq2Seq/Dataset/VocabNoisylabel --phenome_train_prefix=/home/emlab/Desktop/syuuron/phonemeWordSeq2Seq/Noisytraindata --phenome_dev_prefix=/home/emlab/Desktop/syuuron/phonemeWordSeq2Seq/Dataset/Noisydevdata --phenome_test_prefix=/home/emlab/Desktop/syuuron/phonemeWordSeq2Seq/Dataset/Noisytestdata --num_gpus=1 --attention_architecture=MultiInput
