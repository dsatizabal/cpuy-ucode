import cocotb
from cocotb.triggers import ReadWrite, Timer

@cocotb.test()
async def ucode_test(dut):
    # Verifies that for every possible opcode the operation type is unique as it only depends on opcode value
    for opcode in range(256):
        dut.opcode_tb.value = opcode
        dut.w_tb.value = 0
        dut.carry_tb.value = 0
        dut.zero_tb.value = 0

        await ReadWrite()
        await Timer(10, units="ns");

        assert dut.alu_operation_tb.value + dut.jump_operation_tb.value + dut.mov_operation_tb.value + dut.stack_operation_tb.value <= 1, f"Unexpected mutitype operation: opcode {dut.opcode_tb.value}, alU {dut.alu_operation_tb.value}, jmp {dut.jump_operation_tb.value}, mov {dut.mov_operation_tb.value}, stack {dut.stack_operation_tb.value}";  
