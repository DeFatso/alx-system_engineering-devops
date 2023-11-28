#!/usr/bin/env ruby

def match_school(input)
  regex = /School/
  matches = input.scan(regex)
  puts matches.empty? ? "$" : matches.join("")
end

if ARGV.empty?
  puts "Please provide an argument."
else
  match_school(ARGV[0])
end
