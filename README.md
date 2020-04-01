# AdventOfCode2019

Python code to solve daily puzzles of http://adventofcode.com/2019

Code is tested with Python 3.6.6 (Anaconda distribution) on Win10. Developed with VSCode.

## Days

* Day 1:  Easy looping through a list.
* Day 2:  Introduced an "Intcode" program, with addition/multiplication/halt operations.  I suspect that this will be expanded upon in the future.  Needed deepcopy.  Times:  00:17:40 / 00:31:12.  Ranks:  1286 / 1382.
* Day 3:  Instructions to walk on a grid.  Did part 1 with a cleverish use of numpy, but had to rewrite much of it for part 2 (to keep track of separate grids for the two instructions so that the step number could be stored).
* Day 4:  Count numbers that meet criteria (the trickiest of which was digit-matching, requiring string conversion).  Times:  00:19:04 / 00:49:05.  Ranks:  2560 / 2905.  In my defense, my Win10 laptop crashed and needed a reboot!
* Day 5:  Expand the Intcode program, with jumps, I/O, and comparison.  I built it up with a class, perhaps reusable for future days.  Times:  00:59:28 / 01:14:26.  Ranks:  1771 / 1460.
* Day 6:  Part 1 was easy, but I stumbled (two days later due to time restrictions) on Part 2.  It doesn't look pretty, when all I really needed was a breadth-first search.
* Day 7:  Another use of the IntCode program.  The first was easy (given the modularization) especially with itertools.  The second part requires a modification to IntCode, to handle waiting on additional input.
* Day 8:  Processing a fixed-size picture.  Mostly focused on parsing the data in a format that can be used easily.  Times:  00:28:39 / 00:40:34.  Ranks: 1902 / 1458.
* Day 9:  Another IntCode program, with another state value to implement another parameter mode ("relative mode").  This required abstraction of the setting of values too.  Got to it late, so not bothering with time.
* Day 10:  Array with "asteroids".  Part 1 involved checking if any asteroids blocked line of sight.  Part 2 involved sorting the list by angle and removing non-blocked items, to simulate a spinning laser.
* Day 11:  TODO
* Day 12:  Calculated an "energy" metric for a set of items.  Part 2 involves a list of states (looking for a repeat), but TODO.
* Day 13:  Another IntCode program, like Breakout.  Part 2 requires a set of inputs to beat the game.  I did this by displaying the game, set up a loop for my joystick input, and ran it.  This was taking too long, so I "automated" my input by having the paddle track the x value of the  ball.  This ran, and it was a pleasant little movie to watch.

## See previous work at:
* https://github.com/jborlik/AdventOfCode2015
* https://github.com/jborlik/AdventOfCode2016
* https://github.com/jborlik/AdventOfCode2017
* https://github.com/jborlik/AdventOfCode2018
