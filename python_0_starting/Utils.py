class Utils:
    @staticmethod
    def check_version():
        import sys

        required_version = "3.10"
        current_version = sys.version_info

        if current_version < tuple(map(int, required_version.split("."))):
            print(f"Python version {required_version} or higher is required.")
            sys.exit(1)

        # print(f"Python version {current_version.major}.{current_version.minor}.{current_version.micro} is installed.")