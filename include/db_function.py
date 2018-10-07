#!/bin/python
#-*-coding:utf-8-*-

import ConfigParser

def get_item(data_dict,item):
    try:
       item_value = data_dict[item]
       return item_value
    except:
       return '-1'

def get_config(group,config_name):
    config = ConfigParser.ConfigParser()
    config.readfp(open('./etc/db_config.ini','rw'))
    config_value=config.get(group,config_name).strip(' ').strip('\'').strip('\"')
    return config_value

if __name__=='__main__':
	get_config('monitor_server','host')