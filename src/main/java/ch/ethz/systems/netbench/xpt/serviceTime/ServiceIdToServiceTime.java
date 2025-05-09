package ch.ethz.systems.netbench.xpt.serviceTime;

import java.util.HashMap;
import java.util.Map;

public class ServiceIdToServiceTime {

    private final Map<String, Integer> serviceTime;

    public ServiceIdToServiceTime() {
        this.serviceTime = new HashMap<>();

        // Times are in nanoseconds with finer gradation
        // Critical services (1ms–3ms)
        serviceTime.put("VoIP", 30_000);   
        serviceTime.put("Game", 40_000);   
        serviceTime.put("AR", 50_000);  

        // Interactive services (5ms–15ms)
        serviceTime.put("Web", 80_000);   
        serviceTime.put("SSH", 100_000);  

        // Streaming Media
        serviceTime.put("Audio", 150_000);  
        serviceTime.put("Video", 200_000);  

        // Background > 500ms (e.g., software updates, backups)
        serviceTime.put("Backup", 800_000);  
        serviceTime.put("Update", 600_000);  

        // Default background service
        serviceTime.put("Default", 100_000);
    }

    private long calculateInversePriority(long latency) {
        // Invert the priority: smaller latency gets higher priority (smaller rank)
        return 1_000_000L / latency; // Scale to ensure higher priority for smaller latency
    }
    
    public Integer getServiceTime(String serviceId) {
        return (int) calculateInversePriority(serviceTime.getOrDefault(serviceId, 
                                            serviceTime.get("Default")));
    }
}
