#!/bin/zsh
#python -m nmt.nmt \
#    --src=in --tgt=out \
#    --vocab_prefix=./Dataset/ex2/rho=0.05/vocab  \
#    --train_prefix=./Dataset/ex2/rho=0.05/train \
#    --dev_prefix=./Dataset/ex2/rho=0.05/dev  \
#    --test_prefix=./Dataset/ex2/rho=0.05/test \
#    --out_dir=./Models/ex2/rho=0.05 \
#    --num_train_steps=12000 \
#    --steps_per_stats=100 \
#    --num_layers=2 \
#    --num_units=128 \
#    --dropout=0.2 \
#    --metrics=bleu\

python -m nmt.nmt \
    --src=in --tgt=out \
    --vocab_prefix=./Dataset/ex2/rho=0.0/vocab  \
    --train_prefix=./Dataset/ex2/rho=0.0/train \
    --dev_prefix=./Dataset/ex2/rho=0.0/dev  \
    --test_prefix=./Dataset/ex2/rho=0.0/test \
    --out_dir=./Models/ex2/rho=0.0 \
    --num_train_steps=12000 \
    --steps_per_stats=100 \
    --num_layers=2 \
    --num_units=128 \
    --dropout=0.2 \
    --metrics=bleu\

#python -m nmt.nmt \
#    --src=in --tgt=out \
#    --vocab_prefix=./Dataset/ex2/rho=0.15/vocab  \
#    --train_prefix=./Dataset/ex2/rho=0.15/train \
#    --dev_prefix=./Dataset/ex2/rho=0.15/dev  \
#    --test_prefix=./Dataset/ex2/rho=0.15/test \
#    --out_dir=./Models/ex2/rho=0.15 \
#    --num_train_steps=12000 \
#    --steps_per_stats=100 \
#    --num_layers=2 \
#    --num_units=128 \
#    --dropout=0.2 \
#    --metrics=bleu\

#python -m nmt.nmt \
#    --src=in --tgt=out \
#    --vocab_prefix=./Dataset/ex2/rho=0.2/vocab  \
#    --train_prefix=./Dataset/ex2/rho=0.2/train \
#    --dev_prefix=./Dataset/ex2/rho=0.2/dev  \
#    --test_prefix=./Dataset/ex2/rho=0.2/test \
#    --out_dir=./Models/ex2/rho=0.2 \
#    --num_train_steps=12000 \
#    --steps_per_stats=100 \
#    --num_layers=2 \
#    --num_units=128 \
#    --dropout=0.2 \
#    --metrics=bleu\

#    python -m nmt.nmt \
#    --src=in --tgt=out \
#    --vocab_prefix=./Dataset/ex2/rho=0.25/vocab  \
#    --train_prefix=./Dataset/ex2/rho=0.25/train \
#    --dev_prefix=./Dataset/ex2/rho=0.25/dev  \
#    --test_prefix=./Dataset/ex2/rho=0.25/test \
#    --out_dir=./Models/ex2/rho=0.25 \
#    --num_train_steps=12000 \
#    --steps_per_stats=100 \
#    --num_layers=2 \
#    --num_units=128 \
#    --dropout=0.2 \
#    --metrics=bleu\

#python -m nmt.nmt \
#    --src=in --tgt=out \
#    --vocab_prefix=./Dataset/ex2/rho=0.3/vocab  \
#    --train_prefix=./Dataset/ex2/rho=0.3/train \
#    --dev_prefix=./Dataset/ex2/rho=0.3/dev  \
#    --test_prefix=./Dataset/ex2/rho=0.3/test \
#    --out_dir=./Models/ex2/rho=0.3 \
#    --num_train_steps=12000 \
#    --steps_per_stats=100 \
#    --num_layers=2 \
#    --num_units=128 \
#    --dropout=0.2 \
#    --metrics=bleu\




    


