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

import linecache
from random import randrange
import re

def ReadFile(file_path: str) -> None:
    with open(file_path) as file:
        for line in file:
            output = line
    return output

def ReadRandomLine(file_path: str) -> None:
    with open(file_path) as file:
        for count in enumerate(file):
            pass
    line_num = randrange(count[0]+1)
    output = linecache.getline(file_path, line_num)
    
    return output

def WriteFile(file_path: str, data_structure: list) -> None:
    with open(file_path, 'a+') as file:
        for line in data_structure:
            file.write(f"{line}")

def DetectFileFormat(msa_path) -> str:
    file_extension = re.search(".(\w+)\Z", msa_path)
    formats = {'phy':'phylip','ph':'phylip','phylip':'phylip',
            'fa':'fasta','fasta':'fasta',
            'nex':'nexus','nxs':'nexus','nexus':'nexus',
            'aln':'clustal','clustal':'clustal'}
    if file_extension:
        msa_format = formats[file_extension[1].lower()]
        print(msa_format.upper() + ' format detected.')
    else: msa_format = 'phylip'
    return msa_format