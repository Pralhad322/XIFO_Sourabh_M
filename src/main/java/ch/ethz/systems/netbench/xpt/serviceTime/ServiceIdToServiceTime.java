package ch.ethz.systems.netbench.xpt.serviceTime;

import java.util.HashMap;
import java.util.Map;

public class ServiceIdToServiceTime {

    private final Map<String, Double> serviceTime;

    public ServiceIdToServiceTime() {
        this.serviceTime = new HashMap<>();
        // Below informaion are added in millisecond 
        //e.g. 3.0 represents 3 millisecond
        serviceTime.put("MI", 0.01);
        serviceTime.put("CS", 0.1);
        serviceTime.put("TV", 0.5);
        serviceTime.put("YT", 1.5);
        serviceTime.put("SN", 3.0);
        serviceTime.put("RT", 7.0);
        serviceTime.put("EW", 11.0);
        serviceTime.put("QW", 20.0);
        serviceTime.put("YU", 30.0);
        serviceTime.put("GH", 50.0);
        serviceTime.put("RF", 80.0);
        serviceTime.put("Default", 150.0);
    }

    // Getter to retrieve the service time map
    public Double getServiceTime(String serviceId) {
        return serviceTime.get(serviceId);
    }
}
