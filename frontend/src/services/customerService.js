
const baseUrl = '/api/customers'

const getAll = async () => {
    const response = await fetch(baseUrl)
    return await response.json()
}

const getDetail = async (pk) => {
    const response = await fetch(`${baseUrl}/${pk}`)
    return await response.json()
}

export default { getAll, getDetail }