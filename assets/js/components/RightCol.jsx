var React = require('react');

var style = {
	//"float": 'left'
}

var RightCol = React.createClass ({
    render: function() {
        return (
        	<div class="load-right-col" style={style}>
	            <h1>
	            RightCol
	            </h1>
	            Calendar
	        </div>
        )
    }
});

module.exports = RightCol;