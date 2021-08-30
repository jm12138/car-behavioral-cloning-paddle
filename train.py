import paddle
import argparse
import numpy as np
import paddle.nn as nn

from paddle.optimizer import Adam
from paddle.callbacks import ModelCheckpoint, EarlyStopping

from car.model import build_model
from car.utils import CarDataset, load_data

np.random.seed(0)


def train_model(model, args, X_train, X_valid, y_train, y_valid):
    """
    Train the model
    """
    checkpoint = ModelCheckpoint(save_dir=args.save_dir)

    earlystopping = EarlyStopping(monitor='loss',
                                  mode='min',
                                  patience=10,
                                  verbose=1,
                                  min_delta=0,
                                  baseline=None,
                                  save_best_model=True)
    if args.early_stop:
        cbs = [checkpoint, earlystopping]
    else:
        cbs = [checkpoint]

    opt = Adam(learning_rate=args.learning_rate, parameters=model.parameters())

    model = paddle.Model(model)
    model.prepare(loss=nn.MSELoss(), optimizer=opt)

    train_dataset = CarDataset(args.data_dir, X_train, y_train, True)
    val_dataset = CarDataset(args.data_dir, X_valid, y_valid, False)

    model.fit(train_data=train_dataset,
              eval_data=val_dataset,
              epochs=args.nb_epoch,
              batch_size=args.batch_size,
              save_dir=args.save_dir,
              callbacks=cbs,
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
    parser.add_argument('-e',
                        help='early stop',
                        dest='early_stop',
                        type=bool,
                        default=False)
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
