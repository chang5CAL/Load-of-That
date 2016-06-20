var React = require('react');

var Header = React.createClass ({
    render: function() {
        return (
        	<div className="load-header">
        		<div className="load-header-search">
	        		<img src="http://www.edwardsengineering.com/wp-content/uploads/2014/01/random-logo-e1390919001831.png" />
		            <input type="text" />
		        </div>
	            <div className="load-navigation">
	            	<ul>
		            	<li><a href="#test">Home</a></li>
		            	<li><a href="#test">About</a></li>
		            	<li><a href="#test">Contact Us</a></li>
	            	</ul>
	            </div>
            </div>
        )
    }
});

module.exports = Header;