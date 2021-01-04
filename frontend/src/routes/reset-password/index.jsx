import React from 'react'
import { Provider, connect } from 'react-redux'
import * as resetPasswordAction from '../../actions/reset-password'
import style from './style'


class ResetPassword extends React.Component {
  constructor(props) {
    super(props)

    this.state = {
      username: "",
      email: ""
    }

    this.changedUsername = this.changedUsername.bind(this)
    this.changedEmail = this.changedEmail.bind(this)
    this.onSubmit = this.onSubmit.bind(this)
  }

  changedUsername(event) {
    this.setState({ username: event.target.value })
  }

  changedEmail(event) {
    this.setState({ email: event.target.value })
  }

  onSubmit() {
    this.props.resetPasswordUser(this.state.email, this.state.username)
  }

  render() {
    return (
      <div id="reset-password">
        <div className="form">
          <div className="header">Reset password</div>
          <div className="body">
              <input type="text" placeholder="Username" onChange={this.changedUsername} required />
              <input type="email" placeholder="Email" onChange={this.changedEmail} required />
          </div>
          <div className="footer">
            <button onClick={this.onSubmit} className="btn btn-primary">Submit</button>
          </div>
        </div>
      </div>
    )
  }
}

export default connect(state => {
  return {
      user: state.login.user
  }

}, dispatch => {
  return {
      resetPasswordUser: (email, username) => {
          dispatch(resetPasswordAction.actionCreator(email, username))
      }
  }
})(ResetPassword)
