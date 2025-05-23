package ch.ethz.systems.netbench.xpt.tcpextended.sphalftcp;


import ch.ethz.systems.netbench.core.network.TransportLayer;
import ch.ethz.systems.netbench.xpt.newreno.newrenotcp.NewRenoTcpSocket;
import ch.ethz.systems.netbench.xpt.tcpbase.FullExtTcpPacket;

public class SpHalfTcpSocket extends NewRenoTcpSocket {
	
    public SpHalfTcpSocket(TransportLayer transportLayer, long flowId, int sourceId, int destinationId, long flowSizeByte, String serviceId) {
		super(transportLayer, flowId, sourceId, destinationId, flowSizeByte, serviceId);
	}

	/**
     * Create a TCP packet. Used internally as some flags are not needed to specify every time. Override just
     * because we need to add priority
     *
     * @param dataSizeByte      Data size carried in bytes
     * @param sequenceNumber    Sequence number
     * @param ackNumber         Acknowledgment number
     * @param ACK               True iff carries acknowledgment
     * @param SYN               True iff is a synchronization packet
     * @param ECE               True iff it wants to let other party know there congestion was encountered
     *
     * @return  TCP packet instance
     */
    @Override
    protected FullExtTcpPacket createPacket(
        long dataSizeByte,
        long sequenceNumber,
        long ackNumber,
        boolean ACK,
        boolean SYN,
        boolean ECE
    ) {
    	long priority;
    	if(flowSizeByte/2 > sequenceNumber){
    		priority = sequenceNumber;
    	}else {
    		priority = flowSizeByte - sequenceNumber;
    	}
        return new FullExtTcpPacket(
            flowId, dataSizeByte, sourceId, destinationId,
            100, 80, 80, // TTL, source port, destination port
            sequenceNumber, ackNumber, // Seq number, Ack number
            false, false, ECE, // NS, CWR, ECE
            false, ACK, false, // URG, ACK, PSH
            false, SYN, false, // RST, SYN, FIN
            0, // Window size
            priority,
            serviceId
        );
    }

}
