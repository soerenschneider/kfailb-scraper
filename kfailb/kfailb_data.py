"""
Definition of dataclasses used by kfailb.
"""

from dataclasses import dataclass


@dataclass
class Raw:
    line: int
    problem: str
