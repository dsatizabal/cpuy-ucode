`default_nettype none
`timescale 1ns/1ns

/*
this testbench just instantiates the module and makes some convenient wires
that can be driven / tested by the cocotb test.py
*/

module tb (
    // testbench is controlled by test/test_*.py files
    input wire clk_tb,
    input wire [7:0] opcode_tb,
    input wire [7:0] w_tb,
    input wire carry_tb,
    input wire zero_tb,
    output wire alu_operation_tb,
    output wire alu_multibyte_result_tb,
    output wire jump_operation_tb,
    output wire jump_condition_tb,
    output wire mov_operation_tb,
    output wire destination_w_tb,
    output wire destination_flags_tb,
    output wire destination_memory_tb,
    output wire destination_registers_tb,
    output wire destination_ports_tb,
    output reg [2:0] destination_index_tb,
    output wire ram_operand_tb,
    output wire duplicate_w_tb
);

    // instantiate the DUT
    ucode ucode(
        .clk (clk_tb),
        .opcode (opcode_tb),
        .w (w_tb),
        .carry (carry_tb),
        .zero (zero_tb),
        .alu_operation (alu_operation_tb),
        .alu_multibyte_result (alu_multibyte_result_tb),
        .jump_operation (jump_operation_tb),
        .jump_condition (jump_condition_tb),
        .mov_operation (mov_operation_tb),
        .destination_w (destination_w_tb),
        .destination_flags (destination_flags_tb),
        .destination_memory (destination_memory_tb),
        .destination_registers (destination_registers_tb),
        .destination_ports (destination_ports_tb),
        .destination_index (destination_index_tb),
        .ram_operand (ram_operand_tb),
        .duplicate_w (duplicate_w_tb)
    );

endmodule
