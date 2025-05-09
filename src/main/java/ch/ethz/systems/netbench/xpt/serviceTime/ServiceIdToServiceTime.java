package ch.ethz.systems.netbench.xpt.serviceTime;

import java.util.HashMap;
import java.util.Map;

public class ServiceIdToServiceTime {

    private final Map<String, Integer> serviceTime;

    public ServiceIdToServiceTime() {
        this.serviceTime = new HashMap<>();

        // Times are in nanoseconds with finer gradation
        // Critical services (1ms–3ms)
        serviceTime.put("RT", 1_000_000);   // 1ms
        serviceTime.put("EW", 2_000_000);   // 2ms
        serviceTime.put("RF", 3_000_000);   // 3ms

        // Interactive services (5ms–15ms)
        serviceTime.put("MI", 5_000_000);   // 5ms
        serviceTime.put("CS", 10_000_000);  // 10ms
        serviceTime.put("GH", 15_000_000);  // 15ms

        // Media / Best-effort (20ms–50ms)
        serviceTime.put("YT", 20_000_000);  // 20ms
        serviceTime.put("SN", 30_000_000);  // 30ms
        serviceTime.put("TV", 40_000_000);  // 40ms
        serviceTime.put("QW", 50_000_000);  // 50ms

        // Background / Default (75ms–100ms)
        serviceTime.put("YU", 75_000_000);  // 75ms
        serviceTime.put("Default", 100_000_000); // 100ms
    }

    public Integer getServiceTime(String serviceId) {
        return serviceTime.getOrDefault(serviceId, serviceTime.get("Default"));
    }
}
