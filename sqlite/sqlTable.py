# -*- coding: utf-8 -*-
"""
Created on Sun Sep  3 17:20:10 2023

@author: Tiel
"""

import sqlite3 as sql

conn = sql.connect("../workout_log.sl3")
cursor = conn.cursor()

query = """CREATE TABLE workouts (date VARCHAR(255) NOT NULL, type VARCHAR(255) NOT NULL, duration_minutes INT, description VARCHAR(255));"""

cursor.execute(query)
conn.close()
