#!/bin/bash
#SBATCH --partition=SCSEGPU_M2
#SBATCH --qos=q_dmsai 
#SBATCH --nodes=1 
#SBATCH --gres=gpu:1
#SBATCH --mem=30G
#SBATCH --c 10

cd ../
python train.py