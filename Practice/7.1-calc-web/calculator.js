// calculator.js
const express = require('express');
const bodyParser = require('body-parser');

const app = express();
const port = 3000;

app.use(bodyParser.json());

function calculateSimpleInterest(principal, rate, time) {
    const interest = (principal * rate * time) / 100;
    return interest;
}

app.post('/calculate_simple_interest', (req, res) => {
    const { principal, rate, time } = req.body;
    const interest = calculateSimpleInterest(principal, rate, time);
    res.json({ interest });
});

app.listen(port, () => {
    console.log(`Simple Interest Calculator web service is running at http://localhost:${port}`);
});
