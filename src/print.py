def printStartup(initial_software, msa_path, number_initial_trees, refinement_software) -> None:
        printHeader()
        printSoftwareConfig(initial_software, msa_path, number_initial_trees, refinement_software)

def printHeader() -> None:
        print("===============================")
        print("  PHYST Phylogenetic Pipeline  ")
        print("===============================")

        print("PHYST (v 1.0)")
        print("Developed by Joseph Guscott,")
        print("Barker Lab,")
        print("School of Biological Science")
        print("University of Edinburgh")
        print("Copyright (c) 2023 Joseph Guscott")

def printSoftwareConfig(initial_software: str, msa_path: str, number_initial_trees: int, refinement_software: str, time_stamp: str, cores: int) -> None:
        print("===============================")
        print("PHYST configuration:")
        print("  Initial Trees")
        print("    Software:", initial_software)
        print("    MSA:", msa_path)
        print("    Trees evaluated:", number_initial_trees)
        print("    Trees retained: 5")
        print("")
        print("  Likelihood Analysis")
        print("    Software:", refinement_software)
        print("")
        print("  Resources")
        print("    Cores:", cores)
        print("")
        print("Start time: ", time_stamp)
        print("")
        print("MPBoot provided by Hoang, et al., 2018; https://doi.org/10.1186/s12862-018-1131-3")
        print("IQ-Tree provided by Minh, et al., 2020; https://doi.org/10.1093/molbev/msaa015")
        print("===============================")
        print("")

def printDictionary(dictionary: dict) -> None:
       for key in dictionary:
                print (key,':',dictionary[key])