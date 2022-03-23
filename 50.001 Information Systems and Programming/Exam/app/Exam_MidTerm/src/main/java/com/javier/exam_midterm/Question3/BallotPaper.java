package com.javier.exam_midterm.Question3;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class BallotPaper implements Comparable<BallotPaper>
{

    private String firstChoice;
    private String secondChoice;

    BallotPaper(String firstChoice, String secondChoice){
        this.firstChoice = firstChoice;
        this.secondChoice = secondChoice;
    }
    public String getFirstChoice() {
        return firstChoice;
    }

    public String getSecondChoice() {
        return secondChoice;
    }

    public void transferVotes(){
        this.firstChoice = this.secondChoice;
        this.secondChoice = null;
    }

    public String toString(){
        String str = new String();
        if (this.secondChoice == null){
            str = "1:" + this.firstChoice.toString() + " 2: null";
        }
        else {
            str = "1:" + this.firstChoice.toString() + " 2:" + this.secondChoice.toString();
        }
        return str;
    }

    public boolean equals(Object o){
        if(o instanceof BallotPaper && ((BallotPaper) o).getFirstChoice() == this.firstChoice && ((BallotPaper) o).getSecondChoice() == this.secondChoice ){
            return true;
        }
        else if (o == this){
            return true;
        }
        else{
            return false;
        }
    }

    @Override
    public int compareTo(BallotPaper bp){
        Character[] alphas = {'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'};
        List<Character> alphabet = new ArrayList<Character>(Arrays.asList(alphas));
        char[] this_firstchoice_array = this.firstChoice.toCharArray();
        char[] bp_firstchoice_array = bp.getFirstChoice().toCharArray();
        char this_firstchoice_first = this_firstchoice_array[0];
        char bp_firstchioce_first = bp_firstchoice_array[0];
        if (alphabet.indexOf(this_firstchoice_first) > alphabet.indexOf(bp_firstchioce_first)){
            return 1;
        }
        else if(alphabet.indexOf(this_firstchoice_first) == alphabet.indexOf(bp_firstchioce_first)){
            return 0;
        }
        else{
            return -1;
        }
    }



}
