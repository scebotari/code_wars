def make_readable(seconds):
  secs = seconds % 60
  mins = seconds // 60 % 60
  hours = seconds // 3600

  return '{:0>2}:{:0>2}:{:0>2}'.format(hours, mins, secs)

print(make_readable(0)) # == "00:00:00"
print(make_readable(5)) # == "00:00:05"
print(make_readable(60)) # == "00:01:00"
print(make_readable(86399)) # == "23:59:59"
print(make_readable(359999)) # == "99:59:59"