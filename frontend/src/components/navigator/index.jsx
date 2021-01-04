import React from 'react'
import { connect } from 'react-redux'
import { BrowserRouter, Link } from 'react-router-dom'
import * as logoutAction from '../../actions/logout'
import style from './style'

class Navigator extends React.Component {
  constructor(props) {
    super(props)

    this.logoutUser = this.logoutUser.bind(this)
  }

  logoutUser() {
    this.props.logoutUser()
  } 

  render() {
    return (
      <div id="navigator">
        <div className="site-name">
          <Link className="no-decoration" to="/">{this.props.siteName}</Link>
        </div>
        <ul className="link-list">
          { this.props.is_login
            ? <React.Fragment>
              <li><Link to="/password/set">Set password</Link></li>
              <li><a href="#" onClick={this.logoutUser}>Logout</a></li>
            </React.Fragment>
            : <React.Fragment>
              <li><Link to="/login">Login</Link></li>
              <li><Link to="/register">Register</Link></li>
            </React.Fragment>
          }
        </ul>
      </div>
    )
  }
}

export default connect(state => {
  return {
    user: state.login.user,
    is_login: state.login.is_login
  }
}, dispatch => {
  return {
    logoutUser: () => {
      dispatch(logoutAction.actionCreator())
    }
  }
})(Navigator)
