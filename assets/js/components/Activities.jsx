var React = require('react');
var Activity = require('./Activity')

var Activities = React.createClass ({
    render: function() {
        return (
        	<div className="load-activties">
	            <h1>
	            Activities
	            </h1>
	            <Activity />
	            <Activity />
	            <Activity />
	            <Activity />
	            <Activity />
	            <Activity />
	            <Activity />
	            <Activity />
	            <Activity />
	        </div>
        )
    }
});

module.exports = Activities;