public class Player {
    private int score;
    private boolean is_turn;

    public void setScore(int s){
        score = s;
    }
    public void setIsTurn(boolean t){
        is_turn = t;
    }
    
    public int getScore(){
        return score;
    }
    public boolean getIsTurn(){
        return is_turn;
    }

    public void make_hit(){
        //need to implemet
    }
}