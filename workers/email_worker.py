import sys
sys.path.append("/home/aditya/code/email_task")

from controller.custom_worker.CustomWorker import CustomWorker

QUEUE_NAME = 'email_queue'
WORKER_NAME = 'email_worker'


email_queue = CustomWorker(QUEUE_NAME)


if __name__ == '__main__':
    email_queue.start_worker(WORKER_NAME)