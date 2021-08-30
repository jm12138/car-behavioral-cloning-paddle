import paddle.nn as nn


def build_model(keep_prob=0.5):
    model = nn.Sequential(
        nn.Conv2D(in_channels=3,
                  out_channels=24,
                  kernel_size=5,
                  stride=2,
                  padding='valid',
                  data_format='NHWC'), nn.ELU(),
        nn.Conv2D(in_channels=24,
                  out_channels=36,
                  kernel_size=5,
                  stride=2,
                  padding='valid',
                  data_format='NHWC'), nn.ELU(),
        nn.Conv2D(in_channels=36,
                  out_channels=48,
                  kernel_size=5,
                  stride=2,
                  padding='valid',
                  data_format='NHWC'), nn.ELU(),
        nn.Conv2D(in_channels=48,
                  out_channels=64,
                  kernel_size=(3, 3),
                  padding='valid',
                  data_format='NHWC'), nn.ELU(),
        nn.Conv2D(in_channels=64,
                  out_channels=64,
                  kernel_size=(3, 3),
                  padding='valid',
                  data_format='NHWC'), nn.ELU(), nn.Dropout(keep_prob),
        nn.Flatten(), nn.Linear(1152, 100), nn.ELU(), nn.Linear(100, 50),
        nn.ELU(), nn.Linear(50, 10), nn.ELU(), nn.Linear(10, 1))
    return model
