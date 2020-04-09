def experimental_convert_saved_model_v1_to_mlir(saved_model_path, tags,show_debug_info):
  return ExperimentalConvertSavedModelV1ToMlir(
      str(saved_model_path).encode('utf-8'),
      str(tags).encode('utf-8'), show_debug_info)

