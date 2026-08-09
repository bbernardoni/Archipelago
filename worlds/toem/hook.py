import os
import shutil

from BaseClasses import MultiWorld
from fuzz import OUT_DIR, BaseHook


class Hook(BaseHook):

    def setup_main(self, args):
        os.makedirs(os.path.join(OUT_DIR, "benchmark"))

    def after_generate(self, mw: MultiWorld, output_path):
        if mw is None or len(mw.worlds) == 0:
            return

        time = getattr(mw.worlds[1], "benchmark_time", False)
        if time:
            with open(os.path.join(OUT_DIR, "benchmark", f"benchmark_{os.getpid()}.log"), "a") as f:
                f.write(f"{time}\n")

    def finalize(self):
        times = []
        benchmark_files = [
            os.path.join(OUT_DIR, "benchmark", f)
            for f in os.listdir(os.path.join(OUT_DIR, "benchmark"))
            if f.startswith("benchmark_")
        ]
        for filename in benchmark_files:
            with open(filename) as f:
                times.extend([float(line.strip()) for line in f.readlines()])

        shutil.rmtree(os.path.join(OUT_DIR, "benchmark"))
        print()
        print(f"Successful GER avg time (out of {len(times)}): {sum(times)/len(times):.4f} s")
        print(f"Max: {max(times)} s")
