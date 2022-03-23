package piwords;

import com.sun.tools.javac.util.ArrayUtils;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.Iterator;
import java.util.List;
import java.util.PrimitiveIterator;

public class MainTest {
    public static void main(String[] args) {
//        Character[] ch = {'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'};
//        List<Character> test = new ArrayList<Character>(Arrays.asList(ch));
//        char[] ch_prim = new char[ch.length];
//        for (int i = 0; i < ch.length; i++){
//            ch_prim[i] = ch[i];
//        }
//
//        String str = new String(ch_prim);
//        System.out.println(str);


//        int base = 26;
//        System.out.println(AlphabetGenerator.generateFrequencyAlphabet(base, test));


//        try{
//            f(-1);
//            System.out.println("R");
//        }catch(Exception e){
//            System.out.println("S");
//        }
//    }
//
//    static void f(int x) throws Exception {
//        try{
//            if( x<0 ) throw new Exception();
//            System.out.println("P");
//        }finally{
//            System.out.println("Q");
//        }
        class Point2D{
            private double x = 1;
            private double y;

            Point2D(){
                this.y = 2;
            }

            public double getX() {return x; }
            public double getY() { return y; }
        }

        class Point3D extends Point2D{
            private double z;

            Point3D( double z ){
                this.z = z;
            }

            public double getZ() { return z; }
        }

        Point3D obj = new Point3D(3);
        System.out.println(obj.getX());
        System.out.println(obj.getY());
        System.out.println(obj.getZ());
    }
}