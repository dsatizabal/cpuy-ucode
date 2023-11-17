`default_nettype none
`timescale 1ns/1ns

module ucode (
    input wire clk,
    input wire [7:0] opcode,
    input wire [7:0] w,
    input wire carry,
    input wire zero,
    output wire alu_operation,
    output wire alu_multibyte_result,
    output wire jump_operation,
    output wire jump_condition,
    output wire mov_operation,
    output wire destination_w,
    output wire destination_flags,
    output wire destination_memory,
    output wire destination_registers,
    output wire destination_ports
);

	reg regalu_op;
    reg alu_mb;
    reg jmp_op;
    reg jmp_condition;
    reg mov_op;
    reg dst_w;
    reg dst_f;
    reg dst_memory;
    reg dst_reg;
    reg dst_por;

	always @(posedge clk) begin
		alu_op <= 0;
		alu_mb <= 0;
		jmp_op <= 0;
		jmp_condition <= 0;
		mov_op <= 0;
		dst_w <= 0;
		dst_f <= 0;
		dst_memory <= 0;
		dst_reg <= 0;
		dst_por <= 0;

		case (opcode)
			// Instructions without operands
			8'b0000_0000: begin // NOP does nothing
			end
			8'b0000_0001: begin // Dec
				alu_op <= 1;
				dst_w <= 1;
			end
			8'b0000_0010: begin // Inc
				alu_op <= 1;
				dst_w <= 1;
			end
			8'b0000_0011: begin // Not
				alu_op <= 1;
				dst_w <= 1;
			end
			8'b0000_0100: begin // SetC
				alu_op <= 1;
				dst_f <= 1;
			end
			8'b0000_0101: begin // ClrC
				alu_op <= 1;
				dst_f <= 1;
			end
			8'b0000_0110: begin // RL
				alu_op <= 1;
				dst_w <= 1;
			end
			8'b0000_0111: begin // RR
				alu_op <= 1;
				dst_w <= 1;
			end
			8'b0000_1000: begin // RLC
				alu_op <= 1;
				dst_w <= 1;
			end
			8'b0000_1001: begin // RRC
				alu_op <= 1;
				dst_w <= 1;
			end
			8'b0000_1010: begin // Swap
				alu_op <= 1;
				dst_w <= 1;
			end
			8'b0000_1011: begin
			end
			8'b0000_1100: begin
			end
			8'b0000_1101: begin
			end
			8'b0000_1110: begin
			end
			8'b0000_1111: begin
			end
			8'b0001_0000: begin
			end
			8'b0001_0001: begin
			end
			8'b0001_0010: begin
			end
			8'b0001_0011: begin
			end
			8'b0001_0100: begin
			end
			8'b0001_0101: begin
			end
			8'b0001_0110: begin
			end
			8'b0001_0111: begin
			end
			8'b0001_1000: begin
			end
			8'b0001_1001: begin
			end
			8'b0001_1010: begin
			end
			8'b0001_1011: begin
			end
			8'b0001_1100: begin
			end
			8'b0001_1101: begin
			end
			8'b0001_1110: begin
			end
			8'b0001_1111: begin
			end
			8'b0010_0000: begin
			end
			8'b0010_0001: begin
			end
			8'b0010_0010: begin
			end
			8'b0010_0011: begin
			end
			8'b0010_0100: begin
			end
			8'b0010_0101: begin
			end
			8'b0010_0110: begin
			end
			8'b0010_0111: begin
			end
			8'b0010_1000: begin
			end
			8'b0010_1001: begin
			end
			8'b0010_1010: begin
			end
			8'b0010_1011: begin
			end
			8'b0010_1100: begin
			end
			8'b0010_1101: begin
			end
			8'b0010_1110: begin
			end
			8'b0010_1111: begin
			end
			8'b0011_0000: begin
			end
			8'b0011_0001: begin
			end
			8'b0011_0010: begin
			end
			8'b0011_0011: begin
			end
			8'b0011_0100: begin
			end
			8'b0011_0101: begin
			end
			8'b0011_0110: begin
			end
			8'b0011_0111: begin
			end
			8'b0011_1000: begin
			end
			8'b0011_1001: begin
			end
			8'b0011_1010: begin
			end
			8'b0011_1011: begin
			end
			8'b0011_1100: begin
			end
			8'b0011_1101: begin
			end
			8'b0011_1110: begin
			end
			8'b0011_1111: begin
			end

			8'b0100_0000: begin // MovWP0
				mov_op <= 1;
				dst_por <= 1;
			end
			8'b0100_0001: begin // MovWP1
				mov_op <= 1;
				dst_por <= 1;
			end
			8'b0100_0010: begin
			end
			8'b0100_0011: begin
			end
			8'b0100_0100: begin
			end
			8'b0100_0101: begin
			end
			8'b0100_0110: begin
			end
			8'b0100_0111: begin
			end

			8'b0100_1000: begin // MovP0W
				mov_op <= 1;
				dst_w <= 1;
			end
			8'b0100_1001: begin // MovP1W
				mov_op <= 1;
				dst_w <= 1;
			end
			8'b0100_1010: begin
			end
			8'b0100_1011: begin
			end
			8'b0100_1100: begin
			end
			8'b0100_1101: begin
			end
			8'b0100_1110: begin
			end
			8'b0100_1111: begin
			end

			8'b0101_0000: begin // MovWR0
				mov_op <= 1;
				dst_reg <= 1;
			end
			8'b0101_0001: begin // MovWR1
				mov_op <= 1;
				dst_reg <= 1;
			end
			8'b0101_0010: begin // MovWR2
				mov_op <= 1;
				dst_reg <= 1;
			end
			8'b0101_0011: begin // MovWR3
				mov_op <= 1;
				dst_reg <= 1;
			end
			8'b0101_0100: begin // MovWR4
				mov_op <= 1;
				dst_reg <= 1;
			end
			8'b0101_0101: begin // MovWR5
				mov_op <= 1;
				dst_reg <= 1;
			end
			8'b0101_0110: begin // MovWR6
				mov_op <= 1;
				dst_reg <= 1;
			end
			8'b0101_0111: begin // MovWR7
				mov_op <= 1;
				dst_reg <= 1;
			end

			8'b0101_1000: begin // MovR0W
				mov_op <= 1;
				dst_w <= 1;
			end
			8'b0101_1001: begin // MovR0W
				mov_op <= 1;
				dst_w <= 1;
			end
			8'b0101_1010: begin // MovR0W
				mov_op <= 1;
				dst_w <= 1;
			end
			8'b0101_1011: begin // MovR0W
				mov_op <= 1;
				dst_w <= 1;
			end
			8'b0101_1100: begin // MovR0W
				mov_op <= 1;
				dst_w <= 1;
			end
			8'b0101_1101: begin // MovR0W
				mov_op <= 1;
				dst_w <= 1;
			end
			8'b0101_1110: begin // MovR0W
				mov_op <= 1;
				dst_w <= 1;
			end
			8'b0101_1111: begin // MovR0W
				mov_op <= 1;
				dst_w <= 1;
			end

			8'b0110_0000: begin // SetbW 0
			end
			8'b0110_0001: begin // SetbW 1
			end
			8'b0110_0010: begin // SetbW 2
			end
			8'b0110_0011: begin // SetbW 3
			end
			8'b0110_0100: begin // SetbW 4
			end
			8'b0110_0101: begin // SetbW 5
			end
			8'b0110_0110: begin // SetbW 6
			end
			8'b0110_0111: begin // SetbW 7
			end

			8'b0110_1000: begin // ClrbW 0
			end
			8'b0110_1001: begin // ClrbW 1
			end
			8'b0110_1010: begin // ClrbW 2
			end
			8'b0110_1011: begin // ClrbW 3
			end
			8'b0110_1100: begin // ClrbW 4
			end
			8'b0110_1101: begin // ClrbW 5
			end
			8'b0110_1110: begin // ClrbW 6
			end
			8'b0110_1111: begin // ClrbW 7
			end

			8'b0111_0000: begin
			end
			8'b0111_0001: begin
			end
			8'b0111_0010: begin
			end
			8'b0111_0011: begin
			end
			8'b0111_0100: begin
			end
			8'b0111_0101: begin
			end
			8'b0111_0110: begin
			end
			8'b0111_0111: begin
			end
			8'b0111_1000: begin
			end
			8'b0111_1001: begin
			end
			8'b0111_1010: begin
			end
			8'b0111_1011: begin
			end
			8'b0111_1100: begin
			end
			8'b0111_1101: begin
			end
			8'b0111_1110: begin
			end
			8'b0111_1111: begin
			end

			// Instructions with operands
			8'b1000_0000: begin
				
			end
			8'b1000_0001: begin
			end
			8'b1000_0010: begin
			end
			8'b1000_0011: begin
			end
			8'b1000_0100: begin
			end
			8'b1000_0101: begin
			end
			8'b1000_0110: begin
			end
			8'b1000_0111: begin
			end
			8'b1000_1000: begin
			end
			8'b1000_1001: begin
			end
			8'b1000_1010: begin
			end
			8'b1000_1011: begin
			end
			8'b1000_1100: begin
			end
			8'b1000_1101: begin
			end
			8'b1000_1110: begin
			end
			8'b1000_1111: begin
			end
			8'b1001_0000: begin
			end
			8'b1001_0001: begin
			end
			8'b1001_0010: begin
			end
			8'b1001_0011: begin
			end
			8'b1001_0100: begin
			end
			8'b1001_0101: begin
			end
			8'b1001_0110: begin
			end
			8'b1001_0111: begin
			end
			8'b1001_1000: begin
			end
			8'b1001_1001: begin
			end
			8'b1001_1010: begin
			end
			8'b1001_1011: begin
			end
			8'b1001_1100: begin
			end
			8'b1001_1101: begin
			end
			8'b1001_1110: begin
			end
			8'b1001_1111: begin
			end
			8'b1010_0000: begin
			end
			8'b1010_0001: begin
			end
			8'b1010_0010: begin
			end
			8'b1010_0011: begin
			end
			8'b1010_0100: begin
			end
			8'b1010_0101: begin
			end
			8'b1010_0110: begin
			end
			8'b1010_0111: begin
			end
			8'b1010_1000: begin
			end
			8'b1010_1001: begin
			end
			8'b1010_1010: begin
			end
			8'b1010_1011: begin
			end
			8'b1010_1100: begin
			end
			8'b1010_1101: begin
			end
			8'b1010_1110: begin
			end
			8'b1010_1111: begin
			end
			8'b1011_0000: begin
			end
			8'b1011_0001: begin
			end
			8'b1011_0010: begin
			end
			8'b1011_0011: begin
			end
			8'b1011_0100: begin
			end
			8'b1011_0101: begin
			end
			8'b1011_0110: begin
			end
			8'b1011_0111: begin
			end
			8'b1011_1000: begin
			end
			8'b1011_1001: begin
			end
			8'b1011_1010: begin
			end
			8'b1011_1011: begin
			end
			8'b1011_1100: begin
			end
			8'b1011_1101: begin
			end
			8'b1011_1110: begin
			end
			8'b1011_1111: begin
			end
			8'b1100_0000: begin
			end
			8'b1100_0001: begin
			end
			8'b1100_0010: begin
			end
			8'b1100_0011: begin
			end
			8'b1100_0100: begin
			end
			8'b1100_0101: begin
			end
			8'b1100_0110: begin
			end
			8'b1100_0111: begin
			end
			8'b1100_1000: begin
			end
			8'b1100_1001: begin
			end
			8'b1100_1010: begin
			end
			8'b1100_1011: begin
			end
			8'b1100_1100: begin
			end
			8'b1100_1101: begin
			end
			8'b1100_1110: begin
			end
			8'b1100_1111: begin
			end
			8'b1101_0000: begin
			end
			8'b1101_0001: begin
			end
			8'b1101_0010: begin
			end
			8'b1101_0011: begin
			end
			8'b1101_0100: begin
			end
			8'b1101_0101: begin
			end
			8'b1101_0110: begin
			end
			8'b1101_0111: begin
			end
			8'b1101_1000: begin
			end
			8'b1101_1001: begin
			end
			8'b1101_1010: begin
			end
			8'b1101_1011: begin
			end
			8'b1101_1100: begin
			end
			8'b1101_1101: begin
			end
			8'b1101_1110: begin
			end
			8'b1101_1111: begin
			end
			8'b1110_0000: begin
			end
			8'b1110_0001: begin
			end
			8'b1110_0010: begin
			end
			8'b1110_0011: begin
			end
			8'b1110_0100: begin
			end
			8'b1110_0101: begin
			end
			8'b1110_0110: begin
			end
			8'b1110_0111: begin
			end
			8'b1110_1000: begin
			end
			8'b1110_1001: begin
			end
			8'b1110_1010: begin
			end
			8'b1110_1011: begin
			end
			8'b1110_1100: begin
			end
			8'b1110_1101: begin
			end
			8'b1110_1110: begin
			end
			8'b1110_1111: begin
			end
			8'b1111_0000: begin
			end
			8'b1111_0001: begin
			end
			8'b1111_0010: begin
			end
			8'b1111_0011: begin
			end
			8'b1111_0100: begin
			end
			8'b1111_0101: begin
			end
			8'b1111_0110: begin
			end
			8'b1111_0111: begin
			end
			8'b1111_1000: begin
			end
			8'b1111_1001: begin
			end
			8'b1111_1010: begin
			end
			8'b1111_1011: begin
			end
			8'b1111_1100: begin
			end
			8'b1111_1101: begin
			end
			8'b1111_1110: begin
			end
			8'b1111_1111: begin
			end
		endcase
	end

endmodule