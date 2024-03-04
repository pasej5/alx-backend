import { createClient } from 'redis';

const client = createClient();

function redisConnect() {
  client
    .on('connect', function () {
      console.log('Redis client connected to the server');
    })
    .on('error', (err) => {
      console.log(`Redis client not connected to server: ${err}`);
    });
}

function setNewSchool(schoolName, value) {
  client.set(schoolName, value, print);
}

function displaySchoolValue(schoolName) {
  client.get(schoolName, function (error, result) {
    if (error) {
      console.log(error);
      throw error;
    }
  });
  console.log(result);
}

displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');
