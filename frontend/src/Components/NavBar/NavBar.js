import React, { useState } from 'react'
import { connect } from 'react-redux'
import { store } from '../../store'
import { Nav } from 'react-bootstrap'
import { Tabs, Input,Avatar} from 'antd'
import { useHistory } from 'react-router-dom'
import { update_isLoggedIn, update_Username } from '../../redux/actions/actions'
import Login from '../Modals/Login/Login'
import def_Avatar from '../../images/avatar.png'
import './NavBar.css'

let logged;
const { Search } = Input;

function mapStateToProps(state) {
  return {
    Username: state.Username,
    isLoggedIn: state.isLoggedIn,
    Avatar:state.Avatar,
  };
}

const NavBar = (props) => {
  const { TabPane } = Tabs;
  const history = useHistory()
  const [show, setShow] = useState(false)
  const avatar = props.Avatar
  const [text,settext] = useState("")

  function onShow() {
    setShow(true)
  }

  function onHide() {
    setShow(false)
  }

  function onSearch() {
    if (text.trim()) {
      history.push('/' + text + '/Stats/page=1')
    }
  }
  function LogOut() {
    store.dispatch(update_isLoggedIn(false))
    store.dispatch(update_Username(""))
  }
  
  function callback(tab) {
    if (tab === 'Play') {
      history.push('/' + tab)
    } 
    else {
      history.push('/' + tab + '/page=1')
    }
  }
  
  if (!props.isLoggedIn) {
    logged = 
    <Nav.Link style = {{ color: "white" }} onClick = { onShow } > Log In </Nav.Link>

  } else {
    logged = < Nav.Link style = {{ color: "white" }} onClick = { LogOut }> Log Out</Nav.Link>
  }
  const path = String(window.location.pathname) + '/'
  const start_pos = path.indexOf('/') + 1;
  const end_pos = path.indexOf('/', start_pos);
  const activeTab = path.substring(start_pos, end_pos)
    
  return ( 
    <div className = "nav">
      <div className = "nav-tabs">
        <Tabs style = {{ color: "white" }} defaultActiveKey = { activeTab } onChange = { callback }>
          <TabPane tab = "Play" key = "Play"></TabPane> 
          <TabPane tab = "Stats" key = "Stats"></TabPane>
          <TabPane tab = "Forum" key = "Forum"></TabPane>
        </Tabs> 
      </div> 
      <div className = "nav-right">
        <li className = "nav-logbtn" >{ logged }</li>
        <li className = "nav-avatar" style={{display:!props.isLoggedIn ? "none":""}} ><Avatar src={avatar ? avatar: def_Avatar }/></li>
        <li className = "nav-search">< Search onSearch={onSearch} onChange={(e) =>settext(e.target.value)} value={text} placeholder = "Search User.."/></li> 
        <li><Login show = { show } onHide = { onHide }/></li>
      </div> 
    </div>
  );
}
export default connect(mapStateToProps)(NavBar);