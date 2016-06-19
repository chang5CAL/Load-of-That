var React = require('react');
var Activity = require('./Activity')

var Activities = React.createClass ({
    render: function() {
        return (
        	<div class="load-activties">
	            <h1>
	            Activities
	            </h1>
	            <Activity />
	        </div>
        )
    }
});

module.exports = Activities;