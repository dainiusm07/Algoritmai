#include <iostream>

using namespace std;

int involution (int number, int times) { // Kelimas laipsniu
    if (times!=0){
        int n=number;
        for (int i=1 ; i<times ; i++)
        n*=number;

        return n;
    }
    else return 1;
}

void baseToBase (string numberGiven, int baseFrom, int baseTo){

    string bases = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ";
    string result = "";
    int number=0 , check=0;

    for (int i=0 ; i<numberGiven.size() ; i++){ // Checkina ar visai galima taip, ta prasme 2-tainej sistemoj negali gi but raidziu
        numberGiven[i]=toupper(numberGiven[i]);
        if (baseFrom < bases.find(numberGiven[i])){
            check++;
            break;
        }
    }

    if (check==0){ // Checkina ar viskas ok, jei jo tai varom toliau
        for (int i=0 ; i<numberGiven.size() ; i++) // Vertimas i decimal
        number += bases.find(numberGiven[i]) * involution( baseFrom , numberGiven.size()-(i+1) ); 

        while (number > 0){ // Vertimas is decimal i reikiama base
            result = bases[number % baseTo] + result;
            number /= baseTo;
        }

        cout << "Your result is - " << result << endl;
    }
    else cout << "Something went wrong!" << endl;
    
}
int main () {

    baseToBase("zgg",36,10);

    return 0;
}
