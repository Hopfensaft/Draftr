points_kill = 3
points_death = -1
points_assist = 2
points_win = 2


class player():
    def __init__(self, player_id):
        self.player_id = player_id
        self.expected_score = 0
        self.value = 0



    def score_player(self, kills, deaths, assists):
        self.expected_score = kills * points_kill + deaths * points_death + assists * points_assist

    def player_value(self, cost):
        self.value = self.expected_score/cost
