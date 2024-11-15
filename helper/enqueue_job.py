from workers.email_worker import email_queue, QUEUE_NAME
from logs.custom_logger import custom_logging
    
def enqueue_job(job, *args):
    try:
        queue = email_queue.get_queue(QUEUE_NAME)
        queue.enqueue(job, *args)
        custom_logging.info("Enqueued job successfully")
    
    except Exception as e:
        custom_logging.error(f"Error enqueuing job: {e}", exc_info=True)
    