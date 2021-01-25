from nipype.interfaces.mrtrix3 import MRConvert
from pathlib import Path


def mrtrix_conversion(inputs: dict, output: Path):
    in_file, json, bvec, bval = [
        inputs.get(key) for key in ["nii", "json", "bvec", "bval"]
    ]
    mrconvert = MRConvert()
    mrconvert.inputs.in_file = in_file
    if bvec:
        mrconvert.inputs.in_bvec = bvec
    if bval:
        mrconvert.inputs.in_bval = bval
    mrconvert.inputs.args = f"-json_import {json}"
    mrconvert.inputs.out_file = output
    mrconvert.run()
