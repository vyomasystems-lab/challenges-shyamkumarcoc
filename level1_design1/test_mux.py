# See LICENSE.vyoma for details

import cocotb
from cocotb.triggers import Timer
import random

@cocotb.test()
async def test_mux(dut):
    """Test for mux2"""

    for i in range(31):

        sel = random.randint(0, 31)
        out = random.randint(0, 31)

        dut.a.value = sel
        dut.b.value = out
        await Timer(2, units='ns')
        dut._log.info(f'sel={sel:05} out={out:05} model={sel!=out:05} DUT={int(dut.result.value):05}')
        assert dut.result.value == sel!=out, "Randomised test failed with: {sel} != {out} = {Result}".format(
            sel=dut.a.value, out=dut.b.value, Result=dut.result.value)
