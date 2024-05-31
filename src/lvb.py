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

from utils import DetectFileFormat

def GenerateLVBCommand(initial_software: str, msa_path: str) -> str:
    software_path = f'{initial_software} '
    pass_msa_path = "-i " + msa_path
    p_threads = 1
    msa_format = DetectFileFormat(msa_path)

    command = software_path + pass_msa_path + ' -f ' + msa_format + ' -p ' + str(p_threads)
    
    return command
