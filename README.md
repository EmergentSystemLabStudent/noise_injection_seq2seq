



NoiseMakeData : 
SDMと入力Vocabulary の作成に用いるコードがある。
ここでDatasetを作成

nmt:
Seq2Seqを作成


recodescript :
録音をするために作成するように


1,Datasetを作成する。
./DataMake.sh

2,学習させる
nmtを実行する。
/home/emlab/Desktop/syuuron/nmt/NTIME.sh

3,推論する。
/home/emlab/Desktop/syuuron/nmt/INFERECENTIME.sh




#下記コード例を記述


python -m nmt.nmt --src=vi --tgt=en --vocab_prefix=/tmp/nmt_data/vocab --train_prefix=/tmp/nmt_data/train --dev_prefix=/tmp/nmt_data/tst2012 --test_prefix=/tmp/nmt_data/tst2013 --out_dir=/tmp/nmt_model --num_train_steps=12000 --steps_per_stats=100 --num_layers=2 --num_units=128 --dropout=0.2 --metrics=bleu --attention_architecture=standard --attention=luong


python -m nmt.nmt --src=in --tgt=out --vocab_prefix=/home/emlab/Desktop/syuuron/nmt/Dataset/Vocab --train_prefix=/home/emlab/Desktop/syuuron/nmt/Dataset/traindata --dev_prefix=/home/emlab/Desktop/syuuron/nmt/Dataset/devdata --test_prefix=/home/emlab/Desktop/syuuron/nmt/Dataset/testdata --out_dir=/home/emlab/Desktop/syuuron/nmt/Noisy_model --num_train_steps=12000 --steps_per_stats=100 --num_layers=1 --num_units=128 --dropout=0.2 --metrics=bleu --attention_architecture=standard --attention=luong

//これがやりたいやつ
python -m nmt.nmt --src=in --tgt=out --vocab_prefix=/home/emlab/Desktop/syuuron/phonemeWordSeq2Seq/Dataset/Vocab --train_prefix=/home/emlab/Desktop/syuuron/phonemeWordSeq2Seq/Dataset/traindata --dev_prefix=/home/emlab/Desktop/syuuron/phonemeWordSeq2Seq/Dataset/devdata --test_prefix=/home/emlab/Desktop/syuuron/phonemeWordSeq2Seq/Dataset/testdata --out_dir=/home/emlab/Desktop/syuuron/phonemeWordSeq2Seq/Wordphoneme_model --num_train_steps=12000 --steps_per_stats=100 --num_layers=1 --num_units=128 --dropout=0.2 --metrics=bleu --phenome_vocab_prefix=/home/emlab/Desktop/syuuron/phonemeWordSeq2Seq/Dataset/VocabNoisylabel --phenome_train_prefix=/home/emlab/Desktop/syuuron/phonemeWordSeq2Seq/Noisytraindata --phenome_dev_prefix=/home/emlab/Desktop/syuuron/phonemeWordSeq2Seq/Dataset/Noisydevdata --phenome_test_prefix=/home/emlab/Desktop/syuuron/phonemeWordSeq2Seq/Dataset/Noisytestdata --attention_architecture=MultiInput




python -m nmt.nmt --src=in --tgt=out --vocab_prefix=/home/emlab/Desktop/syuuron/phonemeWordSeq2Seq/Dataset/Vocab --train_prefix=/home/emlab/Desktop/syuuron/phonemeWordSeq2Seq/Dataset/traindata --dev_prefix=/home/emlab/Desktop/syuuron/phonemeWordSeq2Seq/Dataset/devdata --test_prefix=/home/emlab/Desktop/syuuron/phonemeWordSeq2Seq/Dataset/testdata --out_dir=/home/emlab/Desktop/syuuron/phonemeWordSeq2Seq/Wordphoneme_model --num_train_steps=12000 --steps_per_stats=100 --num_layers=1 --num_units=128 --dropout=0.2 --metrics=bleu --phenome_vocab_prefix=/home/emlab/Desktop/syuuron/phonemeWordSeq2Seq/Dataset/VocabNoisylabel --phenome_train_prefix=/home/emlab/Desktop/syuuron/phonemeWordSeq2Seq/Noisytraindata --phenome_dev_prefix=/home/emlab/Desktop/syuuron/phonemeWordSeq2Seq/Dataset/Noisydevdata --phenome_test_prefix=/home/emlab/Desktop/syuuron/phonemeWordSeq2Seq/Dataset/Noisytestdata --attention_architecture=MultiInput

