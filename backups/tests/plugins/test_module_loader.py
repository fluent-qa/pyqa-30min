from revisited.r_meta.py_meta_demo.package_demos.module_loader import load_module, load_module_from_file


def test_module_loader():
    m1 = load_module_from_file("plugins","../../plugins/module_demo.py")
    m2 = load_module_from_file("plugins","../../plugins/module_demo_2.py")
    m1.module_demo()
    m2.module_demo()
