# Seminar paper AI 2022

<p style='text-align: justify;'>This is the practical half of my seminar paper written in 2022 as part of my whole scientific work:  
**"Artificial intelligence in computer games - AI learns to play a 2-dimensional game through reinforcement learning"**
All the code i used can be found in the folders above.  

All rights for usage of images and animations have been obtained. All artists are credited in the collective texture files.  
A few graphics were created by hand, free for use for anybody.

In the following paragraph I will be talking about how the idea of the remake of an “intellectualized” Undertale came about
and what kinds of issues as well as solutions became visible after starting through with the project.

## Idea and inspiration

<p style='text-align: justify;'>The inspiration for the topic "Undertale remake" comes from my personal enthusiasm for the 2015 released indie game “Undertale”, developed by Toby Fox.  
The game was nominated for the best indie game the same year it came out and blew away its fans and community by how captivating the storyline was written.  
The only “problem” the game had from a AI-enthusiast-perspective was that both the dialogues as well as the encounters with enemies in game were hard coded into the game  
so there wasn’t any way for the algorithm to evolve or get better at the game itself.  
And I wanted to change that.

## Problems

<p style='text-align: justify;'>Having the idea to start a project is one thing but implementing it is a whole other story so here are all the little problems I ran into while writing the code and designing the “finished” product.  
Right away the first very important decision to make as a game developer is what game engine to use.  
As the original Undertale game was made in GameMaker Studio I also opted for GameMaker as my primary game engine.  
The second very important question was what kind of machine learning algorithm I wanted to use for the simulated enemy in that game.  
I decided for reinforcement learning since this could be interesting as the player only has a limited movement range of 410x410 (minus 25 on both axis for player size) and the enemy (who must react to player movement) only has the option to pick between 5 different moves.  
For training the AI I used the Tensorflow Keras framework and a custom OpenAI Gym environment to simulate the game.  
This posed the issue of not being able to migrate the AI to GameMaker after it had finished its training.

### Solutions/Workarounds

<p style='text-align: justify;'>Possible solutions for solving the AI-migration-problem could be to migrate the game itself to python using a python game rendering library like pygame or further investigate in the GameMaker language (GML)  to read the generate weight data for the neural network and process it for the enemy object to use it.  
As a short term fix the “trained AI state” has been hardcoded to how the AI would play if the neural net was trained perfectly.  
The “untrained AI state” is coded in properly as it just relies on randomly picking a legal move to execute.  
There also was the problem of Tensorflow not accepting the custom environment given to it.  
This problem was later fixed by manipulating the box-shape of the observation space if the environment.

## Restrictions

<p style='text-align: justify;'>The restrictions of the neural network are small but present.  
Different values for the environment variables for the algorithm can produce widely spread results depending on exactly those values.  
Setting a higher sample size (for example nb_steps_warmup=200.000)  strongly accelerates the learning process for the first 200.000 generations but the iteration speed falls off immensely after these repetitions, so using a lower sample size of about 20.000 but a bigger step sum of 50.000 to 500.000 (depending on your system specs) could vastly accelerate the learning process of the AI.  
Another really big factor for performance is the number of nodes used in the net.  
In this particular example the AI is built on six dense nodes (layers), with eight neurons per layer in- or decreasing these numbers could also take a large impact in system performance.  
The restrictions of the ANN itself aside there are restriction put on the enemy or player by the way the game is designed.  The enemy only being able to use a maximum of five legal attacks at any stage in the game reduces the ceiling load of the AI massively.  
This restriction could be reworked as it is purely a game design choice.
