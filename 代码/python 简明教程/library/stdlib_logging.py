import os
import platform
import logging

logging_file = os.path.join(os.getenv('HOME'), 'test.log')

print("Loggin to", logging_file)

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s : %(levelname)s : %(message)s',
    filename=logging_file,
    filemode='w',
)

logging.debug("Start of the")
logging.info("Doing sth")
logging.warning("Dying now")

