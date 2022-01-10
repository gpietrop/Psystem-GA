#!/usr/bin/env python
# coding: utf-8

# In[5]:


import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

import os
import csv
import sys

mu = 1
max_lhs = (1, 2, 3)
max_rhs = (1, 2, 3)
max_ruleset_size = (10, 20, 40)
max_mutation = (10, 20, 40)
mu = (1, 5, 10)


problems = ["send-in-2-fitness.csv", "send-in-3-fitness.csv", "send-in-4-fitness.csv", "send-in-5-fitness.csv",
            "send-out-2-fitness.csv", "send-out-3-fitness.csv", "send-out-4-fitness.csv", "send-out-5-fitness.csv",
            "assignment-2-fitness.csv", "assignment-3-fitness.csv", "assignment-4-fitness.csv", "assignment-5-fitness.csv",
            "tm-2-fitness.csv", "tm-3-fitness.csv", "tm-4-fitness.csv", "tm-5-fitness.csv"]

for problem in problems:
    directory_10_1__1_1 = "results/" + str(mu[0]) + "/" + str(max_ruleset_size[0]) + "/" + str(max_mutation[0]) + "/" + str(max_lhs[0]) + "/" + str(max_rhs[0]) + "/" + problem 
    directory_10_1__2_2 = "results/" + str(mu[0]) + "/" + str(max_ruleset_size[0]) + "/" + str(max_mutation[0]) + "/" + str(max_lhs[1]) + "/" + str(max_rhs[1]) + "/" + problem
    directory_10_1__3_3 = "results/" + str(mu[0]) + "/" + str(max_ruleset_size[0]) + "/" + str(max_mutation[0]) + "/" + str(max_lhs[2]) + "/" + str(max_rhs[2]) + "/" + problem

    directory_10_5__1_1 = "results/" + str(mu[1]) + "/" + str(max_ruleset_size[0]) + "/" + str(max_mutation[0]) + "/" + str(max_lhs[0]) + "/" + str(max_rhs[0]) + "/" + problem
    directory_10_5__2_2 = "results/" + str(mu[1]) + "/" + str(max_ruleset_size[0]) + "/" + str(max_mutation[0]) + "/" + str(max_lhs[1]) + "/" + str(max_rhs[1]) + "/" + problem
    directory_10_5__3_3 = "results/" + str(mu[1]) + "/" + str(max_ruleset_size[0]) + "/" + str(max_mutation[0]) + "/" + str(max_lhs[2]) + "/" + str(max_rhs[2]) + "/" + problem


    directory_10_10__1_1 = "results/" + str(mu[2]) + "/" + str(max_ruleset_size[0]) + "/" + str(max_mutation[0]) + "/" + str(max_lhs[0]) + "/" + str(max_rhs[0]) + "/" + problem
    directory_10_10__2_2 = "results/" + str(mu[2]) + "/" + str(max_ruleset_size[0]) + "/" + str(max_mutation[0]) + "/" + str(max_lhs[1]) + "/" + str(max_rhs[1]) + "/" + problem
    directory_10_10__3_3 = "results/" + str(mu[2]) + "/" + str(max_ruleset_size[0]) + "/" + str(max_mutation[0]) + "/" + str(max_lhs[2]) + "/" + str(max_rhs[2]) + "/" + problem



    directory_20_1__1_1 = "results/" + str(mu[0]) + "/" + str(max_ruleset_size[1]) + "/" + str(max_mutation[1]) + "/" + str(max_lhs[0]) + "/" + str(max_rhs[0]) + "/" + problem
    directory_20_1__2_2 = "results/" + str(mu[0]) + "/" + str(max_ruleset_size[1]) + "/" + str(max_mutation[1]) + "/" + str(max_lhs[1]) + "/" + str(max_rhs[1]) + "/" + problem
    directory_20_1__3_3 = "results/" + str(mu[0]) + "/" + str(max_ruleset_size[1]) + "/" + str(max_mutation[1]) + "/" + str(max_lhs[2]) + "/" + str(max_rhs[2]) + "/" + problem

    directory_20_5__1_1 = "results/" + str(mu[1]) + "/" + str(max_ruleset_size[1]) + "/" + str(max_mutation[1]) + "/" + str(max_lhs[0]) + "/" + str(max_rhs[0]) + "/" + problem
    directory_20_5__2_2 = "results/" + str(mu[1]) + "/" + str(max_ruleset_size[1]) + "/" + str(max_mutation[1]) + "/" + str(max_lhs[1]) + "/" + str(max_rhs[1]) + "/" + problem
    directory_20_5__3_3 = "results/" + str(mu[1]) + "/" + str(max_ruleset_size[1]) + "/" + str(max_mutation[1]) + "/" + str(max_lhs[2]) + "/" + str(max_rhs[2]) + "/" + problem


    directory_20_10__1_1 = "results/" + str(mu[2]) + "/" + str(max_ruleset_size[1]) + "/" + str(max_mutation[1]) + "/" + str(max_lhs[0]) + "/" + str(max_rhs[0]) + "/" + problem
    directory_20_10__2_2 = "results/" + str(mu[2]) + "/" + str(max_ruleset_size[1]) + "/" + str(max_mutation[1]) + "/" + str(max_lhs[1]) + "/" + str(max_rhs[1]) + "/" + problem
    directory_20_10__3_3 = "results/" + str(mu[2]) + "/" + str(max_ruleset_size[1]) + "/" + str(max_mutation[1]) + "/" + str(max_lhs[2]) + "/" + str(max_rhs[2]) + "/" + problem


    rows = []
    if os.path.exists(directory_10_1__1_1):
        with open(directory_10_1__1_1, 'r') as file:
            csvreader = csv.reader(file)
            for row in csvreader:
                rows.append(row)
        if len(rows[-1])!=30:
            ass_10_1__1_1 = rows[-2]
        else:
            ass_10_1__1_1 = rows[-1]
        ass_10_1__1_1 = [float(el) for el in ass_10_1__1_1 if el!=' ']
    else:
        ass_10_1__1_1 = [1 for _ in range(30)]

    rows = []
    if os.path.exists(directory_10_1__2_2):
        with open(directory_10_1__2_2, 'r') as file:
            csvreader = csv.reader(file)
            for row in csvreader:
                rows.append(row)
        if len(rows[-1])!=30:
            ass_10_1__2_2 = rows[-2]
        else:
            ass_10_1__2_2 = rows[-1]
        ass_10_1__2_2 = [float(el) for el in ass_10_1__2_2 if el!=' ']
    else:
        ass_10_1__2_2 = [1 for _ in range(30)]

    rows = []
    if os.path.exists(directory_10_1__3_3):
        with open(directory_10_1__3_3, 'r') as file:
            csvreader = csv.reader(file)
            for row in csvreader:
                rows.append(row)
        if len(rows[-1])!=30:
            ass_10_1__3_3 = rows[-2]
        else:
            ass_10_1__3_3 = rows[-1]
        ass_10_1__3_3 = [float(el) for el in ass_10_1__3_3 if el!=' ']
    else:
        ass_10_1__3_3 = [1 for _ in range(30)]

    rows = []
    if os.path.exists(directory_10_5__1_1):
        with open(directory_10_5__1_1, 'r') as file:
            csvreader = csv.reader(file)
            for row in csvreader:
                rows.append(row)
        if len(rows[-1])!=30:
            ass_10_5__1_1 = rows[-2]
        else:
            ass_10_5__1_1 = rows[-1]
        ass_10_5__1_1 = [float(el) for el in ass_10_5__1_1 if el!=' ']
    else:
        ass_10_5__1_1 = [1 for _ in range(30)]

    rows = []
    if os.path.exists(directory_10_5__2_2):
        with open(directory_10_5__2_2, 'r') as file:
            csvreader = csv.reader(file)
            for row in csvreader:
                rows.append(row)
        if len(rows[-1])!=30:
            ass_10_5__2_2 = rows[-2]
        else:
            ass_10_5__2_2 = rows[-1]
        ass_10_5__2_2 = [float(el) for el in ass_10_5__2_2 if el!=' ']
    else:
        ass_10_5__2_2 = [1 for _ in range(30)]

    rows = []
    if os.path.exists(directory_10_5__3_3):
        with open(directory_10_5__3_3, 'r') as file:
            csvreader = csv.reader(file)
            for row in csvreader:
                rows.append(row)
        if len(rows[-1])!=30:
            ass_10_5__3_3 = rows[-2]
        else:
            ass_10_5__3_3 = rows[-1]
        ass_10_5__3_3 = [float(el) for el in ass_10_5__3_3 if el!=' ']
    else:
        ass_10_5__3_3 = [1 for _ in range(30)]

    rows = []
    if os.path.exists(directory_10_10__1_1):
        with open(directory_10_10__1_1, 'r') as file:
            csvreader = csv.reader(file)
            for row in csvreader:
                rows.append(row)
        if len(rows[-1])!=30:
            ass_10_10__1_1 = rows[-2]
        else:
            ass_10_10__1_1 = rows[-1]
        ass_10_10__1_1 = [float(el) for el in ass_10_10__1_1 if el!=' ']
    else:
        ass_10_10__1_1 = [1 for _ in range(30)]

    rows = []
    if os.path.exists(directory_10_10__2_2):
        with open(directory_10_10__2_2, 'r') as file:
            csvreader = csv.reader(file)
            for row in csvreader:
                rows.append(row)
        if len(rows[-1])!=30:
            ass_10_10__2_2 = rows[-2]
        else:
            ass_10_10__2_2 = rows[-1]
        ass_10_10__2_2 = [float(el) for el in ass_10_10__2_2 if el!=' ']
    else:
        ass_10_10__2_2 = [1 for _ in range(30)]

    rows = []
    if os.path.exists(directory_10_10__3_3):
        with open(directory_10_10__3_3, 'r') as file:
            csvreader = csv.reader(file)
            for row in csvreader:
                rows.append(row)
        if len(rows[-1])!=30:
            ass_10_10__3_3 = rows[-2]
        else:
            ass_10_10__3_3 = rows[-1]
        ass_10_10__3_3 = [float(el) for el in ass_10_10__3_3 if el!=' ']
    else:
        ass_10_10__3_3 = [1 for _ in range(30)]

    rows = []
    if os.path.exists(directory_20_1__1_1):
        with open(directory_20_1__1_1, 'r') as file:
            csvreader = csv.reader(file)
            for row in csvreader:
                rows.append(row)
        if len(rows[-1])!=30:
            ass_20_1__1_1 = rows[-2]
        else:
            ass_20_1__1_1 = rows[-1]
        ass_20_1__1_1 = [float(el) for el in ass_20_1__1_1 if el!=' ']
    else:
        ass_20_1__1_1 = [1 for _ in range(30)]

    rows = []
    if os.path.exists(directory_20_1__2_2):
        with open(directory_20_1__2_2, 'r') as file:
            csvreader = csv.reader(file)
            for row in csvreader:
                rows.append(row)
        if len(rows[-1])!=30:
            ass_20_1__2_2 = rows[-2]
        else:
            ass_20_1__2_2 = rows[-1]
        ass_20_1__2_2 = [float(el) for el in ass_20_1__2_2 if el!=' ']
    else:
        ass_20_1__2_2 = [1 for _ in range(30)]

    rows = []
    if os.path.exists(directory_20_1__3_3):
        with open(directory_20_1__3_3, 'r') as file:
            csvreader = csv.reader(file)
            for row in csvreader:
                rows.append(row)
        if len(rows[-1])!=30:
            ass_20_1__3_3 = rows[-2]
        else:
            ass_20_1__3_3 = rows[-1]
        ass_20_1__3_3 = [float(el) for el in ass_20_1__3_3 if el!=' ']
    else:
        ass_20_1__3_3 = [1 for _ in range(30)]


    rows = []
    if os.path.exists(directory_20_5__1_1):
        with open(directory_20_5__1_1, 'r') as file:
            csvreader = csv.reader(file)
            for row in csvreader:
                rows.append(row)
        if len(rows[-1])!=30:
            ass_20_5__1_1 = rows[-2]
        else:
            ass_20_5__1_1 = rows[-1]
        ass_20_5__1_1 = [float(el) for el in ass_20_5__1_1 if el!=' ']
    else:
        ass_20_5__1_1 = [1 for _ in range(30)]

    rows = []
    if os.path.exists(directory_20_5__2_2):
        with open(directory_20_5__2_2, 'r') as file:
            csvreader = csv.reader(file)
            for row in csvreader:
                rows.append(row)
        if len(rows[-1])!=30:
            ass_20_5__2_2 = rows[-2]
        else:
            ass_20_5__2_2 = rows[-1]
        ass_20_5__2_2 = [float(el) for el in ass_20_5__2_2 if el!=' ']
    else:
        ass_20_5__2_2 = [1 for _ in range(30)]

    rows = []
    if os.path.exists(directory_20_5__3_3):
        with open(directory_20_5__3_3, 'r') as file:
            csvreader = csv.reader(file)
            for row in csvreader:
                rows.append(row)
        if len(rows[-1])!=30:
            ass_20_5__3_3 = rows[-2]
        else:
            ass_20_5__3_3 = rows[-1]
        ass_20_5__3_3 = [float(el) for el in ass_20_5__3_3 if el!=' ']
    else:
        ass_20_5__3_3 = [1 for _ in range(30)]


    rows = []
    if os.path.exists(directory_20_10__1_1):
        with open(directory_20_10__1_1, 'r') as file:
            csvreader = csv.reader(file)
            for row in csvreader:
                rows.append(row)
        if len(rows[-1])!=30:
            ass_20_10__1_1 = rows[-2]
        else:
            ass_20_10__1_1 = rows[-1]
        ass_20_10__1_1 = [float(el) for el in ass_20_10__1_1 if el!=' ']
    else:
        ass_20_10__1_1 = [1 for _ in range(30)]

    rows = []
    if os.path.exists(directory_20_10__2_2):
        with open(directory_20_10__2_2, 'r') as file:
            csvreader = csv.reader(file)
            for row in csvreader:
                rows.append(row)
        if len(rows[-1])!=30:
            ass_20_10__2_2 = rows[-2]
        else:
            ass_20_10__2_2 = rows[-1]
        ass_20_10__2_2 = [float(el) for el in ass_20_10__2_2 if el!=' ']
    else:
        ass_20_10__2_2 = [1 for _ in range(30)]

    rows = []
    if os.path.exists(directory_20_10__3_3):
        with open(directory_20_10__3_3, 'r') as file:
            csvreader = csv.reader(file)
            for row in csvreader:
                rows.append(row)
        if len(rows[-1])!=30:
            ass_20_10__3_3 = rows[-2]
        else:
            ass_20_10__3_3 = rows[-1]
        ass_20_10__3_3 = [float(el) for el in ass_20_10__3_3 if el!=' ']
    else:
        ass_20_10__3_3 = [1 for _ in range(30)]

    fitness_10_1__1_1 = np.mean(ass_10_1__1_1)
    fitness_10_1__2_2 = np.mean(ass_10_1__2_2)
    fitness_10_1__3_3 = np.mean(ass_10_1__3_3)

    fitness_20_1__1_1 = np.mean(ass_20_1__1_1)
    fitness_20_1__2_2 = np.mean(ass_20_1__2_2)
    fitness_20_1__3_3 = np.mean(ass_20_1__3_3)

    fitness_10_5__1_1 = np.mean(ass_10_5__1_1)
    fitness_10_5__2_2 = np.mean(ass_10_5__2_2)
    fitness_10_5__3_3 = np.mean(ass_10_5__3_3)

    fitness_20_5__1_1 = np.mean(ass_20_5__1_1)
    fitness_20_5__2_2 = np.mean(ass_20_5__2_2)
    fitness_20_5__3_3 = np.mean(ass_20_5__3_3)

    fitness_10_10__1_1 = np.mean(ass_10_10__1_1)
    fitness_10_10__2_2 = np.mean(ass_10_10__2_2)
    fitness_10_10__3_3 = np.mean(ass_10_10__3_3)

    fitness_20_10__1_1 = np.mean(ass_20_10__1_1)
    fitness_20_10__2_2 = np.mean(ass_20_10__2_2)
    fitness_20_10__3_3 = np.mean(ass_20_10__3_3)


    fitness_1_1 = [fitness_10_1__1_1, fitness_10_5__1_1, fitness_10_10__1_1, 
                   fitness_20_1__1_1, fitness_20_5__1_1, fitness_20_10__1_1]
    fitness_2_2 = [fitness_10_1__2_2, fitness_10_5__2_2, fitness_10_10__2_2, 
                   fitness_20_1__2_2, fitness_20_5__2_2, fitness_20_10__2_2]
    fitness_3_3 = [fitness_10_1__3_3, fitness_10_5__3_3, fitness_10_10__3_3,
                   fitness_20_1__3_3, fitness_20_5__3_3, fitness_20_10__3_3]

    hyperparam = ["(10,1)", "(10,5)", "(10,10)", "(20,1)", "(20,5)", "(20,10)"]
    sns.set_theme(style="whitegrid")
    max_fit = max(  fitness_10_1__1_1, fitness_10_5__1_1, fitness_10_10__1_1, 
                    fitness_20_1__1_1, fitness_20_5__1_1, fitness_20_10__1_1, 
                    fitness_10_1__2_2, fitness_10_5__2_2, fitness_10_10__2_2, 
                    fitness_20_1__2_2, fitness_20_5__2_2, fitness_20_10__2_2,
                    fitness_10_1__3_3, fitness_10_5__3_3, fitness_10_10__3_3,
                    fitness_20_1__3_3, fitness_20_5__3_3, fitness_20_10__3_3)

    min_fit = 0
    fig, axes = plt.subplots(nrows=1, ncols=2) #, figsize=(10,5))
    lwd = 1.5

    if problem[:-14]!='tm':
        axes[0].plot(fitness_1_1[:3], 'D-', color="black", linewidth=lwd, markersize=12,          markerfacecolor='w', markeredgewidth=1.5, markeredgecolor="black", ls='dashed', alpha=0.65)
    axes[0].plot(fitness_2_2[:3], 's-', color="black", linewidth=lwd, markersize=12, markerfacecolor='silver',
                 markeredgewidth=1.5, markeredgecolor="black", ls='dotted', alpha=0.65)
    axes[0].plot(fitness_3_3[:3], 'o-', color="black", linewidth=lwd, markersize=12, markerfacecolor='gray',
                 markeredgewidth=1.5, markeredgecolor="black", ls='dashdot', alpha=0.65)

    axes[0].set_xticks(range(3))
    axes[0].set_xticklabels(hyperparam[:3])

