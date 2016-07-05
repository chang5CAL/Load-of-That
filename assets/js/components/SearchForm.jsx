var React = require('react');
var FormGroup = require('react-bootstrap').FormGroup;
var FormControl = require('react-bootstrap').FormControl;
var ControlLabel = require('react-bootstrap').ControlLabel;
var Button = require('react-bootstrap').Button;
var Row = require('react-bootstrap').Row;
var Col = require('react-bootstrap').Col;
var Glyphicon = require('react-bootstrap').Glyphicon;

var style = {
	marginTop: "5px",
}

var SearchForm = React.createClass ({
	getInitialState: function() {
		return {
			city: "",
			state: "",
			country: "",
			type: "",

		};
	},
	propTypes: {
		newQuery: React.PropTypes.func.isRequired,
	},
    handleCityChange: function(e) {
    	this.setState({
    		city: e.target.value,
    	});
    },
    handleStateChange: function(e) {
    	this.setState({
    		state: e.target.value,
    	});
    },
    handleCountryChange: function(e) {
    	this.setState({
    		country: e.target.value,
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
	            <form className="form-inline">
	            	<Row className="show-grid">
		            	<FormGroup>
		            		<Col md={2}>
		            			<ControlLabel style={style}>Location </ControlLabel>
		            		</Col>
		            		<Col md={3} className="load-search-form-inputs">
		            			<FormControl type="text" placeholder="City" value={this.state.city} onChange={this.handleCityChange}></FormControl>
		            		</Col>
		            		<Col md={3}>
		            			<FormControl type="text" placeholder="State/Territory" value={this.state.state} onChange={this.handleStateChange}></FormControl>
		            		</Col>
		            		<Col md={3}>
		            			<FormControl type="text" placeholder="Country" value={this.state.country} onChange={this.handleCountryChange}></FormControl>
		            		</Col>
		            	</FormGroup>
	            	</Row>
	            	<hr />
	            	<Row className="show-grid">
		            	<FormGroup>
		            		<Col md={5} className="load-search-form-activity-label">
		            			<ControlLabel style={style}>Activity </ControlLabel>
		            		</Col>
		            		<Col md={4}>
		            			<FormControl type="text" placeholder="Activity" value={this.state.type} onChange={this.handleTypeChange}></FormControl>
		            		</Col>
		            	</FormGroup>
	            	</Row>
	            </form>
	            <hr />
	            <Button bsStyle="default" onClick={this.props.newQuery.bind(null, this.state.city, this.state.state, this.state.country, this.state.type)}><Glyphicon glyph="search" /><b> Search</b></Button>
	        </div>
        )
    }
});

module.exports = SearchForm;