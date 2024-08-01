# Nairobi Police and Citizens Protests Adventure Documentation

## Table of Contents

1. [Introduction](#introduction)
2. [User Manual](#user-manual)
   - [1.1 Game Overview](#game-overview)
   - [1.2 Getting Started](#getting-started)
   - [1.3 Game Mechanics](#game-mechanics)
   - [1.4 Scenarios and Decision Making](#scenarios-and-decision-making)
   - [1.5 Winning and Losing Conditions](#winning-and-losing-conditions)
3. [Developer Guide](#developer-guide)
   - [2.1 Project Structure](#project-structure)
   - [2.2 Installation and Setup](#installation-and-setup)
   - [2.3 Adding New Features](#adding-new-features)
   - [2.4 Code Standards and Best Practices](#code-standards-and-best-practices)
   - [2.5 Contributing Guidelines](#contributing-guidelines)
4. [API Documentation](#api-documentation)
   - [3.1 Overview](#api-overview)
   - [3.2 Classes and Methods](#classes-and-methods)
   - [3.3 Event Handling](#event-handling)
   - [3.4 Multiplayer Functionality](#multiplayer-functionality)
5. [Technical Documentation](#technical-documentation)
   - [4.1 Game Architecture](#game-architecture)
   - [4.2 Data Management](#data-management)
   - [4.3 Error Handling and Debugging](#error-handling-and-debugging)
6. [FAQ](#faq)
7. [Troubleshooting](#troubleshooting)
8. [Glossary](#glossary)
9. [License](#license)
10. [Contact Information](#contact-information)

---

## Introduction

The "Nairobi Police and Citizens Protests Adventure" is an engaging text-based simulation game that immerses players in the challenging role of a police officer in Nairobi. The game emphasizes ethical decision-making and resource management while responding to a variety of real-world scenarios, including public protests, natural disasters, and political interference. Players must navigate these events while maintaining public support, personnel morale, and ethical integrity.

## User Manual

### 1.1 Game Overview

- **Objective**: The primary objective is to maintain public order and safety while managing resources and making ethical decisions.
- **Roles and Characters**: Players can choose from four character backgrounds, each providing unique advantages and challenges:
  - **Veteran Officer**: Experienced and respected, but may struggle with adapting to new strategies.
  - **Rookie Officer**: Energetic and innovative, but lacks experience and credibility.
  - **Community Liaison**: Trusted by the public, skilled in communication but limited in enforcement capabilities.
  - **Tactical Expert**: Strategically minded, excels in crisis management but may be perceived as aggressive.

### 1.2 Getting Started

#### Installation

1. **System Requirements**:
   - **Operating System**: Windows, macOS, or Linux
   - **Python**: Version 3.6 or higher
   - **Memory**: 2GB RAM or more
   - **Storage**: 100MB of free disk space

2. **Cloning the Repository**:
   ```bash
   git clone https://github.com/Nyandiekahh/Final-Maandamano-game-using-CLI
   cd NairobiPoliceGame
   ```

3. **Setting Up a Virtual Environment**:
   - Create a virtual environment to isolate the game dependencies.
   ```bash
   python -m venv myenv
   source myenv/bin/activate  # On Windows, use `myenv\Scripts\activate`
   ```

4. **Installing Dependencies**:
   - Install the required Python packages using pip.
   ```bash
   pip install -r requirements.txt
   ```

5. **Running the Game**:
   - Start the game using the following command:
   ```bash
   python main.py
   ```

### 1.3 Game Mechanics

#### Resources Management

- **Personnel**: The workforce available to handle events. Overworking can lead to burnout and reduced effectiveness.
- **Equipment**: Essential for various operations. Limited equipment can hinder response capabilities.
- **Public Support**: A critical resource that reflects the public's trust in the police force. Losing public support can lead to unrest.
- **Morale**: Indicates the overall mood and motivation of the personnel. Low morale can result in poor performance.

#### Decision Making

- Each event presents multiple choices, each with potential consequences on resources and public perception. Players must weigh the risks and benefits of each decision.

### 1.4 Scenarios and Decision Making

#### Types of Scenarios

1. **Protests and Demonstrations**: Manage large crowds and ensure public safety while respecting citizens' rights.
2. **Media Scrutiny**: Handle the media's portrayal of police actions, balancing transparency and confidentiality.
3. **Natural Disasters**: Allocate resources effectively to manage crises like floods or earthquakes.
4. **Political Interference**: Navigate politically charged situations that may affect operational decisions.

#### Ethical Decision Making

- The game includes choices that test the player's ethical considerations. Some decisions may lead to immediate game over if they are deemed unethical, such as using excessive force.

### 1.5 Winning and Losing Conditions

#### Winning the Game

- Successfully navigate through all the days without depleting any resources.
- Maintain a high level of public support and morale.

#### Losing the Game

- The game ends if:
  - Personnel, equipment, or public support reaches zero.
  - The player makes an unethical decision leading to a loss of public trust or severe consequences.

## Developer Guide

### 2.1 Project Structure

- **main.py**: The entry point for the game.
- **game/**: Core game logic and components.
  - **nairobi_police_game.py**: Main game class handling the game loop and logic.
  - **game_state.py**: Manages the state of the game, including resources and events.
  - **player.py**: Defines the player class, including character backgrounds and attributes.
  - **colors.py**: Contains ANSI color codes for text styling.
  - **help.py**: Provides help and guidance information.
  - **quit.py**: Handles game termination.
- **network/**: Multiplayer functionality.
  - **multiplayer.py**: Manages multiplayer connections and game state synchronization.
- **assets/**: Assets used in the game, such as audio files and data.
  - **high_score.json**: Stores high scores.

### 2.2 Installation and Setup

Refer to the [Getting Started](#getting-started) section for detailed instructions on installing and setting up the game.

### 2.3 Adding New Features

#### Adding New Scenarios

- To add new scenarios, update the `handle_location_event()` method in `nairobi_police_game.py`. Define new events and the corresponding options.

#### Expanding Character Backgrounds

- New character backgrounds can be added in the `Player` class in `player.py`. Define the strengths and weaknesses of the new character and how they impact gameplay.

#### Enhancing Multiplayer Mode

- To enhance multiplayer features, modify `multiplayer.py`. This could include adding new communication protocols, improving synchronization, or adding competitive/cooperative elements.

### 2.4 Code Standards and Best Practices

- **Code Style**: Follow PEP 8 guidelines for Python code.
- **Testing**: Implement unit tests for new features and changes.
- **Documentation**: Update the README and documentation with any new features or changes.

### 2.5 Contributing Guidelines

1. **Fork the Repository**: Create your own copy of the repository.
2. **Create a Branch**: Work on a feature or fix in a new branch.
3. **Submit a Pull Request**: Once your changes are complete and tested, submit a pull request for review.

## API Documentation

### 3.1 Overview

The API documentation provides details about the classes and methods used in the game. This section is essential for developers looking to understand the internal workings of the game or extend its functionality.

### 3.2 Classes and Methods

#### NairobiPoliceGame

- **Methods**:
  - `start_game()`: Initiates the game sequence.
  - `character_creation()`: Handles character selection and setup.
  - `main_game_loop()`: The main loop where events are handled.
  - `get_player_input(prompt)`: Collects and processes player input.
  - `handle_location_event()`: Manages the occurrence of location-specific events.
  - `unethical_choice(message)`: Ends the game when an unethical choice is made.
  - `update_game_state()`: Updates the game state, including resources.
  - `end_game()`: Finalizes the game and displays results.

### 3.3 Event Handling

- **Event Management**: Events are triggered based on the game state and player actions. Each event has associated choices that affect the game's resources and outcome.

### 3.4 Multiplayer Functionality

- **MultiplayerManager**: Handles the setup and management of multiplayer games, including hosting and joining sessions, and synchronizing game states.

## Technical Documentation

### 4.1 Game Architecture

- The game is structured into distinct modules for clarity and maintainability. Core game logic is separated from network functionality and user interface elements.

### 4.2 Data Management



- **State Management**: The `GameState` class manages all game data, including resources and events.
- **Persistent Data**: High scores and progress are saved in `high_score.json`.

### 4.3 Error Handling and Debugging

- Implement error handling throughout the codebase to manage unexpected situations gracefully. Log errors and provide meaningful messages to the player when issues arise.

## FAQ

1. **How do I reset the game?**
   - You can reset the game by deleting the `high_score.json` file and starting a new session.

2. **Can I play with a friend?**
   - Yes, the game supports multiplayer mode where you can host or join a game with another player.

3. **What should I do if I encounter a bug?**
   - Please report bugs by opening an issue on our GitHub repository.

## Troubleshooting

- **Common Issues**: Refer to this section for solutions to common problems, such as installation errors or gameplay issues.
- **Support**: Contact the development team for further assistance.

## Glossary

- **Public Support**: A measure of the public's trust and approval of police actions.
- **Morale**: The general mood and motivation of the police force.
- **Multiplayer Mode**: A feature allowing multiple players to play together, either cooperatively or competitively.

## License

This project is licensed under the MIT License. For more information, see the [LICENSE](LICENSE) file.

## Contact Information

For any issues, questions, or suggestions, please reach out via our [GitHub repository](https://github.com/Nyandiekahh/Final-Maandamano-game-using-CLI) or contact the project maintainers directly.

---

Thank you for exploring the Nairobi Police and Citizens Protests Adventure! We appreciate your interest and look forward to your feedback and contributions.