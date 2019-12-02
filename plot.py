import numpy as np
import matplotlib.pyplot as plt
import matplotlib.lines as lines

class MyLine(lines.Line2D):
    def __init__(self, *args, **kwargs):

        lines.Line2D.__init__(self, *args, **kwargs)



    def set_figure(self, figure):

        lines.Line2D.set_figure(self, figure)

    def set_axes(self, axes):

        lines.Line2D.set_axes(self, axes)

    def set_transform(self, transform):

        lines.Line2D.set_transform(self, transform)

    def set_data(self, x, y):

        lines.Line2D.set_data(self, x, y)

    def draw(self, renderer):

        lines.Line2D.draw(self, renderer)

# # Fixing random state for reproducibility
# np.random.seed(19680801)
#
#
# fig, ax = plt.subplots()
# x, y = np.random.rand(2, 20)
# line = MyLine(x, y, mfc='red', ms=12, label='line label')
# #line.text.set_text('line label')
# line.text.set_color('red')
# line.text.set_fontsize(16)
#
# ax.add_line(line)
#
# plt.show()