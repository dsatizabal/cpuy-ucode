# cocotb setup
MODULE = test.test_alu_ucode
export MODULE
TOPLEVEL = tb
VERILOG_SOURCES = tb.v

include $(shell cocotb-config --makefiles)/Makefile.sim

synth_ucode:
	yosys -p "read_verilog ucode.v; proc; opt; show -colors 2 -width -signed ucode"

test_ucode:
	rm -rf sim_build/
	mkdir sim_build/
	iverilog -o sim_build/sim.vvp -s tb -s dump -g2012 dump_ucode.v ucode.v tb.v
	PYTHONOPTIMIZE=${NOASSERT} vvp -M $$(cocotb-config --prefix)/cocotb/libs -m libcocotbvpi_icarus sim_build/sim.vvp
	! grep failure results.xml

gtkwave_ucode:
	gtkwave ucode.vcd ucode.gtkw

formal_ucode:
	sby -f ucode.sby
