# -*- coding: utf-8 -*-
# @Author: chandan
# @Date:   2017-07-08 00:32:09
# @Last Modified by:   chandan
# @Last Modified time: 2017-07-08 11:13:46

from data_utils import read_file
from config import DATA_DIR, SCORE_COLUMNS 
import os
from model import train_model, test_model

import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split

import os.path as osp

ACC_FILE = 'RAW_ACCELEROMETERS.txt'
GPS_FILE = 'RAW_GPS.txt'
VEHDET_FILE = 'PROC_VEHICLE_DETECTION.txt'
SCORE_FILE = 'SEMANTIC_ONLINE.txt'


def main():
	# read acc, gps, veh det for multiple drivers, scenes
	X_dfs, Y_dfs = [], []
	driver_dir = 'D1'

	for drive_dir in os.listdir(osp.join(DATA_DIR, driver_dir)):
		drive_path = osp.join(DATA_DIR, driver_dir, drive_dir)
		print drive_path

		acc = read_file(osp.join(drive_path, ACC_FILE))
		gps = read_file(osp.join(drive_path, GPS_FILE))
		veh = read_file(osp.join(drive_path, VEHDET_FILE))
		
		score = read_file(osp.join(drive_path, SCORE_FILE))
		datasets = [acc, gps, veh, score]
		n_rows = min(map(len, datasets))
		
		# sample high frequency data to lowest frequency
		for i in range(len(datasets)):
			# drop time column
			datasets[i].drop(0, 1, inplace=True)

			if len(datasets[i]) > n_rows:
				step = len(datasets[i]) / n_rows
				ndx = xrange(0, n_rows * step, step)
				datasets[i] = datasets[i].ix[ndx]
				datasets[i] = datasets[i].reset_index(drop=True)

		score_df = datasets[-1]
		datasets = datasets[:-1]
		Y_df = score.ix[:, SCORE_COLUMNS]

		# create dataset
		X_df = pd.concat(datasets, axis=1, ignore_index=True)
		X_df.fillna(0, inplace=True)
		print "X:", X_df.shape
		print "Y:", score_df.shape

		X_dfs.append(X_df)
		Y_dfs.append(Y_df)

	# preprocess
	X_df = pd.concat(X_dfs, ignore_index=True)
	X = X_df.values.astype('float32')
	Y = pd.concat(Y_dfs, ignore_index=True).values

	print "X shape:", X.shape
	print "Y shape:", Y.shape

	scaler = MinMaxScaler(feature_range=(0, 1))
	X = scaler.fit_transform(X)

	X_tr, X_ts, Y_tr, Y_ts = train_test_split(X, Y, test_size=0.2)

	# train
	print "X Train shape:", X_tr.shape
	print "Y Train shape:", Y_tr.shape
	
	print "X test shape:", X_ts.shape
	print "Y test shape:", Y_ts.shape
	
	seq_len = 16

	X_tr_seq = X_to_seq(X, seq_len, 1)
	Y_tr = Y_tr[seq_len:]

	X_ts_seq = X_to_seq(X_ts, seq_len, 1)
	Y_ts = Y_ts[seq_len:]

	#train_model(X_tr, Y_tr)

	loss = test_model(X_ts_seq, Y_ts)
	print loss

def X_to_seq(X, seq_len=16, stride=1):
	X_seqs = []

	for start_ndx in range(0, len(X) - seq_len, stride):
		X_seqs.append(X[start_ndx : start_ndx + seq_len])
	
	return np.array(X_seqs)

if __name__ == '__main__':
	main()