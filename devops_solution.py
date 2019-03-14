# Author: Ryan LeBon
# Exercise: Devops Challenge
# Date: 3/14/2019

import subprocess
from urllib.parse import urlparse
import re
from xml.dom import minidom
from io import StringIO
from lxml import etree
import sys

def main():
    try:
        print('Manipulating XML File...')
        # read in 3 arguments, pom file, organization name and repo name
        pom_file = sys.argv[1]
        org_name = sys.argv[2]
        branch_name = sys.argv[3]
        # validate pom file
        with open(pom_file, 'r') as xml_file:
            check = xml_file.read()   
            try:
                etree.parse(StringIO(check))
                print('XML is validated')
            except IOError:
                print('Invalid File!')
        tree = minidom.parse(pom_file)
        name = tree.getElementsByTagName("version")[0] 
        new_name = 'ci_{}_{}-SNAPSHOT'.format(org_name,branch_name)
        name.firstChild.data = new_name
        new_tree = open(pom_file, "w")
        tree.writexml(new_tree)
        new_tree.close()
        print('Finished manipulating XML!')
    except Exception as e:
        print('ERROR!',e)
        print('When executing script use: python3 devops_solution.py pom.xml org_name branch_name')

if __name__ == "__main__":
    main()