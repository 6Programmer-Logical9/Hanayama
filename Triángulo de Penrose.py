import turtle as t
def fig_01():
       t.left(240)
       t.forward(170)
       t.right(120)
       t.forward(30)
       t.right(60)
       t.forward(200)
       t.right(120)
       t.forward(170)
       t.right(120)
       t.forward(30)
       t.right(60)
       t.forward(110)
def volver():
       t.right(180)
       t.forward(110)
       t.right(120)
       t.forward(80)
       t.left(60)
       t.forward(30)
       t.right(120)
color = ["black", "grey", "silver"]
for i in range(3):
      t.color(color[i])
      t.begin_fill()
      fig_01()
      t.end_fill()
      if i<2:
           volver()
t.done()