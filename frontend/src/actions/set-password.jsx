const type = 'SET_PASSWORD'

const actionCreator = (currentPassword, newPassword) => {
    return {
        type,
        currentPassword,
        newPassword
    }
}