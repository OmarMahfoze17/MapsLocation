# -*- coding: utf-8 -*-
"""
Created on Fri May 11 23:46:32 2018

@author: om1014
"""
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from mapsplotlib import mapsplot as mplt

mplt.register_api_key('AIzaSyAnRmqg-kRi7wBE_v1wkujL12RqQV2dGIA')
data = pd.DataFrame({
'lat':[-58, 2, 145, 30.32, -4.03, -73.57, 36.82, -38.5],
'lon':[-34, 49, -38, 59.93, 5.33, 45.52, -1.29, -12.97],
'name':['Buenos Aires', 'Paris', 'melbourne', 'St Petersbourg', 'Abidjan', 'Montreal', 'Nairobi', 'Salvador']
})


# all plots can now be performed here