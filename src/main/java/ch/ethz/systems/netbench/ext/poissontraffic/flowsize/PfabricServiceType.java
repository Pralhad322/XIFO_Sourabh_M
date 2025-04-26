package ch.ethz.systems.netbench.ext.poissontraffic.flowsize;

public class PfabricServiceType extends ServiceDistribution {

    public PfabricServiceType() {
        super();
    }

    @Override
    public String serviceDisribution() {
        double outcome = independentRng.nextDouble();

        if (outcome >= 0.0 && outcome <= 0.1) {
            return "MI";
        } else if (outcome > 0.1 && outcome <= 0.2) {
            return "CS";
        } else if (outcome > 0.2 && outcome <= 0.3) {
            return "TV";
        } else if (outcome > 0.3 && outcome <= 0.4) {
            return "YT";
        } else if (outcome > 0.4 && outcome <= 0.5) {
            return "SN";
        } else if (outcome > 0.5 && outcome <= 0.6) {
            return "RT";
        } else if (outcome > 0.6 && outcome <= 0.7) {
            return "EW";
        } else if (outcome > 0.7 && outcome <= 0.8) {
            return "QW";
        } else if (outcome > 0.8 && outcome <= 0.9) {
            return "YU";
        } else if (outcome > 0.9 && outcome <= 0.95) {
            return "GH";
        } else if (outcome > 0.95 && outcome <= 0.98) {
            return "RF";
        } else {
            return "Default";
        }
    }

}