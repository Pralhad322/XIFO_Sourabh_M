package ch.ethz.systems.netbench.xpt.serviceTime;

import java.util.HashMap;
import java.util.Map;

public class ServiceIdToServiceTime {

    private final Map<String, Integer> serviceTime;

    public ServiceIdToServiceTime() {
        this.serviceTime = new HashMap<>();

        // Times are in nanoseconds with finer gradation
        // Critical services (1ms–3ms)
        serviceTime.put("VoIP", 3_000);   
        serviceTime.put("Game", 4_000);   
        serviceTime.put("AR", 5_000);  

        // Interactive services (5ms–15ms)
        serviceTime.put("Web", 8_000);   
        serviceTime.put("SSH", 10_000);  

        // Streaming Media
        serviceTime.put("Audio", 15_000);  
        serviceTime.put("Video", 20_000);  

        // Background > 500ms (e.g., software updates, backups)
        serviceTime.put("Backup", 80_000);  
        serviceTime.put("Update", 60_000);  

        // Default background service
        serviceTime.put("Default", 100_000);
    }

    private long calculateInversePriority(long latency) {
        return 1_000_000L / latency; 
    }
    
    public Integer getServiceTime(String serviceId) {
        return (int) calculateInversePriority(serviceTime.getOrDefault(serviceId, 
                                            serviceTime.get("Default")));
    }
}
