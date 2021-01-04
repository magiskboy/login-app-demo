const type = 'REGSITER'

const actionCreator = (content) => {
  return {
    type,
    user: content
  }
}

export { type, actionCreator }