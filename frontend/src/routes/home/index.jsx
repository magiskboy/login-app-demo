import React from 'react'
import { Redirect } from 'react-router-dom'
import { Provider, connect } from 'react-redux'
import style from './style'


class Home extends React.Component {
  constructor(props) {
    super(props)
  }

  render() {
    return (
      <div id="home">
        { !this.props.is_login && <Redirect to="/login"></Redirect>}
        <div className="heading">
          <h1>Hello, {this.props.user.username}</h1>
          <h1>Wellcome to Login Project</h1></div>
      </div>
    )
  }
}

export default connect((state) => {
  return {
    user: state.login.user,
    is_login: state.login.is_login
  }
}, null)(Home)
