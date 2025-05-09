package ch.ethz.systems.netbench.ext.poissontraffic.flowsize;

public class PfabricServiceType extends ServiceDistribution {

    public PfabricServiceType() {
        super();
    }

    @Override
    public String serviceDisribution() {
        double outcome = independentRng.nextDouble();

        if (outcome >= 0.0 && outcome <= 0.15) {
            return "Video";
        } else if (outcome > 0.15 && outcome <= 0.40) {
            return "Web";
        } else if (outcome > 0.40 && outcome <= 0.55) {
            return "VoIP";
        } else if (outcome > 0.55 && outcome <= 0.58) {
            return "Backup";
        } else if (outcome > 0.58 && outcome <= 0.61) {
            return "Update";
        } else if (outcome > 0.61 && outcome <= 0.63) {
            return "SSH";
        } else if (outcome > 0.63 && outcome <= 0.78) {
            return "Game";
        } else if (outcome > 0.78 && outcome <= 0.83) {
            return "AR";
        } else if (outcome > 0.83 && outcome <= 0.98) {
            return "Audio";
        } else {
            return "Default";
        }
    }

}