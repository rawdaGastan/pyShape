.PHONY: all clean

deps:  ## Install dependencies
	pip install poetry
	poetry install

doc: 
	pdoc --http localhost:8080 pyShape/*
