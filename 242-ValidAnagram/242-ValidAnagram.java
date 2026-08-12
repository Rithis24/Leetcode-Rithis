// Last updated: 8/12/2026, 11:49:58 AM
class Solution {
    public boolean isAnagram(String s, String t) {
        char a1[]=s.toLowerCase().toCharArray();
        char a2[]=t.toLowerCase().toCharArray();
        Arrays.sort(a1);
        Arrays.sort(a2);
        boolean v=Arrays.equals(a1,a2);
        return v;
    }
}