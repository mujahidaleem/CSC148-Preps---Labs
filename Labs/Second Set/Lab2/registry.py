CATEGORIES = 'u20','u30','u40','o40'

class Race:
    '''
    === Attributes (Public and Private) ==
    name:
        The name of the race
    all_runners:
        The runners in the race
    race_category:
        A dictionary containing each category
    === Representation Invariants ===
    '''

    name: str
    all_runners: list[Runner]
    race_category: dict[str:list[Runner]]

    def __init__(self, name: str) -> None:
        self.name = name
        self.all_runners = []
        self.race_categories = dict.fromkeys(CATEGORIES)

    def add_runner(self, runner: list) -> None:
        '''Adds runners and seperates them into categories'''
        if runner.


    def update_categories(self) -> None:
        '''Updates the categories'''
        pass

    def category(self, category) -> list[Runners]:
        'Returns all racers with the specified'
        return


class Runner:
    '''The organizaer for the 5k running tournament thing

    === Attributes ===
    name:
        The name of the runner
    email:
        The email of the runner
    speed:
        Speed of the runner
    category:
        Race category of the horse

     === Representation Invariants ===
    - Speed can only be within these ranges:
        -> under 20 minutes
        -> under 30 minutes
        -> under 40 minutes
        -> 40 minutes or over

    '''
    name: str
    email: str
    speed: int
    category: str

    def __init__(self, name: str, email: str, speed: int ) -> None:
        self.name = name
        self.email = email
        self.speed = speed
        self.category = self.update_category()

    def update_category(self) -> None:
        if self.speed < 20:
            self.category = 'under 20 minutes'
        elif self.speed < 30:
            self.category = 'under 30 minutes'
        elif self.speed < 40:
            self.category = 'under 40 minutes'
        else:
            self.category = '40 minutes or over'

    def change_email(self, new:str) -> None:
        self.email = new

    def change_speed(self, speed:int) -> None:
        self.speed = speed
        self.update_category()

    def withdraw(self) -> None:
        del self

if __name__ == '__main__':
    race = Race()
    race.add_runner(Runner('Gerhard', 'Gerhard@123.com', 39))
    race.add_runner(Runner('Tom', 'Tom@123.com', 29))
     Runner('Toni', 'Toni@123.com', 19),
     Runner('Margot', 'Margot@123.com', 28),
     Runner('Gerhard', 'Gerhard@123.com', 26)
    print(race.category('u30'))

