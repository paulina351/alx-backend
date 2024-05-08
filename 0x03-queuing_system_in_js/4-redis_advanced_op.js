await client.hSet('HolbertonSchools', {
    Portland: '50',
    Seattle: '80',
    'New York': '20',
    Bogota: '20',
    Cali: '40',
    Paris: '2',
})

let userSession = await client.hGetAll('HolbertonSchools');
console.log(JSON.stringify(userSession, null, 2));