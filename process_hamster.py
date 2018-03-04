#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Description:      : Simple script to process data exported from hamster into importable toggl
#                     format
# File              : process_hamster.py
# Author            : Tom Durrant <t.durrant@metocean.co.nz>
# Date              : 05.03.2018
# Last Modified Date: 05.03.2018
# Last Modified By  : Tom Durrant <t.durrant@metocean.co.nz>

import pandas as pd
from datetime import datetime, timedelta
import numpy as np

data = pd.read_table('~/Downloads/hamster.tsv')
with open('output.txt', 'w') as f:
    f.write('Email,Start date,Start time,Duration,Project,Description,Tags\n')
    for index, row in data.iterrows():
        start = datetime.strptime(row['start time'],'%Y-%m-%d %H:%M:%S')
        startdate = start.strftime('%Y-%m-%d')
        starttime = start.strftime('%H:%M:%S')
        duration = timedelta(seconds = int(row['duration minutes']) * 60)
        try:
            if np.isnan(row.tags):
                tags = ''
        except Exception as e:
            tags = row.tags
        try:
            f.write(','.join(['thdurrant@gmail.com', startdate, starttime, str(duration), row.category, row.activity, '"'+tags+'"'])+'\n')
        except Exception as e:
            print startdate, starttime, str(duration), row.category, row.activity, tags

