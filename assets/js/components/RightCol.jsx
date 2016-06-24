var React = require('react');
var AddedEvents = require('./AddedEvents')

var RightCol = React.createClass ({
	propTypes: {
		listOfEvents: React.PropTypes.array.isRequired,
	},
    render: function() {
    	var listEvents = this.props.listOfEvents.map(function(event) {
        	return <AddedEvents key={event.id} event={event} />;
        }.bind(this));

        return (
        	<div className="load-right-col">
	            <h1>Events</h1>
	            <ul>
	            	{listEvents}
	            </ul>
	        </div>
        );
    }
});

module.exports = RightCol;