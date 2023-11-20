import cocotb
from cocotb.clock import Clock
from cocotb.triggers import ClockCycles, Timer
from .result import Result

## NOP
obj0 = Result(0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0) # NOP

# ALU Operations
obj1 = Result(1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0) # Dec
obj2 = Result(2, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0) # Inc
obj3 = Result(3, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0) # Not
obj4 = Result(4, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0) # SetC
obj5 = Result(5, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0) # ClrC
obj6 = Result(6, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0) # RL
obj7 = Result(7, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0) # RR
obj8 = Result(8, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0) # RLC
obj9 = Result(9, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0) # RRC
obj10 = Result(10, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0) # Swap

cases = [obj0, obj1, obj2, obj3, obj4, obj5, obj6, obj7, obj8, obj9, obj10]

@cocotb.test()
async def ucode_test(dut):
    clock = Clock(dut.clk_tb, 10, "us")
    cocotb.fork(clock.start())

    await ClockCycles(dut.clk_tb, 2)

    for case in cases:
        dut.opcode_tb.value = case.opcode
        dut.w_tb.value = case.w
        dut.carry_tb.value = case.carry
        dut.zero_tb.value = case.zero

        await ClockCycles(dut.clk_tb, 2)
        await Timer(10, units="ns");

        assert dut.alu_operation_tb.value == case.alu_operation, f"Unexpected alu_operation for opcode {dut.opcode_tb.value}";  
        assert dut.alu_multibyte_result_tb.value == case.alu_multibyte_result, f"Unexpected alu_multibyte_result for opcode {dut.opcode_tb.value}";  
        assert dut.jump_operation_tb.value == case.jump_operation, f"Unexpected jump_operation for opcode {dut.opcode_tb.value}";  
        assert dut.jump_condition_tb.value == case.jump_condition, f"Unexpected jump_condition for opcode {dut.opcode_tb.value}";  
        assert dut.mov_operation_tb.value == case.mov_operation, f"Unexpected mov_operation for opcode {dut.opcode_tb.value}";  
        assert dut.destination_w_tb.value == case.destination_w, f"Unexpected destination_w for opcode {dut.opcode_tb.value}";  
        assert dut.destination_flags_tb.value == case.destination_flags, f"Unexpected destination_flags for opcode {dut.opcode_tb.value}";  
        assert dut.destination_memory_tb.value == case.destination_memory, f"Unexpected destination_memory for opcode {dut.opcode_tb.value}";  
        assert dut.destination_registers_tb.value == case.destination_registers, f"Unexpected destination_registers for opcode {dut.opcode_tb.value}";  
        assert dut.destination_ports_tb.value == case.destination_ports, f"Unexpected destination_ports for opcode {dut.opcode_tb.value}"; 

        assert dut.destination_index_tb.value == case.destination_index, f"Unexpected destination_index for opcode {dut.opcode_tb.value}"; 
        assert dut.ram_operand_tb.value == case.ram_operand, f"Unexpected ram_operand for opcode {dut.opcode_tb.value}"; 
        assert dut.duplicate_w_tb.value == case.duplicate_w, f"Unexpected duplicate_w for opcode {dut.opcode_tb.value}"; 

        assert dut.source_ports_tb.value == case.source_ports, f"Unexpected source_ports for opcode {dut.opcode_tb.value}"; 
        assert dut.source_registers_tb.value == case.source_registers, f"Unexpected source_registers for opcode {dut.opcode_tb.value}"; 
