#include </home/haipeng/code/leetcode.git/leetcode.h>
#include <math.h>
#include <iostream>
using namespace std;
int main(int argc, char const* argv[])
{
    int r,N;
    cout<<"please input the N:"<<endl;
    cin>>N;
    cout<<"number\t"<<"power\t"<<"check"<<endl;
    for(int i = 1;i<10000000;i++){ 
        r = isPowerOfN(i,N);
        if(r!=0){
            cout<<i<<"\t"<<r<<"\t"<<pow(N,r)<<endl;
        }
    }
    return 0;
}
