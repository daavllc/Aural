import datetime as dt
import time
from enum import Enum, auto
import uuid

from helpers.timer import Timer

class Type(Enum):
        PCM = auto() # Wave Format
        ExtPCM = auto() # Wave Format Extensible

class State(Enum):
    NEW = auto()
    STOP = auto()
    ACQUIRE = auto()
    PAUSE = auto()
    RUN = auto()

class SampleRate(Enum):
    hz22050 = 22050
    hz44100 = 44100
    hz48000 = 48000
    hz88200 = 88200
    hz96000 = 96000
class AudioCable:
    """
    A Virtual Audio Cable instance
        Contains details about the VAC:
         Name, Sample Rate Min/Max, Bits Per Sample Min/Max, State, Latency Time, Channels Min/Max
         Process ID, Thread ID, Life time, Type, FMS transferred
    TODO: Clock Correction Ratio, Capture/Render Port Type
    """
    def __init__(self):
        self._Generate()

    def _Generate(self):
        self.Configuration = dict(
            Name = "Default Audio Cable",
            SampleRateMin = SampleRate.hz44100,
            SampleRateMax = SampleRate.hz44100,
            BitsPerSampleMin = 8,
            BitsPerSampleMax = 16,
            ChannelsMin = 1,
            ChannelsMax = 2,
            Internal = dict(
                UUID = uuid.uuid4(),
                ProcessID = None,
                ThreadID = None,
                State = State.NEW,
                Type = None
            ),
            Stats = dict(
                LifeTime = None,
                FramesTransferred = None # Audio Frames transfered since creation
            )
        )

    def GetUUID(self) -> uuid.UUID:
        return self.Configuration['Internal']['UUID']

    def GetConfiguration(self) -> dict:
        return self.Configuration

    def SetConfiguration(self, config: dict) -> None:
        self.Configuration = config
