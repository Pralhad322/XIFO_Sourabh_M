package ch.ethz.systems.netbench.xpt.ports.XIFO;

import ch.ethz.systems.netbench.core.log.SimulationLogger;
import ch.ethz.systems.netbench.core.network.NetworkDevice;
import ch.ethz.systems.netbench.core.network.Packet;
import ch.ethz.systems.netbench.xpt.tcpbase.FullExtTcpPacket;
import ch.ethz.systems.netbench.xpt.tcpbase.PriorityHeader;
import ch.ethz.systems.netbench.xpt.ports.XIFO.KLLSketch;

import java.util.*;
import java.util.concurrent.ArrayBlockingQueue;


public class XIFOQueue implements Queue {
    
    private final ArrayList<ArrayBlockingQueue> queueList;
    private final Map queueBounds;
    private int ownId;
    private String stepSize;
    private final SampleBufferKLL scheduler;
    public XIFOQueue(long numQueues, long perQueueCapacity, NetworkDevice ownNetworkDevice, String stepSize){
        this.queueList = new ArrayList((int)numQueues);
        this.queueBounds = new HashMap();
        
        this.scheduler = new SampleBufferKLL(100, 20);
        ArrayBlockingQueue fifo;
        for (int i=0; i<(int)numQueues; i++){
            fifo = new ArrayBlockingQueue<Packet>((int)perQueueCapacity);
            queueList.add(fifo);
            queueBounds.put(i, 0);
        }
        this.ownId = ownNetworkDevice.getIdentifier();
        this.stepSize = stepSize;
    }
    // Packet dropped and null returned if selected queue exceeds its size
    @Override
    public boolean offer(Object o) {

        // Extract rank from header
        Packet packet = (Packet) o;
        PriorityHeader header = (PriorityHeader) packet;
        int rank = (int)header.getPriority();
        scheduler.insert(rank);
        int queue = scheduler.getQueueIndex(rank);
        boolean result = queueList.get(queue).offer(o);
        if(!result){
            return false;
        }
        return true;
    }

    @Override
    public Object poll() {
        Packet p;
        for (int q=0; q<queueList.size(); q++){
            p = (Packet) queueList.get(q).poll();
            if (p != null){

                PriorityHeader header = (PriorityHeader) p;
                int rank = (int)header.getPriority();

                // Log rank of packet enqueued and queue selected if enabled
                if(SimulationLogger.hasRankMappingEnabled()){
                    SimulationLogger.logRankMapping(this.ownId, rank, q);
                }

                if(SimulationLogger.hasQueueBoundTrackingEnabled()){
                    for (int c=queueList.size()-1; c>=0; c--){
                        SimulationLogger.logQueueBound(this.ownId, c, (int)queueBounds.get(c));
                    }
                }

                // Check whether there is an inversion: a packet with smaller rank in queue than the one polled
                if (SimulationLogger.hasInversionsTrackingEnabled()) {
                    int count_inversions = 0;
                    for (int i = 0; i <= queueList.size() - 1; i++) {
                        Object[] currentQueue = queueList.get(i).toArray();
                        for (int j = 0; j < currentQueue.length; j++) {
                            int r = (int) ((FullExtTcpPacket) currentQueue[j]).getPriority();
                            if (r < rank) {
                                count_inversions++;
                            }
                        }
                    }
                    if (count_inversions != 0) {
                        // SimulationLogger.logInversionsPerService(rank, count_inversions);
                    }
                }
                return p;
            }
        }
        return null;
    }

    @Override
    public int size() {
        int size = 0;
        for (int q=0; q<queueList.size(); q++){
            size += queueList.get(q).size();
        }
        return size;
    }

    @Override
    public boolean isEmpty() {
        boolean empty = true;
        for (int q=0; q<queueList.size(); q++){
            if(!queueList.get(q).isEmpty()){
                empty = false;
            }
        }
        return empty;
    }

    @Override
    public boolean contains(Object o) {
        return false;
    }

    @Override
    public Iterator iterator() {
        return null;
    }

    @Override
    public Object[] toArray() {
        return new Object[0];
    }

    @Override
    public Object[] toArray(Object[] objects) {
        return new Object[0];
    }

    @Override
    public boolean add(Object o) {
        return false;
    }

    @Override
    public boolean remove(Object o) {
        return false;
    }

    @Override
    public boolean addAll(Collection collection) {
        return false;
    }

    @Override
    public void clear() { }

    @Override
    public boolean retainAll(Collection collection) {
        return false;
    }

    @Override
    public boolean removeAll(Collection collection) {
        return false;
    }

    @Override
    public boolean containsAll(Collection collection) {
        return false;
    }

    @Override
    public Object remove() {
        return null;
    }

    @Override
    public Object element() {
        return null;
    }

    @Override
    public Object peek() {
        return null;
    }
}
