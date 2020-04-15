def n56(file_name):
    if file_name == "-":
        module = types.ModuleType("input_scenes"); code = "from manimlib.imports import *\n\n" + sys.stdin.read()
        try:
            exec(code, module.__dict__); return module;
        except Exception as e:
            print(f"Failed to render scene: {str(e)}"); sys.exit(2);
    else:
        module_name = file_name.replace(os.sep, ".").replace(".py", ""); spec = importlib.util.spec_from_file_location(module_name, file_name); module = importlib.util.module_from_spec(spec);
        spec.loader.exec_module(module)
        return module

def n57(self, vmobject, ctx):
    self.set_cairo_context_path(ctx, vmobject); self.apply_stroke(ctx, vmobject, background=True); self.apply_fill(ctx, vmobject); self.apply_stroke(ctx, vmobject);
    return self
    
