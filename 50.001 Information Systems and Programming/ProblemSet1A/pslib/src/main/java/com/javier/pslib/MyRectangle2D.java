package com.javier.pslib;

public class MyRectangle2D {
    //center of rect
    private double x;
    private double y;

    //width and height of rect
    private double width;
    private double height;

    //getter and setter for center of rect
    double getX(){
        return x;
    }
    double getY(){
        return y;
    }
    void setX(double new_x){
        x = new_x;
    }
    void setY(double new_y){
        y = new_y;
    }

    //getter and setter for width and height of rect
    double getWidth(){
        return width;
    }
    double getHeight(){
        return height;
    }
    void setWidth(double new_width){
        if(new_width > 0) {
            width = new_width;
        }
        else{
            System.out.println("Width must be more than 0");
            return;
        }
    }
    void setHeight(double new_height){
        if(new_height > 0) {
            height = new_height;
        }
        else{
            System.out.println("Height must be more than 0");
            return;
        }
    }


    //constructors
    MyRectangle2D(){
        x = 0;
        y = 0;
        height = 1;
        width = 1;
    }
    MyRectangle2D(double new_x, double new_y, double new_width, double new_height){
        x = new_x;
        y = new_y;
        height = new_height;
        width = new_width;
    }


    //get Area
    double getArea(){
        return height * width;
    }

    //get perimeter
    double getPerimeter(){
        return 2*height + 2*width;
    }

    //contains coordinates
    boolean contains(double input_x, double input_y){
        double left = x - width/2;
        double right = x + width/2;
        double up = y + height/2;
        double down = y - height/2;

        if(input_x >= left && input_x <= right && input_y <= up && input_y >= down){
            return true;
        }
        else{
            return false;
        }
    }

    //contains rectangle
    boolean contains(MyRectangle2D r){
        //find boundaries for object rectangle
        double left = x - width/2;
        double right = x + width/2;
        double up = y + height/2;
        double down = y - height/2;

        //find boundaries for r
        double r_left = r.getX() - r.getWidth()/2;
        double r_right = r.getX() + r.getWidth()/2;
        double r_up = r.getY() + r.getHeight()/2;
        double r_down = r.getY() - r.getHeight()/2;

        if(r_left >= left && r_right <= right && r_up <= up && r_down >= down){
            return true;
        }
        else{
            return false;
        }
    }

    //overlaps
    boolean overlaps(MyRectangle2D r){

        //find boundaries for object rectangle
        double left = x - width/2;
        double right = x + width/2;
        double up = y + height/2;
        double down = y - height/2;

        //find boundaries for r
        double r_left = r.getX() - r.getWidth()/2;
        double r_right = r.getX() + r.getWidth()/2;
        double r_up = r.getY() + r.getHeight()/2;
        double r_down = r.getY() - r.getHeight()/2;

        boolean up_in_boundary;
        boolean down_in_boundary;
        boolean left_in_boundary;
        boolean right_in_boundary;

        //check left in boundary
        if(r_left >= left && r_left <= right){
            left_in_boundary = true;
        }
        else{
            left_in_boundary = false;
        }
        //check right in boundary
        if(r_right >= left && r_right <= right){
            right_in_boundary = true;
        }
        else{
            right_in_boundary = false;
        }
        //check up in boundary
        if(r_up >= down && r_up <= up){
            up_in_boundary = true;
        }
        else{
            up_in_boundary = false;
        }
        //check down in boundary
        if(r_down >= down && r_down <= up){
            down_in_boundary = true;
        }
        else{
            down_in_boundary = false;
        }

        //final check
        if(up_in_boundary == true || down_in_boundary == true){
            if(left_in_boundary == true || right_in_boundary == true){
                return true;
            }
            else{
                return false;
            }
        }
        else{
            return false;
        }
    }
}
