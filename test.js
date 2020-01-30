
const express = require('express');

const app = express();
app.use(express.json());

app.get('/', (req, res) => {
    res.send('<h1>Hello Fucking World GET</h1>');
});
app.post('/', (req, res) => {
    
    res.send(JSON.stringify(req.body) + 'POSTING RETURNNNNNNNNN');
});
  
const port = process.env.PORT || 3222
app.listen(port, () => console.log(`Listening on port${port}...`) );