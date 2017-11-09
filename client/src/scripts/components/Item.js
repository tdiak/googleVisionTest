import React from 'react';


export default class Item extends React.Component{
	constructor(props){
		super(props);
		console.log(this)
	}

	render(){
		return (
			<li className="item col-md-3">
				<p>{this.props.item.title}</p>
				<img src={this.props.item.img} />
				<div className="row">
					<button className="btn btn-primary col-md-3 col-md-offset-2">More</button>
					<button className="btn btn-danger col-md-3 col-md-offset-2">Delete</button>
				</div>
			</li>
		)
	}
}