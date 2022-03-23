package com.javier.exam_midterm.Question3;

import java.util.ArrayList;
import java.util.Collections;

public class TestBallotPaper {

    //ATTENTION: Pressing BUILD then RUN executes Question3.main()

    public static void main(String[] args) {
        BallotPaper b1 = new BallotPaper("ray","emma");
        System.out.println(b1.toString()); // 1:ray 2:emma
        b1.transferVotes();
        System.out.println(b1.toString()); // 1:emma 2:null

        ArrayList<BallotPaper> testBallotPapers = new ArrayList<>();
        testBallotPapers.add( new BallotPaper("ray","emma"));
        testBallotPapers.add( new BallotPaper("phil","ray"));
        testBallotPapers.add( new BallotPaper("don","emma"));
        Collections.sort( testBallotPapers);
        // [1:don 2:emma, 1:phil 2:ray, 1:ray 2:emma]
        System.out.println(testBallotPapers);

        BallotPaper b2 = new BallotPaper("ray", "emma");
        BallotPaper b3 = new BallotPaper("ray", "emma");
        BallotPaper b4 = new BallotPaper("emma", "ray");
        BallotPaper b5 = new BallotPaper("ray", "emma");
        b5.transferVotes();
        BallotPaper b6 = new BallotPaper("emma", "ray");
        b6.transferVotes();
        /* output:
        truetruefalse
        falsefalsefalse */
        try{
            System.out.println("" + b2.equals(b2) + b2.equals(b3) + b2.equals(b4) );
            //Uncomment if you wish to test for the case where secondChoice is null
            System.out.println("" + b2.equals(b5) + b5.equals(b2) + b5.equals(b6) );
        }catch( NullPointerException e){
            e.printStackTrace();
        }
    }
}

