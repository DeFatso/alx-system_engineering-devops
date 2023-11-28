#!/usr/bin/env ruby

def extract_capital_letters(input)
  capital_letters = input.scan(/[A-Z]/).join
  puts capital_letters.empty? ? "$" : capital_letters
end

if ARGV.empty?
  puts "Please provide an argument."
else
  extract_capital_letters(ARGV[0])
end
