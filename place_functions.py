__author__ = "Cody Swain"
__copyright__ = "TimeSpent"

import random
import googlemaps
from googlemaps import geolocation
from googlemaps import places
from datetime import datetime

# Migrate to Environment Variable
gmaps = googlemaps.Client(key='AIzaSyC94G_D29MnwKOepVNsTOqfu99PYtlcuAU')


# Create first event
def initialize_story(start_location=None):
	story = list() #Individual users story -- A List of Dicts

	if start_location:
		start_loc = gmaps.geocode(start_location)
	else: 
		start_loc = geolocation.geolocate(client=gmaps)

	# Create a start event from start loc
	start_event = {}
	start_event = dict(start_loc) #Copy the start loc dict
	start_event['name'] = "__START__"

	## --------------------------------
	## ADD FUTURE EVENT PROPERTIES HERE
	## --------------------------------
	story.append(start_event)
	return story


# Returns dict with nearby events
def list_nearby_events(curr_location=None, search_radius=None, event_type=None):

	if event_type:
		nearby_gmaps_results = places.places_nearby(client=gmaps, location=curr_location, keyword="Food", radius=search_radius)
	else:
		nearby_gmaps_results = places.places_nearby(client=gmaps, location=curr_location, keyword="Food", radius=search_radius)

	# Convert google maps into "Story" compatible data type
	if nearby_gmaps_results:
		nearby_events = nearby_gmaps_results['results']
		return nearby_events

def append_event_to_story(story, event):
	story.append(event)
	return story # Python dicts mutable --Remove 'return' ?


def list_nearby_event_names(data):
	for i in range(len(data)):
		print(data[i]['name'])

# DEV
def random_event_picker(nearby_events_list):
	return random.choice(nearby_events_list)

# def choose_category(self, previous_event, current_time):
# 	return None

# def allocate_time(self, event):
# 	return None

# Example structure of story
example_story = [
	{
		"Event Title": "Bowling",
		"Category": "Activity",
		"Event location": "1234 Haashole Rd, Goober Germany, 91111", # lmao
		"Start Time": "4:00 PM",
		"End Time": "5:00 PM",
	},
	{
		"Event Title": "Dinner",
		"Cateogry": "Food",
		"Event location": "111 Camelia Lane, Walnut Creek, CA 94595",
		"Start Time": "6:00 PM",
		"End Time": "7:00 PM",
	}
]


if __name__ == "__main__":
	
	'''Event #1'''
	story = initialize_story()

	'''Event #2'''
	if 'location' in story[0]:
		lat_lng = story[0]['location']
	else:
		lat_lng = story[0]['geometry']['location']
	nearby_places_dict = list_nearby_events(curr_location=lat_lng, search_radius=1000) #Search radius in meters
	specific_event = random_event_picker(nearby_places_dict)
	story = append_event_to_story(story, specific_event)

	'''Event #3'''
	if 'location' in story[1]:
		lat_lng = story[1]['location']
	else:
		lat_lng = story[1]['geometry']['location']

	nearby_places_dict = list_nearby_events(curr_location=lat_lng, search_radius=1000) #Search radius in meters
	specific_event = random_event_picker(nearby_places_dict)
	story = append_event_to_story(story, specific_event)

	'''Event #4'''
	if 'location' in story[2]:
		lat_lng = story[2]['location']
	else:
		lat_lng = story[2]['geometry']['location']
	nearby_places_dict = list_nearby_events(curr_location=lat_lng, search_radius=1000) #Search radius in meters
	specific_event = random_event_picker(nearby_places_dict)
	story = append_event_to_story(story, specific_event)
	
	''' Print Event Names'''
	for idx in range(len(story)):
		print(story[idx]['name'])













	### TEMP

	# start_loc = [37.8898303, -122.06701120000002] #This is the starting location 

	# story = initialize_story(start_loc)
	# print("DEV -- Print out story:: " + str(story[0]['location']))
	# event_list = list_nearby_events(story[0])
	# event_list = list_nearby_events(story[0]['location'])

	# chosen_event = random_event_picker(event_list)
	# story = append_event_to_story(story, chosen_event)


	### END TEMP

	# list_nearby_event_names(places_dict)

	# Get directions from one point to another
	# now = datetime.now()
	# directions_results = gmaps.directions("161 Camelia Lane", "UCLA", mode="transit", departure_time=now)
	# print(directions_results)