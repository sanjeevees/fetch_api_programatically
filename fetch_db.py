#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 11 10:45:12 2021

@author: sanjeevahuja
"""

import sqlite3
import collections

keys = []
newlist= []

def iterate_over(data):
    for row in data:
        for key,value in row.items():   
            if key not in keys:
                keys.append(key)
            if type(value)==list:
                if type(value[0])== dict:
                    iterate_over(value)

def transform_data(data):
    newDict = {}
    newlist = []
    for row in data:
        for key,value in row.items():  
            if  type(value)!=list:
                newDict[key] = value
        for key,value in row.items(): 
            if type(value)==list:
                for newDict2 in value:
                    newDictTemp = {}
                    for keyNew,valueNew in newDict2.items():
                        newDictTemp[keyNew] = valueNew
                    newlist.append( {**newDict, **newDictTemp})                
    return newlist


class fetch_db(object):
    """
    This class is to define common functions for db processing

    """


    def __init__(self, table_name, data):
        """
        The constructor for db class
        
        """
        self.db = sqlite3.connect(table_name)
        self.cursor = self.db.cursor()
        iterate_over(data)
        print(keys)

        
    def drop_table (self, table_name):
        """
        The create table is used saving the data
        
        """   
        try:
            
            # Find all keys      
            # Print table definition
            drop_table =  """Drop TABLE {0}""".format(table_name)

            self.cursor.execute(drop_table)
            
        except Exception as E:
            print('Error :', E)
        else:
            print('{0} table dropped'.format(table_name))
    

    def create_table (self, data, table_name):
        """
        The create table is used saving the data
        
        """   
        try:
            
            # Print table definition
            create_table =  """CREATE TABLE {0}(
              {1}
            );""".format(table_name,",\n  ".join(map(lambda key: "{0} VARCHAR".format(key), keys)))

            self.cursor.execute(create_table)
            
            print(create_table)
                        
        except Exception as E:
            print('Error :', E)
        else:
            print('table created')

    def save_data(self, data, table_name):
        """
        The create table is used saving the data
        
        """   
        try:
            data = transform_data(data)
            for row in data:
                insert_query = """INSERT INTO {0} VALUES({1});""".format(table_name,
                    ",".join(map(lambda key: '"{0}"'.format(row[key]) if key in row else "NULL", keys)))
                print(insert_query)
                self.cursor.execute(insert_query) 
        except Exception as E:
            print('Error :', E)
        else:
            self.db.commit()
        print('data inserted')
        
    def print_data(self, table_name):
        """
        The create table is used printing the table
        
        """   
        try:
            cursor = self.db.cursor()
            print("Fetching all the records from {0} table".format(table_name))
            cursor.execute("""SELECT * FROM {0}""".format(table_name))
        except Exception as E:
            print ('Error: ', E)
        else:
            for row in cursor.fetchall():
                    print (row)
        self.db.close()