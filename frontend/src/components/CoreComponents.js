import React, { Component } from 'react';
import {  Button} from 'semantic-ui-react'


class CoreContent extends Component {
  render() {
    return (
		<div className="CoreContent">
			
			
        <Button onClick={this.props.toggle}>Toggle Visibility</Button>
		</div>
	)
  }
}

export default CoreContent;
	



	
