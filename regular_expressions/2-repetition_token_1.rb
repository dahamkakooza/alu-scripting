#!/usr/bin/env ruby
#puts the 1st arg in a variable
input = ARGV[0]

#checks matches
puts input.scan(/hb?tn/).join
