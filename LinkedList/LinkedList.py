class LinkedListItem:
    def __init__(self, value):
        self.value = value
        self.__next = None

    def get_next(self):
        return self.__next

    def set_next(self, next_item):
        self.__next = next_item

    def has_next(self):
        return self.__next is not None

class LinkedList:
    def __init__(self):
        self.__head = None
        self.__tail = None
        self.__len = 0

    def __getitem__(self, index):
        current = self.__head
        for _ in range(index):
            if current is None or not current.has_next():
                raise IndexError
            current = current.get_next()
        return current.value

    def __contains__(self, item):
        '''
        Implements 'in' keyword
        '''
        current = self.__head
        while True:
            if current is None:
                return False
            elif current.value == item:
                return True
            current = current.get_next()

    def __len__(self):
        return self.__len

    def add(self, value, index=None):
        self.__len += 1
        new_item = LinkedListItem(value)

        if index is None or index==self.__len-1:
            # Если индекс не передан функции / вставка в конец списка => вставляем как обычно
            if not self.__head:
                self.__head = new_item
            else:
                self.__tail.set_next(new_item)
            self.__tail = new_item
        else:
            prev, curr = self._get_elem_and_next(index)  # Получить (i-1)-ый и i-ый элементы
            if prev is None:
                # если предыдущего элемента нет (то есть вставляем в начало),
                # то new_item становится новой головой
                self.__head = new_item
                if curr is not None:
                    self.__head.set_next(curr)
            else:
                # если с предыдущим элементом всё ок (вставляем не в начало), то
                # prev -> curr  ==>  prev -> new_item -> curr
                prev.set_next(new_item) # устанавливаем у "prev" следующим наш "new_item"
                new_item.set_next(curr)  # для "new_item" устанавливаем "curr" как следующий элемент

    def _get_elem_and_next(self, index):
        '''
        Получает (i-1)-ый элемент и следующий для него (i-ый)
        Если (i-1)-го не существует, то вернёт (None, i)
        '''
        if index == 0:
            return None, self.__head
        
        current = self.__head
        for _ in range(index-1):
            if current is None or not current.has_next():
                raise IndexError
            current = current.get_next()
        return current, current.get_next()

    def extend(self, values, index=None):
        '''
        To add many: a.extend([])
        '''
        if index is None:
            for value in values:
                self.add(value)
        elif index == 0:
            self.__len += len(values)

            current = LinkedListItem(values[-1])
            current.set_next(self.__head)  # если вставляем по нулевому индексу, то для последнего элемента массива устанавливаем next как head
            for value in values[-2::-1]:  # итерация в обратную сторону, до первого элемента не включительно
                new_current = LinkedListItem(value)
                new_current.set_next(current)
                current = new_current
            self.__head = current
        else:
            self.__len += len(values)
            prevv, nextt = self._get_elem_and_next(index)  # Получить (i-1)-ый и i-ый элементы
            # prevv -> nextt  ==>  prevv -> [i -> i+1 -> ...] -> nextt
            for value in values:
                curr = LinkedListItem(value)
                prevv.set_next(curr)  # устанавливаем у "prevv" следующим наш "values[i]"
                prevv = curr  # "values[i]" превращаем в "prevv" 
            curr.set_next(nextt)  # для последнего элемента "values[-1]" следующим делаем тот, который раньше был для prevv

    def pop(self, index=None):
        if index is None:
            index = self.__len - 1
        if index != 0:
            self.__len -= 1
            prevv, nextt = self._get_elem_and_next(index)
            if prevv is not None and nextt is not None:
                # были и предыдущий и i-ый
                prevv.set_next(nextt.get_next())

            if nextt is not None and nextt.get_next() is None:
                # если удалённый оказался последним -- обновляем __tail
                self.__tail = prevv

            if prevv is None and nextt is not None:
                # предыдущего нет
                self.__head = None
            elif prevv is None and nextt is None:
                # предыдущего и следующего нет -- опустошаем список
                self.__head = None
                self.__tail = None

        elif index == 0:
            self.__len -= 1
            # для нулевого индекса -- меняем значение __head
            self.__head = self.__head.get_next()
            if self.__head is None:
                self.__tail = None


    def remove_last_occurence(self, value):
        last_occ = None
        ind = 0
        current = self.__head
        for _ in range(self.__len):
            if current.value == value:
                last_occ = ind
            
            ind += 1
            current = current.get_next()
        
        self.pop(last_occ)

    


    def first(self):
        return self.__head.value

    def last(self):
        return self.__tail.value