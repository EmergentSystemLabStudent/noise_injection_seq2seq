#!/bin/zsh
python -m nmt.nmt \
    --src=in --tgt=out \
    --vocab_prefix=./Dataset/ex2/rho=0.05/vocab  \
    --train_prefix=./Dataset/ex2/rho=0.05/train \
    --dev_prefix=./Dataset/ex2/rho=0.05/dev  \
    --test_prefix=./Dataset/ex2/rho=0.05/test \
    --out_dir=./Models/ex2/rho=0.05 \
    --num_train_steps=12000 \
    --steps_per_stats=100 \
    --num_layers=2 \
    --num_units=128 \
    --dropout=0.2 \
    --metrics=bleu\
    




    


