var React = require('react');

var AddedEvents = React.createClass ({
	propTypes: {
		event: React.PropTypes.object.isRequired,
        giveLink: React.PropTypes.func.isRequired,
	},
    render: function() {
        start = new Date(this.props.event.start_time);
        end = new Date(this.props.event.start_time);
        startMinutes = start.getMinutes() < 10 ? "0" + start.getMinutes() : start.getMinutes();
        endMinutes = end.getMinutes() < 10 ? "0" + end.getMinutes() : end.getMinutes();
        
        startDate = start.getMonth() + "/" + start.getDate() + "/" + start.getFullYear() + " " + start.toLocaleTimeString();
        endDate = end.getMonth() + "/" + end.getDate() + "/" + end.getFullYear() + " " + end.toLocaleTimeString();
        
        return (
    		<div>
    			<b>Event:</b> {this.props.giveLink(this.props.event)}
    			<br />
                <b>When:</b> {startDate} - {endDate}
                <br />
                <b>Where:</b> {this.props.event.place.street} {this.props.event.place.city}, {this.props.event.place.state}
                <hr />
    		</div>
        )
    }
});

module.exports = AddedEvents;