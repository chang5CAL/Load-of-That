var React = require('react');

var SearchForm = React.createClass ({
    render: function() {
        return (
        	<div className="load-search-form">
	            <form>
	            	Location: <input type="text" />
	            	<br />
	            	Type:     <input type="text" />
	            	<br />
	            	<button>Submit</button>
	            </form>
	        </div>
        )
    }
});

module.exports = SearchForm;