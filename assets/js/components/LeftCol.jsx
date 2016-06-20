var React = require('react');
var SearchForm = require('./SearchForm.jsx')
var Activities = require('./Activities')

var LeftCol = React.createClass ({
	getInitialState: function() {
		return {
			events: [{title: "Gameworks", url:"http://gameworks.com", image: "http://www.newportonthelevee.com/Portals/newportonthelevee/Images/Directory/Gameworks.png"}, 
					 {title: "Dave and Busters", url: "http://www.daveandbusters.com/", image: "http://www.daveandbusters.com/media/1023/logo_no_shadow.png"}, 
					 {title: "Disney Land", url: "https://disneyland.disney.go.com/", image: "https://s-media-cache-ak0.pinimg.com/236x/e0/71/0d/e0710d8c6cf4c5b707fd55375e9c740c.jpg"}]
		};
	},
    render: function() {
        return (
        	<div className="load-left-col">
	            <div>
	            	<SearchForm />
	            	<Activities events={this.state.events} />
	            </div>
	        </div>
        )
    }
});

module.exports = LeftCol;