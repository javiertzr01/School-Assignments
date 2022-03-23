package com.javier.problemset2A.Qn7_Robot;

import java.util.ArrayList;

public class GetPath {

    //Fill in your answer for this method
    public static boolean getPath (int r, int c, ArrayList<Point> path, final int [][] grid) {

        //if cannot go down and cannot go right, return false
        //if can go down or go right, return true

        //base case
        if (r==0 && c==0){
            Point start = new Point(0,0);
            path.add(start);
            return true;
        }
        else if(grid[r][c] == 1){
            return false;
        }
        //recursive case
        else {
            Point current_point = new Point(r, c);
            Point left_point = new Point(c-1, r);
            Point up_point = new Point(c, r-1);

            boolean go_left = false;
            boolean go_up = false;

            //checking if can go left or up
            if (c-1 >= 0 && grid[left_point.y][left_point.x] == 0) {
                go_left = true;
            }
            if (r-1 >= 0 && grid[up_point.y][up_point.x] == 0){
                go_up = true;
            }

            if(go_left == true){
                boolean path_left_found = getPath(r, c-1, path, grid);
                if (path_left_found){
                    path.add(current_point);
                }
                return true;
            }
            if(go_up == true){
                boolean path_up_found = getPath(r-1, c, path, grid);
                if (path_up_found){
                    path.add(current_point);
                }
                return true;
            }
            return false;
        }
    }
}
