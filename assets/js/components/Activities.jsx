var React = require('react');
var Activity = require('./Activity')

var Activities = React.createClass ({
	propTypes: {
		//events: React.PropTypes.array.isRequired,
	},

	getDefaultProps: function() {
		return {
			events: []
		}
	},
    render: function() {
    	var listEvents = this.props.events.map(function(event) {
        	return <Activity title={event.title} url={event.url} image={event.image} />;
        });
        return (
        	<div className="load-activities">
	            <h1>
	            Activities
	            </h1>
	            {listEvents}
	        </div>
        )
    }
});

module.exports = Activities;