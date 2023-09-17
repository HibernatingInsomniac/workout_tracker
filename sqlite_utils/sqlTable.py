# -*- coding: utf-8 -*-
"""
Created on Sun Sep  3 17:20:10 2023

@author: Tiel
"""

import sqlite3 as sql

def load_db_tables(sql_file):
    conn = sql.connect(sql_file)
    cursor = conn.cursor()
    query = """SELECT name from sqlite_master"""
    yip = cursor.execute(query).fetchall()
    print(yip)
    
#Create enum table identifying workout types
def create_workout_enum_table(cursor):
    query = """CREATE TABLE workout_types_enum (workout_type_num INT NOT NULL, workout_type VARCHAR(255) NOT NULL);"""    
    cursor.execute(query) 
    queries = []
    #TODO: Make table auto-increment and have primary key
    queries.append("INSERT INTO workout_types_enum (workout_type_num, workout_type) VALUES (1, 'Push')")
    queries.append("INSERT INTO workout_types_enum (workout_type_num, workout_type) VALUES (2, 'Pull')")
    queries.append("INSERT INTO workout_types_enum (workout_type_num, workout_type) VALUES (3, 'Leg_Day')")
    queries.append("INSERT INTO workout_types_enum (workout_type_num, workout_type) VALUES (4, 'Pure_Cardio')")
    queries.append("INSERT INTO workout_types_enum (workout_type_num, workout_type) VALUES (5, 'Other')")
    for q in queries:
        cursor.execute(q)

#TODO: Make table categorizing intensity from 1 to 10 as easy/moderate/hard



if __name__ =="__main__":
    conn = sql.connect("../workout_log.sl3")
    cursor = conn.cursor()
    query = """CREATE TABLE workouts (date VARCHAR(255) NOT NULL, type VARCHAR(255) NOT NULL, duration_minutes INT, description VARCHAR(255));"""    
    cursor.execute(query)

    create_workout_enum_table(cursor)
    conn.close()

    
