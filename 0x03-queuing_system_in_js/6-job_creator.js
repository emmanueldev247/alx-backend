const kue = require('kue');

const queue = kue.createQueue();

const jobObject = {
 phoneNumber: '+234*******',
  message: 'Hello bro!'
}

const job = queue.create('push_notification_code', jobObject).save((err) => {
  if (err) {
    console.log('Notification job failed');
    return;
  }
  console.log(`Notification job created: ${job.id}`);
});

job.on('complete', () => {
  console.log('Notification job completed');
});

job.on('failed', () => {
  console.log('Notification job failed');
})
