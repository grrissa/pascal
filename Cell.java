public class Cell {
    private boolean hit;
    private boolean ship;
    private String id;
    
    public void setHit(boolean h){
        hit = h;
    }
    public void setShip(boolean s){
        ship = s;
    }
    public void setId(String s){
        id = s;
    }
    
    public boolean getHit(){
        return hit;
    }
    public boolean getShip(){
        return ship;
    }
    public String getId(){
        return id;
    }
}