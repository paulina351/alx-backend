import { createClient } from 'redis';

const client = await createClient()
  .on('error', err => console.log('Redis Client Error', err))
  .connect();

await client.set('key', 'value');
const value = await client.get('key');
await client.disconnect();

const setNewSchool(schoolName, value) => {
    console.log(redis.print);
};

const displaySchoolValue(schoolName) => {

}


displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');