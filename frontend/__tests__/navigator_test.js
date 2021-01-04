import React from 'react'
import { BrowserRouter } from 'react-router-dom'
import { Provider } from 'react-redux'
import { createStore } from 'redux'
import renderer from 'react-test-renderer'
import Navigator from '../src/components/navigator'
import reducers from '../src/reducers'


test("Login route", () => {
  const store = createStore(reducers)
  const component = renderer.create(
    <Provider store={store}>
      <BrowserRouter>
        <Navigator siteName="Test" />
      </BrowserRouter>
    </Provider>
  )
  let tree = component.toJSON()
  expect(tree).toMatchSnapshot()
})
