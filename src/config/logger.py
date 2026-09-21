import logging

logger=logging.getLogger("job_market")
logger.setLevel(logging.INFO)


console_handler = logging.StreamHandler()

formatter = logging.Formatter(
    "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
) 

console_handler.setFormatter(formatter)

logger.addHandler(console_handler)

#logger.info("Logger is Working!")