"""
create dataclass `Engine`
"""
from dataclasses import dataclass
@dataclass
class Engine:
        volume : float = 1.6
        pistons : int = 4