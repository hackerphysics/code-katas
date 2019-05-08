#include <math.h>
int isPowerOfN(int n, int N){
    double t = log(n)/log(N);
    int T = (int)(t);
    double eps = 1/pow(N,t+2);
    if((t-T)<eps){
        return T;
    }
    if((T+1-t)<eps){
        return T+1;
    }
    return 0;
}
