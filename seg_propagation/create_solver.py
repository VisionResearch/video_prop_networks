#!/usr/bin/env python

'''
    File name: create_solver.py
    Author: Varun Jampani
'''

# ---------------------------------------------------------------------------
# Video Propagation Networks
#----------------------------------------------------------------------------
# Copyright 2017 Max Planck Society
# Distributed under the BSD-3 Software license [see LICENSE.txt for details]
# ---------------------------------------------------------------------------

import tempfile
from init_caffe import *
from davis_data import *
from caffe.proto import caffe_pb2 as PB

def create_solver(solver_param, file_name=""):
    if file_name:
        f = open(file_name, 'w')
    else:
        f = tempfile.NamedTemporaryFile(mode='w+', delete=False)
    f.write(str(solver_param))
    f.close()
    solver = caffe.get_solver(f.name)
    return solver


def create_solver_proto(train_net,
                        test_net,
                        lr,
                        prefix,
                        test_iter=100,
                        test_interval=1000,
                        max_iter=1e5,
                        iter_size=1,
                        snapshot=1000,
                        display=1,
                        debug_info=False):
    solver = PB.SolverParameter()
    solver.train_net = train_net
    solver.test_net.extend([test_net])

    solver.test_iter.extend([test_iter])
    solver.test_interval = test_interval

    solver.display = display
    solver.max_iter = max_iter
    solver.iter_size = iter_size
    solver.snapshot = snapshot
    solver.snapshot_prefix = prefix
    solver.random_seed = RAND_SEED
    solver.average_loss = 20

    solver.solver_mode = PB.SolverParameter.GPU
    solver.solver_type = PB.SolverParameter.ADAM
    solver.base_lr = lr
    solver.lr_policy = "fixed"
    solver.power = 0.9
    solver.momentum = 0.9
    solver.momentum2 = 0.999

    solver.debug_info = debug_info
    return solver
