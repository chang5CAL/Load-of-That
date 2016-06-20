var React = require('react');
var SearchForm = require('./SearchForm.jsx')
var Activities = require('./Activities')

var style = {
	//float: 'left'
}

var LeftCol = React.createClass ({
    render: function() {
        return (
        	<div className="load-left-col" style={style}>
	            <div>
	            	<SearchForm />
	            	<Activities />
	            </div>
	        </div>
        )
    }
});

module.exports = LeftCol;