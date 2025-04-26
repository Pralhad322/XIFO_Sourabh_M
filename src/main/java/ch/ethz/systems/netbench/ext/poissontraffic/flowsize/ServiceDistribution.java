package ch.ethz.systems.netbench.ext.poissontraffic.flowsize;

import ch.ethz.systems.netbench.core.Simulator;

import java.util.Random;

public abstract class ServiceDistribution {

    Random independentRng;

    ServiceDistribution() {
        this.independentRng = Simulator.selectIndependentRandom("Service_Type");
    }

    public abstract String serviceDisribution();
}

