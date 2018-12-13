#pragma once
#include <array>
#include <vector>
#include <list>

class Day9
{
public:
	Day9();
	~Day9();
	void winnerPoints();
	void part2(int players, long long lastmarble);

	long long placeMarble(long long marbleCounter, long long index, std::vector<long long>& circle, long long player);
	std::list<long long>::iterator placeMarble2(long long marbleCounter, std::list<long long>::iterator marbleindex, std::list<long long>& circle, long long player);
	
	std::array<long, 404> scores;
	std::vector<long long> scores2;
	std::vector<long long> winningscore;
	std::vector<long long> winningscore2;
};

