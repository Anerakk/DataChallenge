#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 13 15:56:48 2018

@author: bryceanderson
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import scipy.stats
import json
with open('nobel.json', 'r') as f:
    nobel = json.load(f)
names = []
year = []
cat = []
share = []

for prizes in nobel['prizes']:
    for i in range(len(prizes['laureates'])):
        cat.append(prizes['category'])
        year.append(prizes['year'])
        names.append(prizes['laureates'][i]['firstname'] +" "+ prizes['laureates'][i]['surname'])
        share.append("1/" + prizes['laureates'][i]['share'])

nobel_prizes = pd.DataFrame({'category': cat, 'year': year, 'share': share}, index = names)
#%%-----------------------------------------