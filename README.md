# Hide & Seek

Hide & Seek is a horror-themed, choose your own adventure game. It is targeted at users who would like to play an interactive story where their decisions will influence how the game story plays out.

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

## Future Expansion

# Design

The game was inspired by classic text adventure games and choose your own adventure books. It is told in a second-person narrative to immerse the player as they are the main character in the story. There is limited ASCII art to illustrate the story and a slow printing effect for the story text.

## Story

Hide & Seek is a small horror game. The story design is inspired by classic choose your own adventure books. The user moves one way through the story and is prompted to make decisions at important branches. These decisions alter variables or call different functions within the code which changes how the story plays out. It is not possible to see the entire story in one play through. 

Unlike some text adventure games, a user cannot go back and revisit a decision, they have to continue with the decisions they have made until the story ends. For example, if they chose to pick up one object rather than another, they can't go back and change their mind. To find all the endings or to see alternative routes through the story, the game has to be played multiple times. 

The design is also loosely inspired by the games designed by Roberta Williams and others from that era. Classic Sierra games are often criticised for being "unfair" as the user could easily miss an important pick up or make an incorrect decision without realising it as they weren't always given the information they needed to know or told what they needed to do. The user was expected to fail and try again until they figured out what game wanted from them. 

While it can be frustrating to lose based on what seems like arbitrary decisions, I felt as though this logic behind the game design worked quite well in a horror game. On first playthrough, the user doesn't know what will happen and so can only make decisions arbitrarily based on minimal information and then watch how it plays out. Hopefully, the user will feel this is a challenge and be inspired to play again and make different, more informed decisions upon completing the game for the first time.

## Graphics
![ASCII Art](readme-docs/graphics.webp)

The game is limited graphically as it is designed to be played in the terminal. However, to provide a slightly better user experience some ASCII art has been implemented.

Images.py contains a dictionary of ASCII art which is printed to the terminal where appropriate to illustrate the game. Using pyfiglet, the title on the title screen and "the end" at the end of the game are also printed using an ASCII shadow "font".

## Slowprint
![Slowprint](readme-docs/window.webp)

A slowprint function was used to create an effect where it appeared as through the story was being printed to the terminal as the user read it. This is to try to add a little more immersion to the story. It also serves to give the user time to read the text on screen before the input prompt appears. 

Before the slowprint function, time.sleep() was used instead to delay progression of the story where necessary. However, the effect was such that text appeared quite abruptly and the screen felt very static while the user read the story. 

Using a combination of slowprint and time.sleep(), where necessary, the flow of the story was improved.

# Technologies Used

- [HTML5](https://en.wikipedia.org/wiki/HTML5): mark-up language.
- [CSS3](https://en.wikipedia.org/wiki/CSS): styling.
- [Python](https://en.wikipedia.org/wiki/Python_(programming_language)): programming language.
  - Libraries:
    - Pyfiglet: to create ASCII titles.
    - OS: for the clear terminal function.
    - Time: for time.sleep().
- [GIT](https://git-scm.com): for version control.
- [GitHub](https://github.com): for host repository.
- [Gitpod](https://www.gitpod.io): online IDE.
- [Inkscape](https://inkscape.org): to create the favicon.

# Testing


# Deployment

## Steps to deploy site using Heroku:
- On the Heroku dashboard, select "New" and click "Create new app"
  - Create a unique app name
  - Select your region
  - Click "Create app"
- Go to the settings tab:
  - Scroll down to the config vars section and select "Reveal Config Vars"
  - Add necessary config vars
  - In this case, in the key field enter "PORT" and the value field enter "8000"
  - Click "Add"
  - Scroll down to Buildpacks and click "Add buildpack"
  - Add the necessary buildpacks.
  - In this case, select "python" and click "Save changes"
  - Then, select "node.js" and click "Save changes"
- Go to the Deploy tab:
  - Select GitHub and confirm connection to GitHub account
  - Search for the repository and click "Connect"
  - Scroll down to the deploy options
  - Select automatic deploys if you would like automatic deployment with each new push to the GitHub repository
  - In manual deploy, select which branch to deploy and click "Deploy Branch"
  - Heroku will start building the app
- The link to the app can be found at the top of the page by clicking "Open app"

The live site can be found here: [Hide & Seek](https://ci-pp3-hide-and-seek.herokuapp.com/)

## Steps to clone site:
- In the GitHub repository, click the "Code" button.
- Select "HTTPS" and copy the URL.
- Open Git Bash and navigate to the repository where you would like to locate the cloned repository.
- Type "git clone" followed by the copied URL.
- Press enter to create the clone.

# Credits