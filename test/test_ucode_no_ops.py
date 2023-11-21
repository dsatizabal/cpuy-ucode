import cocotb
from cocotb.clock import Clock
from cocotb.triggers import ClockCycles, Timer
from .result import Result

obj61 = Result(61, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0) # Ret
obj62 = Result(62, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0) # CPU Cfg
obj63 = Result(63, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1) # TMR Cfg

# Mov W2Port
obj64 = Result(64, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0)
obj65 = Result(65, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0) 

# Mov Port2W
obj72 = Result(72, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0)
obj73 = Result(73, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0)

# Mov W2Reg
obj80 = Result(80, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
obj81 = Result(81, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0)
obj82 = Result(82, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0)
obj83 = Result(83, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 3, 0, 0, 0, 0, 0, 0, 0, 0)
obj84 = Result(84, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 4, 0, 0, 0, 0, 0, 0, 0, 0)
obj85 = Result(85, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 5, 0, 0, 0, 0, 0, 0, 0, 0)
obj86 = Result(86, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 6, 0, 0, 0, 0, 0, 0, 0, 0)
obj87 = Result(87, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 7, 0, 0, 0, 0, 0, 0, 0, 0)

# Mov Reg2W
obj88 = Result(88, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0)
obj89 = Result(89, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0)
obj90 = Result(90, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 2, 0, 0, 0, 1, 0, 0, 0, 0)
obj91 = Result(91, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 3, 0, 0, 0, 1, 0, 0, 0, 0)
obj92 = Result(92, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 4, 0, 0, 0, 1, 0, 0, 0, 0)
obj93 = Result(93, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 5, 0, 0, 0, 1, 0, 0, 0, 0)
obj94 = Result(94, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 6, 0, 0, 0, 1, 0, 0, 0, 0)
obj95 = Result(95, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 7, 0, 0, 0, 1, 0, 0, 0, 0)

# SetbW
obj96 = Result(96, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
obj97 = Result(97, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
obj98 = Result(98, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
obj99 = Result(99, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
obj100 = Result(100, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
obj101 = Result(101, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
obj102 = Result(102, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
obj103 = Result(103, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)

# ClrbW
obj104 = Result(104, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
obj105 = Result(105, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
obj106 = Result(106, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
obj107 = Result(107, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
obj108 = Result(108, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
obj109 = Result(109, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
obj110 = Result(110, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
obj111 = Result(111, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)

cases = [obj64, obj65, obj72, obj73, obj80, obj81, obj82, obj83, obj84, obj85, obj86, obj87, obj88, obj89, 
         obj90, obj91, obj92, obj93, obj94, obj95, obj96, obj97, obj98, obj99, obj100, obj101, obj102, obj103,
         obj104, obj105, obj106, obj107, obj108, obj109, obj110, obj111]

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
        dut.sign_tb.value = case.sign
        
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

        assert dut.stack_operation_tb.value == case.stack_operation, f"Unexpected stack_operation for opcode {dut.opcode_tb.value}"; 
        assert dut.stack_direction_tb.value == case.stack_direction, f"Unexpected stack_direction for opcode {dut.opcode_tb.value}"; 
        assert dut.destination_cpu_config_tb.value == case.destination_cpu_config, f"Unexpected destination_cpu_config for opcode {dut.opcode_tb.value}"; 
        assert dut.destination_timer_config_tb.value == case.destination_timer_config, f"Unexpected destination_timer_config for opcode {dut.opcode_tb.value}";
