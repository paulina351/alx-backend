const kue = require('kue')
    , queue = kue.createQueue();


const job = queue.create('push_notification_code', {
      phoneNumber: string
    , message: string,
});


job.on('created', function(result){
    console.log('Notification job created: JOB ID', result);
  
}).on('complete', function(errorMessage, doneAttempts){
    console.log('Notification job completed');
  
}).on('failed', function(errorMessage){
    console.log('Notification job failed');
  
});