//test and word これは成功する
//これをphonemdataにしても動く
python -m nmt.nmt\
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
    --metrics=bleu --phenome_vocab_prefix=/home/emlab/Desktop/syuuron/phonemeWordSeq2Seq/Dataset/Vocab  --phenome_train_prefix=/home/emlab/Desktop/syuuron/phonemeWordSeq2Seq/Dataset/traindata --phenome_dev_prefix=/home/emlab/Desktop/syuuron/phonemeWordSeq2Seq/Dataset/devdata --phenome_test_prefix=/home/emlab/Desktop/syuuron/phonemeWordSeq2Seq/Dataset/testdata --attention_architecture=MultiInput









//ここでWordInput 

python -m nmt.nmt\
    --src=vi --tgt=en \
    --vocab_prefix=/tmp/nmt_data/vocab  \
    --train_prefix=/tmp/nmt_data/train \
    --dev_prefix=/tmp/nmt_data/tst2012  \
    --test_prefix=/tmp/nmt_data/tst2013 \
    --out_dir=/tmp/nmt_model \
    --num_train_steps=12000 \
    --steps_per_stats=100 \
    --num_layers=1 \
    --num_units=128 \
    --dropout=0.2 \
    --metrics=bleu --phenome_vocab_prefix=/tmp/nmt_data/vocab  --phenome_train_prefix=/tmp/nmt_data/train --phenome_dev_prefix=/tmp/nmt_data/tst2012 --phenome_test_prefix=/tmp/nmt_data/tst2013 --attention_architecture=MultiInput


//動く
python -m nmt.nmt --src=vi --tgt=en --vocab_prefix=/tmp/nmt_data/vocab --train_prefix=/tmp/nmt_data/train --dev_prefix=/tmp/nmt_data/tst2012 --test_prefix=/tmp/nmt_data/tst2013 --out_dir=/tmp/nmt_model --num_train_steps=12000 --steps_per_stats=100 --num_layers=1 --num_units=128 --dropout=0.2 --metrics=bleu --phenome_vocab_prefix=/tmp/nmt_data/vocab --phenome_train_prefix=/tmp/nmt_data/train --phenome_dev_prefix=/tmp/nmt_data/tst2012 --phenome_test_prefix=/tmp/nmt_data/tst2013 --attention_architecture=MultiInput





//本番用

python -m nmt.nmt --src=in --tgt=out --vocab_prefix=/home/emlab/Desktop/syuuron/phonemeWordSeq2Seq/Dataset/Vocab --train_prefix=/home/emlab/Desktop/syuuron/phonemeWordSeq2Seq/Dataset/traindata --dev_prefix=/home/emlab/Desktop/syuuron/phonemeWordSeq2Seq/Dataset/devdata --test_prefix=/home/emlab/Desktop/syuuron/phonemeWordSeq2Seq/Dataset/testdata --out_dir=/home/emlab/Desktop/syuuron/phonemeWordSeq2Seq/Wordphoneme_model --num_train_steps=12000 --steps_per_stats=100 --num_layers=1 --num_units=128 --dropout=0.2 --metrics=bleu --phenome_vocab_prefix=/home/emlab/Desktop/syuuron/phonemeWordSeq2Seq/Dataset/VocabNoisylabel --phenome_train_prefix=/home/emlab/Desktop/syuuron/phonemeWordSeq2Seq/Dataset/Noisytraindata --phenome_dev_prefix=/home/emlab/Desktop/syuuron/phonemeWordSeq2Seq/Dataset/Noisydevdata --phenome_test_prefix=/home/emlab/Desktop/syuuron/phonemeWordSeq2Seq/Dataset/Noisytestdata --attention_architecture=MultiInput


