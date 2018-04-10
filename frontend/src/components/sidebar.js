import React, { Component } from 'react';
import { Sidebar,  Menu,  Icon } from 'semantic-ui-react'



class SideBarContent extends Component  {
	render() {

	const hello = () => {
		console.log('value');
	} 
    return (
		 <Sidebar as={Menu} width='thin' visible={this.props.visible} icon='labeled' vertical inverted>
            <Menu.Item name='home'>
              <Icon name='home' />
              Home
            </Menu.Item>
            <Menu.Item name='gamepad'>
              <Icon name='gamepad' />
              Games
            </Menu.Item>
            <Menu.Item name='camera'>
              <Icon name='camera' />
              Channels
            </Menu.Item>
          </Sidebar>
		 
    );
  }
}

export default SideBarContent;
