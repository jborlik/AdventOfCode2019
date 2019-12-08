# AdventOfCode2019

Python code to solve daily puzzles of http://adventofcode.com/2019

Code is tested with Python 3.6.6 (Anaconda distribution) on Win10. Developed with VSCode.

## Days

* Day 1:  Easy looping through a list.
* Day 2:  Introduced an "Intcode" program, with addition/multiplication/halt operations.  I suspect that this will be expanded upon in the future.  Needed deepcopy.  Times:  00:17:40 / 00:31:12.  Ranks:  1286 / 1382.
* Day 3:  Instructions to walk on a grid.  Didn't complete part 2 yet.
* Day 4:  Count numbers that meet criteria (the trickiest of which was digit-matching, requiring string conversion).  Times:  00:19:04 / 00:49:05.  Ranks:  2560 / 2905.  In my defense, my Win10 laptop crashed and needed a reboot!
* Day 5:  Expand the Intcode program, with jumps, I/O, and comparison.  I built it up with a class, perhaps reusable for future days.  Times:  00:59:28 / 01:14:26.  Ranks:  1771 / 1460.
* Day 6:  Part 1 was easy, but I stumbled (two days later due to time restrictions) on Part 2.  It doesn't look pretty, when all I really needed was a breadth-first search.
* Day 7:  Another use of the IntCode program.  The first was easy (given the modularization) especially with itertools.  Didn't get to this until the next day.
* Day 8:  Processing a fixed-size picture.  Mostly focused on parsing the data in a format that can be used easily.  Times:  00:28:39 / 00:40:34.  Ranks: 1902 / 1458.


## See previous work at:
* https://github.com/jborlik/AdventOfCode2015
* https://github.com/jborlik/AdventOfCode2016
* https://github.com/jborlik/AdventOfCode2017
* https://github.com/jborlik/AdventOfCode2018
