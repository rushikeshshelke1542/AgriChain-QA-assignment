import java.util.*;
public class Main {
    static int solve(String s) {
        HashMap < Character, Integer > map = new HashMap < Character, Integer > ();

        int l = 0,
        int r = 0;
        int n = s.length();
        int len = 0;
        while (r < n) {
            if (map.containsKey(s.charAt(r))) {
            l = Math.max(map.get(s.charAt(r)) + 1, l);
            }

            map.put(s.charAt(r), r);

            len = Math.max(len, r - l + 1);
            r++;
        }
        return len;
    }

    public static void main(String args[]) {
        String str = "abcdde";
        System.out.println(solve(str));

    }
}