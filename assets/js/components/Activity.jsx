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
		place: React.PropTypes.object.isRequired,
		url: React.PropTypes.string.isRequired,
		image: React.PropTypes.string.isRequired,
		remove: React.PropTypes.func.isRequired,
		event: React.PropTypes.object.isRequired,
		giveLink: React.PropTypes.func.isRequired,
	},

	stripHTML: function(html)
	{
	   var tmp = document.createElement("DIV");
	   tmp.innerHTML = html;
	   return tmp.textContent || tmp.innerText || "";
	},

    render: function() {
    	start = new Date(this.props.start_time);
    	end = new Date(this.props.start_time);
    	startMinutes = start.getMinutes() < 10 ? "0" + start.getMinutes() : start.getMinutes();
    	endMinutes = end.getMinutes() < 10 ? "0" + end.getMinutes() : end.getMinutes();
    	
    	startDate = start.getMonth() + "/" + start.getDate() + "/" + start.getFullYear() + " " + start.toLocaleTimeString();
        endDate = end.getMonth() + "/" + end.getDate() + "/" + end.getFullYear() + " " + end.toLocaleTimeString();
        var body = this.stripHTML(this.props.description)
        return (
        	<Row className="load-activity">
	            <Col md={5} className="activity-image-container"><img className="activity-image" src={this.props.image} /></Col>
	            <Col md={6} className="activity-content-body">
		            <div className="activity-title"><b>Event:</b> {this.props.giveLink(this.props.event)}</div>
		            <p className="activity-body">{body}</p>
		            <p className="activity-date"><b>When:</b> {startDate} - {endDate}</p>
		            <p className="activity-location"><b>Where:</b> {this.props.place.street} {this.props.place.city}, {this.props.place.state}</p>
		            <Button bsStyle="danger" onClick={this.props.remove.bind(null, this.props.name)}><Glyphicon glyph="remove" /></Button>
		            <Button bsStyle="success" className="activity-url" onClick={this.props.add.bind(null, this.props.event)}>Add to List</Button>
	            </Col>
	        </Row>
        )
    }
});

module.exports = Activity;