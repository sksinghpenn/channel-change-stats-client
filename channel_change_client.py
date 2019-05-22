# This is a client script to connect to the CCR Server.
# The script puts a JSON message to the server after establishing the connection with server.

# author: SK Singh
# date: Nov 9, 2014

import json
import urllib.request

#library containing function to get list of JSON message
import channel_change_report


# This the URL of the RESTful service
# The RESTful service  accepts JSON message    
url = 'http://localhost:8080/CCR/ccrService/ccrJason'

#configured to generate number of channel change report per client
number_of_report_per_client = 5 

# gets the list of JSON messages for all reports
channel_change_json_list = channel_change_report.get_channel_change_json_report(number_of_report_per_client)

# iterate through all the JSON messages in the list 
for channel_change_list in channel_change_json_list:
    
    # iterate through all the messages in a report
    for data in  channel_change_list:
        
        # sample JSON message
        #data = {"serviceName":"History", "manifestUrl":"http://192.168.0.186/hls/history/main-04.m3u8", "channelJoinTime":"2007-07-16T18:20:30+01:00", "channelLeaveTime":"2007-07-16T18:25:30+01:00", "mapListEntry":"false"}
        
        # gets json dump
        data_json = json.dumps(data)

        # encode into ascii
        binary_data = data.encode('ascii')

        # build the header set the Content-type and Accept header
        headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}

        #get the request
        req = urllib.request.Request(url, binary_data, headers=headers, method='PUT')

        # send the JSON request
        resp = urllib.request.urlopen(req)

        print ("JSON: " + data );

