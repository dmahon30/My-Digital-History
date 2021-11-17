#!/usr/bin/python

from miditime.miditime import MIDITime

mymidi = MIDITime(120, 'myfile.mid')

midinotes = [
    [0, 60, 200, 3],  #At 0 beats (the start), Middle C with attack 200, for 3 beats
    [10, 61, 200, 4]  #At 10 beats (12 seconds from start), C#5 with attack 200, for 4 beats
]

mymidi.add_track(midinotes)

mymidi.save_midi()