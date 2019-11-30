#!/usr/bin/env python

###############################################################################################################
######   Popis: 
######          
######   Autor: Tomas Klein,  R-SYS 2019
######   Datum: 28.11.2019
###############################################################################################################

from os import listdir, remove
import argparse, logging, re, sys, json

################################# PYTHON BASIC SETUP ##########################################################
#Arguments definition
ap = argparse.ArgumentParser()
ap.add_argument("-cfg", "--config_file", required=True, help="Configuration file")
ap.add_argument("-d", "--debug_mode",  required=False, action='store_true', help="DEBUG MODE")

args = ap.parse_args()

logFileName = "xtamService.log"

#Logger setting 
if(args.debug_mode == True):
    logging.basicConfig(
        level=logging.DEBUG,
        format="%(asctime)s - %(levelname)s - %(message)s",
        handlers=[
            logging.FileHandler(logFileName),
            logging.StreamHandler()
    ])
else:
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s",
        handlers=[
            logging.FileHandler(logFileName),
            logging.StreamHandler()
    ])

###############################################################################################################

logging.info("-----------START-----------")

###### LOAD CONFIGURATION FILE ######
try:
    with open(args.config_file) as configfile_contents:
        config = json.load(configfile_contents)
    logging.info("Config file loaded successfully!")
except:
    logging.error("Config file cant be loaded!")
    logging.info("-----------END-----------")
    sys.exit(0)

###### NOTAM #####
if "NOTAM" in config:
    logging.info("NOTAM config found") 
    
    try:
        


logging.info("-----------END-----------")