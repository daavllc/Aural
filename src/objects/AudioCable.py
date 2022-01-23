import datetime as dt
import time
from enum import Enum, auto
import uuid

from helpers.timer import Timer

class AudioCable:
    """
    A Virtual Audio Cable instance
        Contains details about the VAC:
         Name, Sample Rate Min/Max, Bits Per Sample Min/Max, State, Latency Time, Channels Min/Max
         UUID, Process ID, Thread ID, Life time, Type, FMS transferred
    TODO: Clock Correction Ratio, Capture/Render Port Type
    """
    class Type(Enum):
        PCM = auto() # Wave Format
        ExtPCM = auto() # Wave Format Extensible

    class State(Enum):
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

    def _Generate(self):
        self.Settings = dict(
            Name = None,
            SampleRateMin = self.SampleRate.hz44100,
            SampleRateMax = self.SampleRate.hz44100,
            BitsPerSampleMin = 8,
            BitsPerSampleMax = 16,
            ChannelsMin = 1,
            ChannelsMax = 2,
            Internal = dict(
                UUID = uuid.uuid4(),
                ProcessID = None,
                ThreadID = None,
                State = None,
                Type = None
            ),
            Stats = dict(
                LifeTime = None,
                FMsTransferred = None # Audio Frames transfered since creation
            )
        )
        Timer.Get().Add(str(self.Settings['Internal']['UUID']))

    def _Update(self):
        self.Settings['Stats']['LifeTime'] = Timer.Get().GetElapsed(str(self.Settings['Internal']['UUID']))
