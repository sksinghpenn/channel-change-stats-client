import random
import start_end_time
import datetime;

###################LIST OF CHANNEL CHANGE EVENT IN JSON #######################
# The function returns list of channel change report message in JSON format.
# The number of element in the list is based on the input passed to the function.
def get_channel_change_json_report(number_of_report_per_client):
	
	# get the list of number of channel changed by  the clients
	# the list will contain numbers; if the list say contain 5 numbers: 4, 20, 12, 2, 3
	# it means first report will have 4 json messages, the second will have 20 json messages,
	# the third report will have 12 json messages, fourth will have 2 and the last will have 3 json messages
	# in the report
	list_of_count_channel_change_event = pouplate_count_of_channel_change_by_each_client(number_of_report_per_client)
	
	json_event_list = []
	
	# for each report build the json of channel change event
	for count_of_change_event in list_of_count_channel_change_event:
		
		print("Count of channel change event in each report:" + str(count_of_change_event))
		# the list will have list of channel change
		#for example ['BRAVO', 'NICK AT NITE', 'ABC FAMILY', 'A&E']
		list_of_channel_changed= get_list_of_channel_changed(count_of_change_event)	
			
		service_json_list = []
		
		
		
		i = 0
		start_time = start_end_time.get_random_start_date_time()
		end_time = datetime.datetime.now()
		
		# for each channel for example 'BRAVO'
		for channel_name in list_of_channel_changed:
			# get the manfest url for example http://192.168.0.186/hls/nick at nite/main-04.m3u8
			channel_manifest_url = get_manifest_url(channel_name)
			if ( i == 0):
				start_time = start_end_time.get_random_start_date_time()
			else:
				start_time = start_end_time.get_random_end_date_time(end_time)
				
			start_time_isoformat = start_time.isoformat()
			
			end_time = start_end_time.get_random_end_date_time(start_time)
			end_time_isoformat = end_time.isoformat()
					
			service_json_str = ""
			
			service_json_str = service_json_str + "{\"service_name\"" + ":" + "\"" + channel_name.strip() + "\"" +"," + "\"manifest_url\"" + ":" + "\"" +  channel_manifest_url.strip('\n\r') + "\"" +"," + "\"channel_join_time\"" + ":" + "\"" + start_time_isoformat.lstrip('\n\r')  + "\"," +  "\"channel_leave_time\"" + ":" + "\"" + end_time_isoformat.lstrip('\n\r') + "\"" +"," + "\"map_list_entry\"" + ":\"false\"}"
			service_json_list.append(service_json_str)
			i = i + 1
		
		json_event_list.append(service_json_list)
		
		
	
	return json_event_list
##############################****END*****#####################################


###################LIST OF CHANNEL CHANGE NAME#################################
# List of 20 most popular channel in 2013 
# resource http://www.thewrap.com/2013-most-watched-basic-cable-rankings/

channel_list = ["HISTORY", "USA-NETWORK", "ADULT-SWIM", "FOX-NEWS", 
                "TNT", "NICK-AT-NITE", "CARTOON-NETWORK", "ESPN", "NBC", 
                "CNN", "TBS", "HGTV", "FX", "AMC", "BRAVO", "DISCOVERY", 
                "FOOD-NETWORK", "ABC-FAMILY", "TVLAND", "LIFETIME"]


def get_random_channel():
	return random.randrange(RANDOM_NUMBER_START, RANDOM_NUMBER_STOP)

def get_list_of_channel_changed(how_many):
	list_of_channel_change_changed = []
	index_prev = -1
	for x in range(START, how_many):
		# to make sure next channel is different than the previous channel
		while True:
			index  = get_random_channel()
			if (index_prev != index):
				break
		index_prev = index       
		list_of_channel_change_changed.insert(x,channel_list[index])    
	return list_of_channel_change_changed
##############################****END*****#####################################


############################Manifest URL Section###############################
HOST_URL ="http://192.168.0.186/hls/"
TRAILING_URL="/main-04.m3u8"

def get_manifest_url(channel_name):    
	return HOST_URL+channel_name.lower()+TRAILING_URL
##############################****END*****#####################################




#########################LIST Of COUNT OF CHANNEL CHNAGE EVENT#################
RANDOM_NUMBER_START = 1
RANDOM_NUMBER_STOP = len(channel_list) 
START = 0

# This function is used to generate random number between range
def get_number_of_random_channel_change_event():
	return random.randrange(RANDOM_NUMBER_START, RANDOM_NUMBER_STOP)

count_of_channel_change_by_each_client = []

def pouplate_count_of_channel_change_by_each_client(number_of_report_per_client):
	for x in range(START, number_of_report_per_client):
		number_of_random_channel_change_event = get_number_of_random_channel_change_event()		
		count_of_channel_change_by_each_client.append(number_of_random_channel_change_event)	
		
	return count_of_channel_change_by_each_client
##############################****END*****#####################################	