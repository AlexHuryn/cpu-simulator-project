from cpu import CPU

INSTRUCTION_INPUT_FILE = "instruction_input.txt"
DATA_INPUT_FILE = "data_input.txt"


def fetch_instructions():
    instruction_file = open(INSTRUCTION_INPUT_FILE, 'r')
    instructions = instruction_file.readlines()
    instructions = list(map(lambda s: s.strip(), instructions))
    return instructions


def fetch_data():
    instruction_file = open(INSTRUCTION_INPUT_FILE, 'r')
    instructions = instruction_file.readlines()
    instructions = list(map(lambda s: s.strip(), instructions))
    return instructions


def initialize_memory_bus(cpu):
    data_loaded = fetch_data()
    for data in data_loaded:
        data_parsed = data.split(",")
        cpu.write_memory_bus(data_parsed[0], data_parsed[1])


def send_instructions_to_cpu(cpu):
    instructions_loaded = fetch_instructions()
    for instruction in instructions_loaded:
        cpu.parse_instruction(instruction)


my_cpu = CPU()
print("---------------------------------------------------")
print("Welcome to the Python CPU Simulator!")
print("---------------------------------------------------")
print("Initializing Memory Bus from data input file...")
initialize_memory_bus(my_cpu)
print("Memory Bus successfully initialized")
print("---------------------------------------------------")
print("Sending instructions to CPU...")
send_instructions_to_cpu(my_cpu)
print("---------------------------------------------------")
print("Terminating CPU Processing...")
