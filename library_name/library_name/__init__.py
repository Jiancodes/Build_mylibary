# -*- coding: utf-8 -*-

"""Top-level package for proto_sep."""

__author__ = """Developer"""
__email__ = 'Developer email'


from .utils.configuration import library_name_config, show_configuration
from .utils.logging import (
    activate_warnings,
    silence_warnings,
    update_logging_level,
)


from .protostars import Protostar, Group, Region, Catalog
