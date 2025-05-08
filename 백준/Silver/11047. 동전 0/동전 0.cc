#include <iostream>
#include <sstream>
#include <vector>
#include <algorithm>

using namespace std;

int main() {

	// 1. 입력 받아서 배열에 넣기
	// 2. 금액이 큰 순서대로 역순 정렬
	// 3. k원을 만들기 위해 더할 수 있는 큰 수부터 더해가기

	int N, K, inputValue, result = 0;
	cin >> N >> K;

	vector<int> arr;

	while (N--) {
		cin >> inputValue;
		arr.push_back(inputValue);
	}

	//arr을 정렬하는데 greater<int>을 이용해 역순으로 정렬
	reverse(arr.begin(), arr.end());

	for (int i = 0; i < arr.size(); i++) {
		if (arr[i] > K) {
			continue;
		}
		else {
			// K원에 필요한 Ai가치의 동전의 개수
			result += K / arr[i];
			K -= (K / arr[i]) * arr[i];
		}
	}
	cout << result << endl;
}
