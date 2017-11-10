import React from 'react';
import Modal from 'react-modal';


export default class Item extends React.Component{
	constructor(props){
		super(props);
		console.log(this);
		this.state = {
			'modalIsOpen': false
		}
	}

	changeModal(){
		this.setState({'modalIsOpen': !this.state.modalIsOpen})
	}

	render(){
		return (
			<li className="item col-md-3" onClick={this.changeModal.bind(this)}>
				<p>{this.props.item.filename}</p>
				<img src={this.props.item.file} />
				<div className="row">
					<button className="btn btn-primary col-md-3 col-md-offset-2">More</button>
					<button className="btn btn-danger col-md-3 col-md-offset-2">Delete</button>
				</div>
				<Modal
				  isOpen={this.state.modalIsOpen}
				  onRequestClose={this.changeModal.bind(this)}
				  aria={{
				    labelledby: "{this.props.item.filename}",
				  }}>
					  <h1 id="heading">{this.props.item.filename}</h1>
					  <div id="full_description row">
					    <img class="col-md-6" src={this.props.item.file} />
					    
					    <ul class="col-md-2">
					    	<h2>Colors</h2>
					    	{this.props.item.color_set.map(function(object, i){
								return <li><p> - ({object.red}, {object.green}, {object.blue})</p></li>
							})}
					    </ul>

					    <ul class="col-md-2">
					    	<h2>Labels</h2>
					    	{this.props.item.label_set.map(function(object, i){
								return <li><p> - {object.label}</p></li>
							})}
					    </ul>

					    <ul class="col-md-2">
					    	<h2>Emotions</h2>
					    	{this.props.item.emotion_set.map(function(object, i){
								return <li><p> - {object.emotion_type} : {object.result}</p></li>
							})}
					    </ul>
					  </div>
				</Modal>
			</li>
		)
	}
}