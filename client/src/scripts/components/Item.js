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

	deletePhoto(id){
		fetch(location.href + "photos/" + id, {
	      method: "DELETE",
	    }).then(function (res) {
	      if (res.ok) {
	        location.reload();
	      } else if (res.status == 401) {
	        alert("Oops! ");
	      }
	    }, function (e) {
	      alert("Error submitting form!");
	    });
	}

	render(){
		return (
			<li className="item col-md-3">
				<p>{this.props.item.filename}</p>
				<img src={this.props.item.file} />
				<div className="row">
					<button className="btn btn-primary col-md-3 col-md-offset-2" onClick={this.changeModal.bind(this)}>More</button>
					<button className="btn btn-danger col-md-3 col-md-offset-2" onClick={() => this.deletePhoto(this.props.item.id)}>Delete</button>
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