#include "pch.h"
#include "Worker.h"


Worker::Worker()
{
}


Worker::~Worker()
{
}

bool Worker::isBusy()
{
	return busy;
}

void Worker::startJob(char c)
{
	busy = true;
	int time = int(c - 64) + 60;
	secondsToGo = time;
	job = c;
}

bool Worker::doCycle()
{
	if (!busy)
	{
		return false;
	}

	secondsToGo--;
	if (secondsToGo == 0)
	{
		busy = false;
		return true;
	}
	return false;
}

char Worker::getJob()
{
	return job;
}
