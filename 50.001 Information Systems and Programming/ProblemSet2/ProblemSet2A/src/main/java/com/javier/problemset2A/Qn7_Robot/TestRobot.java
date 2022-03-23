package com.javier.problemset2A.Qn7_Robot;

import java.util.ArrayList;

public class TestRobot {
    public static void main(String[] args) {
        final int [][] grid0 = {
                {0,0,0,0},
                {0,0,1,0},
                {0,0,0,1},
                {0,1,0,0}
        };

//        final int[][] grid = {
//                {0,0,0,1},
//                {0,1,0,0},
//                {0,1,1,1},
//                {0,0,0,1},
//                {1,1,0,0},
//                {1,1,1,0}
//        };
        ArrayList<Point> path = new ArrayList<>();

//        for(int r = 0; r < 6;r++) {
//            for (int c = 0; c < 4; c++) {
        int r = 3;
        int c = 2;
                boolean success = GetPath.getPath(r, c, path, grid0);

                String result = String.format("(%d,%d) : %b", r, c, success);
                System.out.println(result);
                if (success) {
                    System.out.println(path);
                }
                path.clear();
//            }
//        }
    }
}
