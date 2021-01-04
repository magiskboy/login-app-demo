import * as jQuery from 'jquery'
import * as loginAction from '../actions/login'
import * as registerAction from '../actions/register'
import * as logoutAction from '../actions/logout'
import * as resetPasswordAction from '../actions/reset-password'
import * as setPasswordAction from '../actions/set-password'


const BACKEND_SERVER = 'http://localhost:5000'
const LOGIN_URL = '/session'
const LOGOUT_URL = '/session'
const PASSWORD_RESET_URL = '/password/reset'
const GET_USER_URL = '/user'
const SET_PASSWORD_URL = '/user'
const REGISTER_URL = '/user'

const defaultState = {
  user: {
    username: '',
    email: '',
    is_active: false
  },
  is_login: false
}

export default function loginReducer(prevState = defaultState, action) {
  let nextState = Object.assign({}, prevState)
  switch (action.type) {
    case loginAction.type: {
      const payload = {
        username: action.content.username,
        password: action.content.password
      }
      jQuery.ajax({
        url: BACKEND_SERVER + LOGIN_URL,
        method: 'POST',
        async: false,
        contentType: 'application/json',
        dataType: 'json',
        data: JSON.stringify(payload),
        success: (result, status, xhr) => {
          console.log(result)
          localStorage.setItem("access_token", result.access_token)
          localStorage.setItem("refresh_token", result.refresh_token)
          jQuery.ajax({
            url: BACKEND_SERVER + LOGIN,
            method: 'GET',
            beforeSend: (xhr, settings) => {
              xhr.setRequestHeader('Authorization', `Bearer ${result.access_token}`)
            },
            async: false,
            dataType: 'json',
            success: (result, status, xhr) => {
              nextState.user = result
              nextState.is_login = true
              return nextState
            },
            error: (xhr, status, error) => {
              console.error(error)
              return nextState
            }
          })
        },
        error: (xhr, status, error) => {
          console.error(error)
          return nextState
        },
      })
    }

    case registerAction.type: {
      const payload = {
        username: action.username,
        email: action.email,
        password: action.password
      }
        console.log(payload)

      jQuery.ajax({
        url: BACKEND_SERVER + REGISTER_URL,
        method: 'POST',
        contentType: 'application/json',
        data: payload,
        async: false,
        success: (result, status, xhr) => {
          if (status === 401) {
            console.error(result.message)
          }
          else if (status === 201) {
            console.log(result)
          }
        },
        error: (xhr, status, error) => {
          console.error(error)
        }
      })

      return nextState
    }

    case logoutAction.type: {
      // Send ajax request to server for logout

      // Clear user
      nextState.user = {
        username: '',
        email: '',
        password: ''
      }
      nextState.is_login = false
      return nextState
    }

    case resetPasswordAction.type: {
      console.log('Reset password with data', action)
      return nextState
    }

    case setPasswordAction.type: {
      console.log('Set password with data', action)
      return nextState
    }

    default:
      return prevState
  }
}
