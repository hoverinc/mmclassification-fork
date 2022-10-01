_base_ = [
    '../_base_/models/efficientnet_b0.py',
    '../_base_/datasets/manowar.py',
    '../_base_/schedules/imagenet_bs1024_adamw_conformer.py',
    '../_base_/default_runtime.py',
]