var React = require('react');
var AddedEvents = require('./AddedEvents')

var RightCol = React.createClass ({
	propTypes: {
		listOfEvents: React.PropTypes.array.isRequired,
	},
	check: function() {
		if (document.getElementById("a-t")) {
			return (<div><h1>Events</h1> You're currently logged into Outlook</div>)
		} else {
			return(
				<div>
					<h1>Events</h1>
					You have to be logged in to save your data to your calendar:
					<a href="https://login.microsoftonline.com/common/oauth2/v2.0/authorize?client_id=003a3ad3-9d6a-493d-820e-6738c415f350&response_type=code&redirect_uri=http://localhost:8000/api/test&scope=openid Calendars.ReadWrite&state=12345&nonce=678910">
						Outlook</a> 
				</div>
			);
		}
	},
    render: function() {
    	var listEvents = this.props.listOfEvents.map(function(event) {
        	return <AddedEvents key={event.id} event={event} />;
        }.bind(this));

        return (
        	<div className="load-right-col">
	            {this.check()}
	            <ul>
	            	{listEvents}
	            </ul>
	        </div>
        );
    }
});

module.exports = RightCol;