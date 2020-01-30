const axios = require('axios')

axios.post('http://localhost:3222', {
  todo: 'Buy the milk'
})
.then((res) => {
  console.log(`statusCode: ${res.statusCode}`)
  console.log(res)
})
.catch((error) => {
  console.error(error)
})