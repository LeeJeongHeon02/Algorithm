#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
	ios::sync_with_stdio(0);
	cin.tie(0);

	vector<int> arr;
	int N, M;
	int num;

	cin >> N;
	while (N--)
	{
		// N개의 정수를 저장하는 배열 생성
		cin >> num;
		arr.push_back(num);
	}
	// N개의 정수를 오름차순으로 정렬
	sort(arr.begin(), arr.end());

	cin >> M;
	while (M--)
	{
		// M개의 수를 입력받으면서 각 수마다 binary_search 실행
		cin >> num;
		// 수가 배열에 존재하면 1, 없으면 0 출력
		if (binary_search(arr.begin(), arr.end(), num))
		{
			cout << "1" << "\n";
		}
		else {
			cout << "0" << "\n";

		}
	}
}
