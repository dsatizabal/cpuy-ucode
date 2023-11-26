class Result:
    def __init__(self, opcode, w, carry, zero, sign, alu_operation, alu_multibyte_result, jump_operation, jump_condition, mov_operation, destination_w, destination_flags, destination_memory, destination_registers, destination_ports, destination_index, ram_operand, duplicate_w, source_ports, source_registers, stack_operation, stack_direction, destination_cpu_config, destination_timer_config, source_operands):
        self.opcode = opcode
        self.w = w
        self.carry = carry
        self.zero = zero
        self.sign = sign
        self.alu_operation = alu_operation
        self.alu_multibyte_result = alu_multibyte_result
        self.jump_operation = jump_operation
        self.jump_condition = jump_condition
        self.mov_operation = mov_operation
        self.destination_w = destination_w
        self.destination_flags = destination_flags
        self.destination_memory = destination_memory
        self.destination_registers = destination_registers
        self.destination_ports = destination_ports
        self.destination_index = destination_index
        self.ram_operand = ram_operand
        self.duplicate_w = duplicate_w
        self.source_ports = source_ports
        self.source_registers = source_registers
        self.stack_operation = stack_operation
        self.stack_direction = stack_direction
        self.destination_cpu_config = destination_cpu_config
        self.destination_timer_config = destination_timer_config
        self.source_operands = source_operands