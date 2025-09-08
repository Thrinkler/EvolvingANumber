# Evolving a Number
A genetic Algorithm built from scratch just to understand the basics of artificial evolution
using just a simple concept: Finding a number.

---
# Motivation
I had the idea to make this project ever since I was 15 years old. I grasped the idea by just
watching videos about AI (before chatgpt, when AI was just some program trying to find a way to
solve a maze or play a videogame alone), but by the time it just seemed a little bit too stupid
to do, the concept is just so simple that why bother doing it. So that's why, when I was too 
bored playing ping-pong, it just came to me:

Why wouldn't I make it?

So there I imagined working on the most complex way to find the number you are thinking would
be. Not only asking chatgpt, but making my own AI to search for that number, and with the 
basic knowledge I still have with those, it was just too perfect: A guy trying to grasp 
every bit of the knowledge he watched on YouTube and putting it inside a project to find the
desired number the user wants.

So, this is it. The biggest and most complex project to find the number the user is thinking
of.
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


