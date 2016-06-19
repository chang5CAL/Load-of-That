var React = require('react');
var Header = require('./Header.jsx')
var LeftCol = require('./LeftCol.jsx')
var RightCol = require('./RightCol.jsx')

var style = {
	backgroundColor: "#ddd6f3"
}

var Container = React.createClass ({
    render: function() {
        return (
        	<div class="load-container" style={style}>
	            <h1>
	            Container
	            </h1>
	            <Header />
		            <LeftCol />
		            <RightCol />
	        </div>
        )
    }
});

module.exports = Container;