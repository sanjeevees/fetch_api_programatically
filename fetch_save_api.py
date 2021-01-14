#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 11 10:45:12 2021

@author: sanjeevahuja
"""

from fetch_db import fetch_db
from api_call import api
import argparse
import collections

def main():
    # """
    # Function to execute all the required steps in a sequence to generate
    # desired output data file
    # """

    parser = argparse.ArgumentParser(
        description="This is a tool to fetch the data from an api and save it into db")

    parser.add_argument('--url',
                        type=str,
                        default="https://api.polygon.io/v2/aggs/ticker/AAPL/range/1/day/2020-06-01/2020-06-17?apiKey=kgWJgJ5G3b2l7CpOStlTuquWTw5ugZJi",
                        help="")
    
    parser.add_argument('--tableName',
                        type=str,
                        default="tableName",
                        help="Enter the table Name")
    
    
    parser.add_argument('--dropTable',
                        type=bool,
                        default=False,
                        required=False,
                        help="Enter the table Name")

    args = parser.parse_args()
    
    api_instance = api()

    data = api_instance.fetch_api(args.url) 
    if(type(data)!=list):
        data = [data]
    fetch_db_instance = fetch_db(args.tableName, data) 
    if (args.dropTable):
        fetch_db_instance.drop_table(args.tableName)
    fetch_db_instance.create_table(data, args.tableName)
    fetch_db_instance.save_data(data, args.tableName)  
    
    fetch_db_instance.print_data(args.tableName)
    
if __name__ == '__main__':
    main()
