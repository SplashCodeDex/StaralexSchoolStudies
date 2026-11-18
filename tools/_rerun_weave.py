import importlib.util

spec = importlib.util.spec_from_file_location("figs", r"W:\StaralexSchoolStudies\tools\build_va_figures.py")
m = importlib.util.module_from_spec(spec)
spec.loader.exec_module(m)
m.weave_plain()
print("done")
