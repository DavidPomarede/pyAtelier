"""
SCAMP Example: Random Durations and Rests

Loops a C major arpeggio twice, but with random, floating-point durations.
Also sometimes adds a rest of up to a second between notes.
"""

#  ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++  #
#  This file is part of SCAMP (Suite for Computer-Assisted Music in Python)                      #
#  Copyright © 2020 Marc Evanstein <marc@marcevanstein.com>.                                     #
#                                                                                                #
#  This program is free software: you can redistribute it and/or modify it under the terms of    #
#  the GNU General Public License as published by the Free Software Foundation, either version   #
#  3 of the License, or (at your option) any later version.                                      #
#                                                                                                #
#  This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY;     #
#  without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.     #
#  See the GNU General Public License for more details.                                          #
#                                                                                                #
#  You should have received a copy of the GNU General Public License along with this program.    #
#  If not, see <http://www.gnu.org/licenses/>.                                                   #
#  ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++  #

# import the scamp namespace
from scamp import *
# import the random module from
# the python standard library
import random

# construct a session object
s = Session()
# add a new violin part to the session
violin = s.new_part("Violin")
sax = s.new_part("Saxaphone")
brass = s.new_part("Brass")

for _ in range(2):  # loop twice
    for pitch in [80, 55, 112, 45, 97, 78, 66, 33,
91, 60, 72, 123, 40, 105, 83, 47,
99, 62, 88, 41, 75, 110, 54, 71,
58, 122, 76, 39, 93, 116, 43, 89,
118, 44, 92, 67, 113, 56, 79, 32,
115, 50, 106, 84, 65, 103, 70, 36,
53, 98, 77, 38, 86, 120, 48, 68,
121, 46, 107, 64, 81, 95, 42, 73]:
        # pick a duration between 0.5 to 1.5
        dur = random.uniform(0.05, 0.5)
        dur2 = random.uniform(0.02, 0.1)
        # play a note of that duration
        violin.play_note(pitch, 1, dur)
        sax.play_note(pitch, 1, dur2)
        # with probability of one half, wait for between 0 and 1 seconds
#        if random.random() < 0.5:
            # note that "wait" is the same here as "s.wait". What "wait" does it find the
            # clock operating on the given thread and call wait on that. In this case, that
            # clock is the Session as a whole.
#            wait(random.random())
def sequence1():
    violin.play_note(pitch, 1, dur)

def sequence2():
    sax.play_note(pitch, 1, dur2)

def sequence3():
    brass.play_note(80, 1, 30)

fork(sequence1)
fork(sequence3)
sequence2()