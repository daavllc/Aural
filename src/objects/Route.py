from enum import Enum, auto

class Route:
    """
    A Route instance
        Contains details about the Route:
         Name, Type, Volume, Receivers, IsMuted,
      Receivers: (INTERNAL only) List of routes to send output to
      TODO: Equalizer, Echo, Reverb, Brightness, Compressor, Noise Gate, Panning
    """
    class Type(Enum):
        INPUT = auto() # Takes the output of a sound device
        OUTPUT = auto() # Sends the output of sound devices to another