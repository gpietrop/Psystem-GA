# Inferring P Systems From Their Computing Steps: An Evolutionary Approach

Python implementation for paper "Inferring P Systems From Their Computing Steps: An Evolutionary Approach": Alberto Leporatia, Luca Manzoni, Giancarlo Mauria, Gloria Pietropolli, Claudio Zandrona, 2021.

## Abstract
Inferring the structure and operation of a computing model, given some observations of its behavior, is in general a desirable but daunting task. In this paper we try to solve a constrained version of this problem. Given a P system Π with active membranes and using cooperative rewriting, communication, and division
rules, let C be a collection of pairs (Ci, Ci+1) of consecutive configurations of Π, for 0 ≤ i < n. We feed this collection as input to a (µ+λ) evolutionary algorithm that evolves a population of (initially random) P systems, each with its own rules, with the aim of obtaining an individual that approximates Π as well as
possible. We discuss the results obtained on four different benchmark problems, designed to test the ability to infer cooperative rewriting, communication, and
membrane division rules. We will also provide a description of how fitness results are influenced by different setting of the hyperparameters of the evolutionary
algorithm. The results show that the proposed approach is able to find correct solutions for small problems, and it is a promising research direction for the
automatic synthesis of P systems.

## Instructions

To run the code, enter the following command:

```bash
python3 experiments.py --problem --size --number_run conf.json --prefix 
```
where the inputs arguments stands for: 
* ```python
--problem ```
