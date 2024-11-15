from rq import Worker, Queue
from connection.connections import redis_connection
from logs.custom_logger import custom_logging


class CustomWorker:
    
    def __init__(self,queue_names: list[str] | str):
        
       
        
        
        if type(queue_names) == str:
            queue_names = [queue_names]
        
        try:
            self.__queues = [Queue(name, connection=redis_connection) for name in queue_names]
            
            self.__queue_dict = dict(zip(queue_names,self.__queues))
            
        except Exception as e:
            custom_logging.error(f"Error initializing custom worker: {e}", exc_info=True)
            
    def start_worker(self, worker_name: str = None):
        try:
            worker = Worker(self.__queues, name=worker_name, connection=redis_connection)
            custom_logging.info(f"Worker {worker.name} started successfully")
            worker.work()
            
        except Exception as e:
            custom_logging.error(f"Error in starting worker: {e}", exc_info=True)
        
    def get_queue(self, queue_name: str):
        return self.__queue_dict.get(queue_name)
        
    
