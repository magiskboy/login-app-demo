const type = 'RESET_PASSWORD'

const actionCreator = (username, email) => {
    return {
        type,
        username,
        email
    }
}