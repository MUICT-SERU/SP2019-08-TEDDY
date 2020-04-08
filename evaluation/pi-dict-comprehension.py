def ConvertBetweenDataFormats(x, data_format_src, data_format_dst):
  """Converts 4D tensor between data formats."""

  valid_data_formats = ["NHWC", "NCHW", "HWNC", "HWCN"]
  if data_format_src not in valid_data_formats:
    raise ValueError("data_format_src must be of %s, got %s." %
                     (valid_data_formats, data_format_src))
  if data_format_dst not in valid_data_formats:
    raise ValueError("data_format_dst must be of %s, got %s." %
                     (valid_data_formats, data_format_dst))
  if len(x.shape) != 4:
    raise ValueError("x must be 4D, got shape %s." % x.shape)

  if data_format_src == data_format_dst:
    return x

  dim_map = {d: i for i, d in enumerate(data_format_src)}
  transpose_dims = [dim_map[d] for d in data_format_dst]
  return np.transpose(x, transpose_dims)