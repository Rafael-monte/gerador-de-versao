class TerminalController:
    __WARNING_COLOR='\033[93m'
    __ERROR_COLOR='\033[1;31;43m'
    __EOL='\033[0;0m'
    __INFO_COLOR='\033[94m'
    
    def print_warn(self, warn_message):
        print(f'{self.__WARNING_COLOR} {warn_message} {self.__EOL}')
    
    def print_error(self, error_message):
        print(f'{self.__ERROR_COLOR} {error_message} {self.__EOL}')

    def print_info(self, info_message):
        print(f'{self.__INFO_COLOR} {info_message} {self.__EOL}')