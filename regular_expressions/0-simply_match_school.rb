#!/usr/bin/env ruby
#this code put the 1st arg in the variable input
input = ARGV[0]
#thi one checks if the arg matches school
puts input.scan(/School/).join
