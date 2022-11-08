public abstract class Ship {
    private int length;
    private int num_hits;
    private String id;
    private boolean alive;
    private boolean horizontal;

    abstract int get_length();
    abstract boolean is_valid();
}
