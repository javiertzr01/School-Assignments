package com.javier.exam_midterm.Question3;

public class TestCountBallotBox {

    //ATTENTION: Pressing BUILD then RUN executes Question3.main()

    public static void main(String[] args) {
        CountBallotBox countBallotBox = new CountBallotBox();
        countBallotBox.addBallot( new BallotPaper("ray","emma") );
        countBallotBox.addBallot( new BallotPaper("ray","phil") );
        countBallotBox.addBallot( new BallotPaper("phil","ray") );
        countBallotBox.addBallot( new BallotPaper("don","emma") );
        // output: 2
        System.out.println(countBallotBox.getVotesFor("ray"));
        countBallotBox.eliminateCandidate("ray");
        System.out.println("After eliminate\n");
        /* output:
        1:don 2:emma
        1:emma 2:null
        1:phil 2:null
        1:phil 2:ray */
        System.out.println(countBallotBox);

        CountBallotBox countBallotBox2 = new CountBallotBox();
        countBallotBox2.addBallot( new BallotPaper("don","emma") );
        countBallotBox2.addBallot( new BallotPaper("emma","don") );
        countBallotBox2.addBallot( new BallotPaper("emma","don") );
        countBallotBox2.transferCandidate( new BallotPaper("emma", "don"), 1);
        System.out.println("After Transfer \n");
        /* output:
        1:don 2:emma
        1:don 2:null
        1:emma 2:don */
        System.out.println(countBallotBox2);
    }
}
