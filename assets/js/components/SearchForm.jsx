var React = require('react');


var SearchForm = React.createClass ({
    hello: function(message) {
    	alert(message);
    },
    render: function() {
    	var asd = this.hello.bind(this, "adsfasdq234");
        return (
        	<div className="load-search-form">
	            <form>
	            	Location: <input type="text" />
	            	<br />
	            	Type: <input type="text" />
	            	<br />
	            </form>
	            <button onClick={asd}>Submit</button>
	        </div>
        )
    }
});

module.exports = SearchForm;