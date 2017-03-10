CPP_FILES := $(wildcard *.cpp)
EXE_FILES := $(notdir $(CPP_FILES:.cpp=.x))

all: ${EXE_FILES}

clean:
	rm -f ${EXE_FILES}

%.x:%.cpp
	g++ -std=c++11 $< -o $@
