package com.javier.pslib;


import java.util.ArrayList;
import java.util.Iterator;

public class Test {

    public static void main(String[] args) {
        ArrayList<Integer> a = new ArrayList<>();
        a.add(2);
        a.add(3);
        a.add(4);

        Iterator<Integer> iter = a.iterator();
        System.out.println(iter.next());
//        System.out.println(iter.next());

    }
}
