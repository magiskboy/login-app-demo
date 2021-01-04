import ReactDOM from 'react-dom'
import { createStore } from 'redux'
import reducers from './reducers'
import { Provider } from 'react-redux'
import { BrowserRouter, Route } from 'react-router-dom'
import Navigator from './components/navigator'
import Login from './routes/login'
import Register from './routes/register'
import Home from './routes/home'
import ResetPassword from './routes/reset-password'
import SetPassword from './routes/set-password'
import style from './style'


const store = createStore(reducers)

class Application extends React.Component {
  constructor(props) {
    super(props)
  }

  render() {
    return (
      <BrowserRouter>
        <Navigator siteName="Login Project" />
        <Route exact path="/" component={Home} />
        <Route exact path="/login" component={Login} />
        <Route exact path="/register" component={Register} />
        <Route exact path="/password/set" component={SetPassword} />
        <Route exact path="/password/reset" component={ResetPassword} />
      </BrowserRouter>
    )
  }
}

export default class ApplicationBootstrapping extends React.Component {
  constructor(props) {
    super(props)
  }

  render() {
    return (
      <Provider store={store}>
        <Application />
      </Provider>
    )
  }
}

ReactDOM.render(<ApplicationBootstrapping />, document.getElementById('root'))
