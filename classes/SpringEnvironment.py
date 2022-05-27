from classes.AbstractEnvironment import AbstractEnvironment

class SpringEnvironment(AbstractEnvironment):
    
    def __init__(self):
        self.environment_name = 'spring'
        self.get_environment_from_file()