# -*- coding: utf-8 -*-
# @Author: chandan
# @Date:   2017-07-08 00:32:09
# @Last Modified by:   chandan
# @Last Modified time: 2017-07-08 02:10:04

from data_utils import read_file
from config import DATA_DIR 
import os
from train import train_model

import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split

import os.path as osp

def main():
	# read acc, gps, veh det for multiple drivers, scenes
	acc = read_file(osp.join(DATA_DIR, 'D1/20151110175712-16km-D1-NORMAL1-SECONDARY/RAW_ACCELEROMETERS.txt'))
	gps = read_file(osp.join(DATA_DIR, 'D1/20151110175712-16km-D1-NORMAL1-SECONDARY/RAW_GPS.txt'))
	veh = read_file(osp.join(DATA_DIR, 'D1/20151110175712-16km-D1-NORMAL1-SECONDARY/PROC_VEHICLE_DETECTION.txt'))

	score = read_file(osp.join(DATA_DIR, 'D1/20151110175712-16km-D1-NORMAL1-SECONDARY/SEMANTIC_ONLINE.txt'))
	score.drop(0, 1, inplace=True)
	print score.shape

	datasets = [acc, gps, veh]

	n_rows = min(map(len, datasets))

	# sample high frequency data to lowest frequency
	for i in range(len(datasets)):
		datasets[i].drop(0, 1, inplace=True)
		if len(datasets[i]) > n_rows:
			step = len(datasets[i]) / n_rows
			ndx = xrange(0, n_rows * step, step)
			datasets[i] = datasets[i].ix[ndx]
			datasets[i] = datasets[i].reset_index(drop=True)

	# create dataset
	data = pd.concat(datasets, axis=1, ignore_index=True)
	data.fillna(0, inplace=True)
	data = data.values.astype('float32')

	# preprocess
	scaler = MinMaxScaler(feature_range=(0, 1))
	X = scaler.fit_transform(data)
	Y = score.ix[:, 2].values

	X_tr, X_ts, Y_tr, Y_ts = train_test_split(X, Y, test_size=0.2)

	# train
	print "X Train shape:", X_tr.shape
	print "Y Train shape:", Y_tr.shape

	seq_len, stride = 16, 1
	Y_tr = Y_tr[seq_len:]
	X_tr_seqs = []

	for start_ndx in range(0, len(X_tr) - seq_len, stride):
		X_tr_seqs.append(X_tr[start_ndx : start_ndx + seq_len])

	X_tr_seqs = np.array(X_tr_seqs)

	train_model(X_tr_seqs, Y_tr)

if __name__ == '__main__':
	main()