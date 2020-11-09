import axios from 'axios'

let $axios = axios.create({
  baseURL: '/api/',
  timeout: 5000,
  headers: { 'Content-Type': 'application/json' }
})

// Request Interceptor
$axios.interceptors.request.use(function (config) {
  config.headers['Authorization'] = 'Fake Token'
  return config
})

// Response Interceptor to handle and log errors
$axios.interceptors.response.use(function (response) {
  return response
}, function (error) {
  // Handle Error
  console.log(error)
  return Promise.reject(error)
})

export default {
  getPeopleSearch (query) {
    return $axios.get(
      `search/keyword`,
      { params: { q: query } }
    )
      .then(response => response.data)
  },
  getPeopleData (id) {
    return $axios.get(
      `search/get/` + id.toString()
    )
      .then(response => response.data)
  }
}
