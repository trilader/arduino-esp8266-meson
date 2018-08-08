#!/usr/bin/env python3

import shutil
import os
import sys
import subprocess
import tempfile

def main():
    if len(sys.argv) != 5:
        print("this is not how this works...")
        sys.exit(1)

    infile = sys.argv[1]
    outfile = sys.argv[2]
    depfile = sys.argv[3]
    ccexe = sys.argv[4]

    indir = os.path.dirname(infile)
    outdir = os.path.dirname(outfile)

    dependencies = set([infile])

    def preprocess(infile, outfile):
        with tempfile.NamedTemporaryFile(mode="w+") as tmpfile:
            sub = subprocess.run([
                ccexe,
                '-CC',
                '-E',
                '-P',
                '-DVTABLES_IN_FLASH',
                infile,
                '-o', outfile,
                '-MD',
                '-MF', tmpfile.name
            ])
            if sub.returncode != 0:
                print("subprocess.run failed with exit code", sub.returncode)
                sys.exit(1)

            data = tmpfile.read()
            data = data.replace("\\\n", "")
            if ":" in data:
                deps = data.split(":")[1].split(" ")
                for d in deps:
                    d = d.strip()
                    if not d:
                        continue
                    dependencies.add(os.path.realpath(d))

    shutil.copy(infile, os.path.join(outdir, os.path.basename(infile)))

    to_inspect = [infile]
    while len(to_inspect) != 0:
        candidate = to_inspect.pop()
        with open(candidate, "r") as fp:
            for line in fp:
                if line.startswith("INCLUDE"):
                    _, name = line.split(" ", maxsplit=1)
                    name = name.strip("\"\n")
                    absname = os.path.join(indir, name)
                    newname = os.path.join(outdir, name)
                    os.makedirs(os.path.dirname(newname), exist_ok=True)

                    if os.path.exists(absname+".h"):
                        to_inspect.append(newname)
                        dependencies.add(os.path.realpath(absname+".h"))
                        preprocess(absname+".h", newname)
                    else:
                        to_inspect.append(absname)
                        dependencies.add(os.path.realpath(absname))
                        shutil.copy(absname, newname)
    with open(depfile, "w") as fp:
        fp.write("{}: {}".format(infile, " ".join(dependencies)))

if __name__ == "__main__":
    main()
