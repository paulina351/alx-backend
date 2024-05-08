import { createClient } from 'redis';

const client = createClient();


const kue = require('kue')
    , queue = kue.createQueue();

queue.process('push_notification_code', function(job, done){
    push_notification_code(job.data.to, done);
});


function sendNotification(sendNotification, message) {
    console.log(`Sending notification to PHONE_NUMBER: ${MESSAGE}`);
};


client.on('error', err => console.log('Redis Client Error', err));

await client.connect();
