"""Controler events of buttons"""
# pylint: disable=import-error

from core.api_utils import save_key_api

class Controller:
    """Class for copycharmntroller events of buttons"""
    def __init__(self):
        pass


    def save_key_api(self, key_api):
        """call func from core for save api key"""
        save_key_api(key_api)