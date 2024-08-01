# nairobi_police_game.py

import json
import random
import pygame
import os
from .colors import Colors  # Import the Colors class
from .game_state import GameState
from .player import Player
from .help import Help
from .quit import Quit

class NairobiPoliceGame:
    def __init__(self):
        self.game_state = GameState()
        self.load_high_score()
        self.load_progress()
        self.locations = ["CBD", "Kibera", "Mathare", "Uhuru Park", "City Hall", "Nairobi Hospital"]
        self.current_day = 1
        self.max_days = 7
        pygame.init()
        pygame.mixer.init()
        self.buzz_sound = pygame.mixer.Sound("assets/buzz-buzz-95806.mp3")

    def load_high_score(self):
        try:
            with open("db.json", "r") as f:
                data = json.load(f)
                if isinstance(data, dict):
                    self.high_score = data.get("high_score", 0)
                else:
                    print(f"{Colors.FAIL}Unexpected data structure in db.json. Expected a dictionary.{Colors.RESET}")
                    self.high_score = 0
        except FileNotFoundError:
            self.high_score = 0
        except json.JSONDecodeError:
            print(f"{Colors.FAIL}Error decoding JSON from db.json.{Colors.RESET}")
            self.high_score = 0

    def save_high_score(self):
        data = {
            "high_score": max(self.high_score, self.game_state.score),
            "score": self.game_state.score,
            "current_day": self.current_day,
            "resources": self.game_state.resources
        }
        with open("db.json", "w") as f:
            json.dump(data, f)

    def load_progress(self):
        try:
            with open("db.json", "r") as f:
                data = json.load(f)
                self.game_state.score = data.get("score", 0)
                self.current_day = data.get("current_day", 1)
                self.game_state.resources = data.get("resources", self.game_state.resources)
        except FileNotFoundError:
            pass

    def start_game(self):
        print(f"{Colors.HEADER}Welcome to the Nairobi Police and Citizens Protests Adventure!{Colors.RESET}")
        print(f"{Colors.OKGREEN}Current High Score: {self.high_score}{Colors.RESET}")
        self.character_creation()
        self.main_game_loop()

    def character_creation(self):
        print(f"{Colors.BOLD}Choose your character background:{Colors.RESET}")
        print(f"{Colors.OKCYAN}1. Veteran Officer{Colors.RESET}")
        print(f"{Colors.OKBLUE}2. Rookie Officer{Colors.RESET}")
        print(f"{Colors.OKGREEN}3. Community Liaison{Colors.RESET}")
        print(f"{Colors.WARNING}4. Tactical Expert{Colors.RESET}")

        while True:
            choice = self.get_player_input("Enter your choice (1-4): ")
            if choice in ["1", "2", "3", "4"]:
                backgrounds = ["Veteran Officer", "Rookie Officer", "Community Liaison", "Tactical Expert"]
                self.game_state.player = Player(backgrounds[int(choice) - 1])
                print(f"\n{Colors.OKGREEN}You have chosen: {self.game_state.player.background}{Colors.RESET}")
                print(f"Strengths: {Colors.OKCYAN}" + ", ".join(self.game_state.player.strengths) + f"{Colors.RESET}")
                print(f"Weaknesses: {Colors.FAIL}" + ", ".join(self.game_state.player.weaknesses) + f"{Colors.RESET}")
                break
            else:
                self.buzz_sound.play()  # Play buzzing sound for invalid choice
                print(f"{Colors.FAIL}Invalid choice. Please enter a number between 1 and 4.{Colors.RESET}")

    def get_player_input(self, prompt):
        while True:
            user_input = input(prompt).strip().lower()
            if user_input == 'h':
                Help.display_help()
            elif user_input == 'q':
                Quit.quit_game()
            else:
                return user_input

    def main_game_loop(self):
        while self.current_day <= self.max_days:
            print(f"\n{Colors.BOLD}--- Day {self.current_day} of {self.max_days} ---{Colors.RESET}")
            self.display_game_state()
            self.handle_location_event()
            self.handle_random_event()
            self.handle_player_action()
            self.update_game_state()
            if self.check_game_over():
                break
            self.current_day += 1
        self.end_game()

    def display_game_state(self):
        print(f"\n{Colors.BOLD}Current Location: {self.game_state.current_location}{Colors.RESET}")
        print(f"Score: {self.game_state.score}")
        print(f"Resources:")
        for resource, value in self.game_state.resources.items():
            print(f"  {Colors.BOLD}{resource.capitalize()}: {value}{Colors.RESET}")

    def handle_location_event(self):
        events = {
            "CBD": ["Traffic congestion due to protests", "Business owners complaining about lost revenue"],
            "Kibera": ["Reports of unrest in informal settlements", "Community leaders requesting a meeting"],
            "Mathare": ["Youth groups organizing peaceful demonstrations", "Rumors of potential violence"],
            "Uhuru Park": ["Large gathering for a political rally", "Environmental activists staging a sit-in"],
            "City Hall": ["Government officials demanding action", "Protesters attempting to enter the building"],
            "Nairobi Hospital": ["Injured protesters seeking treatment", "Staff overwhelmed by the influx of patients"]
        }
        event = random.choice(events[self.game_state.current_location])
        print(f"\n{Colors.WARNING}Location Update: {event}{Colors.RESET}")
        self.handle_location_specific_challenge(event)

    def handle_location_specific_challenge(self, event):
        print(f"\n{Colors.BOLD}How do you want to respond to this situation?{Colors.RESET}")
        print(f"{Colors.OKGREEN}1. Take immediate action{Colors.RESET}")
        print(f"{Colors.OKCYAN}2. Gather more information{Colors.RESET}")
        print(f"{Colors.OKBLUE}3. Delegate to a specialized team{Colors.RESET}")
        choice = self.get_player_input("Enter your choice (1-3): ")

        if choice == "1":
            success = random.random() < 0.5
            if success:
                self.print_success("Your quick action resolved the situation effectively.")
                self.update_score(15)
            else:
                self.print_failure("Your hasty decision led to complications.")
                self.update_score(-10)
        elif choice == "2":
            self.print_success("You gained valuable insights by gathering more information.")
            self.update_score(5)
            self.game_state.resources["public_support"] += 3
        elif choice == "3":
            success = random.random() < 0.7
            if success:
                self.print_success("The specialized team handled the situation well.")
                self.update_score(10)
            else:
                self.print_failure("The team struggled to manage the situation effectively.")
                self.update_score(-5)
        else:
            self.buzz_sound.play()  # Play buzzing sound for invalid choice
            self.print_failure("Invalid choice. Opportunity lost.")
            self.update_score(-5)

    def handle_random_event(self):
        events = [
            self.peaceful_protest_event,
            self.media_scrutiny_event,
            self.natural_disaster_event,
            self.political_interference_event,
            self.resource_shortage_event
        ]
        random.choice(events)()

    def peaceful_protest_event(self):
        print(f"\n{Colors.OKBLUE}A peaceful protest has started in Uhuru Park.{Colors.RESET}")
        success = random.random() < 0.6
        if success:
            self.print_success("The protest remained peaceful, thanks to your effective crowd control.")
            self.update_score(10)
        else:
            self.print_failure("The protest turned violent despite your efforts.")
            self.update_score(-15)

    def media_scrutiny_event(self):
        print(f"\n{Colors.OKCYAN}The media is scrutinizing police actions.{Colors.RESET}")
        success = random.random() < 0.7
        if success:
            self.print_success("The media reports were favorable, boosting public support.")
            self.update_score(10)
            self.game_state.resources["public_support"] += 5
        else:
            self.print_failure("The media portrayed the police negatively, causing public backlash.")
            self.update_score(-10)
            self.game_state.resources["public_support"] -= 5

    def natural_disaster_event(self):
        print(f"\n{Colors.WARNING}A natural disaster has struck, complicating the situation.{Colors.RESET}")
        success = random.random() < 0.5
        if success:
            self.print_success("Your team effectively managed the disaster, earning public praise.")
            self.update_score(20)
        else:
            self.print_failure("The disaster response was inadequate, causing further chaos.")
            self.update_score(-20)

    def political_interference_event(self):
        print(f"\n{Colors.FAIL}There is political interference affecting police operations.{Colors.RESET}")
        success = random.random() < 0.6
        if success:
            self.print_success("You successfully navigated the political challenges.")
            self.update_score(15)
        else:
            self.print_failure("Political interference hampered your efforts, leading to setbacks.")
            self.update_score(-15)

    def resource_shortage_event(self):
        print(f"\n{Colors.WARNING}A shortage of resources is limiting police effectiveness.{Colors.RESET}")
        self.print_failure("You need to allocate your resources wisely to overcome this challenge.")
        self.update_score(-10)
        self.game_state.resources["equipment"] -= 10

    def handle_player_action(self):
        print(f"\n{Colors.BOLD}Choose your action:{Colors.RESET}")
        print(f"{Colors.OKGREEN}1. Address the crowd with a calming speech{Colors.RESET}")
        print(f"{Colors.OKCYAN}2. Deploy a small, visible police presence{Colors.RESET}")
        print(f"{Colors.OKBLUE}3. Organize a dialogue with community leaders{Colors.RESET}")
        print(f"{Colors.WARNING}4. Allow protests to proceed with minimal intervention{Colors.RESET}")
        choice = self.get_player_input("Enter your choice (1-4): ")

        if choice == "1":
            success = random.random() < 0.7
            if success:
                self.print_success("Your speech calmed the crowd, reducing tension.")
                self.update_score(10)
                self.game_state.resources["public_support"] += 5
            else:
                self.print_failure("The crowd reacted negatively to your speech.")
                self.update_score(-10)
        elif choice == "2":
            success = random.random() < 0.5
            if success:
                self.print_success("The visible police presence deterred potential violence.")
                self.update_score(10)
                self.game_state.resources["personnel"] -= 5
            else:
                self.print_failure("The presence escalated tensions.")
                self.update_score(-10)
        elif choice == "3":
            success = random.random() < 0.8
            if success:
                self.print_success("Dialogue with leaders was successful in easing tensions.")
                self.update_score(15)
            else:
                self.print_failure("The dialogue failed to achieve its goals.")
                self.update_score(-5)
        elif choice == "4":
            success = random.random() < 0.4
            if success:
                self.print_success("Allowing the protests to proceed peacefully was a wise decision.")
                self.update_score(5)
            else:
                self.print_failure("The lack of intervention led to unrest.")
                self.update_score(-15)
        else:
            self.buzz_sound.play()  # Play buzzing sound for invalid choice
            self.print_failure("Invalid choice. No action taken.")
            self.update_score(-5)

    def update_game_state(self):
        self.update_resources()

    def update_resources(self):
        self.game_state.resources["personnel"] += random.randint(-5, 5)
        self.game_state.resources["equipment"] += random.randint(-5, 5)
        self.game_state.resources["public_support"] += random.randint(-5, 5)
        self.game_state.resources["morale"] += random.randint(-5, 5)

        for key in self.game_state.resources:
            self.game_state.resources[key] = max(0, min(self.game_state.resources[key], 100))

    def print_success(self, message):
        print(f"{Colors.OKGREEN}{message}{Colors.RESET}")

    def print_failure(self, message):
        print(f"{Colors.FAIL}{message}{Colors.RESET}")

    def update_score(self, points):
        self.game_state.score += points

    def check_game_over(self):
        if self.game_state.resources["personnel"] <= 0:
            print(f"\n{Colors.FAIL}Game Over: All personnel have been exhausted.{Colors.RESET}")
            return True
        if self.game_state.resources["equipment"] <= 0:
            print(f"\n{Colors.FAIL}Game Over: All equipment has been lost.{Colors.RESET}")
            return True
        if self.game_state.resources["public_support"] <= 0:
            print(f"\n{Colors.FAIL}Game Over: Public support has been lost.{Colors.RESET}")
            return True
        if self.game_state.resources["morale"] <= 0:
            print(f"\n{Colors.FAIL}Game Over: Morale is too low to continue.{Colors.RESET}")
            return True
        return False

    def end_game(self):
        print(f"\n{Colors.BOLD}Game Over! Your final score is {self.game_state.score}.{Colors.RESET}")
        if self.game_state.score > self.high_score:
            print(f"{Colors.OKGREEN}Congratulations! You've set a new high score: {self.game_state.score}{Colors.RESET}")
            self.high_score = self.game_state.score
            self.save_high_score()
        else:
            print(f"The current high score is: {self.high_score}")
        self.save_progress()
