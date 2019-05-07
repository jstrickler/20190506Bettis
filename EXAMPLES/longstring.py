#!/usr/bin/python

s = (
      "This is a very long string that would normally go over "
      "seventy-eight characters. In fact, this string, once "
      "concatenated, will have three hundred one characters."
      "Sometimes this could be necessary for building config"
      "files, for inserting various kinds of embedded scripts,"
      "or other interesting kinds of textual data."
)

print(len( s ))
print(s)