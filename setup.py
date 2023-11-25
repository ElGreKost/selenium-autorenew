from cx_Freeze import setup, Executable

setup(
    name="LibAutoRenew",
    version="1.0",
    options={"build_exe": {
        "packages": ["selenium", "time", "datetime", "os", "tkinter"],
        "include_files": [r'/home/kostiskak/programming/PycharmProjects/NtuaLibRenew_v2/credentials']
    }},
    executables=[Executable("NtuaLibAutoRenew.py")]
)
