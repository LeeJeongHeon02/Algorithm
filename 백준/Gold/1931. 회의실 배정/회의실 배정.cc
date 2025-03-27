#include <iostream>
#include <vector> // 동적배열 사용
#include <utility> // pair 기능 사용
#include <algorithm> // sort 기능 사용

using namespace std;
/*
1차시도 실패. 맞는거같은데.. 싶어서 좀 찾아보니까
회의의 시작시간도 정렬해줘야함. 반례가 있었다.
2
1 2
2 2
위와같은경우 2 2가 먼저 들어와버리면 result가 1인데
1 2가 먼저 들어오면 result가 2이다.
즉 문제에서 "회의의 시작시간과 끝나는 시간이 같을 수도 있다"
라는 조건떄문에 시작시간도 정렬해줘야한다.
*/
int result;

int main() {
	int N; //회의의 수
	int a, b; //회의의 시작시간과 끝나는시간
	int tempEnd = 0; //현재 회의의 끝나는 시간을 임시저장
	vector<pair<int, int>> arr; // 배열 안에 (1, 2) 이런식으로 저장

	//문제 입력 및 동적배열 세팅
	cin >> N;
	while (N--) {
		cin >> a >> b;
		arr.push_back({ a, b });
	}
	
	// pair값 중 second값이 작은것을 기준으로 정렬 후 second 값이 같은것은 first기준으로 정렬
	sort(arr.begin(), arr.end(), [](const pair<int, int>& a, const pair<int, int>& b) {
		return (a.second < b.second) || (a.second == b.second && a.first < b.first);
		});

	//배열을 루프돌면서 가장 빨리 끝나는 회의의 끝값을 temp에 저장.
	for (const auto& p : arr) {
		if (p.first >= tempEnd) {
			result++;
			tempEnd = p.second;
		}
	}
	//결과출력
	cout << result;
}