#!/usr/bin/env python 
"""
ideone.com
API sample

This script shows how to use ideone api.
"""

from SOAPpy import WSDL

# creating wsdl client
wsdlObject = WSDL.Proxy('http://ideone.com/api/1/service.wsdl')

# calling test method
response = wsdlObject.testFunction('test','test')

# printing returned values
for item in response['item']:
        print item
