#!/usr/bin/env ruby

def phone_number(input)

  regex = /^\d{10}$/
  match = input.match(regex)
  puts match ? "#{match[0]}" : "$"
end
if ARGV.empty?
  puts "Please provide a phone number as an argument."
else
  phone_number(ARGV[0])
end
