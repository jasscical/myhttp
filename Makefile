all: httpd

httpd: httpd.cpp
	g++ -W -Wall -o httpd httpd.cpp -lpthread -std=c++11

clean:
	rm httpd