python -m nmt.nmt --src=in --tgt=out --vocab_prefix=/home/emlab/Desktop/syuuron/phonemeWordSeq2Seq/Dataset/VocabNoisylabel --train_prefix=/home/emlab/Desktop/syuuron/phonemeWordSeq2Seq/Dataset/Noisytraindata --dev_prefix=/home/emlab/Desktop/syuuron/phonemeWordSeq2Seq/Dataset/Noisydevdata --test_prefix=/home/emlab/Desktop/syuuron/phonemeWordSeq2Seq/Dataset/Noisytestdata --out_dir=/home/emlab/Desktop/syuuron/phonemeWordSeq2Seq/Wordphoneme_model --num_train_steps=12000 --steps_per_stats=100 --num_layers=1 --num_units=128 --dropout=0.2 --metrics=bleu --phenome_vocab_prefix=/home/emlab/Desktop/syuuron/phonemeWordSeq2Seq/Dataset/Vocab --phenome_train_prefix=/home/emlab/Desktop/syuuron/phonemeWordSeq2Seq/Dataset/traindata --phenome_dev_prefix=/home/emlab/Desktop/syuuron/phonemeWordSeq2Seq/Dataset/devdata --phenome_test_prefix=/home/emlab/Desktop/syuuron/phonemeWordSeq2Seq/Dataset/testdata --attention_architecture=MultiInput

#実験音声データの場合WAN





./nmt/scripts/download_iwslt15.sh /tmp/nmt_data 

時系列データの長さをチェックする


//tensorboardによる
tensorboard --logdir=train_log/ --host=127.0.0.1



#run_decodeをみていく



#nmtの場合 GG
python -m nmt.nmt \
    --out_dir=/home/emlab/Desktop/syuuron/nmt/ \
　　　　--vocab_prefix=/tmp/nmt_data/vocab \
    --inference_input_file=/tmp/my_infer_file.vi \
    --inference_output_file=/tmp/nmt_model/output_inferData \
    --metrics=bleu \
    --attention_architecture=MultiInput



#WANGの結果
python -m nmt.nmt --src=in --tgt=out --vocab_prefix=/home/emlab/Desktop/syuuron/phonemeWordSeq2Seq/Dataset/VocabNoisylabel --train_prefix=/home/emlab/Desktop/syuuron/phonemeWordSeq2Seq/Dataset/Noisytraindata --dev_prefix=/home/emlab/Desktop/syuuron/phonemeWordSeq2Seq/Dataset/Noisydevdata --test_prefix=/home/emlab/Desktop/syuuron/phonemeWordSeq2Seq/Dataset/Noisytestdata --out_dir=/home/emlab/Desktop/syuuron/phonemeWordSeq2Seq/Wordphoneme_model --num_train_steps=12000 --steps_per_stats=100 --num_layers=1 --num_units=128 --dropout=0.2 --metrics=bleu --phenome_vocab_prefix=/home/emlab/Desktop/syuuron/phonemeWordSeq2Seq/Dataset/Vocab --phenome_train_prefix=/home/emlab/Desktop/syuuron/phonemeWordSeq2Seq/Dataset/traindata --phenome_dev_prefix=/home/emlab/Desktop/syuuron/phonemeWordSeq2Seq/Dataset/devdata --phenome_test_prefix=/home/emlab/Desktop/syuuron/phonemeWordSeq2Seq/Dataset/testdata --attention_architecture=MultiInput




#WANGの結

python -m nmt.nmt --src=in --tgt=out --vocab_prefix=/home/emlab/Desktop/syuuron/nmt/Dataset/Vocab --train_prefix=/home/emlab/Desktop/syuuron/nmt/Dataset/traindata --dev_prefix=/home/emlab/Desktop/syuuron/nmt/Dataset/devdata --test_prefix=/home/emlab/Desktop/syuuron/recodescript/${data}/google_phonemeresultdata --out_dir=/home/emlab/Desktop/syuuron/nmt/attention_${var}_model --num_train_steps=12000 --steps_per_stats=100 --num_layers=1 --num_units=128 --dropout=0.2 --metrics=bleu --attention_architecture=standard --attention=luong

















