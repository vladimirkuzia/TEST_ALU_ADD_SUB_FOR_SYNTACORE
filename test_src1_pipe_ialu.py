# This file is public domain, it can be freely copied without restrictions.
# SPDX-License-Identifier: CC0-1.0

# test_my_design.py (simple)
import cocotb
import unittest
from cocotb.triggers import Timer , RisingEdge
from cocotb.clock import Clock

@cocotb.test()
async def test_alu_add(dut):
    """Exercise an Analog Front-end and its digital controller."""

    # clock = Clock(dut.clk, 10, units="us")  # create a 1us period clock on port clk
    cocotb.start_soon(Clock(dut.clk, 1, units = 'ns').start())  # start the clock
    # flag = False
    i                   = 0
    count               = 0
    l_1                 = []
    l_2                 = []
    l_add               = []
    op1                 = [  0x2BAE89B ,0x1FFFFFFF,0xFFFFFFF9,0x7FFFFFFD,0x7FFFFFFD,0x49E7F942,0xB61806BE,0x7FFCDBBE,0xFFFFFFFF,0xF2330000,0xFFFFFFFF,0x0]
    op2                 = [  0x6BA0DAF5,0xFFFFFFF ,0x7       ,0x49E7F942,0xB61806BE,0x80000003,0xCFC5C101,0x7FFCDBBE,0x00000001,0x80000000,0xFFFFFFFF,0x0]
    expected_add        = [0,0x6E5BC390,0x2FFFFFFE,0x0       ,0xC9E7F93F,0x361806BB,0xC9E7F945,0x85DDC7BF,0xFFF9B77C,0x0       ,0x72330000,0xFFFFFFFE,0x0] # expected_add = [i for i in range(0,38,2)]
 
    for clk in range(12):
        while i <= 11:
         await RisingEdge(dut.clk)  # wait for rising edge/"posedge"
         dut.exu2ialu_cmd_i.value = 0b00100; 
         dut._log.info("exu2ialu_cmd_i is %s", dut.exu2ialu_cmd_i.value)
         dut.exu2ialu_addr_op1_i.value = 0b00000000000000000000000000000000;
         dut.exu2ialu_addr_op2_i.value = 0b00000000000000000000000000000000;
         dut.exu2ialu_main_op1_i.value = op1[i]
         l_1.append(dut.exu2ialu_main_op1_i.value)
         dut.exu2ialu_main_op2_i.value = op2[i]
         l_2.append(dut.exu2ialu_main_op2_i.value)
         dut.exu2ialu_rvm_cmd_vd_i.value = 0b0;        
         dut.ialu2exu_rvm_res_rdy_o.value = 0b0;
         l_add.append(dut.ialu2exu_main_res_o.value) 
         dut._log.info("ialu2exu_main_res_o is %s", dut.ialu2exu_main_res_o.value.buff)
         #  dut._log.info("l_add is %s", l_sub)
         #  dut._log.info("expected_add is %s", expected_add)
         count += l_add[i] != expected_add[i]
         dut._log.info("count is %s", count)
         i+=1
    
      
    await Timer(1, units="ns")
    assert count == 0, "FAILED"
    dut.rst_n.value     = 1
    

@cocotb.test()
async def test_alu_sub(dut):
    """Exercise an Analog Front-end and its digital controller."""

    # clock = Clock(dut.clk, 10, units="us")  # create a 1us period clock on port clk
    cocotb.start_soon(Clock(dut.clk, 1, units = 'ns').start())  # start the clock
    # flag = False
    i                   = 0
    count               = 0
    l_1                 = []
    l_2                 = []
    l_sub               = []
    op1                 = [  0XBEA6263D ,0xF0000000,0xFFFFFFFF,0xF00FFFFF,0x0       ,0xFFFF8999,0x7FFFFFFF,0x7       ,0x49E7F942,0x4ACB310A,0x880CE409,0x0       ,0xFFFFFFFF,0x80000000,0x0]
    op2                 = [  0xE88ADB6C ,0x0FFFFFFF,0xFFFFFFFF,0x7FFFFFF1,0xFFFF8999,0x0       ,0x80000000,0x14      ,0x80000003,0x1F0095D ,0x49635BC3,0xFFFFFFFF,0x00000001,0x7FFFFFFF,0x0]
    expected_sub        = [0,0xD61B4AD1 ,0xE0000001,0x0       ,0x7010000E,0x00007667,0xFFFF8999,0xFFFFFFFF,0xFFFFFFF3,0xC9E7F93F,0x48DB27AD,0x3EA98846,0x00000001,0xFFFFFFFE,0x1       ,0x0] # ex_sub = [i for i in range(0,38,2)]
    for clk in range(15):
        while i <= 14:
         await RisingEdge(dut.clk)  # wait for rising edge/"posedge"
         dut.exu2ialu_cmd_i.value = 0b00101; 
         dut._log.info("exu2ialu_cmd_i is %s", dut.exu2ialu_cmd_i.value)
         dut.exu2ialu_addr_op1_i.value = 0b00000000000000000000000000000000;
         dut.exu2ialu_addr_op2_i.value = 0b00000000000000000000000000000000;
         dut.exu2ialu_main_op1_i.value = op1[i]
         l_1.append(dut.exu2ialu_main_op1_i.value)
         dut.exu2ialu_main_op2_i.value = op2[i]
         l_2.append(dut.exu2ialu_main_op2_i.value)
         dut.exu2ialu_rvm_cmd_vd_i.value = 0b0;        
         dut.ialu2exu_rvm_res_rdy_o.value = 0b0;
         l_sub.append(dut.ialu2exu_main_res_o.value) 
         dut._log.info("ialu2exu_main_res_o is %s", dut.ialu2exu_main_res_o.value.buff)
         #  dut._log.info("l_sub is %s", l_sub)
         #  dut._log.info("expected_sub is %s", expected_sub)
         count += l_sub[i] != expected_sub[i]
         dut._log.info("count is %s", count)
         i+=1
    
      
    await Timer(1, units="ns")
    assert count == 0, "FAILED"
    