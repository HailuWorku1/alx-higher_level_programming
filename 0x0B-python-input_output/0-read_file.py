#!/usr/bin/python3

def read_file(filename=""):
    with open('dog_breeds.txt', 'r') as reader:
    # Read and print the entire file line by line
        line = reader.readline()
        while line != '':  # The EOF char is an empty string
            print(line, end='')
            line = reader.readline()
