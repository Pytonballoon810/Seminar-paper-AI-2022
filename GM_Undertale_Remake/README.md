# GM_Undertale_Remake

<p style='text-align: justify;'>What do we use GameMaker for? - GameMaker is used to create a "quick" visual markup of how the finished product would look like so that the use has a better understanding of the concrete application of AI in the visual context of games.  
At the current stage (08.11.2022) the game demo is not finished but certain features can be tested out already.  
(Note that because of using the free version of GameMaker I was not able to compile the game into an executable (which would not have been the point anyways since I want you to be able to look at the code)).  
I will be including a few screenshots of possible game-situations (both for trained and untrained AI the possible game states are the same.  
The difference in training only shows itself by the reaction of the AI to the player position)</p>

## Implementation despite limitations

<p style='text-align: justify;'>The "trained AI state" has been hardcoded to pick certain moves just depending on player position.  
This obviously is not the best possible implementation since this method does not include any movement direction or speed data. This is definitely one of the more interesting implementations to fix since it would completely change how the game is played (although implementing the game in a engine natural to python would be better for use with AI)  
The "untrained AI state" is coded in synonymously to how the AI stated out in actual training since both algorithms rely on randomly picking a move to use (at first)</p>

## Explanation of variables

<p style='text-align: justify;'>Since GameMaker language (GML) is very object oriented and has a graphical interface it can be hard to keep track of what variables there are ant what they do so here is a list of all implemented variables (that are meant to be changed by users to test the game)</p>


| name                 | effect                                                                    | object       | type | default |
|----------------------|---------------------------------------------------------------------------|--------------|------|---------|
| lives                | changes the amount of lives the player starts with upon entering a screen | master_enc01 | int  | 3       |
| invincibility_frames | amount of frames to be invincible after being hit                         | master_enc01 | int  | 70      |
| button_margin        | pixels of margin between buttons                                          | master_enc01 | int  | 10      |
| movement_speed       | the amount of pixels the player moves per tick                            | player       | int  | 5       |
| start_x              | start x coordinate of the player                                          | player       | int  | 960     |
| start_y              | start y coordinate of the player                                          | player       | int  | 540     |

## Images

![game00](game00.png)  
![game01](game01.png)  
![game02](game02.png)  
![game03](game03.png)  