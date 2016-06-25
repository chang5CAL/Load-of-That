var React = require('react');
var Header = require('./Header.jsx')
var LeftCol = require('./LeftCol.jsx')
var RightCol = require('./RightCol.jsx')

var Container = React.createClass ({
	getInitialState: function() {
		return {
			// TODO change from list to a dictionary of key: object 
			events: [
					 {id: 1, title: "Gameworks", url:"http://gameworks.com", image: "http://www.newportonthelevee.com/Portals/newportonthelevee/Images/Directory/Gameworks.png"}, 
					 {id: 2, title: "Dave and Busters", url: "http://www.daveandbusters.com/", image: "http://www.daveandbusters.com/media/1023/logo_no_shadow.png"}, 
					 {id: 3, title: "Disney Land", url: "https://disneyland.disney.go.com/", image: "https://s-media-cache-ak0.pinimg.com/236x/e0/71/0d/e0710d8c6cf4c5b707fd55375e9c740c.jpg"},
					],
			listOfEvents: []
		};
	},
	remove: function(eventId) {
		//e.preventDefault();
		console.log(eventId);
		var newEvents = this.state.events.filter(function(event) {
			return event.id !== eventId 
		});
		this.setState({
			events: newEvents, 
		});
	},
	newQuery: function(location, type) {
		var newEvents = [
						 {id: 4, title: "Tokyo", url:"https://pbs.twimg.com/profile_images/575521516399423488/ELY3fVCn.png", image:"https://pbs.twimg.com/profile_images/575521516399423488/ELY3fVCn.png"}, 
						 {id: 5, title: "United States", url: "https://www.usa.gov/about-the-us", image: "http://i.infopls.com/images/states_imgmap.gif"}, 
						 {id: 6, title: "Spain", url: "https://en.wikipedia.org/wiki/Spain", image: "http://www.bmiresearch.com/sites/default/files/Spain.png"},
					   ];
		this.setState({
			events: newEvents,
		});
	},
	addEvent: function(event) {
		this.setState({
			listOfEvents: this.state.listOfEvents.concat([event])
		});
		this.remove(event.id)
	},
	removeAllAddedEvent: function() {
		this.setState({
			listOfEvents: [],
		});
	},
	addToCalendar: function() {
		var token = document.getElementById("a-t").value
		console.log("add to calendar called");
		for (var i = 0; i < this.state.listOfEvents.length; i++) {
			/*
			payload = {}
			var json = JSON.stringify(payload);
			$.ajax({
				type: "POST",
				url: 'https://outlook.office.com/api/v2.0/me/events',
				headers: {'Authorization': 'Bearer ' + token,
						  'Content-Type': 'application/json',
						 },
				data: json,
				'error': function(jqXHR, textStatus, errorThrown) {
					console.log(jqXHR)
				},
				'success': function(res) {
					console.log(res);
					alert("success");
				}	
			});*/
			console.log("printing out " + this.state.listOfEvents[i]);
		}
		this.removeAllAddedEvent();
	},
    render: function() {
        return (
        	<div classNa="load-container">
	            {/*<Header />*/}
	            <LeftCol events={this.state.events} 
	            		 remove={this.remove} 
	            		 newQuery={this.newQuery} 
	            		 addEvent={this.addEvent} />
	            <RightCol listOfEvents={this.state.listOfEvents} addToCalendar={this.addToCalendar}/>
	        </div>
        )
    }
});

module.exports = Container;