#!/usr/bin/env python

"""run_exp.py: Script to execute in order to produce experiments."""

import os
import itertools

beta = [1]
unroll_critic = [5]
critic_type = ['separate']
regularizers = ['nce']

comb_test_params = itertools.product(beta, unroll_critic, critic_type, regularizers)
labels_test_params = ['beta', 'unroll_critic', 'critic_type', 'regularizer']

fixed_params = {'ema_decay': 0.99, 'epoch': 200}

for param_comb in comb_test_params:
    command_line = "python3 demo_gan.py "
    command_line += "--labels_test_params {} ".format(' '.join(labels_test_params))
    for fix_param_name, fix_param_value in fixed_params.items():
        command_line += "--{} {} ".format(fix_param_name, fix_param_value)
    for i, param in enumerate(param_comb):
        command_line += "--{} {} ".format(labels_test_params[i], param)
    print(command_line)
    os.system(command_line)
print("All experiments were successfully carried out. ")
