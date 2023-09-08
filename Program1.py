"""
CSCI-UA.0002 Spring 2024
Assignment #10, Program 1
Your name here
"""

# This program retrieves weather information form the Internet and then delivers it to the user
import urllib.request
import xml.etree.ElementTree
import ssl
ssl._create_default_https_context = ssl._create_unverified_context


# function:   create_dictionary
# input:      a URL (string)
# processing: Retrieve XML using input URL.
#             Parse XML
#             Initialize dictionary
#             Search for required elements in XML and store them in the dictionary
# output:     a dictionary
