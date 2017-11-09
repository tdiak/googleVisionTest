import React from 'react';
import Item from './Item';

export default class List extends React.Component{
	constructor(props){
		super(props);
		let photos = [];

		//mock
		for(let i=0; i<30; i++){
			let obj = {
				'id': i,
				'img': '/static/img/bg.jpg',
				'title': 'Title ' + i
			}

			photos.push(obj);
		}
		this.state = {
			'photos': photos
		}
	}

	render(){
		return (
			<ul className="list row">
				{this.state.photos.map(function(object, i){
					return <Item item={object} key={i} />
				})}
			</ul>
		)
	}
}