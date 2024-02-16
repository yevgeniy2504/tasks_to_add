public class MergeSort {
    public static void main(String[] args) {
        int[] array = {12, 11, 13, 5, 6, 7};
        System.out.println("Исходный массив:");
        printArray(array);

        mergeSort(array, 0, array.length - 1);

        System.out.println("Отсортированный массив:");
        printArray(array);
    }

    public static void mergeSort(int[] array, int left, int right) {
        if (left < right) {
            // Находим середину массива
            int middle = left + (right - left) / 2;

            // Сортируем левую и правую половины массива
            mergeSort(array, left, middle);
            mergeSort(array, middle + 1, right);

            // Объединяем две отсортированные половины
            merge(array, left, middle, right);
        }
    }

    public static void merge(int[] array, int left, int middle, int right) {
        // Определяем размер временных массивов
        int n1 = middle - left + 1;
        int n2 = right - middle;

        // Создаем временные массивы
        int[] L = new int[n1];
        int[] R = new int[n2];

        // Копируем данные во временные массивы
        for (int i = 0; i < n1; ++i) {
            L[i] = array[left + i];
        }
        for (int j = 0; j < n2; ++j) {
            R[j] = array[middle + 1 + j];
        }

        // Индексы для временных массивов
        int i = 0, j = 0;

        // Индекс для основного массива
        int k = left;

        // Слияние временных массивов
        while (i < n1 && j < n2) {
            if (L[i] <= R[j]) {
                array[k] = L[i];
                i++;
            } else {
                array[k] = R[j];
                j++;
            }
            k++;
        }

        // Копируем оставшиеся элементы из L[], если таковые остались
        while (i < n1) {
            array[k] = L[i];
            i++;
            k++;
        }

        // Копируем оставшиеся элементы из R[], если таковые остались
        while (j < n2) {
            array[k] = R[j];
            j++;
            k++;
        }
    }

    public static void printArray(int[] array) {
        for (int value : array) {
            System.out.print(value + " ");
        }
        System.out.println();
    }
}
