from Model.extractor import FeatureExtractor
from Model.Model_reg import Regressor
import warnings
warnings.filterwarnings("ignore")


if __name__ == '__main__':
    print('Reading Data and Preprocessing it')
    a = FeatureExtractor('./data/train.csv', './data/store.csv')
    a.fit()
    X, y = a.transform()

    print('Constructing the Model')
    clf = Regressor()
    clf.fit(X, y)

    print('Saving the Model')
    clf.save()

    print('Ready to go')
