import React from 'react';
import ReactDOM from 'react-dom';
import Header from './components/Header';
import List from './components/List'


class App extends React.Component{
	render(){
		return (
			<div className="row wrapper">
				<Header />
				<List />
			</div>
		)
	}
}

ReactDOM.render(<App />, document.getElementById('app'));
