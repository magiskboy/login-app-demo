const type = 'LOGIN'

const actionCreator = (content, callback) => {
  return {
    type,
    content,
    callback
  }
}

export { type, actionCreator }
