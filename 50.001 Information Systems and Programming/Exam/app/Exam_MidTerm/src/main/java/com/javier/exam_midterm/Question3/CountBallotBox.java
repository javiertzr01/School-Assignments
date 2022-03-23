package com.javier.exam_midterm.Question3;
import java.util.ArrayList;
import java.util.Collections;

public class CountBallotBox {

    private ArrayList<BallotPaper> ballots;

    CountBallotBox(){
        ballots = new ArrayList<>();
    }

    public void addBallot(BallotPaper b){
        ballots.add(b);
    }

    public int getVotesFor(String candidate){
        int count = 0;
        for (BallotPaper bp: ballots){
            if (bp.getFirstChoice() == candidate){
                count += 1;
            }
        }

        return count;
    }

    private void sortBallots(){
        Collections.sort(ballots);
    }

    public void eliminateCandidate(String candidate){
        for (BallotPaper bp: ballots){
            if (bp.getFirstChoice() == candidate){
                bp.transferVotes();
            }
        }
    }

    public void transferCandidate( BallotPaper sampleBallotPaper, int numberOfVotes){
        int count = 0;
        for(int i = 0; i < ballots.size(); i++){
            if (count >= numberOfVotes){
                break;
            }
            else if(sampleBallotPaper==ballots.get(i)){
                ballots.get(i).transferVotes();
                count+=1;
            }
        }
    }

    @Override
    public String toString(){
        this.sortBallots();
        String result = "";
        for(int i = 0; i<ballots.size();i++){
            result += ballots.get(i).toString() + "\n";
        }
        return result;
    }












}
