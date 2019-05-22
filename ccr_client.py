# This is a client script to connect to the CCR Server.
# The script puts a JSON message to the server after establishing the connection.with server.

# author: SK Singh
# date: Oct 30, 2014

import http.client
import urllib.parse
import json
import channel_change_report

# local 
connection = http.client.HTTPConnection("localhost", 8081)


#server
#connection = http.client.HTTPConnection("146.186.90.203", 8081)


#configured to generate number of channel change report per client
number_of_report_per_client = 5 

# gets the list of JSON messages for all reports
channel_change_json_list = channel_change_report.get_channel_change_json_report(number_of_report_per_client)

# iterate through all the JSON messages in the list 
for channel_change_list in channel_change_json_list:
    
    # iterate through all the messages in a report
    for data in  channel_change_list:
        
        json_data = json.loads(data)
        jason_urlencodes_input = urllib.parse.urlencode(json_data)
        connection.request('PUT', jason_urlencodes_input)          
        connection.close()
        
        

