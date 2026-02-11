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

import itertools
import linecache
import os
import re

from iqtree import IqtreeEvaluateTreesCommand
from log import LOG
from print import Print


class FilterTrees:
    def __init__(self, MSA_INPUT_PATH: str, HARDWARE: int, NUM_MP_TREES: int) -> None:
        self.MSA_INPUT_PATH = MSA_INPUT_PATH
        self.HARDWARE = HARDWARE
        self.NUM_MP_TREES = NUM_MP_TREES
        self.FilterInitialTrees()

    def FilterInitialTrees(self) -> None:
        evaluate_command = IqtreeEvaluateTreesCommand(
            self.MSA_INPUT_PATH, self.HARDWARE
        )
        print("EVALUATE_COMMAND: %s", evaluate_command)
        os.system(evaluate_command)
        best_trees_dict = self.GetBestTreesDictionary()

        best_tree_numbers = dict(
            itertools.islice(best_trees_dict.items(), self.NUM_MP_TREES)
        )

        print(type(best_tree_numbers))
        print(f"best_tree_numbers: {best_tree_numbers}")

        LOG.info("Highest scoring likelihood trees:")

        Print.PrintDictionary(best_tree_numbers)

        self.WriteBestInitialTreesFile(best_tree_numbers)

    def GetBestTreesDictionary(self) -> dict[str, float]:
        file = self.MSA_INPUT_PATH + ".log"
        print("LOGFILE: %s", file)
        best_trees_dict = {}
        iqtree_regex = r"^(Tree \d+) \/ (LogL:) (-\d*.\d*)$"

        with open(file, "r", encoding="utf-8") as fp:
            for line in fp:
                tree_search = re.search(iqtree_regex, line)
                if tree_search is not None:
                    best_trees_dict[str(tree_search.group(1))] = float(
                        tree_search.group(3)
                    )

        best_trees_dict = dict(
            sorted(best_trees_dict.items(), key=lambda item: item[1], reverse=True)
        )

        return best_trees_dict

    def WriteBestInitialTreesFile(self, best_trees_number: dict[str, float]) -> None:
        file = "initial_trees.treefile"
        lines = []
        line_numbers: list[int] = []

        for key in best_trees_number:
            tree_number = int(key.split()[-1])
            line_numbers.append(tree_number)

        for line_number in line_numbers:
            x = linecache.getline(file, line_number).strip()
            lines.append(x)

        with open("initial_trees_best.treefile", "w", encoding="utf-8") as fp:
            for line in lines:
                fp.write(f"{line}\n")

        for i in range(self.NUM_MP_TREES):
            j = str(i + 1)
            file_name = "initial_trees_best_" + j + ".treefile"

            with open(file_name, "w", encoding="utf-8") as fp:
                fp.write(f"{lines[i]}\n")
