from enum import Enum
from typing import List


class EventParamType(Enum):
    STRING = "string"
    BOOLEAN = "boolean"
    INTEGER = "integer"


class EventType(Enum):
    KEYBOARD = "KEYBOARD"


class EventParam:
    def __init__(self, name: EventType, ptype: EventParamType):
        self.name = name
        self.ptype = ptype


class Event:
    def __init__(self, name: str, description: str, parameters: List[EventParam]):
        self.name = name
        self.description = description
        self.parameters = parameters


events: List[Event] = [
    Event(EventType.KEYBOARD, "Emulates a given keyboard shortcut",
          [EventParam("shortcut", EventParamType.STRING)])
]
