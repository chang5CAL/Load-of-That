var React = require('react');
var Header = require('./Header.jsx')
var LeftCol = require('./LeftCol.jsx')
var RightCol = require('./RightCol.jsx')

var Container = React.createClass ({
    render: function() {
        return (
        	<div className="load-container">
	            <Header />
	            <LeftCol />
	            <RightCol />
	        </div>
        )
    }
});

module.exports = Container;