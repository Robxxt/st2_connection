import subprocess
import csv
import sys
import os

class   MainProgram:
    '''
    - self._selected_instace is a nested list with the next format:
    [
        [instance_hostname1, instance_alias2],
        ...
        [instance_hostname<n>, instance_alias<n>]
    ]
    '''
    def __init__(self):
        self._instances = None
        self._csv_file = None
        self._selected_instance_hostname = None

    '''
    Reads the csv file containing the instances and populates
    self._instances.
    '''
    def load_csv(self, csv_filename):
        try:
            with open(csv_filename, mode='r', newline='') as file:
                self._instances = [row for row in csv.reader(file)]
        except:
            # maybe instead of exiting directly I can first try to call update_csv
            print(f"{csv_filename} doesn't exists or you don't have permissions", file=sys.stderr)
            sys.exit(1)
    
    '''
    Retrieves the list with the instances and
    stores them in instances.csv to retrieve all the data.
    '''
    def update_csv(self):
        # to implement
        pass

    '''
    Displays instances in a "pretty" manner
    '''
    def display_instances(self):
        print("-" * 29)
        print("| WELCOME TO st2_connection |")
        print("-" * 29, '\n')
        print('INSTANCE LIST\n')
        print('index\tinstance alias\tinstance hostname\n')
        for index, instance in enumerate(self._instances):
            print(f' {index} |\t{instance[0]}\t| {instance[1]}')
    
    '''
    Reads an int from the user. Keeps asking for until the user
    provides a valid int number that is within the range
    of _instances list. Once it reads correctly, sets _selected_instance_hostname
    to be the instance hostname.
    '''
    def read_instance_index(self):
        while True:
            try:
                intance_index = int(input())
                # check weather instance_index is out of range.
                if (intance_index < 0 or intance_index >= len(self._instances)):
                    raise ValueError
                self._selected_instance_hostname = self._instances[intance_index][0]
                break
            except KeyboardInterrupt:
                sys.exit(1)
            except ValueError:
                print("Invalid instance! the index doesn't exists", file=sys.stderr)
    
    '''
    Connects to the remote instance
    '''
    def connect(self):
        username = os.environ.get('USER')
        target = f"{username}@{self._selected_instance_hostname}"
        # payload refers to the command that we want to execute
        payload = f"ssh -A -J {target} {target}"
        print(payload)
        '''
        ---------------------------------------------------------
        | DON'T RUN UNTIL YOU HAVE A CORRECT instances.csv FILE!|
        --------------------------------------------------------
        command = subprocess.run(payload, shell=True)
        if (command.returncode != 0):
            print("[ERROR]: Couldn't establish/keep the connection", file=sys.stderr)
            sys.exit(1)
        else:
            print('Everything went fine! Hope to see you next time ;)')
            sys.exit(0)
        '''
    def run(self):
        self.display_instances()
        self.read_instance_index()
        self.connect()

if __name__ == '__main__':
    app = MainProgram()
    app.load_csv('instances.csv')
    app.run()