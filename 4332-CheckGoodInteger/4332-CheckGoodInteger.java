// Last updated: 8/12/2026, 11:46:18 AM
class Solution {
    public boolean checkGoodInteger(int n) {
        int d=0;
        int s=0;
        while(n>0){
            int dg=n%10;
            d+=dg;
            s+=dg*dg;
            n/=10;
        }
        return (s-d)>=50;
    }
}