import time
import logging


class TimerContext:
    def __enter__(self):
        self.start_time = time.time()
        # print(f'Starting at {self.start_time}')
        print("Starting")
        return self

    def __exit__(self, exc_type, exc_value, tb):
        end = time.time() - self.start_time
        # print(f'Finishing at {time.time()}')
        logging.info(f"execution time: {end} seconds")
        print("Finishing")


# Set up logging configuration
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
with TimerContext():
    time.sleep(2)
