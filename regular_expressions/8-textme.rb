#!/usr/bin/env ruby

# Get the input string from the first argument
log_entry = ARGV[0]

# Use regular expressions to capture the sender, receiver, and flags
sender = log_entry[/\[from:(.*?)\]/, 1]
receiver = log_entry[/\[to:(.*?)\]/, 1]
flags = log_entry[/\[flags:(.*?)\]/, 1]

# Print the result in the desired format
puts "#{sender},#{receiver},#{flags}"
