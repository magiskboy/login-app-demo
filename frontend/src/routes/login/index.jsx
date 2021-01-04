import React from 'react'
import { connect } from 'react-redux'
import { Link, Redirect } from 'react-router-dom'
import style from './style'


class Login extends React.Component {
  constructor(props) {
    super(props)
    this.state = {
      username: "",
      password: ""
    }

    this.changedUsername = this.changedUsername.bind(this)
    this.changedPassword = this.changedPassword.bind(this)
    this.onSubmit = this.onSubmit.bind(this)
  }

  changedUsername(event) {
    this.setState({ username: event.target.value })
  }

  changedPassword(event) {
    this.setState({ password: event.target.value })
  }

  onSubmit() {
    this.props.submitLoginUser(this.state, (response, status) => {
      if (status == 201) {
        toastr.success("Login success")
      }
      else if (status == 401) {
        toastr.error("Login failure")
      }
    })
  }

  render() {
    return (
      <div id="login">
        {this.props.is_login && <Redirect to="/"></Redirect>}
        <div className="form">
          <div className="header">Login</div>
          <div className="body">
              <input type="text" placeholder="Username" onChange={this.changedUsername} required />
              <input type="password" placeholder="Password" onChange={this.changedPassword} required />
              <div className="link">
                <p>If don't have account, <Link className="bold no-decoration" to="/register">create new</Link>.</p>
                <p><Link className="bold no-decoration" to="/password/reset">I forget password!</Link>.</p>
              </div>
          </div>
          <div className="footer">
            <button onClick={this.onSubmit} className="btn btn-primary">Login</button>
          </div>
        </div>
      </div>
    )
  }
}

export default connect((state) => {
  return {
    user: state.login.user,
    is_login: state.login.is_login
  }
}, null)(Login)
