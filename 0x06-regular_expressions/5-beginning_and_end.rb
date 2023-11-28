#!/usr/bin/env ruby

def match_pattern(input)
  regex = /^h.n$/
  match = input.match(regex)
  puts match ? "#{match[0]}" : ""
end

if ARGV.empty?
  puts "Please provide an argument."
else
  match_pattern(ARGV[0])
end
