
from classes.FileHandler import FileHandler
class AbstractEnvironment:
    environment_name=''
    command=''
    version=''
    environment=''
    defaultEnvironment=''
    CONFIG_FILE_LOCATION='setup-files\$CONFIG-FILE-NAME$-config.json'
    CONFIG_FILE_TOKEN='$CONFIG-FILE-NAME$'

    ##CONVERTE PARA OBJETO DO AMBIENTE
    def get_environment_from_file(self) -> object:
        env_instance = FileHandler.convert_json_to_object(self.CONFIG_FILE_LOCATION.replace(self.CONFIG_FILE_TOKEN, self.environment_name))
        self.version = env_instance.version;
        self.command=env_instance.command;
        self.environment=env_instance.environment;
        self.ENV_NAME_TOKEN=env_instance.ENV_NAME_TOKEN;
        self.AVAILABLE_ENVIRONMENTS=env_instance.AVAILABLE_ENVIRONMENTS;
        return env_instance;
    
    def versionar(self):
        pass;
    
    def get_config_file_in_location(self) -> str:
        return FileHandler.get_file_by_location(self.CONFIG_FILE_LOCATION)
