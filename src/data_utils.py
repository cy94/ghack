# -*- coding: utf-8 -*-
# @Author: chandan
# @Date:   2017-07-08 00:32:17
# @Last Modified by:   chandan
# @Last Modified time: 2017-07-08 01:20:07

import pandas as pd

def read_file(fname):
	df = pd.read_csv(fname, sep=' ', header=None)
	return df
	