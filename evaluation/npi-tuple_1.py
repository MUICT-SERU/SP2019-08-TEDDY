#NPI pattern on line 8-9-10, 15-16-17
def _adjustHueNp(self, x_np, delta_h):
    self.assertEqual(x_np.shape[-1], 3)
    x_v = x_np.reshape([-1, 3])
    y_v = np.ndarray(x_v.shape, dtype=x_v.dtype)
    channel_count = x_v.shape[0]
    for i in xrange(channel_count):
      r = x_v[i][0]
      g = x_v[i][1]
      b = x_v[i][2]
      h, s, v = colorsys.rgb_to_hsv(r, g, b)
      h += delta_h
      h = math.fmod(h + 10.0, 1.0)
      r, g, b = colorsys.hsv_to_rgb(h, s, v)
      y_v[i][0] = r
      y_v[i][1] = g
      y_v[i][2] = b
    return y_v.reshape(x_np.shape)