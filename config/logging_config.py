import logging
import logging.config
import yaml

def setup_logging(config_path='config/log_config.yaml'):
    """Sets up logging configuration."""
    with open(config_path, 'r') as file:
        config = yaml.safe_load(file.read())
        logging.config.dictConfig(config)

# Default logger setup
setup_logging()
logger = logging.getLogger(__name__)
