const kue = require('kue')
    , queue = kue.createQueue();


const jobs = [
    {
      phoneNumber: '4153518780',
      message: 'This is the code 1234 to verify your account'
    },
    {
      phoneNumber: '4153518781',
      message: 'This is the code 4562 to verify your account'
    },
    {
      phoneNumber: '4153518743',
      message: 'This is the code 4321 to verify your account'
    },
    {
      phoneNumber: '4153538781',
      message: 'This is the code 4562 to verify your account'
    },
    {
      phoneNumber: '4153118782',
      message: 'This is the code 4321 to verify your account'
    },
    {
      phoneNumber: '4153718781',
      message: 'This is the code 4562 to verify your account'
    },
    {
      phoneNumber: '4159518782',
      message: 'This is the code 4321 to verify your account'
    },
    {
      phoneNumber: '4158718781',
      message: 'This is the code 4562 to verify your account'
    },
    {
      phoneNumber: '4153818782',
      message: 'This is the code 4321 to verify your account'
    },
    {
      phoneNumber: '4154318781',
      message: 'This is the code 4562 to verify your account'
    },
    {
      phoneNumber: '4151218782',
      message: 'This is the code 4321 to verify your account'
    }
  ];

const job = queue.create('push_notification_code', {
      phoneNumber: string
    , message: string,
});

for (i = 0; i < jobs.length; i++)
{
  if (jobs[i] = "created") {
    console.log("Notification job created: JOB ID")
  }
  else if (job[i] = "completed") {
    console.log("Notification job JOB ID completed");
  }
  else if (job[i] = "failed") {
    console.error("Notification job JOB ID failed ERROR");
  }
  else {
    console.log('\r  job #' + job.id + ' ' + progress + '% complete with data ', data );
  }

};