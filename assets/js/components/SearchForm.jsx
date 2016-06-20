var React = require('react');


var SearchForm = React.createClass ({
	getInitialState: function() {
		return {
			location: "Seattle",
			type: "code",
		};
	},
	propTypes: {
		newQuery: React.PropTypes.func.isRequired,
	},
    handleLocationChange: function(e) {
    	this.setState({
    		location: e.target.value,
    	});
    },
    handleTypeChange: function(e) {
    	this.setState({
    		type: e.target.value,
    	})
    },
    render: function() {
        return (
        	<div className="load-search-form">
	            <form>
	            	Location: <input type="text" value={this.state.location} onChange={this.handleLocationChange} />
	            	<br />
	            	Type: <input type="text" value={this.state.type} onChange={this.handleTypeChange} />
	            	<br />
	            </form>
	            <button onClick={this.props.newQuery.bind(null, this.state.location, this.state.type)}>Submit</button>
	        </div>
        )
    }
});

module.exports = SearchForm;