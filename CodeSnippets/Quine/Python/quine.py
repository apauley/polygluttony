src = """print 'src = ' + (chr(34) * 3) + src + (chr(34) * 3)
print 'exec(src)'
"""
exec(src)
