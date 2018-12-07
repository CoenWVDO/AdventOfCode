#pragma once
class Worker
{
public:
	Worker();
	~Worker();
	bool isBusy();
	void startJob(char c);
	bool doCycle();
	char getJob();
	
private:
	char job;
	int secondsToGo = 0;
	bool busy = false;
};

