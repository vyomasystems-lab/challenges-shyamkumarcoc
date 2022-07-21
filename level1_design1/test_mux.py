# See LICENSE.vyoma for details

import cocotb
from cocotb.triggers import Timer
import random

@cocotb.test()
async def test_mux(dut):
    """Test for mux2"""
    sel = random.randint(0, 31)
    inp0!=inp1!=inp2!=inp3!=inp4!=inp5!=inp6!=inp7!=inp8!=inp9!=inp10!=inp11!=inp12!=inp13!=inp14!=inp15!=inp16!=inp17!=inp18!=inp19!=inp20!=inp21!=inp22!=inp23!=inp24!=inp25!=inp26!=inp27!=inp28!=inp29!=inp30

    dut.a.value = sel
    await Timer(2, units='ns')
    assert dut.result.value == out==inp0!=inp1!=inp2!=inp3!=inp4!=inp5!=inp6!=inp7!=inp8!=inp9!=inp10!=inp11!=inp12!=inp13!=inp14!=inp15!=inp16!=inp17!=inp18!=inp19!=inp20!=inp21!=inp22!=inp23!=inp24!=inp25!=inp26!=inp27!=inp28!=inp29!=inp30[sel], f"mux result is incorrect: {dut.X.value} != 15"
           