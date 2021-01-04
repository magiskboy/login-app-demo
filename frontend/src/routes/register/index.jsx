import React from 'react'
import { Provider, connect } from 'react-redux'
import { Link } from 'react-router-dom'
import * as registerAction from '../../actions/register'
import style from './style'


class Register extends React.Component {
  constructor(props) {
    super(props)

    this.state = {
      username: "",
      email: "",
      password: ""
    }

    this.changedUsername = this.changedUsername.bind(this)
    this.changedEmail = this.changedEmail.bind(this)
    this.changedPassword = this.changedPassword.bind(this)
    this.onSubmit = this.onSubmit.bind(this)
  }

  changedUsername(event) {
    this.setState({ username: event.target.value })
  }

  changedEmail(event) {
    this.setState({ email: event.target.value })
  }

  changedPassword(event) {
    this.setState({ password: event.target.value })
  }

  onSubmit() {
    this.props.submitRegisterUser(this.state)
  }

  render() {
    return (
      <div id="register">
        <div className="form">
          <div className="header">Register</div>
          <div className="body">
              <input type="text" placeholder="Username" onChange={this.changedUsername} required />
              <input type="email" placeholder="Email" onChange={this.changedEmail} required />
              <input type="password" placeholder="Password" onChange={this.changedPassword} required />
          </div>
          <div className="footer">
            <button onClick={this.onSubmit} className="btn btn-primary">Register</button>
          </div>
        </div>
      </div>
    )
  }
}

export default connect((state) => {
  return {
    user: state.login.user
  }
}, (dispatch) => {
  return {
      submitRegisterUser: (content) => {
          dispatch(registerAction.actionCreator(content))
      }
  }
})(Register)
