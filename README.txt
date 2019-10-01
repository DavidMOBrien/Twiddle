====================
TWIDDLE
Author: DavidMOBrien
====================


Twiddle is a puzzle game played on a 3x3 grid. Each puzzle starts with the numbers 1-9
"randomly" shuffled among the nine tiles in the grid.

Example:

9 5 7
2 3 1
8 4 6

Tiles in the grid can be moved by rotating a group of tiles around one of the four interior
intersection points either clockwise or counterclockwise. These will be referred
to as A,B,C, and D.

In the example listed above:
	Turning point A would pivot 9,5,2, and 3 in the indicated direction.
	Turning point B would pivot 5,7,3, and 1 in the indicated direction.
	Turning point C would pivot 2,3,8, and 4 in the indicated direction.
	Turning point D would pivot 3,1,4, and 6 in the indicated direction.

The goal is to try to manipulate the board around the 4 points to get to the goal state
which is:

1 2 3
4 5 6
7 8 9

If you want to try playing this for yourself, use the link:
	https://www.chiark.greenend.org.uk/~sgtatham/puzzles/js/twiddle.html#3x3n2:9,5,7,2,3,1,8,4,6

This python code (twiddle.py) does not allow the user to play the game. Instead, this code's 
job is to find the fastest (least # of steps) solution to a given board.

This goal is accomplished by using an "Iterative Deepening Depth First Search" Algorithm,
more info on the specifics of this Algorithm can be found here:
	http://theoryofprogramming.com/2018/01/14/iterative-deepening-depth-first-search-iddfs/

After finding the solution, the python code outputs the following:
	- A sequence of points and directions it takes to get from the specific board
	to a solution.
	- # of Moves it takes to reach the solution.
	- # of Moves (called Nodes) that were generated in memory but were not analyzed
	before our solution was found, this is referred to as a "fringe"
	- # of Moves (called Nodes) that were analyzed before our solution was found.