import torch.nn as nn


class _TensorParallel1D(nn.Module):
    """
    PyTorch module for 1D tensor parallelism
    """

    def __init__(self, model):
        super().__init__()
