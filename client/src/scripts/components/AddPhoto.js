import React from 'react';
import Dropzone from 'react-dropzone'


export default class AddPhoto extends React.Component{
	constructor(props){
		super(props);
		this.state = {
			'current_image': null
		}
		this.extensions = ['jpg', 'jpeg', 'png']
	}

	submitForm(){
		console.log('test');
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
				<button type="button">Send photo!</button>
			</form>
		)
	}
}