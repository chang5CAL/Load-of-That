var React = require('react');
var Button = require('react-bootstrap').Button;

var Button = require('react-bootstrap').Button;
var Row = require('react-bootstrap').Row;
var Col = require('react-bootstrap').Col;
var Glyphicon = require('react-bootstrap').Glyphicon;

var style = {paddingLeft: "5px",}

var Activity = React.createClass ({
	propTypes: {
		name: React.PropTypes.string.isRequired,
		description: React.PropTypes.string.isRequired,
		start_time: React.PropTypes.string.isRequired,
		end_time: React.PropTypes.string.isRequired,
		url: React.PropTypes.string.isRequired,
		image: React.PropTypes.string.isRequired,
		remove: React.PropTypes.func.isRequired,
		event: React.PropTypes.object.isRequired,
	},

    render: function() {
        return (
        	<Row className="load-activity">
	            <Col md={5} className="activity-image-container"><img className="activity-image" src={this.props.image} /></Col>
	            <Col md={6} className="activity-content-body">
		            <div className="activity-title"><b>Event:</b> <a href={this.props.url}>{this.props.name}</a></div>
		            <p className="activity-body">{this.props.description}</p>
		            <p className="activity-date"><b>When:</b> {this.props.start_time} - {this.props.end_time}</p>
		            <p className="activity-location"><b>Where:</b> Location</p>
		            <Button bsStyle="danger" onClick={this.props.remove.bind(null, this.props.name)}><Glyphicon glyph="remove" /></Button>
		            <Button bsStyle="success" className="activity-url" onClick={this.props.add.bind(null, this.props.event)}>Add to List</Button>
	            </Col>
	        </Row>
        )
    }
});

module.exports = Activity;