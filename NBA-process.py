#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 26 00:05:27 2022

@authors:
    Stephen Leung 301399135
    Alex Liang 301397756
    
This program evaluates and processes NBA data, using Machine Learning algorithms to
determine which player features are related to an increased salary. (ADJUST)
"""

import numpy as np
import pandas as pd
import sys

def main(in_directory, out_directory):
    data = pd.read.csv(in_directory)
    print('gay')

if __name__=='__main__':
    in_directory = sys.argv[1] #(NBA direc)
    out_directory = 'output.csv'
    main(in_directory, out_directory)



