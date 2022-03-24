# -*- coding: utf-8 -*-
"""
Created on Sat May 12 14:04:12 2018

@author: om1014
"""

from mapsplotlib import mapsplot as mplt
import pandas as pd
mplt.register_api_key('AIzaSyAnRmqg-kRi7wBE_v1wkujL12RqQV2dGIA')
data = pd.DataFrame({
'latitude':[-58, 2, 145, 30.32, -4.03, -73.57, 36.82, -38.5],
'longitude':[-34, 49, -38, 59.93, 5.33, 45.52, -1.29, -12.97],
'color':['blue','red','gray','orange','purple','yelow','green','black'],
'name':['Buenos Aires', 'Paris', 'melbourne', 'St Petersbourg', 'Abidjan', 'Montreal', 'Nairobi', 'Salvador']
})

#mplt.plot_markers(data)
mplt.density_plot(data['latitude'], data['longitude'])