

import matplotlib.pyplot as plt
from sklearn.metrics import (confusion_matrix, ConfusionMatrixDisplay, recall_score, 
                             precision_score, f1_score, accuracy_score)


def plot_confusion_matrix(y, pred, title = None):
    '''
    Confusion Matrix를 시각화하는 함수이다.
    [parameter]
        y: ndarray - 정답
        pred: ndarray - model의 예측값
        title: str - graph의 제목
    [return]
        None
    [exception]
        None
    '''
    cm = confusion_matrix(y, pred)
    disp = ConfusionMatrixDisplay(cm)
    disp.plot(cmap = 'Blues')
    if title:
        plt.title(title)
    plt.show()

    
def print_metrics_classification(y, pred, title = None):
    '''
    classification의 evaluation index들을 출력하는 함수이다. accuracy, recall, precision, f1-score를 출력한다.
    [parameter]
        y: ndarray - 정답
        pred: ndarray - model의 예측값
        title: str - graph의 제목
    [return]
        None
    [exception]
        None
    '''
    if title:
        print(title)
    print('Accuracy:', accuracy_score(y, pred))
    print('Recall:', recall_score(y, pred))
    print('Precision:', precision_score(y, pred))
    print('F1-score:', f1_score(y, pred))
