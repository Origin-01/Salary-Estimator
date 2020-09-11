# -*- coding: utf-8 -*-
"""
Created on Fri Sep 11 19:53:55 2020

@author: HP
"""

import Glassdoor_scraper as gs
import pandas as pd

path='C:/Users/HP/Desktop/Salary_Estimator/Salary-Estimator/chromedriver'

df=gs.get_jobs('data scientist',15,False,path,15)

df