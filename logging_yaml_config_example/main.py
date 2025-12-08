import logging.config
import os

import yaml
from module_1 import main

# Get the directory where this script is located
script_dir = os.path.dirname(os.path.abspath(__file__))
config_path = os.path.join(script_dir, 'logging_config.yaml')

with open(config_path, 'rt') as f:
    config = yaml.safe_load(f.read())

logging.config.dictConfig(config)

main()