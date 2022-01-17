import os
import shutil

DATASET_PATH = '/content/drive/MyDrive/NTU - Speech Augmentation/RATS_training_corpus'
TRAIN_A = 'trainA'
TRAIN_B = 'trainB_chanA'

if not os.path.exists(os.path.join(os.getcwd(),'datasets','AudioData')):
    os.makedirs(os.path.join(os.getcwd(),'datasets','AudioData','trainA'))
    os.makedirs(os.path.join(os.getcwd(),'datasets','AudioData','trainB'))

for file in os.listdir(os.path.join(DATASET_PATH,TRAIN_A)):
    shutil.copyfile(os.path.join(DATASET_PATH,TRAIN_A,file),os.path.join(os.getcwd(),'datasets','AudioData','trainA',file))

for file in os.listdir(os.path.join(DATASET_PATH,TRAIN_B)):
    shutil.copyfile(os.path.join(DATASET_PATH,TRAIN_B,file),os.path.join(os.getcwd(),'datasets','AudioData','trainB',file))
