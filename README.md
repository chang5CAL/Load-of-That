api for events:
meetup -
fb -
twitter -
google+
eventful
groupon
eventbrite -

signup api
	- LinkedIn
	- Outlook
	- FB X
	- Gmail X
	- Twitter X

Calender API
	- google
	- outlook

home
login/signup
search database
detailed result page

backend:
api calls to other sites
	- write own wrapper classes as "contributions"
store events in our own system
	- periodic cleaning of our events
user account to memorize events that were already added/deleted
	- periodic cleaning of user accounts
Sign in
-----------------
Rest API calls:

STRETCH
Type: login
/login POST
params: what type of method (gmail, fb, etc), login keys, etc
description:api called when user is logging in
result: verify if the account exist and then add a cookie to remember users

STRETCH
Type: Signup
/signup POST
params: what type of method (gmail, fb, etc), login keys, etc
description:api called when user is logging in, create our own user id and store it with information that's related to our registration service
result: set a cookie saying the user is logged in

MANDATORY
Type: Search
/search GET
params: query, location, category of event
description: searches all of our api to create a json object of all the events available in our api call
result: if we have enough events already cached in our list we just return it for the user. Otherwise make the requests to the apis, cache the data, and then return it to the user.

MANDATORY
Type: clean cache
no-url
description: clean our list of events for things that are already
result: ran daily, clear our list of events for outdated ones

STRETCH
Type: user updating their results
/add-ignore-events POST
parameter: user id, id of events to skip
description: add events that the user chosed to ignore or signed up for
result: creates a list of events to ignore in user's profiel

STRETCH
Type: Client update their own cache
/update-list
paramater: POST, user id, rejected to be list to be updated, accepted to be list updated
description/result: clears the user's data 

DB Schema:
SQL:
Events
- event UUID, eventID, id for site that gave us the information, image, title, description, location, time, url
Users
- user UUID, FB ID, TWitter ID, gmail ID
Rejected
- rejected UUID, user UUID, event UUID
Accepted
- accepted UUID, user UUID, event UUID
CALENDAR????

frontend:
Figure out flow of sites STRETCH
Login/Logout interface with backend STRETCH
Backend calls to get data/show data MANDATORY 
Show/add events to calendar MANDATORY
	- Google + Outlook calender
Make api call for server to remember to remove certain events STRETCH
Make it look good MANDATORY


overall container
	header
		logo
		search bar
		other navigation stuff
			login
			help
			user profile
	left-col
		data input
			types of activities
		events
			list of events
				- picture, title, description, x button, add to event, time, reviews, address, add button 
			save button - api calls to their calendar
	right-col, calendar
