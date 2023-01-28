"""
create dataclass `Engine`
"""
from dataclasses import dataclass
@dataclass
class Engine:
    def __init__(self, volume = 1.6, pistons = 4):
        self.volume = volume
        self.pistons = pistons