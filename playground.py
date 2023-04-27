# 繪製場地邊線
def draw_ground(plt):
  # horizon
  plt.plot([-6, 6], [-3, -3], color="blue")
  plt.plot([6, 30], [10, 10], color="blue")
  plt.plot([-6, 18], [22, 22], color="blue")
  plt.plot([18, 30], [50, 50], color="blue")
  # vertical
  plt.plot([-6, -6], [-3, 22], color="blue")
  plt.plot([6, 6], [-3, 10], color="blue")
  plt.plot([18, 18], [22, 50], color="blue")
  plt.plot([30, 30], [10, 50], color="blue")
  # start end
  plt.plot([-6, 6],[0, 0], color="black")
  plt.plot([18, 30],[40, 37], color="red")
