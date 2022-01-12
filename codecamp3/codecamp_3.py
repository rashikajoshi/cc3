import logging
from urllib.request import urlopen
import urllib.parse as urlparse
import re
import json

logging.basicConfig(filename="test.log",level=logging.INFO,format="%(asctime)s:%(funcName)s:%(message)s")

class Data:
    def __init__(self, url):
        """initialization function

        Args:
            url (regex): URL given as input
        """        
        self.url = url
        self.pageid = 0

    def get_pageid(self):
        """The function extracts the pageid from the URL of a Json page.

        Args:
            url1 (regex): Refers to the URL of the Json page.

        Returns:
            integer: Returns the pageid extracted from the URL of the Json page.
        """    
        response = urlopen(self.url)
        data_json = json.loads(response.read())

        #print(data_json)
        for i in data_json['query']['pages']:
            word=i
        res=data_json['query']['pages'][word]['pageid']
        return res


    def getSeeAlso(self,pageid):
        """The function finds out the links of SEE ALSO references from the Json page of a given URL.

        Args:
            url1 (regex): The Json page URL given, from which the SEE ALSO links are to be extracted.
            pageid (integer): The pageid that has been extracted from the given json page.

        Returns:
            List: The returned list contains the SEE ALSO reference words extracted from the json page of a wikipedia page.
        """    
        a=[]
        response = urlopen(self.url)
        data_json = json.loads(response.read())
        x = (data_json['query']['pages'][str(pageid)]['revisions'][0]['*'])
        lst = x.split('\n')
        main = "==See also=="
        mainCheck = False
        empty = ""
        for element in lst:
            if element == main:
                mainCheck = True
                ele=element.replace("[","").replace("]","").replace("*","")
                ele=re.sub(" [\(\[].*?[\)\]]", "", ele)
                a.append(ele)
            elif mainCheck and element != empty:
                ele=element.replace("[","").replace("]","").replace("*","")
                ele=re.sub(" [\(\[].*?[\)\]]", "", ele)
                a.append(ele)
            elif mainCheck and element == empty:
                break
        a=a[1:]
        return a

    def generate_links(self,a):
        """The function generates valid links using the SEE ALSO reference words and the original json page link.

        Args:
            url1 (regex): URL of the json page of a wikipedia webpage.
            a (list): SEE ALSO reference words extracted from the json page of a wikipedia page.
        """    
        link=[]
        for i in a:
            url1="http://en.wikipedia.org/w/api.php?format=json&action=query&titles="+i+"&prop=revisions&rvprop=content"
            link.append(url1)
            #print(url1)
            logging.info(url1)
    
    
    def urlvalidation(self):
        """Custom exception function to validate a given URL.The function returns if the given URL is valid or not.

        Args:
            URL (regex): URL to be validated

        Returns:
            Boolean: True if URL is valid, False if URL is invalid
        """    
        regex = re.compile(r'^(?:http|ftp)s?://'  # https:// or http://
                        r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?.)+(?:[A-Z]{2,6}.?|[A-Z0-9-]{2,}.?)|'  # domain
                        r'localhost|'  # localhost
                        r'\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3})'  # ip
                        r'(?:/?|[/?]\S+)$', re.IGNORECASE)
        return re.match(regex, self.url) is not None





