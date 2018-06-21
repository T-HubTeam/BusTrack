# import confidparser to read
# 'config.ini' file and obtain
# the required data
import configparser
import io


# loading config file
config = configparser.ConfigParser()
config.read('config.ini')

host		= config['mongo']['host']
db      	= config['mongo']['db']
collection	= config['mongo']['collection']
bus_id		= config['mongo']['busid']
