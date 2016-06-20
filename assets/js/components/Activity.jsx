var React = require('react');

var Activity = React.createClass ({
	propTypes: {
		title: React.PropTypes.string.isRequired,
		url: React.PropTypes.string.isRequired,
		image: React.PropTypes.string.isRequired,
	},

    render: function() {
        return (
        	<div className="load-activity">
	            <div className="activity-image-container"><img className="activity-image" src={this.props.image} /></div>
	            <div className="activity-content-body">
		            <div className="activity-title"><a href={this.props.url}>{this.props.title}</a></div>
		            <p className="activity-body">This is the article body that will show you how great the event will be</p>
		            <button className="activity-url">Add to Calendar </button>
		            <p className="activity-date">Date</p>
		            <p className="activity-location">Location</p>
	            </div>
	        </div>
        )
    }
});

module.exports = Activity;