##
import numpy as np
import time
from sklearn.utils import shuffle
from tensorflow.keras.utils import to_categorical

##
print(str(time.ctime()) + ": Initializing...")
ts = np.load('/gpfs/alpine/gen150/proj-shared/junqi/hea/HEA_train.npy')
vs = np.load('/gpfs/alpine/gen150/proj-shared/junqi/hea/HEA_val.npy')
lt = np.load('/gpfs/alpine/gen150/proj-shared/junqi/hea/label_T_train.npy')
lv = np.load('/gpfs/alpine/gen150/proj-shared/junqi/hea/label_T_val.npy')
print(str(time.ctime()) + ": Successfully loaded all data sets!")

##
print(ts.shape)
print(vs.shape)
print(lt.shape)
print(lv.shape)

##
ts, lt = shuffle(ts, lt, random_state=0)
vs, lv = shuffle(vs, lv, random_state=0)

##
train_size = 4000
val_size = 1000
trainset = ts[0:train_size]
valset = vs[0:val_size]
label_training = lt[0:train_size]
label_validation = lv[0:val_size]

##
lt_onehot = to_categorical(label_training) # make one hot vectors
lv_onehot = to_categorical(label_validation)

ltunique = np.unique(label_training)
lvunique = np.unique(label_validation)

lt_onehot = lt_onehot[:, ltunique]
lv_onehot = lv_onehot[:, lvunique]

print(lt_onehot.shape)
print(lv_onehot.shape)

##
np.savez('savefile.npz', train=trainset, val=valset, labval=label_validation, ltoh=lt_onehot, lvoh=lv_onehot)