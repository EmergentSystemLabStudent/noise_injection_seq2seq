#!/bin/zsh
    
python -m nmt.nmt \
    --src=in --tgt=out \
    --vocab_prefix=./Dataset/ex1/rho=0.1/vocab  \
    --train_prefix=./Dataset/ex1/rho=0.1/train \
    --dev_prefix=./Dataset/ex1/rho=0.1/dev  \
    --test_prefix=./Dataset/ex1/rho=0.1/test \
    --out_dir=./Models/ex1/rho=0.1 \
    --num_train_steps=12000 \
    --steps_per_stats=100 \
    --num_layers=2 \
    --num_units=128 \
    --dropout=0.2 \
    --metrics=bleu\
    --attention=luong



    


