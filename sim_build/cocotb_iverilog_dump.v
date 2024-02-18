module cocotb_iverilog_dump();
initial begin
    $dumpfile("sim_build/scr1_pipe_ialu.fst");
    $dumpvars(0, scr1_pipe_ialu);
end
endmodule
