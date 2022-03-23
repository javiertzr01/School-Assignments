package com.javier.pslib;

import java.util.*;

public class IteratingExamples {

    public static int Act2ForEach(List<Integer> integers) {
        int total = 0;
        for(int i = 0; i < integers.size(); i++){
            total += integers.get(i);
        }
        return total;
    }
}



