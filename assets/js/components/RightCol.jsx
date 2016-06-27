var React = require('react');
var AddedEvents = require('./AddedEvents')
var Button = require('react-bootstrap').Button;

var RightCol = React.createClass ({
	propTypes: {
		listOfEvents: React.PropTypes.array.isRequired,
		addToCalendar: React.PropTypes.func.isRequired,
	},
	componentDidMount: function() {
		this.startPolling()
		//console.log(document.getElementById("logged_in").value);	
	},
	startPolling: function() {
		setTimeout(this.reload, 2000)
	},
	reload: function() {
		console.log("reload called");
		this.forceUpdate()
	},
	login: function() {
		console.log(document.getElementById("logged_in").value);
		console.log(document.getElementById("email_type").value);
		if (document.getElementById("logged_in").value == "True") {
			var type = document.getElementById("email_type").value.replace("_", " ");
			return (
				<div><h1>Events</h1> 
				<h3>You're currently logged into {type}</h3></div>
			);
		} else {
			return(
				<div>
					<h1>Events</h1>
					You have to be logged in to save your events to your calendar:
					<br />
					<a className="btn btn-social btn-microsoft" href="https://login.microsoftonline.com/common/oauth2/v2.0/authorize?client_id=003a3ad3-9d6a-493d-820e-6738c415f350&response_type=code&redirect_uri=http://localhost:8000/api/test&scope=openid https://outlook.office.com/calendars.readwrite&state=12345&nonce=678910">
						<span className="fa fa-windows"></span>Add To Outlook Calendar</a>
					<p />

    				<button className="btn btn-social btn-google" id="authorize-button"><span className="fa fa-google"></span>Add To Google Calendar</button>
					{/*<a href="https://accounts.google.com/o/oauth2/v2/auth?client_id=1084307285600-c271knciittbj18tj02nornfvmangnoa.apps.googleusercontent.com&response_type=code&scope=openid https://www.googleapis.com/auth/calendar&redirect_uri=http://localhost:8000/api/google&state=12345">
						Google</a>*/}
				</div>
			);
		}
	},
	checkout: function() {
		if (document.getElementById("logged_in").value == "True") {
			return (<Button bsSize="large" bsStyle="primary" onClick={this.props.addToCalendar}>Save To Calendar</Button>)
		} else {
			return;
		}
	},
    render: function() {
    	var listEvents = this.props.listOfEvents.map(function(event) {
        	return <AddedEvents key={event.id} event={event} />;
        }.bind(this));

        return (
        	<div className="load-right-col">
	            {this.login()}
	            <ul>
	            	{listEvents}
	            </ul>
	           	{this.checkout()}
	        </div>
        );
    }
});

module.exports = RightCol;