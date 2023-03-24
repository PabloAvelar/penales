import cx_Freeze
import sys

base = None
if sys.platform == "win32":
    base = "Win32GUI"

executables = [cx_Freeze.Executable("Liguilla en penales.py", base=base, icon="fondohd.ico")]

cx_Freeze.setup(
	name="Liguilla",
	version="1.0",
	options={"build_exe": {"packages": ["pygame", "random", "sys"]}},
	description="Liguilla MX",
	executables = executables

	)
