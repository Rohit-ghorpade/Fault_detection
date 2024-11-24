import sys
from typing import Dict, Any
import os
import pandas as pd
import pickle
import yaml
from src.constant import *  # Ensure this imports required constants
from src.exception import CustomException
from src.logger import logging


class MainUtils:
    def __init__(self) -> None:
        pass

    def read_yaml_file(self, filename: str) -> Dict[str, Any]:
        """
        Reads a YAML file and returns its content as a dictionary.
        """
        try:
            with open(filename, "r") as yaml_file:  # Fixed mode to "r"
                return yaml.safe_load(yaml_file)
        except Exception as e:
            logging.error(f"Error reading YAML file: {filename}")
            raise CustomException(e, sys) from e

    def read_schema_config_file(self) -> Dict[str, Any]:
        """
        Reads the schema configuration file.
        """
        try:
            schema_config_path = os.path.join("config", "schema.yaml")  # Hardcoded path
            schema_config = self.read_yaml_file(schema_config_path)
            return schema_config
        except Exception as e:
            logging.error(f"Error reading schema configuration file.")
            raise CustomException(e, sys) from e

    @staticmethod
    def save_object(file_path: str, obj: object) -> None:
        """
        Saves an object to the specified file path using pickle.
        """
        logging.info("Entered the save_object method of MainUtils class")
        try:
            with open(file_path, "wb") as file_obj:
                pickle.dump(obj, file_obj)
            logging.info(f"Object saved successfully at {file_path}")
        except Exception as e:
            logging.error(f"Error saving object to {file_path}")
            raise CustomException(e, sys) from e

    @staticmethod
    def load_object(file_path: str) -> object:
        """
        Loads an object from the specified file path using pickle.
        """
        logging.info("Entered the load_object method of MainUtils class")
        try:
            with open(file_path, "rb") as file_obj:
                obj = pickle.load(file_obj)
            logging.info(f"Object loaded successfully from {file_path}")
            return obj
        except Exception as e:
            logging.error(f"Error loading object from {file_path}")
            raise CustomException(e, sys) from e
