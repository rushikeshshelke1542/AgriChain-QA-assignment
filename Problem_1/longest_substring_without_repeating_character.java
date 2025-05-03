import java.util.*;

public class Main {
    static String solve(String s) {
        HashMap<Character, Integer> mpp = new HashMap<>();

        int left = 0, right = 0;
        int n = s.length();
        int maxLen = 0;
        int maxStart = 0;

        while (right < n) {
            char currentChar = s.charAt(right);

            if (mpp.containsKey(currentChar)) {
                left = Math.max(mpp.get(currentChar) + 1, left);
            }

            mpp.put(currentChar, right);

            if (right - left + 1 > maxLen) {
                maxLen = right - left + 1;
                maxStart = left;
            }

            right++;
        }

        return s.substring(maxStart, maxStart + maxLen);
    }

    public static void main(String args[]) {
        String str = "abccd";
        System.out.println("The longest substring without repeating characters is: " + solve(str));
    }
}
