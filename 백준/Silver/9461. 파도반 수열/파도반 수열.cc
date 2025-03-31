#include <iostream>

using namespace std;

int main() {

	int T;
	cin >> T;

	while (T--) {
		int N;
		//int로 해서 틀렸습니다 떠서 long했는데 또 틀렸습니다
		// -> long long 슛
		long long arr[102];
		cin >> N;

		arr[0] = 1;  arr[1] = 1; arr[2] = 1;

		for (int i = 3; i < N + 1 ; i++) {
			arr[i] = arr[i - 2] + arr[i - 3];
		}

		cout << arr[N - 1] << "\n";
	}
	
	return 0;
}