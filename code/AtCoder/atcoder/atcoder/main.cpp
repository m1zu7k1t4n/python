#include <iostream>
#include <string>

int main(void){
	std::string str("012345");
	std::string sub = str.substr(2, 3);     //  [2] の位置から3文字切り出す
	std::cout << sub << "\n";
	int W, b;
	std::string a;
	a += "DiscoPresentsDiscoveryChannelProgrammingContest2016";

	std::cin >> W;
	b = 51 / W;

	if (W > 51) {
		std::cout << &a << std::endl;
	}
	
	return 0;
}