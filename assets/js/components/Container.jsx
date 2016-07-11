var React = require('react');
var Header = require('./Header.jsx')
var LeftCol = require('./LeftCol.jsx')
var RightCol = require('./RightCol.jsx')

var Row = require('react-bootstrap').Row;
var Col = require('react-bootstrap').Col;


var Container = React.createClass ({
	getInitialState: function() {
		return {
			// TODO change from list to a dictionary of key: object 
			events: [],
			listOfEvents: []
		};
	},
	remove: function(eventName) {
		//e.preventDefault();
		var newEvents = this.state.events.filter(function(event) {
			return event.name !== eventName
		});
		this.setState({
			events: newEvents, 
		});
	},
	ajaxCall: function(url, json) {
		var _this = this;
		console.log("called " + url);
		console.log(json);
		$.ajax({
			url: "/api/" + url,
			method: "GET",
			dataType: "json",
			data: json,
			success: function(result) {
				console.log("success");
				console.log(result);
				_this.setState({
					events: _this.state.events.concat(result),
				});
			},
			error: function(err, res, ros) {
				console.log(res);
			}
		});
	},
	newQuery: function(city, state, country, type) {
		this.setState({
			events: [],
		})
		var request_data = {
			"city": city,
			"state": state,
			"country": country,
			"type": type,
		}
		if (!document.getElementById("facebook-login")) {
			console.log("facebook");
			this.ajaxCall("", request_data);
		}
		
		if (!document.getElementById("eventbrite-login")) {
			console.log("eventbrite");
			this.ajaxCall("eventbrite_call", request_data);
		}
		console.log("meetup");
		this.ajaxCall("meetup", request_data);
		/*var newEvents = [
			{	
				name: "Tokyo", 
				description: "", 
				start_time: "", 
				end_time: "", 
				url:"https://pbs.twimg.com/profile_images/575521516399423488/ELY3fVCn.pnghttps://pbs.twimg.com/profile_images/575521516399423488/ELY3fVCn.pnghttps://pbs.twimg.com/profile_images/575521516399423488/ELY3fVCn.pnghttps://pbs.twimg.com/profile_images/575521516399423488/ELY3fVCn.png", 
				image:"https://pbs.twimg.com/profile_images/575521516399423488/ELY3fVCn.png"}, 
			{name: "United States", description: "", start_time: "", end_time: "", url: "https://www.usa.gov/about-the-us", image: "http://i.infopls.com/images/states_imgmap.gif"}, 
			{name: "Spain", description: "", start_time: "", end_time: "", url: "https://en.wikipedia.org/wiki/Spain", image: "http://www.bmiresearch.com/sites/default/files/Spain.png"},
			{name: "Spain2", description: "", start_time: "", end_time: "", url: "https://en.wikipedia.org/wiki/Spain", image: "http://www.bmiresearch.com/sites/default/files/Spain.png"},
		];
		this.setState({
			events: newEvents,
		});*/
	},
	giveLink: function(event) {
		if (event.url != "") {
			return (<a href={event.url} target='_blank'>{event.name}</a>);
		} else {
			return (event.name);
		}
	},
	addEvent: function(event) {
		this.setState({
			listOfEvents: this.state.listOfEvents.concat([event])
		});
		this.remove(event.name)
	},
	removeAllAddedEvent: function() {
		this.setState({
			listOfEvents: [],
		});
	},
	addToCalendar: function() {
		if (this.state.listOfEvents.length > 0) {
			var token;
			if (document.getElementById("a-t")) {
				token = document.getElementById("a-t").value	
			}
			var type = document.getElementById('email_type').value.replace("_", " ");

			for (var i = 0; i < this.state.listOfEvents.length; i++) {
				var payload = {};

				event = this.state.listOfEvents[i];

				if (type == "Outlook") {
					// setting up the event for Outlook Calendar
					payload["Subject"] = event.name;
					payload['Body'] = {};
					payload['Body']['ContentType'] = "Text";
					payload['Body']['Content'] = jQuery(event.description).text();
					payload['Start'] = {};
					payload['Start']['DateTime'] = event.start_time;
					payload['Start']['TimeZone'] = 'America/Los_Angeles';
					payload['End'] = {};
					payload['End']['DateTime'] = event.end_time;
					payload['End']['TimeZone'] = 'America/Los_Angeles';

					$.ajax({
						type: "POST",
						url: 'https://outlook.office.com/api/v2.0/me/events',
						headers: {'Authorization': 'Bearer ' + token,
								  'Content-Type': 'application/json',
								 },
						data: JSON.stringify(payload),
						'error': function(jqXHR, textStatus, errorThrown) {
							console.log(jqXHR)
						},
						'success': function(res) {
							console.log(res);
						}	
					});
				} else if (type == "Google Calendar") {
					// setting up the event for Google Calendar
					var word = jQuery(event.description).text();
					word = word.replace('"', '\"');
					payload["summary"] = event.name;
					payload['location'] = event.place.street + ", " + event.place.city + ", " + event.place.state
					payload['description'] = word;
					payload['start'] = {};
					payload['start']['dateTime'] = event.start_time;
					payload['start']['timeZone'] = 'America/Los_Angeles'
					payload['end'] = {};
					payload['end']['dateTime'] = event.end_time;
					payload['end']['timeZone'] = 'America/Los_Angeles'

					gapi.client.load('calendar', 'v3').then(function() {
					   // Step 5: Assemble the API request
						var request = gapi.client.calendar.events.insert({
							'calendarId': 'primary',
							'resource': JSON.stringify(payload)
						});
						// Step 6: Execute the API request
						request.execute(function(event) {
						});
					});
				}
				console.log("printing out " + this.state.listOfEvents[i]);
			}
			this.removeAllAddedEvent();
		} else {
			alert("Please add an event to your list")
		}
	},
	render: function() {
		return (
			<div classNa="load-container">
				{/*<Header />*/}
				<LeftCol events={this.state.events} 
						 remove={this.remove} 
						 newQuery={this.newQuery} 
						 addEvent={this.addEvent}
						 giveLink={this.giveLink} />
				<RightCol 
						listOfEvents={this.state.listOfEvents} 
						addToCalendar={this.addToCalendar}
						giveLink={this.giveLink}/>
			</div>
		)
	}
});

module.exports = Container;