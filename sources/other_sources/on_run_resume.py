import sys
import os


class AddSourcesPath:
    @staticmethod
    def add_sources_path():
        sys.path.append(os.getcwd())


class OnRunResume:
    @staticmethod
    def on_run_resume():
        from sources.other_sources.on_resume import OnResume
        o = OnResume()
        o.on_resume()


if __name__ == "__main__":
    AddSourcesPath.add_sources_path()
    OnRunResume.on_run_resume()
