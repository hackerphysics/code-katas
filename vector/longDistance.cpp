#include <vector>
using namespace std;
int longestDistance(vector<int> A,int n){
    int imin,imax,min,max;
    min = 0;
    max = 0;
    imax = imin = 0;
    for (int i=0;i<n;i++) {
        if (A[i]<min) {
            min = A[i];
            imin = i;
        }else if (A[i]>max) {
            max = A[i];
            imax = i;
        }
    }
    if(imax<=imin){
        return 0;
    }else{
        return max-min;
    }
}
