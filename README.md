# Актуальные модели распознавания эмоций лица


### В 1970 году было выделено 7 основных человеческих эмоции: 
- гнев
- страх
- печаль
- отвращение
- презрение
- удивление
- радость

 # 

На данный момент можно выделить два подхода к распознаванию эмоций человека, основанных на использовании нейронных сетей.

Классический подход к задаче классификации эмоций основан на классификации ключевых точек человеческого лица. Расположение ключевых точек фиксирует жесткие и нежесткие деформации лица из-за движений головы и мимики. Для получения ключевых точек человеческого лица могут использоваться такие алгоритмы как __PDM__, __CML__, __AAM__, __DPM__ или __CNN__. 

Следующий этап распознавания при классическом подходе, это классификация ключевых точек. Для классификации ключевых точек хорошо подходит метод опорных векторов.

Альтернативой использованию классического подхода является подход, основанный на сверточных нейронных сетях.

Подход основанный на использование машинного обучения может быть разделен на две основные категории: 

- _статические методы_ (в качестве информации для распознавания, используется единичное изображение человеческого лица.)

- _динамические методы_ (используется последовательность изображений. Кроме информации о каждом изображении в последовательности, динамические методы учитывают временную связь между смежными изображениями)
 

Основной проблемой использования сверточных нейронных сетей при решении задачи
распознавания человеческих эмоций по фото является отсутствия достаточной обучающей выборки, из-за чего возникает проблема переобучения сети. Также проблемой является наличие избыточной информации на изображениях, используемых для обучения сети таких так позиция головы и неравномерное освещение.

#

Предложен общий алгоритм распознавания эмоций человека на изображении лица. В алгоритме используется метод Виолы-Джонса для распознавания лица на изображении, а также метод сверточных нейронной сети для классификации эмоции. Нейронная сеть создавалась на языке программирования Python с помощью библиотеки с открытым исходным кодом __Keras__.


Aвторами разработан следующий алгоритм: 

1. Преобразование фото (или кадра видео) в чёрно-белое изображение. 
2. Поиск лица (с помощью методов Виолы-Джонса и примитивов Хаара) ведётся до тех пор, пока лицо не будет обнаружено.
3. Изменение размеров изображения до размеров фото из обучающей выборки (48 на 48).
4. Нормализация данных. 
5. Классификация эмоции на изображении с помощью многослойной свёрточной нейронной сети.

#

## __Ещё модели__:


- В модели Дж. Рассела водится двумерный базис, в котором каждая эмоция характеризуется знаком (valence) и интенсивностью (arousal).

- Классификация эмоций с применением deep learning. Для того чтобы построить нейросетевой классификатор достаточно взять какую-нибудь сеть с базовой архитектурой, предварительно обученную на ImageNet, и переобучить последние несколько слоев.



