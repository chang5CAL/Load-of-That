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
			location: "",
			type: "",
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
	            <form className="form-inline">
	            	<Row className="show-grid">
		            	<FormGroup>
		            		<Col md={4}>
		            			<ControlLabel style={style}>Location </ControlLabel>
		            		</Col>
		            		<Col md={4}>
		            			<FormControl type="text" placeholder="Location" value={this.state.location} onChange={this.handleLocationChange}></FormControl>
		            		</Col>
		            	</FormGroup>
	            	</Row>
	            	<hr />
	            	<Row className="show-grid">
		            	<FormGroup>
		            		<Col md={4}>
		            			<ControlLabel style={style}>Activity </ControlLabel>
		            		</Col>
		            		<Col md={4}>
		            			<FormControl type="text" placeholder="Activity" value={this.state.type} onChange={this.handleTypeChange}></FormControl>
		            		</Col>
		            	</FormGroup>
	            	</Row>
	            </form>
	            <hr />
	            <Button bsStyle="default" onClick={this.props.newQuery.bind(null, this.state.location, this.state.type)}><Glyphicon glyph="search" /><b> Search</b></Button>
	        </div>
        )
    }
});

module.exports = SearchForm;