from turtle import color, begin_fill, forward, left, end_fill, done, pos
color('red', 'yellow')
begin_fill()
while True:
    forward(400)
    left(170)
    if abs(pos()) < 1:
        break
end_fill()
done()