# Copyright 2024 The PHYST Authors.
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import re
import os
from utils import DetectFileFormat

def TNT_input(msa_path: str) -> str:
    tnt_input = re.sub(".\w+\Z",".tnt",msa_path)
    return tnt_input

def GenerateTNTCommand(initial_software: str, msa_path: str, level: int, hits: int) -> str:
    file_format = DetectFileFormat(msa_path)
    tnt_input = TNT_input(msa_path)
    os.system(f"seqret {msa_path} -sformat1 {file_format} {tnt_input} -osformat2 hennig86")
    with open(tnt_input,'a') as f:
        f.write("procedure /;")

    software_path = f'{initial_software} '
    run_command = "run TNTsearch.run "
    pass_msa_path = f"input {tnt_input} "
    tnt_level = f"level {level} "
    tnt_hits = f"hits {hits} "
    command = software_path + run_command + pass_msa_path + tnt_level + tnt_hits + "treefile "

    return command
