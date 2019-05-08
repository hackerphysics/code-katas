#include <iostream>
#include <string>
using namespace std;


class Solution {
public:

    string convertToTitle(int n) {

        string title;

        if(n==0){

            return title;

        }

        else{

            int nn=(n-1)/26;

            int nm=(n-1)%26+1;

            char mychar=nm+64;

            title+=convertToTitle(nn);

            title+=mychar;

            return title;

        }

    }

};

int main(){
    Solution s;
    string result;
    int n;
    cout<<"input a number:"<<endl;
    cin>>n;
    result=s.convertToTitle(n);
    cout<<"results:"<<endl;
    cout<<n<<"-->"<<result<<endl;
}