#    axes[0].set_ylabel('Fitness')
    fig.suptitle(problem[:-12]) #, fontsize=20)

    if problem[:-14]=='tm':
        axes[0].legend(labels=["(2, 2)", "(3, 3)"])
    else: 
        axes[0].legend(labels=["(1, 1)", "(2, 2)", "(3, 3)"])


    if problem[:-14]!='tm':
        axes[1].plot(fitness_1_1[3:], 'D-', color="black", linewidth=lwd, markersize=12, markerfacecolor='w',
                 markeredgewidth=1.5, markeredgecolor="black", ls = 'dashed', alpha=0.65)
    axes[1].plot(fitness_2_2[3:], 's-', color="black", linewidth=lwd, markersize=12, markerfacecolor='silver',
                 markeredgewidth=1.5, markeredgecolor="black", ls='dotted', alpha=0.65)
    axes[1].plot(fitness_3_3[3:], 'o-', color="black", linewidth=lwd, markersize=12, markerfacecolor='gray',
                 markeredgewidth=1.5, markeredgecolor="black", ls='dashdot', alpha=0.65)

    axes[0].axis([-0.15, 2.15, min_fit - 0.05, max_fit + 0.05])
    axes[1].axis([-0.15, 2.15, min_fit - 0.05, max_fit + 0.05])
    if problem[:4]=="send" or problem[:-12]=="assignment-2":
        axes[0].axis([-0.15, 2.15, min_fit - 0.01, max_fit + 0.05])
        axes[1].axis([-0.15, 2.15, min_fit - 0.01, max_fit + 0.05])

    axes[1].set_xticks(range(3))
    axes[1].set_xticklabels(hyperparam[3:])

    if problem[:-14]=='tm':
        axes[0].legend(labels=["(2, 2)", "(3, 3)"])
    else: 
        axes[0].legend(labels=["(1, 1)", "(2, 2)", "(3, 3)"])

    axes[1].label_outer()

    plt.savefig('results/comp_plot/' + problem[:-4] + '-subplot_comparison.png')
    print(problem[:-12] + " plotted")
#     plt.show()

