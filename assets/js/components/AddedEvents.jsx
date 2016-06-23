var React = require('react');

var AddedEvents = React.createClass ({
	propTypes: {
		event: React.PropTypes.object.isRequired,
	},
    render: function() {
        return (
        	<li className="load-added-event-list">
        		<div>
        			{this.props.event.title}
        			<br />
        			{this.props.event.url}
        		</div>
        	</li>
        )
    }
});

module.exports = AddedEvents;