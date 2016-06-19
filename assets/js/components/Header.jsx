var React = require('react');

var Header = React.createClass ({
    render: function() {
        return (
        	<div class="load-header">
        		<img src="http://www.edwardsengineering.com/wp-content/uploads/2014/01/random-logo-e1390919001831.png" />
	            <h1>Header</h1>
	            <h2>Search Bar</h2>
	            <div class="load-navigation">
	            	<h2>Home</h2>
	            	<h2>About</h2>
	            	<h2>Contact Us</h2>
	            </div>
            </div>
        )
    }
});

module.exports = Header;