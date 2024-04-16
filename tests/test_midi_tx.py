# Copyright 2014-2024 XMOS LIMITED.
# This Software is subject to the terms of the XMOS Public Licence: Version 1.

import pytest
import Pyxsim
from Pyxsim import testers
from pathlib import Path
from uart_tx_checker import UARTTxChecker
from midi_test_helpers import midi_expect_tx, create_midi_tx_file

MAX_CYCLES = 15000000
MIDI_RATE = 31250
CONFIGS = ["xs2", "xs3"]
CONFIGS = ["xs3"]


#####
# This test builds the spdif transmitter app with a verity of presets and tests that the output matches those presets
#####
@pytest.mark.parametrize("config", CONFIGS)
def test_tx(capfd, config):
    xe = str(Path(__file__).parent / f"test_midi/bin/{config}/test_midi_{config}.xe")

    midi_commands = [[0x90, 60, 81]]
    create_midi_tx_file(midi_commands)

    tester = testers.ComparisonTester(midi_expect_tx().expect(midi_commands),
                                        regexp = "uart_tx_checker:.+",
                                        ordered = True)

    
    tx_port = "tile[1]:XS1_PORT_4C"
    baud = MIDI_RATE
    bpb = 8
    parity = 0 
    stop = 1
    length_of_test = sum(len(cmd) for cmd in midi_commands)

    simthreads = [
        UARTTxChecker(tx_port, parity, baud, length_of_test, stop, bpb, debug=False)
    ]

    simargs = ["--max-cycles", str(MAX_CYCLES)]
    # simargs.extend(["--trace-to", "trace.txt", "--vcd-tracing", "-tile tile[1] -ports -o trace.vcd"]) #This is just for local debug so we can capture the run, pass as kwarg to run_with_pyxsim

    # result = Pyxsim.run_on_simulator(
    result = Pyxsim.run_on_simulator(
        xe,
        simthreads=simthreads,
        instTracing=True,
        # clean_before_build=True,
        clean_before_build=False,
        tester=tester,
        capfd=capfd,
        # capfd=None,
        timeout=120,
        simargs=simargs,
        build_options=[
            "-j",
            f"CONFIG={config}",
            "EXTRA_BUILD_FLAGS="
            + f" -DMIDI_RATE_HZ={MIDI_RATE}"
 ,
        ],
    )

    assert result