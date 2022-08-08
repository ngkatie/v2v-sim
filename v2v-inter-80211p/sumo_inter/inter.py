#!/usr/bin/env python3

import os
import sys
import optparse

# Checks that environment variable SUMO_HOME is set
if 'SUMO_HOME' in os.environ:
    tools = os.path.join(os.environ['SUMO_HOME'], 'tools')
    sys.path.append(tools)
else:
    sys.exit("Please declare environment variable 'SUMO_HOME'")

from sumolib import checkBinary # Checks for binary in environ vars
import traci

def get_options():
    opt_parser = optparse.OptionParser()
    opt_parser.add_option("--nogui", action="store_true", default=False, help="Run the commandline version of sumo")

    options, args = opt_parser.parse_args()
    return options

# Contains TraCI control loop
def run():

    step = 0
    
    while traci.simulation.getMinExpectedNumber() > 0:
        traci.simulationStep()
        print(step)
        step+=1

    traci.close()
    sys.stdout.flush()


if __name__ == "__main__":
    options = get_options()

    # Check binary
    if options.nogui:
        sumoBinary = checkBinary('sumo')
    else:
        sumoBinary = checkBinary('sumo-gui')

    # TraCI starts sumo as subprocess and then this script connects and runs
    traci.start([sumoBinary, "-c", "demo.sumocfg", "--tripinfo-output", "tripinfo.xml"])

    run()