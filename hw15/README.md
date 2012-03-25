Homework 15
==========================
Game Pitches
--------------------------

For this assignment come up with three game ideas (by yourself) that you'd be willing to work on.  The games have to be written in python and pygame, but otherwise you are unconstrained.  They can be in realtime or turnbased, realistic or cartoony, serious or persuassive, etc. 

Focus on one good concept for a game that could feasibly be developed by two students of unknown or unequal skill level.  You will work on it until the end of the semester. This concept can be a moment of play, how it will feel, a game mechanic, etc.  Your project will then be implementing this one idea really well.  This means do not come up with ideas like "sims 3", more like "angry birds". 

> **NOTE:** your final game may be a proof-of-concept for a larger project.

Advanced students, you are not limited to the use of pygame if there is another library you want to use. We will work together to get whichever library you need working before the end of the semester on at least my laptop and the lab machines.

### Ideas
 * [Persuasive Games](http://www.persuasivegames.com/)
 * [Serious Games](http://en.wikipedia.org/wiki/Serious_game)
 * [20 Atari Games](http://www.gamasutra.com/view/feature/3679/game_design_essentials_20_atari_.php?print=1)
 * [Youtube](http://www.youtube.com)

### Tools already installed in Lab (we can get more)
 * Physics - [Pymunk](http://code.google.com/p/pymunk/)
 * Networking - [Twisted](http://twistedmatrix.com/trac/)/[Native Python](http://www.tutorialspoint.com/python/python_networking.htm)
 * Menus - [PGU](http://code.google.com/p/pgu/)


### How to do this homework...

Come up with an elevator pitch (one really descriptive sentence that takes about 15 seconds to say) for each concept.  Mention some similar games or a genre so we can get an idea how the game may look or play.  Then make a list of what you see as the elements involved in making this game.  Place them in this file with the format like the one bellow.  Then, simply turn in your ideas as "hw15".  We will send feedback and questions through github.

Before the end of break, as producers we will "score" the difficulty of each. Then we will green light the project we feel is most reasonable to implement in the time remaining in the course.  If you don't want to get stuck with your throw away idea, make sure you are willing to work on any of the three. You will then need to present this idea on Monday so make sure you flesh out the idea and what is involved.  Also, make a list of what you can bring to the table (art, level design, awesome code) to help find a partner.

----

## Prototype Game
A simple point-and-click adventure game about perspective of an underachieving game programmer walking the line between pink slip and productivity.

### Genre
In the style of the old lucasarts adventure games like "Monkey Island".

### Technical Hurdles
 * bottom menu
 * inventory
 * moving character where clicked
 * unique per item behaviors


## Block Dude Adventures
Based on the classic TI83+ game "Blockdude" with metroid-vania/open world level design and multiple block types.

### Genre
Tiled puzzle sidescroller

### Technical Hurdles
 * multiple block types
 * saved state
 * level loading
 * player equipment
 
------------------------------------------------------------------------------------------------------------------------
### Matthew's Pitches


## Gridiron:  Wizard Chess
When wizards have conflicts, they settle things in a civilized manner:  by summoning a team of monsters and playing good, hard-nosed Gridiron Football.  Zombies shamble towards the end zone with a run game, while the Dragons like to put the ball up in the air.  This is the REAL Fantasy Football.

# Genre:
Sports / turn-based strategy
 * gameplay would be either top-down or isometric 2D, possibly switching between the two on player command
 * this would be a working proof of concept in that there would not be a full roster of teams/characters - just enough to play with.
 
# Technical Hurdles:
 * creating at least two monster 'teams' or a set of monsters to mix-and-match before a game starts
 * coding pathfiding / monster AI
 * incorporating either a team AI to play the computer or a multiplayer option

  
# What I bring to the table:
 * willingness to design levels
 * understanding of American/Gridiron Football rules
 * willingness to experiment with pygame-based libraries such as librpg
 * familiarity with sites like <http://opengameart.org/> which can provide some assets
 * familiarity with using GIMP to create small images for games


## Peak
You woke up and the world had ended.  You live in southern Vermont, and one day a major disaster abruptly and without warning cuts off the fossil fuel supply.  Just like that, running on empty....now you have to fend off some hungry wolves and hungrier neighbors.

# Genre
RPG, with elements of survival
 * top-down or isometric view of sprites
 * short game based on survival.

# Technical Hurdles:
 * adding experience-based abilities to the character
 * incorporating social interaction
 * balancing the many, many ways you can die.
 
# What I bring to the table:
 * willingness to design levels, abilities
 * willingness to experiment with pygame-based libraries such as <http://www.pygame.org/project-LibRPG-1293-.html> librpg
 * familiarity with sites like <http://opengameart.org/> which can provide some assets
 * familiarity with using GIMP to create small images for games
 * ability to script dialogue and instructions
 

## The Necromancer
You are the first human born with magic.  You are destined to lead your people to greatness against the oppressive Elves and mighty Dwarves.  That is, once your people are dead.
You're a teenaged girl necromancer who leads an army of undead against elves and dwarves.

# Genre
RTS - you summon undead minions to kill your enemies.
 * This would be a Demo or proof-of-concept as well:  a single map, maybe only one enemy faction

# Technical Hurdles:
 * Pathfinding / Unit AI
 * enemy AI
 * incorporating a number of units for each faction
 * saved skirmishes
 
# What I bring to the table:
 * familiarity with sites like <http://opengameart.org/> which can provide some assets
 * familiarity with using GIMP to create small images for games

### Relative strengths and weaknesses:

# Strengths

Gridiron:  Wizard's Chess:
 * unique, totally awesome
 * lends itself to cutting corners .... who will really know if the pathfinding AI is replaced with predetermined coverage routes?
 
Peak
 * small concept that can be scaled up or down as project demands
 * lends itself well to sequels, expansion
 * probably simplest, code-wise
 * story-wise, my favorite
 
The Necromancer
 * first time an RTS has been innovative since Homeworld?
 * number of options per character is less than in RPG...may make some coding easier

# Weaknesses

Gridiron:  Wizard's Chess:
 * Less involving story is poorer motivator for me
 * roster of monsters could be work-intensive to create

Peak
 * balance could be tricky

The Necromancer
 *  Could be challenging to program the AI

