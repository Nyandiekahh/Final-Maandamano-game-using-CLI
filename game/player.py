# Player class
class Player:
    def __init__(self, background):
        self.background = background
        if background == "Veteran Officer":
            self.strengths = ["Experienced", "High morale boost", "Better negotiation"]
            self.weaknesses = ["Old-fashioned thinking", "Slower physical abilities"]
        elif background == "Rookie Officer":
            self.strengths = ["High energy", "Quick to respond", "Innovative thinking"]
            self.weaknesses = ["Lack of experience", "Lower trust from senior officers"]
        elif background == "Community Liaison":
            self.strengths = ["High trust from citizens", "Good communication skills"]
            self.weaknesses = ["Limited combat training", "Viewed as too lenient"]
        else:  # Tactical Expert
            self.strengths = ["Strategic thinking", "Excellent in crisis management"]
            self.weaknesses = ["Poor interpersonal skills", "Sometimes too aggressive"]
