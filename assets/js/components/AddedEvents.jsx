var React = require('react');

var AddedEvents = React.createClass ({
	propTypes: {
		event: React.PropTypes.object.isRequired,
	},
    render: function() {
        return (
    		<div>
    			<b>Event:</b> {this.props.event.name}
    			<br />
    			{this.props.event.url}
                <br />
                <b>When:</b>
                <br />
                <b>Where:</b>
                <hr />
    		</div>
        )
    }
});

module.exports = AddedEvents;