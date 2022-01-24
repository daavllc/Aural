from enum import Enum, auto
import uuid

class Type(Enum):
    INPUT = auto() # Takes the output of a sound device
    OUTPUT = auto() # Sends the output of sound devices to another
class Route:
    """
    A Route instance
        Contains details about the Route:
         Name, Type, Volume, Sends, IsMuted
         Listen: (INPUT ONLY): what hardware device to recieve from
      Sends:
        INPUT: What routes to send this routes output to
        OUTPUT: What hardware devices to send this routes output to
      TODO: Equalizer, Echo, Reverb, Brightness, Compressor, Noise Gate, Panning
    """
    def __init__(self):
        self._Generate()

    def _Generate(self):
        self.Configuration = dict(
            Name = "Default Route",
            Type = Type.INPUT,
            Volume = 0.0,
            IsMuted = False,
            Listen = None, # Type.INPUT ONLY
            Sends = {},
            Internal = dict(
                UUID = uuid.uuid4()
            )
        )

    def GetUUID(self) -> uuid.UUID:
        return self.Configuration['Internal']['UUID']

    def GetConfiguration(self) -> dict:
        return self.Configuration

    def SetConfiguration(self, config: dict) -> None:
        self.Configuration = config