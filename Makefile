# This file is public domain, it can be freely copied without restrictions.
# SPDX-License-Identifier: CC0-1.0

# Makefile

EXTRA_ARGS += --coverage
EXTRA_ARGS += --trace --trace-structs
# defaults
SIM ?= verilator
TOPLEVEL_LANG ?= verilog
#Paths to HDL source files
VERILOG_SOURCES += $(PWD)/src1_pipe_ialu.sv

# use VHDL_SOURCES for VHDL files

# TOPLEVEL is the name of the toplevel module in your Verilog or VHDL file
TOPLEVEL = scr1_pipe_ialu

# MODULE is the basename of the Python test file
MODULE = test_src1_pipe_ialu

# include cocotb's make rules to take care of the simulator setup
include $(shell cocotb-config --makefiles)/Makefile.sim
