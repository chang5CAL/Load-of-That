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
        	return <Activity key={event.id} 
        					 id={event.id}
        					 title={event.title} 
        					 url={event.url} 
        					 image={event.image}
        					 remove={this.props.remove}
        					 add={this.props.addEvent}
        					 event={event} />;
        }.bind(this));
        return (
        	<div className="load-activities">
	            <h1>
	            Activities
	            </h1>
	            {listEvents}
	        </div>
        );
    }
});

module.exports = Activities;