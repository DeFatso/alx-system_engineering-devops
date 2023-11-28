#!/usr/bin/env ruby
def test(input)
  regex = /money/
  match = input.match(regex)
  puts match ? match[0] : "$"
end

test(ARGV[0])
