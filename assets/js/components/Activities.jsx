var React = require('react');
var Activity = require('./Activity')


var Activities = React.createClass ({
	propTypes: {
		events: React.PropTypes.array.isRequired,
		remove: React.PropTypes.func.isRequired,
		addEvent: React.PropTypes.func.isRequired,
	},

	getDefaultProps: function() {
		return {
			events: [],
		}
	},
    render: function() {
    	var listEvents = this.props.events.map(function(event) {
    		console.log("empty results");
    		// NO_IMAGE path saved on URL: leads to /static/img
    		var image_url = NO_IMAGE;
    		if (event.image != "") {
    			image_url = event.image;
    		}
        	return (<div key={event.id}><Activity 
        					 id={event.id}
        					 title={event.title} 
        					 url={event.url} 
        					 image={event.image}
        					 remove={this.props.remove}
        					 add={this.props.addEvent}
        					 event={event} /><hr className="activity-hr" /></div>);
        }.bind(this));
        return (
        	<div className="load-activities">
	            <h1>
	            Events
	            <hr className="activity-hr" />
	            </h1>
	            {listEvents}
	        </div>
        );
    }
});

module.exports = Activities;