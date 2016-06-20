var React = require('react');

var Activity = React.createClass ({
	propTypes: {
		title: React.PropTypes.string.isRequired,
	},
    render: function() {
        return (
        	<div className="load-activity">
	            <div className="activity-image"><img src="https://pbs.twimg.com/profile_images/606867814025162752/Q3_J5qKH.jpg" /></div>
	            <div className="activity-content-body">
		            <div className="activity-title">{this.props.title}</div>
		            <p className="activity-body">This is the article body that will show you how great the event will be</p>
		            <button className="activity-url">Visit Site</button>
		            <p className="activity-date">Date</p>
		            <p className="activity-location">Location</p>
	            </div>
	        </div>
        )
    }
});

module.exports = Activity;