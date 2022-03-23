package com.javier.pslib;

public class LinearEquation {
    private double a,b,c,d,e,f,det,x,y;

    //constructor
    LinearEquation(double a1, double b1, double c1, double d1, double e1, double f1){
        a = a1;
        b = b1;
        c = c1;
        d = d1;
        e = e1;
        f = f1;
        det = (a * d) - (b * c);
        x = ((d * e) - (b * f))/det;
        y = ((a * f) - (c * e))/det;
    }

    //get methods
    double getA(){
        return a;
    }
    double getB(){
        return b;
    }
    double getC(){
        return c;
    }
    double getD(){
        return d;
    }
    double getE(){
        return e;
    }
    double getF(){
        return f;
    }

    //Can solve?
    boolean isSolvable(){
        return (det != 0);
    }

    double getX(){
        return x;
    }

    double getY(){
        return y;
    }


}
