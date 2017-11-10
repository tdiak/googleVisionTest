import React from 'react';
import Dropzone from 'react-dropzone'


export default class AddPhoto extends React.Component{
	constructor(props){
		super(props);
		this.state = {
			'current_image': null
		}
	}

	submitForm(){
		console.log(this.state.current_image);

		let formData  = new FormData();
		formData.append('filename', this.state.current_image.name);
		formData.append('file', this.state.current_image);


		fetch(location.href + "photos/", {
	      method: "POST",
	      body: formData
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

	onDrop(acceptedFiles, rejectedFiles) {
		console.log(acceptedFiles);
		if(acceptedFiles.length)
			this.setState({'current_image': acceptedFiles[0]});
	}

	render(){
		return (
			<form className="add-form">
				<Dropzone onDrop={this.onDrop.bind(this)}>
					{this.state.current_image ? <p>{this.state.current_image.name }}</p> : <p>Drag files here !!</p>}
				</Dropzone>
				<button type="button" onClick={this.submitForm.bind(this)}>Send photo!</button>
			</form>
		)
	}
}