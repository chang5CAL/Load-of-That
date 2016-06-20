var React = require('react');
var Activity = require('./Activity')

var Activities = React.createClass ({
    render: function() {
        return (
        	<div className="load-activities">
	            <h1>
	            Activities
	            </h1>
	            <Activity title="hello1" />
	            <Activity title="hello2"/>
	            <Activity title="hello3"/>
	            <Activity title="hello4"/>
	            <Activity title="hello5"/>
	            <Activity title="hello6"/>
	        </div>
        )
    }
});

module.exports = Activities;