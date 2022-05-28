from classes.AbstractEnvironment import AbstractEnvironment

class AngularEnvironment(AbstractEnvironment):
    generate_app_afterVersion=False
    app_commands=[]
    
    def __init__(self):
        self.environment_name='angular';
        self.add_aditional_attributes(self.get_environment_from_file())

    def add_aditional_attributes(self, config_i) -> None:
        self.generate_app_afterVersion=config_i.generateAppAfterVersion;
        self.app_commands=config_i.appCommands;

    def show(self) -> None:
        app_commands = ', '.join(self.app_commands);
        print(f'Versao: {self.version}, appCommands: {app_commands}')
        