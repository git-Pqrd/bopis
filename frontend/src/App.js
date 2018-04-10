import React, { Component } from 'react';
import { Sidebar, Segment } from 'semantic-ui-react'
import CoreContent from './components/CoreComponents.js'
import SideBarContent from './components/sidebar.js'

class app extends Component {
	constructor () {
		super()
		this.state = {visible: false }

	}


	render() {
	const handleToggleVisibility = () => {
		this.setState({ visible: !this.state.visible })

	}
    return (
      <div>
		
		<Sidebar.Pushable as={Segment}>
			<SideBarContent visible={this.state.visible} />
		  
		  <Sidebar.Pusher>
            <Segment basic>
			<CoreContent toggle={handleToggleVisibility} />
			</Segment>
          </Sidebar.Pusher>
	  
	  </Sidebar.Pushable>
      </div>
    )
  }
}


export default app;
