import { createClient } from 'redis';

const client = await createClient()
  .on('error', err => console.log('Redis Client Error', err))
  .connect();

await client.set('key', 'value');
const value = await client.get('key');
await client.disconnect();


i//mport { createClient } from 'redis';

//const client = createClient();

//client.on('error', err => console.log('Redis Client Error', err));

a//wait client.connect();