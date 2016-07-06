var React = require('react');
var Activity = require('./Activity')


var Activities = React.createClass ({
	propTypes: {
		events: React.PropTypes.array.isRequired,
		remove: React.PropTypes.func.isRequired,
		addEvent: React.PropTypes.func.isRequired,
        giveLink: React.PropTypes.func.isRequired,
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
            //console.log(event.place);
        	return (<div key={event.name}><Activity 
        					 name={event.name}
                             description={event.description}
                             start_time={event.start_time}
                             end_time={event.end_time} 
                             place={event.place}
        					 url={event.url} 
        					 image={image_url}
        					 remove={this.props.remove}
        					 add={this.props.addEvent}
        					 event={event}
                             giveLink={this.props.giveLink} /><hr className="activity-hr" /></div>);
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