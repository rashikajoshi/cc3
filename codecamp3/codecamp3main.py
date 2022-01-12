from urllib.request import urlopen
import codecamp_3
from codecamp_3 import Data
import logging


logging.basicConfig(filename="test.log",level=logging.INFO,format="%(asctime)s:%(funcName)s:%(message)s")

url = "http://en.wikipedia.org/w/api.php?format=json&action=query&titles=SMALL&prop=revisions&rvprop=content "

d=Data(url)
if d.urlvalidation()==True:
    logging.info(d.urlvalidation())
    pgid=d.get_pageid()
    #print(pgid)
    logging.info(pgid)
    arr=d.getSeeAlso(pgid)
    #print(arr)
    lst=d.generate_links(arr)
    logging.info(d.urlvalidation())





