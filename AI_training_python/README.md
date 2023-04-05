# AI_training_python

<p style='text-align: justify;'>How does this training work? - This is the question that will be answered in this portion of the README.  
For starters: The Tensorflow Keras model is being use as a framework for training and building the AI.  
The environment in which the AI is trained is built by the Gym library and modified using a custom environment.  
To have some variation in sample data (in this case the start condition of the environment) I calculated between 2.000 and 20.000 ("NUM_OF_START_ENVS") possible start-variations in the "create_environments.py".  
It would be possible to iterate over all of them in order to train the AI but was not done here because of time and computing-power reasons.  
One of the biggest bottlenecks of the AI environment is the fact that i cant seem to find a way to pass in a 2D array or an array that is larger than 100 items.</p>

## Structure of the network

The structure of a network with 6 dense layers looks like this:  

```py
model.add(Dense(8, activation="relu", input_shape=states)) # Dense node layer as standard keras neuron to generate deep reinforcement learning algorithms
model.add(Dense(8, activation="relu"))
model.add(Dense(8, activation="relu"))
model.add(Dense(8, activation="relu"))
model.add(Dense(8, activation="relu"))
model.add(Dense(actions, activation="softmax"))
```  

<pre>Model: "sequential"  
_________________________________________________________________  
 Layer (type)                Output Shape              Param #  
=================================================================  
 dense (Dense)               (None, 410, 8)            3288  

 dense_1 (Dense)             (None, 410, 8)            72  

 dense_2 (Dense)             (None, 410, 8)            72  

 dense_3 (Dense)             (None, 410, 8)            72  

 dense_4 (Dense)             (None, 410, 8)            72  

 dense_5 (Dense)             (None, 410, 5)            45  

=================================================================  
Total params: 3,621  
Trainable params: 3,621  
Non-trainable params: 0  
_________________________________________________________________  
</pre>

## Great places to go, to learn more about how TensoFlow, Keras and OpenAI work

[TensorFlow](https://www.tensorflow.org) - The official Tensorflow website  
[TensorFlow - Discord](https://www.google.com/url?sa=t&rct=j&q=&esrc=s&source=web&cd=&cad=rja&uact=8&ved=2ahUKEwiWrbe1zpz7AhV2SfEDHW7ZADoQFnoECBUQAQ&url=https%3A%2F%2Fdiscord.com%2Finvite%2F64MVzQX&usg=AOvVaw3h1AIRKAUQKcu7Mt72nmrX) - The official Tensorflow Discord server  

[Keras](https://keras.io) - The official Keras website  
[Keras-RL Documentation](https://keras-rl.readthedocs.io/en/latest/) - The Keras build used in this implementation  

[OpenAI](https://openai.com) - The library used for the custom environment  
[Gym](https://www.gymlibrary.dev) - The indepth explanation of how the gym library works

# Setup

A brief description of how to set up the coding environment to run the python code

## Install the dependencies

Install TensorFlow on your machine (might be optional depending on what project you already opened in the past)

Install pip

<pre>pip install -r requirements.txt </pre>
This should hopefully install the required dependencies if not, manually install the missing packages from [the pip website](https://pypi.org/project/pip/)

## The order of files to run

First run the _create_environments.py_ once to create the necessary _training_data.csv_

Second run the _learner.py_ to train the AI -> this will all be displayed in the terminal by default
