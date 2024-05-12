import logging

from commons import logging_helpers # type: ignore


def main():
    logging_helpers.setup_logging()
    logger = logging.getLogger(__name__)

    logger.debug("This is a log entry for debugging.")
    logger.info("This is a log entry for information.")
    logger.warning("This is a log entry for a warning.")
    logger.error("This is a log entry for an error.")
    logger.critical("This is a log entry for a critical error.")


if __name__ == "__main__":
    main()
