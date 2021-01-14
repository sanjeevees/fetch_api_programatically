#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 11 10:45:12 2021

@author: sanjeevahuja
"""
import requests
import json
import datetime

class api(object):
    """
    This class is to define common functions for db processing

    """

    def __init__(self):
        """
        The constructor for api class
        
        """

        pass
    
    
    def fetch_api(self, url):

        content = requests.get(url).json()

        return content
    

