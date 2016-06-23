var React = require('react');
var SearchForm = require('./SearchForm.jsx')
var Activities = require('./Activities')

var LeftCol = React.createClass ({
	propTypes: {
		events: React.PropTypes.array.isRequired,
		remove: React.PropTypes.func.isRequired,
		newQuery: React.PropTypes.func.isRequired,
		addEvent: React.PropTypes.func.isRequired,
	},
    render: function() {
        return (
        	<div className="load-left-col">
	            <div>
	            	<SearchForm newQuery={this.props.newQuery} />
	            	<Activities events={this.props.events} 
	            				remove={this.props.remove} 
	            				addEvent={this.props.addEvent} />
	            </div>
	        </div>
        )
    }
});

module.exports = LeftCol;