import React from 'react';
import AddPhoto from './AddPhoto'


export default class Header extends React.Component{
	constructor(props){
		super(props);
		this.state = {
			'title': 'Photos Uploader'
		}
	}

	render(){
		return (
			<header className="col-md-3">
				<h1>{this.state.title}</h1>
				<AddPhoto />
			</header>
		)
	}
}