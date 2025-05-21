package ch.ethz.systems.netbench.xpt.ports.XIFO;
import java.util.*;

class KLLSketch {
    private int capacity;
    private List<Integer> compactor;

    public KLLSketch(int capacity) {
        this.capacity = capacity;
        this.compactor = new ArrayList<>();
    }

    public void insert(int value) {
        int pos = Collections.binarySearch(compactor, value);
        if (pos < 0) pos = -(pos + 1);
        compactor.add(pos, value);

        if (compactor.size() > capacity) {
            compact();
        }
    }

    private void compact() {
        List<Integer> newCompactor = new ArrayList<>();
        Random rand = new Random();

        for (int i = 0; i < compactor.size() - 1; i += 2) {
            int picked = rand.nextBoolean() ? compactor.get(i) : compactor.get(i + 1);
            newCompactor.add(picked);
        }

        if (compactor.size() % 2 == 1) {
            newCompactor.add(compactor.get(compactor.size() - 1));
        }

        compactor = new ArrayList<>(newCompactor);
        Collections.sort(compactor);
    }

    public Integer query(double quantile) {
        if (compactor.isEmpty()) return null;
        if (quantile < 0 || quantile > 1) throw new IllegalArgumentException("Quantile must be in [0, 1]");
        int index = (int) (quantile * compactor.size());
        return compactor.get(Math.min(index, compactor.size() - 1));
    }

    public void reset() {
        compactor.clear();
    }
}

class SampleBufferKLL {
    private int bufferSize;
    private Deque<Integer> buffer;
    private KLLSketch kll;
    private int insertCount;
    private final int REBUILD_INTERVAL = 500; 

    // cached quantiles
    private Integer p10, p25, p40, p55, p70, p85, p95;

    public SampleBufferKLL(int bufferSize, int kllCapacity) {
        this.bufferSize = bufferSize;
        this.buffer = new ArrayDeque<>(bufferSize);
        this.kll = new KLLSketch(kllCapacity);
        this.insertCount = 0;
        this.p10 = this.p25 = this.p40 = this.p55 = this.p70 = this.p85 = this.p95 = null;
    }

    public void insert(int value) {
        if (buffer.size() == bufferSize) {
            buffer.pollFirst();
        }
        buffer.offerLast(value);
        insertCount++;

        if (insertCount % REBUILD_INTERVAL == 0 || kll == null || p10 == null) {
            rebuildKLL();
            cacheQuantiles();
        }
    }

    private void rebuildKLL() {
        kll.reset();
        for (int val : buffer) {
            kll.insert(val);
        }
    }

    private void cacheQuantiles() {
        p10 = kll.query(0.10);
        p25 = kll.query(0.25);
        p40 = kll.query(0.40);
        p55 = kll.query(0.55);
        p70 = kll.query(0.70);
        p85 = kll.query(0.85);
        p95 = kll.query(0.95);
    }

    public int getQueueIndex(int value) {
        if (value <= p10) return 0;
        else if (value <= p25) return 1;
        else if (value <= p40) return 2;
        else if (value <= p55) return 3;
        else if (value <= p70) return 4;
        else if (value <= p85) return 5;
        else if (value <= p95) return 6;
        else return 7;
    }
}


public class KLLSketchQueueMapper {
    public static void main(String[] args) {
        SampleBufferKLL scheduler = new SampleBufferKLL(100, 20);

        int[] flowSizes = {5, 15, 10, 12, 8, 25, 20, 30, 50, 7, 6, 4, 3, 1, 90};

        for (int fs : flowSizes) {
            System.out.println("Inserting flow size: " + fs + " KB");
            scheduler.insert(fs);
            int queue = scheduler.getQueueIndex(fs);
            System.out.println("\u2192 Mapped to Queue: Q" + queue);
            System.out.println("----------------------------------------");
        }
    }
}
