
class _SeqBaseClass():
    _possible_letters = None
    _complement_matrix = None
    def __init__(self, seq):
        # 
        self._counted = None

        # проверка передаваемой строки
        if isinstance(seq, str):
            self.sequence = seq.upper()
        else:
            raise ValueError(f'Expected str, got {type(seq)}')
        
        # проверка, что в классе-ребёнке определена матрица букв (ATGC для ДНК, AUGC для РНК)
        if not self._possible_letters:
            raise NotImplementedError('Subclasses must define _possible_letters')

        # проверка, что в классе-ребёнке определена матрица комплементарности
        if not self._complement_matrix:
            raise NotImplementedError('Subclasses must define _complement_matrix')
        
        
    def __len__(self) -> int:
        return len(self.sequence)

        
    def __iter__(self):
        return iter(self.sequence)

    # def __next__(self):
    #     # not implemented yet
    #     # по причине: и так всё работает
    #     pass

        
    def __str__(self):
        return self.sequence

    # хотя можно обойтись и методом .reverse()
    def __reversed__(self):
        return self.sequence[::-1]

        
    def __hash__(self):
        '''
        Определение hash() функции как hash строки ДНК
        '''
        return hash(self.sequence)

    
    def __eq__(self, other) -> bool:
        '''
        Сравнивать можно с объектом своего класса или же с другой строкой.
        '''
        if isinstance(other, _SeqBaseClass):
            return self.sequence == other.sequence
        elif isinstance(other, str):
            return self.sequence == other.upper()
        else:
            return f'Comparison of {type(self)} and {type(other)} is not defined.'

        
    def gc_content(self) -> float:
        '''
        Позволяет посчитать GC-состав последовательности
        '''
        if not self._counted:
            _ = self.count()
        
        gc = self._counted['G'] + self._counted['C']
        length = sum([self._counted[i] for i in self._possible_letters])
        
        return gc/length
        

    def complement(self):
        '''
        Позволяет получить последовательность ДНК, комплементарную данной
        '''
        
        complement_seq = ''.join([self._complement_matrix[i] for i in self.sequence])
        # return _SeqBaseClass(complement_seq)
        return complement_seq
        

    def reverse(self):
        # берём имя класса-ребёнка -- Dna/Rna (3 -- магическое число, длина названия класса-ребёнка)
        # child_type = str(str(self)[:3])
        # child_class = type(child_type, (), {seq})
        # return child_class(self.sequence[::-1])
        return self.sequence[::-1]


    def reverse_complement(self):
        reverse_complement_seq = ''.join([self._complement_matrix[i] for i in self.sequence[::-1]])
        # return _SeqBaseClass(reverse_complement_seq)
        return reverse_complement_seq
        

    def count(self):
        '''Возвращает нуклеотидный состав ДНК последовательности'''
        
        if self._counted:
            return self._counted
            
        counted = {nucl:0 for nucl in self._possible_letters}
        for nucl in self.sequence:
            counted[nucl] += 1
        self._counted = counted    
            
        return self._counted


class Dna(_SeqBaseClass):
    def __init__(self, seq):
        self._complement_matrix = {
            'A': 'T',
            'T': 'A',
            'C': 'G',
            'G': 'C'
            }

        self._possible_letters = ('A', 'T', 'G', 'C')
        super().__init__(seq)

    def __repr__(self):
        return f"Dna('{self.sequence}')"

    def transcribe(self):
        '''
        Позволяет транскрибировать последовательность ДНК
        '''
        transcribe_matrix = {
            'A': 'U',
            'T': 'A',
            'C': 'G',
            'G': 'C'
        }

        rna_seq = ''.join([transcribe_matrix[i] for i in self.sequence])
        return Rna(rna_seq)
        

class Rna(_SeqBaseClass):
    def __init__(self, seq):
        self._complement_matrix = {
            'A': 'U',
            'U': 'A',
            'C': 'G',
            'G': 'C'
            }

        self._possible_letters = ('A', 'U', 'G', 'C')
        super().__init__(seq)


    def __repr__(self):
        return f"Rna('{self.sequence}')"
