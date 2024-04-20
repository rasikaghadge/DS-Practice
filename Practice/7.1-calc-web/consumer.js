// consumer.js
const axios = require('axios');

function calculateSimpleInterest(principal, rate, time) {
    const data = { principal, rate, time };
    axios.post('http://localhost:3000/calculate_simple_interest', data)
        .then(response => {
            console.log("Simple interest:", response.data.interest);
        })
        .catch(error => {
            console.error("Error:", error.message);
        });
}

// Example usage
calculateSimpleInterest(1000, 5, 2); // Change the values as per your requirement
