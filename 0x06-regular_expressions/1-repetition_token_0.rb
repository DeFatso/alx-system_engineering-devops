#!/usr/bin/env ruby

def find(input)
  regex = /\b\w*t{2,5}\w*\b/
  match = input.match(regex)
  puts match ? match[0] : "$"
end

find(ARGV[0])
