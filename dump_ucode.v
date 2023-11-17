module dump();
	initial begin
		$dumpfile ("ucode.vcd");
		$dumpvars (0, tb);
		#1;
	end
endmodule
