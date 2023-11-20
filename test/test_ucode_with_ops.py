import cocotb
from cocotb.clock import Clock
from cocotb.triggers import ClockCycles, Timer
from .result import Result

# opcode, w, carry, zero, alu_operation, alu_multibyte_result, jump_operation, jump_condition, mov_operation, destination_w, destination_flags, destination_memory, destination_registers, destination_ports
# Instructions with operands
# Mov
obj128 = Result(128, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1, 0) # MovMW
obj129 = Result(129, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1, 0) # MovMW
obj130 = Result(130, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0) # MovWM
obj131 = Result(131, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0) # MovWM
obj132 = Result(132, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0) # MovLW
obj133 = Result(133, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0) # MovLW
obj134 = Result(134, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0) # MovLW
obj135 = Result(135, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0) # MovLW

# Aritmetic and logic
obj136 = Result(136, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0) # AddLW
obj137 = Result(137, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0) # AddLW
obj138 = Result(138, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0) # AddMW
obj139 = Result(139, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0) # AddMW
obj140 = Result(140, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0) # SubLW
obj141 = Result(141, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0) # SubLW
obj142 = Result(142, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0) # SubMW
obj143 = Result(143, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0) # SubMW
obj144 = Result(144, 0, 0, 0, 1, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0) # MulLW
obj145 = Result(145, 0, 0, 0, 1, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0) # MulLW
obj146 = Result(146, 0, 0, 0, 1, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0) # MulMW
obj147 = Result(147, 0, 0, 0, 1, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0) # MulMW
obj148 = Result(148, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0) # AndLW
obj149 = Result(149, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0) # AndLW
obj150 = Result(150, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0) # AndMW
obj151 = Result(151, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0) # AndMW
obj152 = Result(152, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0) # OrLW
obj153 = Result(153, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0) # OrLW
obj154 = Result(154, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0) # OrMW
obj155 = Result(155, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0) # OrMW
obj156 = Result(156, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0) # XorLW
obj157 = Result(157, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0) # XorLW
obj158 = Result(158, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0) # XorMW
obj159 = Result(159, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0) # XorMW

# Xch MW
obj160 = Result(160, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 0, 0, 0, 0, 1)
obj161 = Result(161, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 0, 0, 0, 0, 1)

# Jmp
obj162 = Result(162, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0)
obj163 = Result(163, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0)

# JmpC
obj164 = Result(164, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
obj165 = Result(165, 0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0)

# JmpZ
obj166 = Result(166, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
obj167 = Result(167, 0, 0, 1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0)

# Call
# obj168 = Result(168, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
# obj169 = Result(169, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)

# Tbjc 0
obj224 = Result(224, 255, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
obj225 = Result(225, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0)

# Tbjc 1
obj226 = Result(226, 255, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
obj227 = Result(227, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0)

# Tbjc 2
obj228 = Result(228, 255, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
obj229 = Result(229, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0)

# Tbjc 3
obj230 = Result(230, 255, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
obj231 = Result(231, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0)

# Tbjc 4
obj232 = Result(232, 255, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
obj233 = Result(233, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0)

# Tbjc 5
obj234 = Result(234, 255, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
obj235 = Result(235, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0)

# Tbjc 6
obj236 = Result(236, 255, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
obj237 = Result(237, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0)

# Tbjc 7
obj238 = Result(238, 255, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
obj239 = Result(239, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0)

# Tbjs 0
obj240 = Result(240, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
obj241 = Result(241, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0)

# Tbjs 1
obj242 = Result(242, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
obj243 = Result(243, 2, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0)

# Tbjs 2
obj244 = Result(244, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
obj245 = Result(245, 4, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0)

# Tbjs 3
obj246 = Result(246, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
obj247 = Result(247, 8, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0)

# Tbjs 4
obj246 = Result(248, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
obj249 = Result(249, 16, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0)

# Tbjs 5
obj250 = Result(250, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
obj251 = Result(251, 32, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0)

# Tbjs 6
obj252 = Result(252, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
obj253 = Result(253, 64, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0)

# Tbjs 7
obj254 = Result(254, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
obj255 = Result(255, 128, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0)

cases = [obj128, obj129, obj130, obj131, obj132, obj133, obj134, obj135, obj136, obj137,
         obj138, obj139, obj140, obj141, obj142, obj143, obj144, obj145, obj146, obj147,
         obj148, obj149, obj150, obj151, obj152, obj153, obj154, obj155, obj156, obj157,
         obj158, obj159, obj160, obj161, obj162, obj163, obj164, obj165, obj166, obj167, 
         obj224, obj225, obj226, obj227, obj228, obj229, obj230, obj231, obj232, obj233,
         obj234, obj235, obj236, obj237, obj238, obj239, obj240, obj241, obj242, obj243,
         obj244, obj245, obj246, obj247, obj246, obj249, obj250, obj251, obj252, obj253,
         obj254, obj255]

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
