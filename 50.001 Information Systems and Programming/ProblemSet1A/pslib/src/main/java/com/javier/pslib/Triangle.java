package com.javier.pslib;

public class Triangle extends GeometricObject{
    private double side1,side2 = 1.0 ,side3 = 1.0;

    //constructor
    Triangle(double new1, double new2, double new3){
        side1 = new1;
        side2 = new2;
        side3 = new3;
    }

    double getArea(){
        double p = getPerimeter();
        return Math.pow((p*(p-side1)*(p-side2)*(p-side3)), 0.5);
    }

    double getPerimeter(){
        return side1 + side2 + side3;
    }

    String toString(){
        String a = Double.toString(side1);
        String b = Double.toString(side2);
        String c = Double.toString(side3);
        return "Triangle: side1 = " + a + " side2 = " + b + " side3 = " + c;
    }
}
