var React = require('react');
var Button = require('react-bootstrap').Button;

var Button = require('react-bootstrap').Button;
var Row = require('react-bootstrap').Row;
var Col = require('react-bootstrap').Col;
var Glyphicon = require('react-bootstrap').Glyphicon;

var Activity = React.createClass ({
	propTypes: {
		id: React.PropTypes.number.isRequired,
		title: React.PropTypes.string.isRequired,
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
		            <div className="activity-title"><a href={this.props.url}>{this.props.title}</a></div>
		            <p className="activity-body">This is the article body that will show you how great the event will beqweqweqweqweqweqwewq eqwewq qweqwe qweqw ewqe wqeqw eqwe qwewq ewq eqwe qweqw eqwe qweqw ewqe qweqw ewqe qwe qwe qwewq eqw eqwe qwe</p>
		            <Button bsStyle="success" className="activity-url" onClick={this.props.add.bind(null, this.props.event)}>Add to List</Button>
		            <p className="activity-date">Date</p>
		            <p className="activity-location">Location</p>
		            <Button bsStyle="danger" onClick={this.props.remove.bind(null, this.props.id)}>X</Button>
	            </Col>
	        </Row>
        )
    }
});

module.exports = Activity;