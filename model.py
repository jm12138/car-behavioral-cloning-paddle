import os
import paddle
import argparse
import numpy as np
import pandas as pd
import paddle.nn as nn

from utils import INPUT_SHAPE, dataset
from sklearn.model_selection import train_test_split
from paddle.optimizer import Adam
from paddle.callbacks import ModelCheckpoint, EarlyStopping

np.random.seed(0)


def load_data(args):
    """
    Load training data and split it into training and validation set
    """
    data_df = pd.read_csv(os.path.join(args.data_dir, 'driving_log.csv'))

    X = data_df[['center', 'left', 'right']].values
    y = data_df['steering'].values

    X_train, X_valid, y_train, y_valid = train_test_split(
        X, y, test_size=args.test_size, random_state=0)

    return X_train, X_valid, y_train, y_valid


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


def train_model(model, args, X_train, X_valid, y_train, y_valid):
    """
    Train the model
    """
    checkpoint = ModelCheckpoint(save_dir=args.save_dir)

    earlystopping = EarlyStopping(monitor='loss',
                                  mode='min',
                                  patience=5,
                                  verbose=1,
                                  min_delta=0,
                                  baseline=None,
                                  save_best_model=True)

    opt = Adam(learning_rate=args.learning_rate, parameters=model.parameters())

    model = paddle.Model(model)
    model.prepare(loss=nn.MSELoss(), optimizer=opt)

    train_dataset = dataset(args.data_dir, X_train, y_train, True)
    val_dataset = dataset(args.data_dir, X_valid, y_valid, False)

    model.fit(train_data=train_dataset,
              eval_data=val_dataset,
              epochs=args.nb_epoch,
              batch_size=args.batch_size,
              save_dir=args.save_dir,
              callbacks=[checkpoint, earlystopping],
              verbose=1)


def s2b(s):
    """
    Converts a string to boolean value
    """
    s = s.lower()
    return s == 'true' or s == 'yes' or s == 'y' or s == '1'


def main():
    """
    Load train/validation data set and train the model
    """
    parser = argparse.ArgumentParser(
        description='Behavioral Cloning Training Program')
    parser.add_argument('-d',
                        help='data directory',
                        dest='data_dir',
                        type=str,
                        default='data')
    parser.add_argument('-s',
                        help='save directory',
                        dest='save_dir',
                        type=str,
                        default='save')
    parser.add_argument('-t',
                        help='test size fraction',
                        dest='test_size',
                        type=float,
                        default=0.2)
    parser.add_argument('-k',
                        help='drop out probability',
                        dest='keep_prob',
                        type=float,
                        default=0.5)
    parser.add_argument('-n',
                        help='number of epochs',
                        dest='nb_epoch',
                        type=int,
                        default=100)
    parser.add_argument('-b',
                        help='batch size',
                        dest='batch_size',
                        type=int,
                        default=40)
    parser.add_argument('-l',
                        help='learning rate',
                        dest='learning_rate',
                        type=float,
                        default=1.0e-4)
    args = parser.parse_args()

    print('-' * 30)
    print('Parameters')
    print('-' * 30)
    for key, value in vars(args).items():
        print('{:<20} := {}'.format(key, value))
    print('-' * 30)

    data = load_data(args)
    model = build_model(args.keep_prob)
    train_model(model, args, *data)


if __name__ == '__main__':
    main()
