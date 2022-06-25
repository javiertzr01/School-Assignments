package Week4;

import static org.junit.Assert.assertEquals;

import org.junit.Test;

public class FindMaxTest {
    @Test
    public void FindMaxTestFail(){
        int max = FindMax.max(new int[]{5,6,17,8,2});
        assertEquals(2, max);
    }
}