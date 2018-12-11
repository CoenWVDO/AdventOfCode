#include "pch.h"
#include "Day9Performance.h"
#include <vector>
#include <memory>


Day9Performance::Day9Performance()
{
}


Day9Performance::~Day9Performance()
{
}

struct Marble
{
	long long value;
	//std::shared_ptr<Marble> previousM;
	//std::shared_ptr<Marble> nextM;
	Marble* previousM;
	Marble* nextM;
};


long long Day9Performance::calculateWinnerPoints(int nrPlayers, long long maxMarble)
{
	//std::shared_ptr<Marble> activeMarble(new Marble);
	Marble* activeMarble = new Marble;
	std::vector<long long> playerScores;
	playerScores.resize(nrPlayers, 0);

	activeMarble->value = 0;
	activeMarble->nextM = activeMarble;
	activeMarble->previousM = activeMarble;

	for (long long i = 1; i <= maxMarble; ++i)
	{
		int playerturn = (i - 1) % nrPlayers;
		if (i % 23 == 0)
		{
			activeMarble = activeMarble->previousM->previousM->previousM->previousM->previousM->previousM->previousM;
			playerScores[playerturn] += activeMarble->value + i;
			activeMarble = activeMarble->nextM;
			activeMarble->previousM = activeMarble->previousM->previousM;
			activeMarble->previousM->nextM = activeMarble;
		}

		else
		{
			//std::shared_ptr<Marble> newMarble(new Marble);
			Marble* newMarble = new Marble;
			newMarble->value = i;
			newMarble->nextM = activeMarble->nextM->nextM;
			newMarble->previousM = activeMarble->nextM;

			newMarble->nextM->previousM = newMarble;
			newMarble->previousM->nextM = newMarble;

			activeMarble = newMarble;
		}
	}

	long long answer = 0;
	for (size_t i = 0; i < playerScores.size(); ++i) {
		if (playerScores[i] > answer)
			answer = playerScores[i];
	}

	return answer;
}
