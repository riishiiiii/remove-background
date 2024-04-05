# Determine the operating system
OS := $(shell uname)

# Use different commands based on the operating system
ifeq ($(OS), Linux)
    # Commands for Linux (Ubuntu)
    DC := docker-compose
    BUILD := sudo $(DC) -f docker-compose.yml build
    UP := sudo $(DC) -f docker-compose.yml up
    DOWN := sudo $(DC) -f docker-compose.yml down
else ifeq ($(OS), Windows_NT)
    # Commands for Windows
    DC := docker-compose
    BUILD := $(DC) -f docker-compose-local.yml build
    UP := $(DC) -f docker-compose-local.yml up
    DOWN := $(DC) -f docker-compose-local.yml down
else
    $(error Unsupported operating system)
endif


DC := docker-compose

 
build:
	$(BUILD)

up:
	$(UP)

down d:
	$(DOWN)

run r: build up