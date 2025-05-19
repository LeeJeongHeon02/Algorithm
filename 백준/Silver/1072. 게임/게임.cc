#include <iostream>
#include <algorithm>
/*
    + 앞으로 모든 게임에서 이긴다고 가정
    
    만약 승률이 99% 이상이면 아무리 게임을 진행해도 승률이 100%는 불가능함.
    >> 예외처리, if z >= 99 : print -1
    
    X 값의 최대 10억... 매우 큼 => Binary Search 생각필요함
    >>1부터 longlong까지 Binary Search 진행해서 승률이 Z에서 Z + 1로 변하는 지점을 찾자!
*/
long long defferenceOfWinrate(long long num); // 함수 선언
using namespace std;

long long X, Y, Z; // 게임 횟수, 이긴 게임, 승률 (전역변수)
int main() {
    long long low = 0, high = 1e15, mid;
    
    cin >> X >> Y;
    Z =  Y * 100 / X; // 승률계산

    // Z가 절대 변하지 않는경우 예외처리
    if (Z >= 99) {
        cout << -1;
        return 0;
    }
    
    while (low + 1 < high) {
        mid = (low + high) / 2;
        if (defferenceOfWinrate(mid) > 0)
        {
            high = mid;
        } 
        else // mid의 승률이 Z보다 같을때 (작은경우없음)
        {
            low = mid;
        }
    }
        
    cout << high;
    return 0;
}

long long defferenceOfWinrate(long long num) {
    return ((Y + num) * 100 / (X + num)) - Z; // 승률의 변화량
}