# See LICENSE.vyoma for details

import cocotb
from cocotb.triggers import Timer
import random

@cocotb.test()
async def test_mux(dut):
    """Test for mux2"""
for i in range (31):


    inp12 = random.randint(0, 31)
    inp13 = random.randint(0, 31)

    dut.a.value = inp12
    dut.b.value = inp13
   

    cocotb._log.info(f'inp12={inp12:05} inp13={inp13:05} model={inp12!=inp13:05} DUT={int(dut.result.value):05}')
    assert dut.result.value == inp12!=inp13, "Randomised test failed with: {inp12} + {inp13} = {result}".format(
            inp12=dut.a.value, inp13=dut.b.value, result=dut.sum.value)
