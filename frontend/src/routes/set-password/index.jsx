import React from 'react'
import { Provider, connect } from 'react-redux'
import * as setPasswordAction from '../../actions/set-password'
import style from './style'


class SetPassword extends React.Component {
  constructor(props) {
    super(props)

    this.state = {
      currentPassword: "",
      newPassword: ""
    }

    this.changedCurrentPassword = this.changedCurrentPassword.bind(this)
    this.changedNewPassword = this.changedNewPassword.bind(this)
    this.onSubmit = this.onSubmit.bind(this)
  }

  changedCurrentPassword(event) {
    this.setState({ currentPassword: event.target.value })
  }

  changedNewPassword(event) {
    this.setState({ newPassword: event.target.value })
  }

  onSubmit() {
    this.props.setPasswordUser(
      this.state.currentPassword,
      this.state.newPassword
    )
  }

  render() {
    return (
      <div id="login">
        <div className="form">
          <div className="header">Set password</div>
          <div className="body">
              <input type="password" placeholder="Current password" onChange={this.changedCurrentPassword} required />
              <input type="password" placeholder="New password" onChange={this.changedNewPassword} required />
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
      setPasswordUser: (currentPassword, newPassword) => {
          dispatch(
              setPasswordAction.actionCreator(currentPassword, newPassword)
          )
      }
  }
})(SetPassword)
