"""This module defines songs



Prepared by Mauricio Arias. NetID:  ma6918
This iteration uses simple representations based on frequency and
duration. Two lists are provided: one for the freqs and one for the
durations.
"""

import lib.WAV_utilities_v2 as u

tempo_in_bpm = 90
beat = 60 / tempo_in_bpm  # in seconds

Frere_Jacques_notes = [u.C4, u.D4, u.E4, u.C4,
                       u.C4, u.D4, u.E4, u.C4,
                       u.E4, u.F4, u.G4,
                       u.E4, u.F4, u.G4,
                       u.G4, u.A4, u.G4, u.F4, u.E4, u.C4,
                       u.G4, u.A4, u.G4, u.F4, u.E4, u.C4,
                       u.C4, u.G3, u.C4,
                       u.C4, u.G3, u.C4]

Frere_Jacques_durations = [beat, beat, beat, beat,
                           beat, beat, beat, beat,
                           beat, beat, beat * 2,
                           beat, beat, beat * 2,
                           beat * 0.75, beat * 0.25, beat * 0.5, beat * 0.5, beat, beat,
                           beat * 0.75, beat * 0.25, beat * 0.5, beat * 0.5, beat, beat,
                           beat, beat, beat * 2,
                           beat, beat, beat * 2]
