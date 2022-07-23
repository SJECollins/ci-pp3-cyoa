# Hide & Seek

Hide & Seek is a choose your own adventure game. It is targeted at users who would like to play an interactive story where their decisions will influence how the game story plays out.

Created with Python, Hide & Seek is inspired by classic adventure games where the user interacts with the game by entering commands. And like a classic choose your own adventure story, the choices the user makes when prompted effect the outcome of the game. There are multiple different endings decided by the choices made throughout the game.

The live site can be found here: [Hide & Seek](https://ci-pp3-hide-and-seek.herokuapp.com/)

# Table of Contents

- [User Experience](https://github.com/SJECollins/ci-pp3-hide-and-seek#user-experience)
- [Features](https://github.com/SJECollins/ci-pp3-hide-and-seek#features)
- [Design](https://github.com/SJECollins/ci-pp3-hide-and-seek#design)
- [Technologies Used](https://github.com/SJECollins/ci-pp3-hide-and-seek#technologies-used)
- [Testing](https://github.com/SJECollins/ci-pp3-hide-and-seek#testing)
- [Deployment](https://github.com/SJECollins/ci-pp3-hide-and-seek#deployment)
- [Credits](https://github.com/SJECollins/ci-pp3-hide-and-seek#credits)

# User Experience

## User Story

As a user,
- I would like to understand how to interact with the game and have options for how I interact with the game
- I would like to be able to make decisions within the game that effect outcome and provide replayability
- I would like to be able to replay the game when I reach an ending

# Features
## Title Screen
![Title Screen](readme-docs/title.webp)

The title screen features the name of the game in ASCII using pyfiglet. It gives the user an initial prompt to press enter to begin the game.

Should the player quit while playing the game, they are returned to the title screen.

## Introduction
![Intro Screen](readme-docs/intro.webp)

The introduction screen gives the user three prompts. The first is a prompt to enter their name. This is trimmed and captilised, and stored in the username variable to be used throughout the game.

The game then gives a second prompt, including the username to provide feedback to the user that their input is recorded. This second prompt asks a simple yes/no question to encourage the user to type a response. If the user agrees to play the game, they are given simple instructions to input either the letter a prompt or underlined keywords.

The third prompt asks if they are ready to start. It has the typical layout for prompts featured in the game. At this point, it is expected the user understands how to interact with the game.

## User Interaction
![User Choices](readme-docs/choices.webp)

Throughout the game, the user is prompted to make decisions. They are typically prompted with two options, but there can be as many as four. Also, as explained in the introduction, the user can enter "quit" at any point to return to the title screen even though it is not typically presented as an option.

These decisions that the user makes during the story will effect how the story plays out and the overall outcome.

## End Screen
![End Screen](readme-docs/end.webp)

The end screen features when the user reaches one of the endings of the story. "The End" is displayed in ASCII using pyfiglet. After a brief pause the user is then presented with an option to play again - which brings them back to the starting room - or to quit to the title screen.

# Design

The game was inspired by classic text adventure games and choose your own adventure books. It is told in a second-person narrative to immerse the player as they are the main character in the story. There is limited ASCII art to illustrate the story and a slow printing effect for the story text.


# Technologies Used


# Testing


# Deployment


# Credits