function createPushNotificationsJobs(jobs=[], queue) => {
    if (jobs != [] {
        console.log("Jobs is not an array");
    });
};

var job = queue.create('push_notification_code_3', {
          jobs: ''
});

job.on('created', function(result){
  console.log('Notification job created: JOB_ID ', result);
  
}).on('complete', function(result){
  console.log('Notification job JOB_ID completed');
  
}).on('failed', function(errorMessage){
  console.log('Notification job JOB_ID failed: ERROR');
  
}).on('progress', function(progress, data){
  console.log('Notification job JOB_ID PERCENT% complete');
});