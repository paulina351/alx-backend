import { createClient } from 'redis';

const client = createClient();

const kue = require('kue')
    , queue = kue.createQueue();



const reserveSeat(number, available_seats) => {

}

const getCurrentAvailableSeats() => {
    
}
app.get('/api/available_seats')

app.get('/api/reserve_seat') {
    if (reservationEnabled is false) {
        return({ "status": "Reservation are blocked" });
    }
    
}

client.on('error', err => console.log('Redis Client Error', err));

await client.connect();

