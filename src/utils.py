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


def ReadFile(file_path: str) -> str:
    with open(file_path, encoding="utf-8") as file:
        for line in file:
            output = line

    return output


def WriteFile(file_path: str, data_structure: list) -> None:
    with open(file_path, "a+", encoding="utf-8") as file:
        for line in data_structure:
            file.write(f"{line}")
