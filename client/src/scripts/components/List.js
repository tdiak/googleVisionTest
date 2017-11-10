import React from 'react';
import Item from './Item';

export default class List extends React.Component{
	constructor(props){
		super(props);
		this.state = {
			'photos': []
		}
		this.get_images();
	}

	get_images(){
		fetch('http://localhost:8000/photos/')
		.then(result => result.json())
		.then(data => {
			this.setState({'photos': data})
		});
	}

	render(){
		return (
			<ul className="list row">
				{this.state.photos.map(function(object, i){
					return <Item item={object} key={object.id} />
				})}
			</ul>
		)
	}
}