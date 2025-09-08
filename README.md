# Evolving a Number
A genetic Algorithm built from scratch just to understand the basics of artificial evolution
using just a simple concept: Finding a number.

---
# Motivation
I've had the idea for this project since I was 15. I was fascinated by early AI videos—programs
learning to solve mazes or play games, but the idea of building an AI just to find a number seemed
almost too simple, maybe even a little silly. So, I put it aside.

Then, years later, while bored during a game of ping-pong, the idea came back to me with a new twist:

What if the goal wasn't just to find the number, but to build the most elaborate, over-engineered, 
and educational way to do it?

This project is the result of that thought. It's my attempt to take every bit of knowledge I've absorbed
from watching those old AI videos and channel it into a single mission: to build my own learning algorithm
from the ground up, all for the beautifully simple task of finding a number.

So this is it. The most complex project imaginable to find a number you're thinking of.
(pls don't show it to my CS teachers).
# Core Features.

This is not a simple script but a complete, functional genetic algorithm engine that implements:

- Full Genetic Algorithm From Scratch: No optimization libraries were used. Every
component—selection, reproduction, and mutation—was designed and implemented by hand. (except, of
course, the random library)

- Dynamic Fitness Function: Each individual's fitness is calculated using a parabolic function that
 adapts each generation, becoming stricter as the population converges.

- Tournament Selection: Parents are not chosen at random. They compete in small "tournaments" to
determine which are the fittest to reproduce, balancing selection pressure with diversity.

- Bit-Level Crossover: Instead of a simple average, reproduction simulates a true 50/50 genetic
 crossover. The parents' numerical values are converted into binary "chromosomes," which are then
 sliced and recombined to create an offspring with a new genetic makeup.

- Mutation: A mutation rate is applied to introduce variability into the population, allowing the
 algorithm to explore new solutions and avoid getting stuck in local optima.

# How to use it

Just use:

 `python3 main.py`


