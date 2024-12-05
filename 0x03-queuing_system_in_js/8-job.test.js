import createPushNotificationsJobs from './8-job';
import assert from 'assert';
import kue from 'kue';

const queue = kue.createQueue();

describe('testing createPushNotificationsJobs', () => {
  before(() => {
    queue.testMode.enter();
  });

  afterEach(() => {
    queue.testMode.clear();
  });

  after(() => {
    queue.testMode.exit();
  });

  it('should throw an error if not an array', () => {
    assert.throws(() => {
      createPushNotificationsJobs('not an array', queue);
    }, new Error('Jobs is not an array'));
  });

  it('should create jobs for valid job objects', () => {
    const jobs = [
      { phoneNumber: '4153518780', message: 'This is the code 1234 to verify your account' },
      { phoneNumber: '4153518781', message: 'This is the code 4562 to verify your account' }
    ];

    createPushNotificationsJobs(jobs, queue);
    assert.equal(queue.testMode.jobs.length, 2);
    assert.equal(queue.testMode.jobs[0].type, 'push_notification_code_3');
    assert.equal(queue.testMode.jobs[0].data.phoneNumber, '4153518780');
    assert.equal(queue.testMode.jobs[0].data.message, 'This is the code 1234 to verify your account');
  });
});
