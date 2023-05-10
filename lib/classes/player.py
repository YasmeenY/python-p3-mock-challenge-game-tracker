class Player:

    all = []

    def __init__(self, username):
        self.username = username
        self._results = []
        self._games_played = []

        Player.all.append(self)
        
    @property
    def username(self):
        return self._username
    @username.setter
    def username(self, username):
        if type(username) == str and 2 <= len(username) <= 16:
            self._username = username
        else:
            raise Exception("Invalid username")

    def results(self, new_result=None):
        from classes.result import Result
        if isinstance(new_result, Result):
            self._results.append(new_result)
        return self._results
    def games_played(self, new_game=None):
        from classes.game import Game
        if isinstance(new_game, Game):
            self._games_played.append(new_game)
        return self._games_played
    
    def played_game(self, game):
        return game in self._games_played
    
    def num_times_played(self, game):
        return len([times for times in self._results if times.game == game])
    
    ##Bonus deliverable haven't tested
    @classmethod
    def highest_scored(cls, game):
        if cls.all:
            max_score = 0
            max_player = None

            for player in cls.all:
                if game.average_score(player) > max_score:
                    max_score = game.average_score(player)
                    max_player = player
                return max_player
            return None

