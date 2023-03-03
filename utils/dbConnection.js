const mysql = require('mysql2');

const dbConnection = mysql.createPool({
    host: '127.0.0.1',
    user: 'root',
    password: '12345',
    database: 'nodejs_login'
});

module.exports = dbConnection.promise();