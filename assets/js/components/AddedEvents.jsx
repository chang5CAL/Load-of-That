var React = require('react');

var AddedEvents = React.createClass ({
	propTypes: {
		event: React.PropTypes.object.isRequired,
	},
    render: function() {
        return (
    		<div>
    			{this.props.event.title}
    			<br />
    			{this.props.event.url}
                <hr />
    		</div>
        )
    }
});

module.exports = AddedEvents;